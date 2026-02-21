# Local SEO Implementation (Service + City Pages Strategy)

Summary of what was implemented from the local SEO guide (service/city pages, GMB alignment, internal linking) and what to do next.

---

## Strategy (from the guide)

- **One city + one service = one target keyword.** Don’t target the same city+service with two pages (avoid cannibalization).
- **Home = primary city silo.** Use the home page for your main city + primary offer (e.g. “Landscaping Edmonton”).
- **City pages** = one top-level page per area you care about (e.g. “Edmonton Landscaping Company”, “St. Albert Landscaping”).
- **Internal linking:** Use search-rich anchor text to the home page (e.g. “Serene Landscaping Edmonton”, “Landscaping Edmonton”) not only “Home” or the business name.
- **Don’t overlink.** Link key pages to each other; keep silos clear.
- **Align site with GMB:** Same business name, hours, service areas, and NAP (name, address, phone) where you show it.

---

## Implemented on this site

### 1. GMB alignment
- **Hours:** Site schema `openingHours` updated to match GMB (Mon–Fri 7am–8pm, Sat–Sun 8am–7pm). See `_includes/components/home-schema.html`.
- **Service areas:** Footer “Service Areas” now lists Edmonton, St. Albert, Sherwood Park (linked) plus “Also: Spruce Grove, Stony Plain, Leduc, Beaumont, Fort Saskatchewan, Devon, Morinville” so the site matches schema and GMB service area.
- **Categories:** Schema `serviceType` aligned with GMB: Landscaper, Lawn care service, Fence contractor, Paving contractor, Landscape designer, Landscape architect, Property maintenance, Snow removal service (plus Sod Installation, Retaining Walls, Final Grading, Artificial Grass, Commercial Landscaping).
- **Schema:** `areaServed` and business description already include these cities; NAP and `sameAs` (Google Maps) are in place.

### 2. Cannibalization (home vs Edmonton page)
- **Home (/):** Kept as primary target for “Landscaping Edmonton” (title, content, internal links).
- **Edmonton location page** (`/locations/edmonton-landscaping-company/`): Title and description shifted to “Edmonton Landscaping Company” / “Landscaping company in Edmonton” so it targets a different query than the home page.

### 3. Internal linking (search-rich anchors to home)
- **Footer – Sitemap:** Added “Serene Landscaping Edmonton” linking to `/` (in addition to “Landscaping Edmonton” in Popular Searches).
- **Footer – Popular Searches:** Already had “Landscaping Edmonton” → home; kept as-is.
- **Location page:** Edmonton page already had “Serene Landscaping in Edmonton” → home in body copy.

### 4. Service areas in footer
- “Also: Spruce Grove, Stony Plain, Leduc, Beaumont, Fort Saskatchewan, Devon, Morinville” added under the three linked city pages so the full service area is visible and aligned with GMB/schema. Styled with `.cs-nav-muted` so it reads as supporting text.

---

## Recommendations (next steps)

1. **GMB:** In Google Business Profile, set service areas (if you use a service-area business) to the same cities as on the site and in schema. Keep primary category and services in line with the site (e.g. Landscaper, Snow removal service).
2. **More city pages (if there’s volume):** The guide suggests one top-level page per city/area you want to rank in. You have Edmonton, St. Albert, Sherwood Park. If you see search volume for “landscaping Spruce Grove”, “landscaping Leduc”, etc., add one page per area and target one main keyword per page.
3. **Keyword checks:** Use your SEO tool to confirm one primary term per page (e.g. home = “Landscaping Edmonton”, Edmonton location = “Edmonton landscaping company”) and that you’re not doubling up.
4. **Silos:** Keep linking service pages to the right location pages (e.g. “St. Albert landscaping” from service pages) and location pages to services; avoid stuffing too many links on one page.
5. **Reviews and Maps:** The guide notes that Maps impact is hard to tie 1:1 to one page, but strong local content and consistent NAP/service area help. Keep encouraging Google reviews and keep the sameAs (Google Maps) link in schema.

---

## Files changed

| File | Change |
|------|--------|
| `_includes/sections/footer.html` | Sitemap link “Serene Landscaping Edmonton” → `/`; Service Areas “Also: Spruce Grove, …” line. |
| `_includes/components/home-schema.html` | (Earlier) `openingHours` set to GMB hours. |
| `content/pages/locations/edmonton.html` | Title “Edmonton Landscaping Company”, description “Landscaping company in Edmonton…”. |
| `assets/sass/root.scss` | `.cs-nav-muted` for footer “Also serving” text. |

---

*Strategy source: Local SEO Service & City Pages Strategy (home = primary city, one term per page, search-rich internal links, GMB alignment).*
