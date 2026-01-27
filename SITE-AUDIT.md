# Serene Landscaping — Site Audit

**Date:** January 27, 2026  
**Scope:** Content consistency, SEO, technical checks, accessibility, and build health.

---

## 1. Content consistency (recent updates)

### 1.1 “Since 2014,” “bonded,” “deposits” → removed/updated

| Check | Status |
|-------|--------|
| “since 2014” removed | **Pass** — No instances |
| “bonded” removed | **Pass** — No instances |
| Deposits → “progressive payments only” | **Pass** — Contact page + choose-landscaper blog updated |

The only “10 years” left is in `patio-cost-edmonton.md` (“fails within 5-10 years”), referring to patio lifespan, not company experience. Correct to keep.

### 1.2 Experience (“8+ years”)

| Location | Status |
|----------|--------|
| About, CTA, residential, portfolio, lawn-maintenance, snow-removal, landscape-design, final-grading, hardscaping | **Pass** — “8+ years” / “over 8 years” used consistently |
| Location pages (Edmonton, St. Albert, Spruce Grove, Sherwood Park) | **Pass** — “8+ years” present |
| **Stony Plain** location page | **Warning** — Uses “years of experience” only; no “8+ years.” Consider aligning with other location pages. |

### 1.3 Progressive payments

- **Contact FAQ:** “we use progressive payments only” ✓  
- **Choose-landscaper blog:** Payment sections and FAQ use “progressive payments only” ✓  

---

## 2. SEO

### 2.1 Meta descriptions

- All main pages have unique `description` in front matter ✓  
- **Issue:** The three commercial subpages share the **same** meta description:
  - `commercial-landscaping`
  - `commercial-maintenance`
  - `commercial-snow-removal`  

  **Recommendation:** Give each a distinct description (e.g. focus on “commercial landscaping” vs “commercial maintenance” vs “commercial snow removal”) to avoid duplicate meta and improve snippet differentiation.

### 2.2 Canonical & OG

- Canonical: `{{ client.domain }}{{ page.url }}` in `base.html` ✓  
- OG title, description, url, image use `client.domain` ✓  
- `client.domain`: `https://serenelandscapes.ca` (no trailing slash) ✓  

### 2.3 Structured data

| Page(s) | Schema |
|---------|--------|
| About, Contact, Edmonton, Portfolio, Residential, Commercial, Snow removal, Lawn maintenance | FAQPage ✓ |
| Service pages (snow, lawn, landscape-design, final-grading, hardscaping, commercial-*) | Service ✓ |
| Blog posts | Article schema **disabled** — `post-schema.html` is commented out in `layouts/post.html` |

**Recommendation:** Consider enabling `post-schema.html` for blog posts to support Article rich results.

### 2.4 H1s and headings

- Each page has a single H1 (`cs-title` or `cs-article-title`) ✓  
- FAQ sections use H2 consistently ✓  
- **Stony Plain:** FAQ section uses “Frequently Asked Questions” instead of “Questions About [Stony Plain Landscaping].” Minor inconsistency with other location pages.

---

## 3. Technical

### 3.1 Build

- **Eleventy:** HTML generation succeeds (32 files).  
- **Post-build:** `esbuild` (JS bundle) fails with `spawn EPERM` in this environment. Likely sandbox/permissions, not template or content. Worth confirming `npm run build` completes locally.

### 3.2 SASS

- Dart Sass `@import` deprecation warnings in `local.scss` (e.g. `services`, `why-choose`, `content-page`). Non-blocking; plan migration to `@use` / `@forward` before Dart Sass 3.0.

### 3.3 Blog “Featured” collection

- `featured-posts.html` loops over `collections.featured`.  
- No `featured` tag or custom `featured` collection found; only `post` is used.  
- **Risk:** `collections.featured` may be undefined or empty. The sidebar “Featured Posts” may never show items.  

**Recommendation:** Either add a `featured` tag to selected posts and an `addCollection` that filters `collections.post` by it, or change the component to use `collections.post` (e.g. latest N posts).

### 3.4 Blog image `alt` vs `imageAlt`

- **Front matter:** Blog posts use `imageAlt`.  
- **Templates:**  
  - `layouts/post.html`: `alt="{{ alt }}"`  
  - `blog.html` listing and `featured-posts.html`: `post.data.alt`  
- **Result:** `alt` is never set; `imageAlt` is not used. Blog images effectively have empty `alt`.  

**Recommendation:** Use `imageAlt` in templates (e.g. `alt="{{ imageAlt }}"`, `post.data.imageAlt`) or add `eleventyComputed` to map `imageAlt` → `alt`, then use `alt` everywhere.

---

## 4. Internal links & CTAs

### 4.1 Contact links

- `/contact/` used consistently for CTAs and “Contact us” contextual links ✓  
- Footer, header, CTA, and service/location pages all link to `/contact/` ✓  

### 4.2 Service areas

- “Major Service Areas” and “Also Serving” plus “Contact us” link appear on contact, service, and commercial pages ✓  
- Pattern matches previous standardization ✓  

### 4.3 Blog CTAs

- Blog CTAs list Edmonton, St. Albert, Spruce Grove, Sherwood Park.  
- **Stony Plain** is not mentioned in blog CTAs, while the main CTA and service areas include it. Optional tweak: add Stony Plain to blog CTAs for consistency.

---

## 5. Client/brand data

- **`_data/client.js`:**  
  - `name`: “Serene Construction Landscaping”  
  - `domain`: `https://serenelandscapes.ca`  
- **Site content:** Mostly “Serene Landscaping.”  
- **Footer:** “© 2026 Serene Construction Landscaping.”  

If “Serene Construction Landscaping” is the legal name and “Serene Landscaping” the brand, this is fine. Otherwise, consider aligning.

---

## 6. Sitemap & robots

- `robots.html` outputs `Sitemap: {{ client.domain }}/sitemap.xml` ✓  
- Sitemap plugin uses `client.domain` ✓  
- `Disallow: /admin/`; `Allow: /` ✓  

---

## 7. Summary of recommended actions

| Priority | Item | Action |
|----------|------|--------|
| **High** | Blog image `alt` | Use `imageAlt` (or map to `alt`) in post layout, blog listing, and featured-posts |
| **High** | Commercial meta descriptions | Write unique descriptions for commercial-landscaping, commercial-maintenance, commercial-snow-removal |
| **Medium** | `collections.featured` | Define a `featured` collection or switch featured-posts to e.g. `collections.post` |
| **Medium** | Stony Plain “8+ years” | Add “8+ years” to Stony Plain location page to match other locations |
| **Low** | Stony Plain FAQ heading | Optionally change to “Questions About Stony Plain Landscaping” for consistency |
| **Low** | Blog Article schema | Enable `post-schema.html` for blog layout |
| **Low** | SASS `@import` | Plan move to `@use` / `@forward` |
| **Low** | Blog CTAs + Stony Plain | Optionally add Stony Plain to blog CTA city lists |

---

## 8. Quick reference

- **Pages:** 33 HTML templates (including layout/includes).  
- **Blog:** 9 posts; all have `description` and `imageAlt`.  
- **Service areas:** Edmonton, St. Albert, Spruce Grove, Sherwood Park, Stony Plain.  
- **Canonical base:** `https://serenelandscapes.ca`.
