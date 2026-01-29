# SEO Elements Checklist

Status of sitemap, robots, llms.txt, and other SEO elements in the project.

---

## 1. sitemap.xml

| Item | Status | Details |
|------|--------|--------|
| **File** | OK | `src/sitemap.html` → built as `/sitemap.xml` |
| **Plugin** | OK | `@quasibit/eleventy-plugin-sitemap` (config: `src/config/plugins/sitemap.js`) |
| **Domain** | OK | Uses `client.domain` from `src/_data/client.js` (https://serenelandscapes.ca) |
| **Which pages** | OK | All pages with tag `sitemap`: homepage (`src/index.html`) and all content under `src/content/` (via `src/content/content.json` which sets `tags: "sitemap"`). Sitemap template itself has `eleventyExcludeFromCollections: true` so it is not listed. |

**URL when live:** `https://serenelandscapes.ca/sitemap.xml`

---

## 2. robots.txt

| Item | Status | Details |
|------|--------|--------|
| **File** | OK | `src/robots.html` → built as `/robots.txt` |
| **Rules** | OK | `User-agent: *`, `Disallow: /admin/`, `Allow: /` |
| **Sitemap** | OK | `Sitemap: {{ client.domain }}/sitemap.xml` (uses live domain from client.js) |

**URL when live:** `https://serenelandscapes.ca/robots.txt`

---

## 3. llms.txt (AI / LLM crawler)

| Item | Status | Details |
|------|--------|--------|
| **Source** | OK | `src/llms.txt` |
| **Build** | Fixed | Passthrough added in `.eleventy.js` so it is copied to `public/llms.txt` and served at `/llms.txt`. (Previously it was not in the build output.) |
| **Content** | OK | Service links (serenelandscapes.ca), areas, contact. Update URLs here if you ever change domain. |

**URL when live:** `https://serenelandscapes.ca/llms.txt`

---

## 4. Other SEO elements

### Canonical & Open Graph (per page)

- **Where:** `src/_includes/layouts/base.html`
- **Uses:** `{{ client.domain }}{{ page.url }}` and `{{ image }}` from front matter
- **Set:** Canonical, `og:url`, `og:title`, `og:description`, `og:image`, `og:image:secure_url`, `og:type`
- **Domain:** From `src/_data/client.js` → `domain`

### Meta description & keywords

- **Where:** `src/_includes/layouts/base.html`
- **Set:** `<meta name="description">`, optional `<meta name="keywords">` from page front matter
- **Per page:** Each page sets `description` and `keywords` in front matter

### JSON-LD (Schema.org)

- **Home:** `src/_includes/components/home-schema.html` (LandscapingBusiness)
- **Posts:** `src/_includes/components/post-schema.html`
- **FAQ:** `src/_includes/components/faq-schema.html`, `location-faq.html`
- **Services:** `src/_includes/components/service-schema.html`
- **Per-page:** Many pages include their own `application/ld+json` (ContactPage, Service, LocalBusiness, FAQPage, etc.) in the page template

### Review / aggregate rating (home)

- **Where:** `src/index.html` (Review items with `itemprop`) and home-schema (AggregateRating)
- **Set:** Review snippets and overall rating in schema

---

## 5. Quick verification after deploy

1. **Sitemap:** Open `https://serenelandscapes.ca/sitemap.xml` and confirm it lists your main pages.
2. **Robots:** Open `https://serenelandscapes.ca/robots.txt` and confirm `Sitemap:` points to your domain.
3. **llms.txt:** Open `https://serenelandscapes.ca/llms.txt` and confirm content and links are correct.
4. **Canonical / OG:** View source on a few pages and confirm canonical and `og:url` use `https://serenelandscapes.ca/...`.

---

## 6. If you change domain

- **`src/_data/client.js`** → Update `domain` (and `email` if needed).
- **`src/llms.txt`** → Replace all `https://serenelandscapes.ca/...` with the new domain.
- **Netlify** → Add new domain and DNS; no code change needed for sitemap/robots (they use `client.domain`).
