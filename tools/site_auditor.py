#!/usr/bin/env python3
"""
Local SEO Site Auditor

Usage:
    python tools/site_auditor.py --sitemap <url> --keywords keywords.txt
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple
from urllib.parse import urljoin, urlparse, urlunparse
import xml.etree.ElementTree as ET

import requests
from bs4 import BeautifulSoup
from requests import Response, Session


USER_AGENT = "LocalSEOSiteAuditor/1.0 (+https://serenelandscapes.ca)"
TIMEOUT_SECONDS = 20
RATE_LIMIT_SECONDS = 0.25
MAX_RETRIES = 3
REPORTS_DIR = Path("reports")


CSV_COLUMNS = [
    "url",
    "status_code",
    "final_url",
    "response_time_ms",
    "indexable (yes/no)",
    "canonical",
    "title",
    "title_len",
    "meta_description",
    "meta_description_len",
    "h1",
    "h1_count",
    "h2_count",
    "h3_count",
    "headings_outline",
    "intro_text",
    "keyword_primary",
    "keyword_in_title (yes/no)",
    "keyword_in_h1 (yes/no)",
    "keyword_in_intro (yes/no)",
    "keyword_density_primary_pct",
    "keyword_counts_json",
    "internal_links_out_count",
    "internal_links_unique_out_count",
    "internal_links_in_count",
    "broken_internal_links_out",
    "word_count",
    "schema_types",
    "og_title_present",
    "og_description_present",
    "og_url_present",
    "notes",
]


def normalize_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def word_list(text: str) -> List[str]:
    return re.findall(r"[a-z0-9]+(?:'[a-z0-9]+)?", (text or "").lower())


def localname(tag_name: str) -> str:
    return tag_name.split("}", 1)[-1].lower() if tag_name else ""


def to_json(value: object) -> str:
    return json.dumps(value, ensure_ascii=True)


def strip_fragment(url: str) -> str:
    parsed = urlparse(url)
    return urlunparse((parsed.scheme, parsed.netloc, parsed.path, parsed.params, parsed.query, ""))


def normalize_url(url: str) -> str:
    parsed = urlparse(url.strip())
    scheme = (parsed.scheme or "https").lower()
    netloc = parsed.netloc.lower()
    path = parsed.path or "/"
    path = re.sub(r"/{2,}", "/", path)
    if path != "/" and path.endswith("/"):
        path = path[:-1]
    return urlunparse((scheme, netloc, path, parsed.params, parsed.query, ""))


def same_site(url: str, root_host: str) -> bool:
    host = urlparse(url).netloc.lower()
    return host == root_host or host.endswith("." + root_host)


def keyword_pattern(phrase: str) -> re.Pattern:
    parts = [re.escape(x) for x in phrase.lower().split()]
    joined = r"\s+".join(parts)
    return re.compile(rf"(?<![a-z0-9]){joined}(?![a-z0-9])", flags=re.IGNORECASE)


def detect_parser() -> str:
    try:
        import lxml  # noqa: F401

        return "lxml"
    except Exception:
        return "html.parser"


@dataclass
class LinkStatus:
    status_code: int
    final_url: str
    chain: List[Tuple[int, str]]


@dataclass
class PageAudit:
    url: str
    status_code: int = 0
    final_url: str = ""
    response_time_ms: int = 0
    indexable: str = "no"
    canonical: str = ""
    title: str = ""
    title_len: int = 0
    meta_description: str = ""
    meta_description_len: int = 0
    robots_meta: str = ""
    h1: str = ""
    h1_count: int = 0
    h2_count: int = 0
    h3_count: int = 0
    headings_outline: str = ""
    intro_text: str = ""
    keyword_primary: str = ""
    keyword_in_title: str = "no"
    keyword_in_h1: str = "no"
    keyword_in_intro: str = "no"
    keyword_density_primary_pct: float = 0.0
    keyword_counts: Dict[str, int] = field(default_factory=dict)
    internal_links_out_count: int = 0
    internal_links_unique_out_count: int = 0
    internal_links_in_count: int = 0
    broken_internal_links_out: List[str] = field(default_factory=list)
    word_count: int = 0
    schema_types: List[str] = field(default_factory=list)
    og_title_present: str = "no"
    og_description_present: str = "no"
    og_url_present: str = "no"
    notes: List[str] = field(default_factory=list)
    outlinks_unique: Set[str] = field(default_factory=set)
    redirect_chain: List[Tuple[int, str]] = field(default_factory=list)
    visible_text: str = ""


class SiteAuditor:
    def __init__(self, sitemap_url: str, keywords: List[str], root_domain: Optional[str] = None) -> None:
        self.sitemap_url = sitemap_url
        self.keywords = [k.strip() for k in keywords if k.strip()]
        self.keyword_patterns = {kw: keyword_pattern(kw) for kw in self.keywords}
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})
        self.root_domain = root_domain or self._derive_root_domain(sitemap_url)
        self.root_host = urlparse(self.root_domain).netloc.lower()
        self.parser = detect_parser()
        self.link_status_cache: Dict[str, LinkStatus] = {}
        self.inlink_counts: Dict[str, int] = defaultdict(int)

    @staticmethod
    def _derive_root_domain(url: str) -> str:
        parsed = urlparse(url)
        return f"{parsed.scheme}://{parsed.netloc}"

    def _throttled_request(self, url: str, allow_redirects: bool = True) -> Tuple[Optional[Response], int]:
        backoff = 1.0
        for attempt in range(1, MAX_RETRIES + 1):
            start = time.perf_counter()
            try:
                resp = self.session.get(
                    url,
                    timeout=TIMEOUT_SECONDS,
                    allow_redirects=allow_redirects,
                )
                elapsed = int((time.perf_counter() - start) * 1000)
                if resp.status_code == 429 or 500 <= resp.status_code <= 599:
                    if attempt < MAX_RETRIES:
                        time.sleep(backoff)
                        backoff *= 2
                        continue
                time.sleep(RATE_LIMIT_SECONDS)
                return resp, elapsed
            except requests.RequestException:
                elapsed = int((time.perf_counter() - start) * 1000)
                if attempt < MAX_RETRIES:
                    time.sleep(backoff)
                    backoff *= 2
                    continue
                time.sleep(RATE_LIMIT_SECONDS)
                return None, elapsed
        return None, 0

    def fetch_sitemap_urls(self) -> List[str]:
        queue = [self.sitemap_url]
        seen_sitemaps: Set[str] = set()
        urls: Set[str] = set()
        print(f"[1/5] Fetching sitemap(s) from {self.sitemap_url}")
        while queue:
            sm_url = normalize_url(queue.pop(0))
            if sm_url in seen_sitemaps:
                continue
            seen_sitemaps.add(sm_url)
            resp, _ = self._throttled_request(sm_url, allow_redirects=True)
            if not resp or resp.status_code >= 400:
                print(f"  - Failed sitemap: {sm_url} (status {resp.status_code if resp else 'ERR'})")
                continue
            try:
                root = ET.fromstring(resp.content)
            except ET.ParseError:
                print(f"  - Invalid XML: {sm_url}")
                continue
            root_name = localname(root.tag)
            if root_name == "sitemapindex":
                for node in root.iter():
                    if localname(node.tag) == "loc" and node.text:
                        queue.append(normalize_url(node.text.strip()))
            elif root_name == "urlset":
                for node in root.iter():
                    if localname(node.tag) == "loc" and node.text:
                        normalized = normalize_url(strip_fragment(node.text.strip()))
                        if same_site(normalized, self.root_host):
                            urls.add(normalized)
            else:
                print(f"  - Unknown sitemap root: {root_name} ({sm_url})")
        output = sorted(urls)
        print(f"  - Discovered {len(output)} URL(s) in sitemap.")
        return output

    def crawl_discovered_urls(self, start_url: str, max_depth: int = 3) -> List[str]:
        print(f"[2/6] Crawling from homepage for URL discovery (depth={max_depth})")
        start = normalize_url(strip_fragment(start_url))
        queue: List[Tuple[str, int]] = [(start, 0)]
        visited: Set[str] = set()
        discovered: Set[str] = set()

        while queue:
            current, depth = queue.pop(0)
            if current in visited or depth > max_depth:
                continue
            visited.add(current)
            discovered.add(current)

            resp, _ = self._throttled_request(current, allow_redirects=True)
            if not resp:
                continue

            final_url = normalize_url(strip_fragment(resp.url))
            discovered.add(final_url)
            if final_url not in visited and depth <= max_depth:
                visited.add(final_url)

            content_type = (resp.headers.get("Content-Type") or "").lower()
            if "text/html" not in content_type and "<html" not in resp.text.lower():
                continue
            if depth >= max_depth:
                continue

            soup = BeautifulSoup(resp.text, self.parser)
            for a in soup.find_all("a", href=True):
                href = (a.get("href") or "").strip()
                if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
                    continue
                absolute = normalize_url(strip_fragment(urljoin(final_url, href)))
                if not same_site(absolute, self.root_host):
                    continue
                discovered.add(absolute)
                if absolute not in visited:
                    queue.append((absolute, depth + 1))

            if len(visited) % 25 == 0:
                print(f"  - Discovery crawl visited {len(visited)} page(s)")

        output = sorted(discovered)
        print(f"  - Discovery crawl found {len(output)} unique internal URL(s)")
        return output

    def audit_page(self, url: str) -> PageAudit:
        page = PageAudit(url=url)
        resp, elapsed = self._throttled_request(url, allow_redirects=True)
        page.response_time_ms = elapsed
        if not resp:
            page.notes.append("request_failed")
            return page

        page.status_code = resp.status_code
        page.final_url = normalize_url(strip_fragment(resp.url))
        page.redirect_chain = [
            (r.status_code, normalize_url(strip_fragment(r.url))) for r in (list(resp.history) + [resp])
        ]

        if resp.history:
            chain_note = " -> ".join([u for _, u in page.redirect_chain])
            page.notes.append(f"redirect_chain:{chain_note}")

        content_type = (resp.headers.get("Content-Type") or "").lower()
        if "text/html" not in content_type and "<html" not in resp.text.lower():
            page.notes.append(f"non_html_content_type:{content_type}")
            return page

        soup = BeautifulSoup(resp.text, self.parser)
        self._extract_seo_fields(page, soup)
        self._extract_headings_and_text(page, soup)
        self._extract_links(page, soup, page.final_url or page.url)
        self._extract_keywords(page)
        self._extract_schema_types(page, soup)
        self._compute_indexable(page, resp)
        return page

    def _extract_seo_fields(self, page: PageAudit, soup: BeautifulSoup) -> None:
        title_tag = soup.find("title")
        page.title = normalize_whitespace(title_tag.get_text(" ", strip=True)) if title_tag else ""
        page.title_len = len(page.title)

        desc_tag = soup.find("meta", attrs={"name": re.compile("^description$", re.I)})
        page.meta_description = normalize_whitespace(desc_tag.get("content", "")) if desc_tag else ""
        page.meta_description_len = len(page.meta_description)

        canon_tag = soup.find("link", attrs={"rel": re.compile("canonical", re.I)})
        if canon_tag and canon_tag.get("href"):
            page.canonical = normalize_url(strip_fragment(urljoin(page.final_url or page.url, canon_tag["href"])))

        robots_tag = soup.find("meta", attrs={"name": re.compile("^robots$", re.I)})
        page.robots_meta = (robots_tag.get("content", "") if robots_tag else "").strip().lower()

        page.og_title_present = "yes" if soup.find("meta", attrs={"property": "og:title"}) else "no"
        page.og_description_present = "yes" if soup.find("meta", attrs={"property": "og:description"}) else "no"
        page.og_url_present = "yes" if soup.find("meta", attrs={"property": "og:url"}) else "no"

    def _extract_headings_and_text(self, page: PageAudit, soup: BeautifulSoup) -> None:
        h1_tags = soup.find_all("h1")
        h2_tags = soup.find_all("h2")
        h3_tags = soup.find_all("h3")
        page.h1_count = len(h1_tags)
        page.h2_count = len(h2_tags)
        page.h3_count = len(h3_tags)
        page.h1 = normalize_whitespace(h1_tags[0].get_text(" ", strip=True)) if h1_tags else ""
        if page.h1_count == 0:
            page.notes.append("missing_h1")
        elif page.h1_count > 1:
            page.notes.append("multiple_h1")

        outline = []
        for tag in soup.find_all(re.compile(r"^h[1-3]$")):
            outline.append(tag.name.upper())
        page.headings_outline = "|".join(outline)

        main_or_body = soup.find("main") or soup.body or soup
        working = BeautifulSoup(str(main_or_body), self.parser)
        for noisy in working(["script", "style", "noscript", "template", "svg", "head"]):
            noisy.decompose()
        text = normalize_whitespace(working.get_text(" ", strip=True))
        page.visible_text = text
        words = word_list(text)
        page.word_count = len(words)
        page.intro_text = " ".join(words[:200])
        if page.word_count < 100:
            page.notes.append("intro_too_short_under_100_words")

    def _extract_links(self, page: PageAudit, soup: BeautifulSoup, base_url: str) -> None:
        links: List[str] = []
        for a in soup.find_all("a", href=True):
            href = (a.get("href") or "").strip()
            if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
                continue
            absolute = normalize_url(strip_fragment(urljoin(base_url, href)))
            if same_site(absolute, self.root_host):
                links.append(absolute)
        page.internal_links_out_count = len(links)
        page.outlinks_unique = set(links)
        page.internal_links_unique_out_count = len(page.outlinks_unique)

    def _extract_keywords(self, page: PageAudit) -> None:
        body_text = (page.visible_text or "").lower()
        counts: Dict[str, int] = {}
        for kw, pattern in self.keyword_patterns.items():
            counts[kw] = len(pattern.findall(body_text))
        page.keyword_counts = counts

        if not self.keywords:
            return

        best_keyword = ""
        best_score = -1
        for kw in self.keywords:
            score = counts.get(kw, 0) * max(1, len(kw.split()))
            if score > best_score:
                best_score = score
                best_keyword = kw
        page.keyword_primary = best_keyword

        if page.keyword_primary:
            kw = page.keyword_primary.lower()
            page.keyword_in_title = "yes" if kw in (page.title or "").lower() else "no"
            page.keyword_in_h1 = "yes" if kw in (page.h1 or "").lower() else "no"
            page.keyword_in_intro = "yes" if kw in (page.intro_text or "").lower() else "no"
            occurrences = counts.get(page.keyword_primary, 0)
            words_in_kw = max(1, len(page.keyword_primary.split()))
            if page.word_count > 0:
                density = (occurrences * words_in_kw) / page.word_count * 100.0
                page.keyword_density_primary_pct = round(density, 4)

        if page.keyword_primary and page.keyword_in_intro == "yes":
            intro_words = page.intro_text.split()
            if intro_words:
                intro_first_100 = " ".join(intro_words[:100]).lower()
                if page.keyword_primary.lower() not in intro_first_100:
                    page.notes.append("keyword_not_in_first_100_words")
        elif page.keyword_primary:
            page.notes.append("keyword_missing_in_intro")

    def _extract_schema_types(self, page: PageAudit, soup: BeautifulSoup) -> None:
        found: Set[str] = set()
        scripts = soup.find_all("script", attrs={"type": re.compile(r"application/ld\+json", re.I)})
        for script in scripts:
            raw = (script.string or script.get_text() or "").strip()
            if not raw:
                continue
            try:
                data = json.loads(raw)
            except json.JSONDecodeError:
                continue
            self._collect_schema_types(data, found)
        page.schema_types = sorted(found)

    def _collect_schema_types(self, node: object, out: Set[str]) -> None:
        if isinstance(node, dict):
            typ = node.get("@type")
            if isinstance(typ, str):
                out.add(typ)
            elif isinstance(typ, list):
                for t in typ:
                    if isinstance(t, str):
                        out.add(t)
            for value in node.values():
                self._collect_schema_types(value, out)
        elif isinstance(node, list):
            for item in node:
                self._collect_schema_types(item, out)

    def _compute_indexable(self, page: PageAudit, resp: Response) -> None:
        x_robots = (resp.headers.get("X-Robots-Tag") or "").lower()
        robots_blob = f"{page.robots_meta} {x_robots}".strip()
        if page.status_code == 200 and "noindex" not in robots_blob:
            page.indexable = "yes"
        else:
            page.indexable = "no"
        if page.robots_meta:
            page.notes.append(f"robots_meta:{page.robots_meta}")
        if x_robots:
            page.notes.append(f"x_robots:{x_robots}")

    def check_link_status(self, url: str) -> LinkStatus:
        if url in self.link_status_cache:
            return self.link_status_cache[url]

        resp, _ = self._throttled_request(url, allow_redirects=True)
        if not resp:
            status = LinkStatus(status_code=0, final_url=url, chain=[(0, url)])
            self.link_status_cache[url] = status
            return status

        status = LinkStatus(
            status_code=resp.status_code,
            final_url=normalize_url(strip_fragment(resp.url)),
            chain=[(r.status_code, normalize_url(strip_fragment(r.url))) for r in (list(resp.history) + [resp])],
        )
        self.link_status_cache[url] = status
        return status

    def build_reports(self, pages: List[PageAudit], sitemap_urls: List[str], discovered_urls: List[str]) -> None:
        REPORTS_DIR.mkdir(parents=True, exist_ok=True)
        self._compute_inlinks_and_broken_links(pages, set(sitemap_urls))
        self._write_csv(pages)
        self._write_discovery_comparison_csvs(sitemap_urls, discovered_urls)
        self._write_issues_summary(pages, sitemap_urls, discovered_urls)
        self._write_redirect_suggestions(pages)

    def _compute_inlinks_and_broken_links(self, pages: List[PageAudit], sitemap_set: Set[str]) -> None:
        print("[4/6] Checking internal links and building link graph")
        all_outlinks: Set[str] = set()
        for page in pages:
            all_outlinks.update(page.outlinks_unique)
            for target in page.outlinks_unique:
                if target in sitemap_set:
                    self.inlink_counts[target] += 1

        checked = 0
        for url in sorted(all_outlinks):
            self.check_link_status(url)
            checked += 1
            if checked % 25 == 0:
                print(f"  - Checked {checked}/{len(all_outlinks)} internal link targets")

        for page in pages:
            page.internal_links_in_count = self.inlink_counts.get(page.url, 0)
            broken = []
            for target in sorted(page.outlinks_unique):
                status = self.link_status_cache.get(target)
                if status and status.status_code >= 400:
                    broken.append(target)
            page.broken_internal_links_out = broken
            if broken:
                page.notes.append(f"broken_internal_links:{len(broken)}")

    def _write_csv(self, pages: List[PageAudit]) -> None:
        print("[5/6] Writing reports/site_audit.csv")
        csv_path = REPORTS_DIR / "site_audit.csv"
        with csv_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=CSV_COLUMNS)
            writer.writeheader()
            for page in pages:
                writer.writerow(
                    {
                        "url": page.url,
                        "status_code": page.status_code,
                        "final_url": page.final_url,
                        "response_time_ms": page.response_time_ms,
                        "indexable (yes/no)": page.indexable,
                        "canonical": page.canonical,
                        "title": page.title,
                        "title_len": page.title_len,
                        "meta_description": page.meta_description,
                        "meta_description_len": page.meta_description_len,
                        "h1": page.h1,
                        "h1_count": page.h1_count,
                        "h2_count": page.h2_count,
                        "h3_count": page.h3_count,
                        "headings_outline": page.headings_outline,
                        "intro_text": page.intro_text,
                        "keyword_primary": page.keyword_primary,
                        "keyword_in_title (yes/no)": page.keyword_in_title,
                        "keyword_in_h1 (yes/no)": page.keyword_in_h1,
                        "keyword_in_intro (yes/no)": page.keyword_in_intro,
                        "keyword_density_primary_pct": page.keyword_density_primary_pct,
                        "keyword_counts_json": to_json(page.keyword_counts),
                        "internal_links_out_count": page.internal_links_out_count,
                        "internal_links_unique_out_count": page.internal_links_unique_out_count,
                        "internal_links_in_count": page.internal_links_in_count,
                        "broken_internal_links_out": to_json(page.broken_internal_links_out),
                        "word_count": page.word_count,
                        "schema_types": to_json(page.schema_types),
                        "og_title_present": page.og_title_present,
                        "og_description_present": page.og_description_present,
                        "og_url_present": page.og_url_present,
                        "notes": "; ".join(page.notes),
                    }
                )

    def _write_discovery_comparison_csvs(self, sitemap_urls: List[str], discovered_urls: List[str]) -> None:
        print("[5/6] Writing discovery comparison CSVs")
        sitemap_set = set(sitemap_urls)
        discovered_set = set(discovered_urls)
        sitemap_missing_from_crawl = sorted(sitemap_set - discovered_set)
        crawl_missing_from_sitemap = sorted(discovered_set - sitemap_set)

        with (REPORTS_DIR / "sitemap_missing_from_crawl.csv").open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["url"])
            writer.writeheader()
            for url in sitemap_missing_from_crawl:
                writer.writerow({"url": url})

        with (REPORTS_DIR / "crawl_missing_from_sitemap.csv").open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["url"])
            writer.writeheader()
            for url in crawl_missing_from_sitemap:
                writer.writerow({"url": url})

    def _write_issues_summary(self, pages: List[PageAudit], sitemap_urls: List[str], discovered_urls: List[str]) -> None:
        print("[5/6] Writing reports/issues_summary.md")
        path = REPORTS_DIR / "issues_summary.md"

        duplicates_h1 = self._find_duplicates([(p.url, p.h1) for p in pages if p.h1.strip()])
        duplicates_title = self._find_duplicates([(p.url, p.title) for p in pages if p.title.strip()])
        duplicates_desc = self._find_duplicates([(p.url, p.meta_description) for p in pages if p.meta_description.strip()])
        missing_h1 = [p.url for p in pages if p.h1_count == 0]
        missing_desc = [p.url for p in pages if not p.meta_description]
        missing_canonical = [p.url for p in pages if not p.canonical]
        missing_og = [p.url for p in pages if p.og_title_present == "no" or p.og_description_present == "no" or p.og_url_present == "no"]
        schema_missing = [p.url for p in pages if not p.schema_types]
        bad_status = [p for p in pages if p.status_code >= 400 or p.status_code == 0]
        redirecting_pages = [p for p in pages if len(p.redirect_chain) > 1]
        broken_links = [(p.url, p.broken_internal_links_out) for p in pages if p.broken_internal_links_out]
        orphans = [u for u in sitemap_urls if self.inlink_counts.get(u, 0) == 0]
        top_orphans = sorted(orphans)[:20]
        top_outlink_pages = sorted(
            [(p.url, p.internal_links_unique_out_count) for p in pages],
            key=lambda x: x[1],
            reverse=True,
        )[:20]
        sitemap_set = set(sitemap_urls)
        discovered_set = set(discovered_urls)
        sitemap_missing_from_crawl = sorted(sitemap_set - discovered_set)
        crawl_missing_from_sitemap = sorted(discovered_set - sitemap_set)

        high = [
            ("Broken internal links", len(broken_links), [f"{u} -> {links[0]}" for u, links in broken_links[:5]]),
            ("4xx/5xx or failed pages", len(bad_status), [f"{p.url} ({p.status_code})" for p in bad_status[:5]]),
            ("Missing H1", len(missing_h1), missing_h1[:5]),
            ("Duplicate titles", len(duplicates_title), [f"{t} ({len(us)} pages)" for t, us in list(duplicates_title.items())[:5]]),
            ("Duplicate meta descriptions", len(duplicates_desc), [f"{d[:90]} ({len(us)} pages)" for d, us in list(duplicates_desc.items())[:5]]),
        ]
        medium = [
            ("Orphan pages in sitemap", len(orphans), orphans[:5]),
            ("Missing canonical", len(missing_canonical), missing_canonical[:5]),
            ("Missing meta descriptions", len(missing_desc), missing_desc[:5]),
            ("Missing OG basics", len(missing_og), missing_og[:5]),
            ("Missing schema JSON-LD", len(schema_missing), schema_missing[:5]),
        ]
        low = [
            ("Redirecting URLs in sitemap", len(redirecting_pages), [f"{p.url} -> {p.final_url}" for p in redirecting_pages[:5]]),
            ("Duplicate H1", len(duplicates_h1), [f"{h} ({len(us)} pages)" for h, us in list(duplicates_h1.items())[:5]]),
        ]

        with path.open("w", encoding="utf-8") as f:
            f.write("# Local SEO Issues Summary\n\n")
            f.write(f"- Total pages audited: {len(pages)}\n")
            f.write(f"- Sitemap URLs discovered: {len(sitemap_urls)}\n\n")
            f.write(f"- Homepage crawl URLs discovered (depth 3): {len(discovered_urls)}\n")
            f.write(f"- Sitemap missing from crawl: {len(sitemap_missing_from_crawl)}\n")
            f.write(f"- Crawl missing from sitemap: {len(crawl_missing_from_sitemap)}\n\n")

            self._write_issue_group(f, "High Severity", high)
            self._write_issue_group(f, "Medium Severity", medium)
            self._write_issue_group(f, "Low Severity", low)
            f.write("## Top 20 Orphans\n\n")
            if top_orphans:
                for url in top_orphans:
                    f.write(f"- {url}\n")
            else:
                f.write("- None\n")
            f.write("\n")
            f.write("## Top 20 Pages by Internal Outlinks\n\n")
            if top_outlink_pages:
                for url, count in top_outlink_pages:
                    f.write(f"- {url} ({count})\n")
            else:
                f.write("- None\n")
            f.write("\n")

    def _write_issue_group(self, fh, title: str, issues: List[Tuple[str, int, List[str]]]) -> None:
        fh.write(f"## {title}\n\n")
        for name, count, examples in issues:
            fh.write(f"- **{name}**: {count}\n")
            for ex in examples:
                fh.write(f"  - {ex}\n")
        fh.write("\n")

    def _write_redirect_suggestions(self, pages: List[PageAudit]) -> None:
        print("[5/6] Writing reports/redirects_suggestions.txt")
        path = REPORTS_DIR / "redirects_suggestions.txt"
        seen_pairs: Set[Tuple[str, str]] = set()
        for page in pages:
            if page.url and page.final_url and page.url != page.final_url:
                seen_pairs.add((page.url, page.final_url))
            if len(page.redirect_chain) > 1:
                start = page.redirect_chain[0][1]
                end = page.redirect_chain[-1][1]
                if start != end:
                    seen_pairs.add((start, end))
            for target in page.outlinks_unique:
                status = self.link_status_cache.get(target)
                if status and status.final_url and status.final_url != target and status.status_code < 400:
                    seen_pairs.add((target, status.final_url))

        with path.open("w", encoding="utf-8") as f:
            f.write("301 Redirect Suggestions\n")
            f.write("========================\n\n")
            if not seen_pairs:
                f.write("No redirect candidates detected from sitemap pages and internal links.\n")
                return
            for old, new in sorted(seen_pairs):
                f.write(f"301 {old} -> {new}\n")

    def _find_duplicates(self, pairs: Iterable[Tuple[str, str]]) -> Dict[str, List[str]]:
        grouping: Dict[str, List[str]] = defaultdict(list)
        for url, value in pairs:
            normalized = normalize_whitespace(value).lower()
            if normalized:
                grouping[normalized].append(url)
        return {k: v for k, v in grouping.items() if len(v) > 1}


def load_keywords(path: str) -> List[str]:
    keywords = []
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            keywords.append(line)
    return keywords


def run_audit(
    sitemap_url: str,
    keywords_file: str,
    root_domain: Optional[str] = None,
    discovery_mode: str = "homepage",
    crawl_depth: int = 3,
) -> None:
    keywords = load_keywords(keywords_file)
    if not keywords:
        raise ValueError("No keywords found. Add one keyword per line in the keywords file.")

    if crawl_depth < 0:
        raise ValueError("--crawl-depth must be 0 or greater.")

    auditor = SiteAuditor(sitemap_url=sitemap_url, keywords=keywords, root_domain=root_domain)
    sitemap_urls = auditor.fetch_sitemap_urls()
    if not sitemap_urls:
        raise ValueError("No URLs discovered from sitemap.")

    discovered_urls = []
    if discovery_mode == "homepage":
        homepage = normalize_url(strip_fragment(auditor.root_domain))
        discovered_urls = auditor.crawl_discovered_urls(start_url=homepage, max_depth=crawl_depth)
    else:
        discovered_urls = sorted(set(sitemap_urls))

    print(f"[3/6] Auditing {len(sitemap_urls)} page(s)")
    pages: List[PageAudit] = []
    for idx, url in enumerate(sitemap_urls, start=1):
        print(f"  - ({idx}/{len(sitemap_urls)}) {url}")
        page = auditor.audit_page(url)
        pages.append(page)

    auditor.build_reports(pages, sitemap_urls, discovered_urls)
    print("[6/6] Audit complete.")
    print(f"Reports written to: {REPORTS_DIR.resolve()}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Local SEO Site Auditor")
    parser.add_argument("--sitemap", required=True, help="Sitemap URL (e.g., https://example.com/sitemap.xml)")
    parser.add_argument("--keywords", required=True, help="Path to keywords text file (one keyword per line)")
    parser.add_argument(
        "--root-domain",
        default=None,
        help="Root domain for internal-link matching (default: derived from sitemap URL)",
    )
    parser.add_argument(
        "--discovery-mode",
        choices=["homepage", "none"],
        default="homepage",
        help="How to discover crawl URLs for sitemap comparison (default: homepage)",
    )
    parser.add_argument(
        "--crawl-depth",
        type=int,
        default=3,
        help="Depth for homepage discovery crawl when --discovery-mode homepage (default: 3)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    run_audit(
        sitemap_url=args.sitemap,
        keywords_file=args.keywords,
        root_domain=args.root_domain,
        discovery_mode=args.discovery_mode,
        crawl_depth=args.crawl_depth,
    )


if __name__ == "__main__":
    main()
