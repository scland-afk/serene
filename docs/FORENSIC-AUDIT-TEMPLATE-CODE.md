# Full Forensic Audit: Template / Demo Code

**Site:** serenelandscapes.ca  
**Template source mentioned:** metrosolutionsdemo.netlify.app (no direct references found; repo is CodeStitch Intermediate-Website-Kit-SASS)  
**Audit date:** 2026-02-08  

---

## 1. External References to Original Demo Site

**References to "metrosolutionsdemo" or "metro" (demo):**  
**NONE FOUND** in `src/`, HTML, CSS, or JS.

**Other netlify.app / template URLs:**
- `docs/seo-guidelines.md` line 155: `https://intermediate-astro-kit-decap-cms.netlify.app/` (example URL in docs)
- `docs/NETLIFY-DEPLOY.md`: generic "your-site-name.netlify.app"
- `docs/README.md`: `testing-decapbridge.netlify.app` (example Decap URL)

**Conclusion:** No metrosolutionsdemo or metro-demo references in application code. Repo points to **CodeStitchOfficial/Intermediate-Website-Kit-SASS** in `package.json` (homepage), not Metro Solutions.

---

## 2. Unused CSS Selectors

**Selectors that have NO matching element in the codebase:**

| Selector | File | Line (approx) | Notes |
|----------|------|----------------|------|
| `#hero-1786` | critical.scss | 125, 270, 279 | Homepage uses `#banner`, not hero-1786. Template hero ID. |
| `#h-services-143` | critical.scss | 303, 382, 407, 425 | Homepage uses `#services-1749`. Template services card ID. |
| `#cta-51` | root.scss | 1646+ | No HTML uses `id="cta-51"`. CTA section uses other IDs. |
| `#faq-1261` | root.scss | 2545, 2760, 2775 | No HTML uses `id="faq-1261"`. Site uses `#faq-489`. |
| `#why-choose-12` | why-choose.scss | 7, 170, 187, 198 | HTML uses `#why-choose-1824`. Template variant ID. |
| `#services-264` | services.scss | 7, 168, 200, 210 | No HTML uses `id="services-264"`. Site uses `#services-1749`. |
| `#gallery-4` | local.scss | 931, 999, 1008 | No HTML with `id="gallery-4"` found. |
| `#gallery-43` | local.scss | 1362, 1546, 1561, 1570, 1633 | No HTML with `id="gallery-43"` found. |
| `#gallery-44` | local.scss | 1651, 1759, 1774, 1783 | No HTML with `id="gallery-44"` found. |

**Total: 9 unused ID-based selector groups** (multiple rules each).  

**Recommendation:** Remove or comment out the above blocks to reduce CSS size and confusion. If you plan to add pages that use #gallery-43 / #gallery-44 (e.g. location galleries), keep those and add the matching HTML.

---

## 3. Suspicious Code

**A. Hidden elements**

- **base.html** ~204: `<div id="exit-intent-popup" ... style="display: none;">` – **Legitimate.** Popup shown on interaction.
- **base.html** ~141, 161: `.sticky-quote-button { display: none }` and `.is-visible { display: flex }` – **Legitimate.** Sticky CTA.
- **contact.html** ~100: `<p id="form-success" ... style="display: none;">` – **Legitimate.** Shown after form submit.
- **critical.scss / root.scss / local.scss:** Various `display: none` / `visibility: hidden` for skip link, dark/light toggles, nav states, gallery hidden panels – **Legitimate.**

**No hidden iframes, tracking pixels, or off-screen trackers found.**

**B. External scripts (see Section 6)**

**C. Inline scripts**

- **base.html** (production only): GA4 + Clarity loader (delayed). Uses your IDs: `G-VPZBBTMB1R`, `vcjpxa0bzr`. **Legitimate.**

**D. Tracking pixels**

- **None** found (no `<img src="...track...">` or similar).

---

## 4. Template-Specific File Structure

**Folders/files checked:**

- No `/demo/`, `/template/`, `/sample/`, `/example/`, `/placeholder/` folders.
- No `demo.html`, `template-page.md`, `sample-content.md`, `example-*.js`, `placeholder-*.css`.
- **src/content/pages/_template.txt** – **Not demo code.** Kit template for creating new pages (front matter + extends base). **Keep.**

**Conclusion:** No template/demo artifact folders or files.

---

## 5. CSS Files and Duplicates

**Actual CSS output (public/assets/css/):**

- about.css, blog.css, contact.css, **content-page.css**, **critical.css**, **local.css**, projects.css, reviews.css, root.css, services.css, why-choose.css  
- **No file named critical-root.css.** (If you see it elsewhere, it may be from another build or old deploy.)

**A. Duplicate / overlapping rules (known from prior audit)**

- `#banner`: minimal block in **critical.scss** (LCP); full block in **content-page.scss** (local.css). Intentional for performance.
- `.cs-button-solid`: global in **root.scss**; overrides in **critical.scss**, **content-page.scss**, **local.scss** in section-specific blocks. Consider consolidating to one global + minimal overrides.

**B. Unused page-specific CSS**

- **root.scss:** `#faq-1261`, `#cta-51` – no matching HTML (see Section 2).
- **critical.scss:** `#hero-1786`, `#h-services-143` – no matching HTML.
- **why-choose.scss:** `#why-choose-12` – HTML uses `#why-choose-1824`.
- **services.scss:** `#services-264` – no matching HTML.
- **local.scss:** `#gallery-4`, `#gallery-43`, `#gallery-44` – no matching HTML in scanned templates.

**C. Demo-specific variables**

- **None** found. Variables use names like `--primary`, `--headerColor`, `--bodyTextColorWhite` and Serene brand colors. No `$demo-*`, `$template-*`, or `--metro-*`.

---

## 6. JavaScript Audit

**Scripts in repo (src/assets/js/):**

- dark.js, faq.js, gallery-2235.js, gallery-2281-lightbox.js, gallery-2281.js, gallery-48-lightbox.js, nav.js, touch-interactions.js, why-choose-1824.js

**A. Template/demo references**

- **None** found (no "metro", "metrosolutionsdemo", "demoMode", "templateID", or demo URLs).

**B. Orphaned / unused script**

- **gallery-2235.js** – **Not referenced** in any HTML. Scripts loaded in base or pages: dark, nav, faq, touch-interactions, gallery-48-lightbox (index), gallery-2281, why-choose-1824. **Recommendation:** Remove or ignore; if you never had a “gallery-2235” section, it’s template leftover.

**C. Third-party integrations**

- **base.html (production):** Google Tag Manager (gtag.js, GA_ID `G-VPZBBTMB1R`), Microsoft Clarity (`vcjpxa0bzr`). **Known and intentional.**

**D. API keys / tracking IDs**

- GA and Clarity IDs are in base.html; appear to be yours. No other hardcoded API keys or unknown tracking IDs found.

---

## 7. HTML Template Artifacts

**A. Demo content**

- **None** found (no “Metro Solutions Demo”, “REPLACE”, or obvious template-only text in live sections).

**B. Template comments**

- **index.html** ~30: “Uncomment the code below to enable Structured Data…” – **Legitimate** dev comment.
- **content-page.scss** ~7: “#banner-559 and #content-page-713 are already in root.css” – **Legitimate** note.

**C. Placeholder images**

- **DigitalOcean CDN (template asset):**
  - **index.html** (lines 836–838), **cta.html** (51–53): `https://csimg.nyc3.cdn.digitaloceanspaces.com/Contact-Page/house.jpg` – generic “house” image. **Recommendation:** Replace with your own image and path (e.g. `/assets/images/...`) for branding and to avoid third-party dependency.
  - **index.html** (683, 692, 701, 710): `https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Icons/gym-arrow.svg` – **“gym”** path is template/kit naming; icon is a generic arrow. **Recommendation:** Copy arrow SVG to `/assets/svgs/` and reference locally so you don’t rely on kit CDN.

**D. Template-specific IDs/classes in HTML**

- No `id="metro-hero"`, `class="template-section"`, or `class="demo-wrapper"` found. IDs/classes are kit-style (e.g. `cs-*`, `#banner`, `#content-page-1398`).

---

## 8. Inline Styles (~153 bytes or similar)

**Location:** `src/_includes/layouts/base.html` lines 126–189.

**Content:** Single `<style>` block containing:

- `.sticky-quote-button` – fixed CTA button (default hidden, `.is-visible` shows it).
- `.exit-intent-popup` – full-screen overlay for exit-intent offer.
- `.exit-intent-content` – modal content box.
- `.exit-close` – close button.

**Purpose:** Above-the-fold UI for sticky “View Offer” and exit-intent popup. No tracking or hidden elements.

**Recommendation:** **Keep.** Optionally move to a small `popups.css` and load it on pages that use the popup if you want to reduce inline size; otherwise leaving as-is is fine.

---

## 9. Third-Party Resources

**External origins loaded from HTML/templates:**

| Domain | Purpose | Verdict |
|--------|--------|--------|
| www.googletagmanager.com | GA4 (G-VPZBBTMB1R) | ✅ Known |
| www.clarity.ms, scripts.clarity.ms | Microsoft Clarity | ✅ Known |
| csimg.nyc3.cdn.digitaloceanspaces.com | Icons (phone, mail, pin, down, gym-arrow, red-check), Contact-Page/house.jpg | ⚠️ Template CDN – replace with own assets where possible |
| widgets.sociablekit.com | Google Reviews iframe (index.html ~613) | ✅ Known (reviews widget) |
| schema.org (in JSON-LD) | Structured data | ✅ Standard |
| maps.app.goo.gl / google.com/maps | Map link in header | ✅ Known |
| developers.google.com (in comment) | Doc link for structured data | ✅ Comment only |

**No unexpected tracking domains or links to metrosolutionsdemo.**

---

## 10. Package Dependencies

**package.json:** No template- or demo-specific packages. Dependencies are standard for the stack:

- Eleventy, CodeStitch plugins (minify, sharp-images), sitemap, Decap, Sass, PostCSS, etc.
- **Repository:** `git+https://github.com/CodeStitchOfficial/Intermediate-Website-Kit-SASS.git` – CodeStitch kit, not Metro Solutions.

**No packages named *demo*, *template*, or *metro*.**

---

## 11. Recommended Cleanup Actions

**High priority (remove template leftovers)**

1. **Remove unused CSS blocks** (after confirming you don’t need them):
   - **critical.scss:** Delete `#hero-1786` and `#h-services-143` blocks (homepage uses `#banner` and `#services-1749`).
   - **root.scss:** Delete or comment `#cta-51` and `#faq-1261` (site uses `#faq-489` and no cta-51).
   - **why-choose.scss:** Delete or update `#why-choose-12` to match `#why-choose-1824` (or keep one and use it consistently in HTML).
   - **services.scss:** Delete or comment `#services-264` (site uses `#services-1749`).
   - **local.scss:** If you do not use gallery-4, gallery-43, or gallery-44 anywhere (including dynamic content), remove or comment those sections; otherwise add the matching HTML and keep.

2. **Remove orphaned script:** Delete or stop deploying **src/assets/js/gallery-2235.js** if no page loads it and you don’t plan to use it.

**Medium priority (branding / self-hosting)**

3. **Replace template CDN assets:**
   - Replace `Contact-Page/house.jpg` (index + cta) with your own image and path (e.g. `/assets/images/...`).
   - Replace `Images/Icons/gym-arrow.svg` with a local copy (e.g. `/assets/svgs/arrow.svg`) and update the four references in index.html.

**Low priority (optional)**

4. **Consolidate `.cs-button-solid`** so one global definition lives in root and only necessary overrides remain in other files.
5. **Inline styles:** Optionally move base.html popup/button styles to a small external CSS file if you want to minimize inline CSS.

---

## 12. Summary Table

| Category | Found | Action |
|----------|--------|--------|
| Metrosolutionsdemo / metro references | 0 | None |
| Unused CSS selectors | 9 ID groups | Remove or repoint (see Section 2 & 11) |
| Suspicious hidden/tracking code | 0 | None |
| Template/demo folders or files | 0 | None |
| Duplicate/redundant CSS | #banner, .cs-button-solid | Already documented; optional consolidation |
| Orphaned JS | gallery-2235.js | Remove or stop loading |
| Template placeholder assets | house.jpg, gym-arrow.svg (CDN) | Replace with own/local assets |
| Unknown third-party scripts | 0 | None |
| Inline styles (base.html) | ~1 block | Legitimate; optional move to file |
| Package.json | CodeStitch kit only | No change required |

This audit did not find any references to metrosolutionsdemo or Metro Solutions; the codebase is the CodeStitch SASS kit with Serene Landscaping content. The main cleanup is removing unused template selectors and the unused script, and replacing CDN placeholder assets with your own.
