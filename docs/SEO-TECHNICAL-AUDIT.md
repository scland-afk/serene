# SEO & Technical Audit – Serene Landscaping

**Date:** January 2026  
**Scope:** Meta tags, headings, links, images, schema, accessibility, sitemap, robots, performance.

---

## ✅ What’s in good shape

- **Canonical URLs:** Every page has `<link rel="canonical" href="{{ client.domain }}{{ page.url }}">`.
- **Meta description:** All audited content pages define `description` in front matter (50–160 chars, unique per page).
- **Keywords:** Optional `keywords` used where set; base layout outputs them only when present.
- **Open Graph & Twitter:** og:title, og:description, og:url, og:image; twitter:card, title, description, image.
- **Single H1 per page:** Content pages use one `<h1 class="cs-title">`; hierarchy is logical.
- **Image alt text:** No empty `alt=""` in the sampled content; hero/blog use descriptive alts.
- **Internal links:** Location/service links point to valid permalinks (e.g. `/locations/`, `/services/`, `/contact/`).
- **Sitemap:** `@quasibit/eleventy-plugin-sitemap` generates `/sitemap.xml`; config uses `client.domain`.
- **Robots:** `robots.html` outputs `User-agent: *`, `Allow: /`, and `Sitemap: {{ client.domain }}/sitemap.xml`.
- **Skip link:** Base layout includes “Skip to main content” with `aria-label` and `#main`.
- **Schema:** Service and FAQ JSON-LD present on service/location pages where checked.
- **Favicons & manifest:** Multiple favicon sizes, SVG, apple-touch-icon, `site.webmanifest`.

---

## 🔧 Fixes applied in this pass

1. **Blog empty state H1**  
   When `collections.post` is empty, the page used `<h1>No Recent Posts</h1>`, which is weak for SEO.  
   **Change:** Use a consistent, keyword-friendly H1 for the blog page (e.g. “Landscaping Blog | Edmonton Tips & Advice”) so the blog URL always has a strong, relevant H1.

2. **Default meta description**  
   If any page ever omits `description`, `{{ description }}` would output nothing.  
   **Change:** In the base layout, use a fallback (e.g. `description or defaultDescription`) so meta description and og:description are never blank.

3. **FAQ accordion accessibility**  
   FAQ toggles are `<button>` elements but did not expose expanded/collapsed state to assistive tech.  
   **Change:** In `faq.js`, set `aria-expanded` (and optionally `aria-controls`/`id` on the answer) so screen readers announce open/closed state.

---

## 📋 Recommendations (no code changes in this pass)

### SEO

- **Title length:** Keep `<title>` roughly 50–60 characters where possible; some service/location titles are longer—consider shortening if you see truncation in SERPs.
- **Structured data:** Consider adding `LocalBusiness` (or `Organization`) once on the homepage or contact page with address, phone, and service area.
- **Blog listing:** When you have posts, ensure the blog index has a single, clear H1 (e.g. “Landscaping Blog”) and that each post has its own H1 in the post layout.
- **Image OG:** Important pages (home, key services, locations) could set front matter `image` to a representative image URL so shares use a real photo instead of the default apple-touch-icon.

### Technical

- **Client name:** `_data/client.js` uses `name: "Serene Construction Landscaping"`. If the brand is “Serene Landscaping”, consider a display name (e.g. `name: "Serene Landscaping"` and keep legal name elsewhere) so meta/app titles and OG are consistent with branding.
- **robots.txt:** `robots.html` uses `{{ client.domain }}`; with Eleventy global data this should render. After deploy, confirm `/robots.txt` shows `Sitemap: https://serenelandscapes.ca/sitemap.xml`.
- **Duplicate section IDs:** Many pages use the same section IDs (`id="banner"`, `id="content-page-1398"`, `id="faq-489"`). That’s valid as long as each page has at most one of each; avoid reusing the same ID twice on one page.
- **GA in head:** Google Analytics is in `<head>`; if you later optimize LCP, consider loading GA after first paint (e.g. defer or load after `window.load`).

### Accessibility

- **FAQ:** After adding `aria-expanded`, consider associating each button with its answer panel via `aria-controls` and a unique `id` on the answer block.
- **Decorative images:** Hero/background images that are decorative use `aria-hidden="true"` where checked; keep that pattern for any new decorative images.
- **Form labels:** Exit-intent and contact forms—ensure every input has a visible or `aria-label` so screen readers can name the field.

---

## Summary

- **SEO:** Solid foundations (canonical, meta, OG, one H1, internal links, sitemap, robots). Small improvements: blog H1 when empty, default description, and optional title/OG image tweaks.
- **Technical:** Sitemap and robots set up correctly; client name and GA placement are the main follow-ups.
- **Accessibility:** FAQ accordion is the main fix (aria-expanded); optional aria-controls and form labels for full compliance.

Applying the three code changes above will address the only concrete SEO and a11y issues found in the audit.
