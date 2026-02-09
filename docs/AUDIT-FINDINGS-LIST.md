# Audit Findings — Simple List (Paths + Line Numbers)

**Date:** 2026-02-08

---

## 1. Two "Root" CSS Files — ANSWER

**Finding:** There is **only one** file named "root" in this repo: **`root.css`** (built from `src/assets/sass/root.scss`).

- **`critical-root.css`** — **Does not exist** in this project. Not in `src/`, not in `public/assets/css/`, and not produced by the Sass processor (`.eleventy.js` → `src/config/processors/sass.js`). If you saw "critical-root.css (11.5 KB)" elsewhere, it may be from a different project or an old report.
- **`root.css`** — **Exists:** `public/assets/css/root.css` (source: `src/assets/sass/root.scss`). Loaded on every page from `src/_includes/layouts/base.html` (lines 84–87).
- **`critical.css`** — **Exists:** `public/assets/css/critical.css` (source: `src/assets/sass/critical.scss`). Loaded only on homepage from `src/index.html` (lines 14, 16).

**Conclusion:** No duplicate "root" files. Keep both `critical.css` (homepage LCP) and `root.css` (global). No merge needed; they serve different roles.

---

## 2. The "153-Byte" Inline Style — ANSWER

**Where:** The only inline `<style>` block in your **HTML layout** is:

- **File:** `src/_includes/layouts/base.html`  
- **Lines:** 126–189 (between `<style>` and `</style>`).

**What it does:**  
Styles for (1) **sticky CTA button** (`.sticky-quote-button` — fixed bottom-right “View Offer” button, hidden by default, shown via `.is-visible`) and (2) **exit-intent popup** (`.exit-intent-popup`, `.exit-intent-content`, `.exit-close` — overlay and modal). No tracking, no off-screen elements.

**Size:** In **source** the block is **~1,500+ bytes** (not 153). If a tool reported “153 bytes,” it may mean minified HTML output or a different build.

**Other inline styles:**  
- **File:** `src/assets/favicons/faviconog.svg` — Lines 4–6: small `<style>` (~100 bytes) for `prefers-color-scheme` (light/dark). Used for favicon, not tracking.

**Necessary?** **Yes.** Needed for the sticky button and exit-intent popup. Optional: move to a small `popups.css` and link it if you want to reduce inline CSS.

---

## 3. Metro / Demo References

**Searches run (equivalent):**

- `grep -r "metro" src/`  
- `grep -r "metrosolutionsdemo" src/`  
- `grep -r "demo" src/` (in HTML, JS, CSS, SCSS, MD)  
- `grep -r "template" src/` (in HTML, JS, CSS, SCSS, MD)

**Results:**

- **"metro" / "metrosolutionsdemo":** **No matches** in `src/`.
- **"demo":** Only in words like **"demonstrate"** (e.g. `src/content/pages/portfolio.html` line 64, `src/content/blog/choose-landscaper-edmonton.md` line 135) — not demo-site references.
- **"template":** Only **"grid-template-columns"** in SCSS and **"template"** in `src/_data/client.js` (variable comment). **`_template.txt`** in `src/content/pages/` is the kit’s page template file — not demo content.

**Conclusion:** No references to metrosolutionsdemo or Metro demo. No cleanup needed for metro/demo terms.

---

## 4. Unused CSS Selectors (#id or .class in CSS but not in HTML)

**No `.metro-*`, `#metro-*`, `.demo-*`, `#demo-*`, `.template-*`, `#template-*`** exist in the codebase.

**Unused ID selectors (CSS targets an ID that does not appear in HTML):**

| #id in CSS | File | Line(s) | Note |
|------------|------|--------|------|
| `#hero-1786` | src/assets/sass/critical.scss | 125, 270, 279 | Homepage uses `#banner`. |
| `#h-services-143` | src/assets/sass/critical.scss | 303, 382, 407, 425 | Homepage uses `#services-1749`. |
| `#cta-51` | src/assets/sass/root.scss | 1646+ | No `id="cta-51"` in HTML. |
| `#faq-1261` | src/assets/sass/root.scss | 2545, 2760, 2775 | Site uses `#faq-489`. |
| `#why-choose-12` | src/assets/sass/why-choose.scss | 7, 170, 187, 198 | HTML uses `#why-choose-1824`. |
| `#services-264` | src/assets/sass/services.scss | 7, 168, 200, 210 | Site uses `#services-1749`. |
| `#gallery-4` | src/assets/sass/local.scss | 931, 999, 1008 | No `id="gallery-4"` in HTML. |
| `#gallery-43` | src/assets/sass/local.scss | 1362, 1546, 1561, 1570, 1633 | No `id="gallery-43"` in HTML. |
| `#gallery-44` | src/assets/sass/local.scss | 1651, 1759, 1774, 1783 | No `id="gallery-44"` in HTML. |

**Recommendation:** Remove or comment these blocks in the SCSS files if you do not plan to add matching HTML.

---

## 5. External Scripts Loaded — Full List

**From `src/_includes/layouts/base.html` and pages:**

| Script / source | File | Line(s) | Domain | Need? |
|-----------------|------|--------|--------|--------|
| GA4 (gtag) | base.html | 10–29 (inline), 27 | www.googletagmanager.com | Yes (analytics) |
| Microsoft Clarity | base.html | 33–42, 41 | www.clarity.ms, scripts.clarity.ms | Yes (session recording) |
| dark.js | base.html | 119 | /assets/js/dark.js (same origin) | Yes |
| nav.js | base.html | 120 | same origin | Yes |
| faq.js | base.html | 121 | same origin | Yes |
| touch-interactions.js | base.html | 122 | same origin | Yes |

**From `src/index.html`:**

| Script | File | Line(s) | Need? |
|--------|------|--------|--------|
| gallery-48-lightbox.js | index.html | 32 | Yes (homepage gallery) |
| gallery-2281.js | index.html | 33 | Yes (homepage gallery) |
| why-choose-1824.js | index.html | 34 | Yes (Why Choose section) |

**From `src/content/pages/portfolio.html`:**

| Script | File | Line(s) | Need? |
|--------|------|--------|--------|
| gallery-2281.js | portfolio.html | 434 | Yes |
| gallery-2281-lightbox.js | portfolio.html | 435 | Yes |

**Third-party script URLs:**

- **https://www.googletagmanager.com/gtag/js?id=...** — GA4. **Keep** if you use Google Analytics.
- **https://www.clarity.ms/tag/vcjpxa0bzr** — Clarity. **Keep** if you use Clarity.

**Conclusion:** All external scripts are GTM (GA4) and Clarity. No unknown or template tracking scripts. Keep both if you use analytics and Clarity.

---

## 6. Suspicious Hidden Elements (display:none, visibility:hidden, opacity:0)

**HTML (inline style or class-driven):**

| Location | File | Line | What | Purpose |
|----------|------|------|------|---------|
| .sticky-quote-button | base.html | 141 | `display: none` | Hide sticky CTA until scroll — **OK** |
| .exit-intent-popup | base.html | 161 | `display: none` | Hide popup until exit intent — **OK** |
| #exit-intent-popup | base.html | 204 | `style="display: none;"` | Same popup — **OK** |
| #form-success | contact.html | 100 | `style="display: none;"` | Shown after form submit — **OK** |

**CSS (in SCSS):**

- **critical.scss:** 95, 228, 248, 282, 287 — overlay opacities and hidden states (e.g. nav, gallery). **OK.**
- **root.scss:** 157, 274, 279, 285, 307 (skip link, dark mode, etc.); 389, 439, 500–501, 514, 529, 543, 568, 570, 635, 644, 657, 697, 750, 778, 833, 847, 867, 1015, 1017, 1072, 1074, 1092, 1157, 1212, 1225, 1288, 1583, 1758, 2035, 2388, 2425, 2727, 2851, 2919 — UI states (skip link, dark/light, nav, FAQ, CTA, gallery). **OK.**
- **local.scss:** 200, 204, 333, 388, 390, 398, 495, 584, 590, 805–806, 820, 865, 1084–1085, 1465, 1517, 1534, 1640, 1790, 2119, 2209, 2266, 2392, 2450, 2662, 2758, 2772, 2778, 2852, 2935, 2983 — overlays, gallery, transitions. **OK.**
- **content-page.scss:** 61, 90, 155, 212 — **OK.**
- **about.scss, services.scss, why-choose.scss, contact.scss, blog.scss:** opacity/overlay values (e.g. 0.8, 0.7) — **OK.**

**Content pages (opacity in inline style):**

- **snow-removal.html:** 296, 299, 302 — `opacity: 0.8` / `0.7` on text. **OK.**
- **lawn-maintenance.html:** 275, 278 — same. **OK.**

**Conclusion:** No tracking or suspicious hidden elements. All uses are for skip link, sticky CTA, exit-intent popup, form success message, nav/dark mode, and gallery/UI states.

---

## Summary Table

| Question | Answer |
|----------|--------|
| Two root CSS files? | No. Only `root.css`. `critical-root.css` does not exist here. |
| 153-byte inline style? | Only inline style block is in base.html (lines 126–189), ~1.5KB source; it’s for sticky CTA + exit-intent. Not 153 bytes in source. |
| Metro/demo refs? | None in src. |
| Unused selectors? | 9 ID groups listed above (hero-1786, h-services-143, cta-51, faq-1261, why-choose-12, services-264, gallery-4, gallery-43, gallery-44). |
| External scripts? | GTM (GA4) + Clarity only. Both needed if you use them. |
| Hidden elements? | All legitimate (sticky CTA, exit popup, form success, skip link, nav, gallery). |
