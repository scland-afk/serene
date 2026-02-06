# Location Pages – SEO Refactor Summary

## The Problem

The five location pages (Edmonton, St. Albert, Sherwood Park, Spruce Grove, Stony Plain) had **heavy duplication**:

- Same structure: long intro, six "Service in [City]" h2+paragraph blocks, "Trusted Company" section, service bullets, coverage, FAQ.
- Most copy was identical except the city name (find‑and‑replace style).
- Same FAQs with only the city swapped.

This creates **thin/duplicate content** risk and hurts SEO. Guidance (e.g. Moz, Search Engine Land) suggests **~90%+ unique content** between location pages and **minimal boilerplate**.

---

## What We Did

### 1. **Data-driven setup**

- **`_data/locations.js`** – One source of truth per city:
  - `city`, `h1`, `intro`, `neighborhoods`, `nearby`, `coverage`, `bannerImage`, `contentImage`, `faqs`.
- **`layouts/location.html`** – Single layout that reads `locations[locationKey]` and renders banner, content, FAQ, CTA.
- Each location page is a **minimal template**: front matter (`title`, `description`, `keywords`, `permalink`, `locationKey`) + `extends layouts/location.html`.

### 2. **Shared includes (minimal boilerplate)**

- **`location-services-list.html`** – One "Services we offer" section: short intro + **linked** bullet list to service pages. No more six long "Service in [City]" paragraphs.
- **`location-trusted.html`** – Single "Trusted Landscaping Company" block with **generic** copy (no city). Same on all location pages.
- **`location-faq.html`** – FAQ section + FAQ schema, driven by `loc.faqs` from data.

### 3. **Unique, local-focused content**

- **Intro** – One short paragraph per city; mentions neighborhoods and local context.
- **Service Area Coverage** – Unique per city (neighborhoods, nearby towns).
- **FAQs** – **Varied per city**: different questions and answers where it makes sense (e.g. Edmonton: West Edmonton/Mill Woods; St. Albert: Braeside/Erin Ridge; Stony Plain: cost, commercial). Stored in `locations.js`.

### 4. **Typos and consistency**

- Removed double spaces (e.g. "We provide  landscaping").
- Fixed "proper drainage and  for" → "proper drainage and [topsoil prep] for".
- Fixed "St. Albert's climate, ," (double comma).
- "Asked questions" (Stony Plain) → "FAQ" / "Questions About [City] Landscaping?".

---

## SEO Benefits

- **Less duplication** – No long, repeated "Service in [City]" blocks; shared services list and trusted block only.
- **More unique content** – Unique intros, coverage, and FAQs per city.
- **Easier maintenance** – Change services or trusted copy in one place; add a city by adding data + one small page.
- **Clean structure** – Clear separation of shared vs. city-specific content.

---

## Optional Next Steps

- **CTA image alt** – The global CTA uses `alt="landscaping services Edmonton"`. You could make it generic (e.g. "landscaping services in Edmonton and area") or leave as is.
- **City-specific images** – Right now the content image is the same for all cities. You could add per‑city `contentImage` in `locations.js` when you have local photos.
- **Schema** – Consider `LocalBusiness` + `areaServed` per location if you want richer local SEO signals.

---

## Files Touched

- **Added:** `_data/locations.js`, `_includes/layouts/location.html`, `_includes/sections/location-services-list.html`, `_includes/sections/location-trusted.html`, `_includes/sections/location-faq.html`, `LOCATION-PAGES-SEO.md`
- **Replaced:** `locations/edmonton.html`, `locations/st-albert.html`, `locations/sherwood-park.html`, `locations/spruce-grove.html`, `locations/stony-plain.html` (now minimal templates using the layout)
