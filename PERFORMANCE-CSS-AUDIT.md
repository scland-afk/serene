# Site Performance & CSS Audit Report

**Date:** 2026-02-08  
**Goal:** &lt; 2s load time, no CSS conflicts, Lighthouse score &gt; 90

---

## Executive Summary

The slowdown and banner/layout issues stem from **duplicate CSS**, **missing banner overlay on non-home pages**, **redundant #steps-585 blocks**, **multiple stylesheet loads per page**, and **base layout overrides** that can conflict with section styles. Below are prioritized issues and concrete fixes.

---

## 1. CSS Duplicates & Conflicting Selectors

### 1.1 **CRITICAL: Duplicate `#banner` definitions**

| Location | File | Used on |
|----------|------|---------|
| `critical.scss` (lines 12–119) | `critical.css` | Homepage only (blocking) |
| `content-page.scss` (lines 99–161) | Bundled into `local.css` | Service, about, contact, etc. |

**Problems:**
- Homepage loads both: `critical.css` (has `#banner`) and `local.css` (also has `#banner` via content-page) → duplicate rules, larger payload.
- **Service/about pages:** `#banner` in `content-page.scss` is **missing the dark overlay** (`.cs-background::before`). That block exists only in `critical.scss`, so non-home banners have no overlay → image too bright, text hard to read, “banner not showing” visually.

**Fix:**
1. **Single source for `#banner`:** Keep one full `#banner` definition (including `.cs-background::before` overlay) in `content-page.scss` so all pages get it via `local.css`. Add the overlay to `content-page.scss` (see Section 5.1).
2. **Critical only for LCP:** In `critical.scss`, keep only the minimum needed for LCP (e.g. `#banner` layout + overlay) or remove `#banner` from critical and rely on `local.css` for homepage too (slightly slower LCP but one less duplicate).

### 1.2 **HIGH: Duplicate `#steps-585` block in `local.scss`**

- **First block:** ~lines 1329–1412 (with `&:before` background image and `overflow: hidden`).
- **Second block:** ~lines 1666–1838 (same section, repeated rules, no background decor).

**Fix:** Remove the second `#steps-585` block (1666–1838). Keep the first; if any rules are unique in the second, merge them into the first.

### 1.3 **MEDIUM: `.cs-button-solid` overrides**

`.cs-button-solid` is defined in:
- `root.scss` (global)
- `critical.scss` (`#banner .cs-button-solid`)
- `local.scss` (inside `#gallery-48`, `#reviews-67`, `#faq-489`, `#cs-contact-485`, `#content-page-713`, etc.)

**Fix:** Rely on the global `.cs-button-solid` in `root.scss` and remove or narrow section-level overrides to only what’s truly different (e.g. width, margin). Reduces payload and avoids cascade confusion.

---

## 2. Performance Bottlenecks

### 2.1 **Stylesheet load pattern**

| Page type | Stylesheets loaded (order) |
|-----------|----------------------------|
| **Base (all pages)** | `root.css` |
| **Homepage** | `root.css` + `critical.css` + `local.css` (3 files) |
| **Service / About / most pages** | `root.css` + `local.css` (2 files) |
| **Contact** | `root.css` + `contact.css` + `local.css` (3 files) |
| **Blog** | `root.css` + `local.css` + `blog.css` (3 files) |

**Issues:**
- Every page loads `root.css` (large: fonts, nav, footer, content-page, banner-310/559, etc.).
- Homepage loads three CSS files; contact/blog load three.
- No bundling per route: same `local.css` everywhere (includes home-only sections like `#gallery-2281`, `#h-services-143`).

**Fixes:**
- Consider splitting `local.css` into e.g. `home.css` (home-only) and `shared.css` (banner, content-page, FAQ, steps, etc.) so service/about don’t download home-only CSS.
- Ensure `local.css` is loaded with `rel="stylesheet"` and, on homepage, keep `critical.css` inline or preloaded for LCP; defer non-critical if needed.

### 2.2 **Fonts**

- **root.scss:** Defines Roboto (400, 700, 900), Oswald (400, 700), Open Sans (400).
- **base.html:** Preloads Oswald (400, 700) and Open Sans (400).

**Fix:** If Roboto is not used, remove it from `root.scss` and from any preloads to save requests and parse time. Use only Oswald + Open Sans if that’s the design.

### 2.3 **Scripts in `base.html`**

Multiple blocking/defer scripts on every page:

- `dark.js`, `nav.js`, `faq.js`, `touch-interactions.js`, `gallery-48-lightbox.js`

**Fix:** Keep `nav.js` early for UX; load `faq.js`, `gallery-48-lightbox.js`, and `touch-interactions.js` only on pages that use them (e.g. FAQ section, gallery, touch UI) to reduce main-thread work on other pages.

### 2.4 **Inline styles in base**

- `base.html` contains a large `<style>` block for sticky-quote button and exit-intent popup (~70 lines).

**Fix:** Move to a small `popups.css` (or a shared “UI” CSS) and load it only on pages that show the sticky/popup, or keep inline only for the truly critical above-the-fold part and put the rest in a deferred file.

---

## 3. Banner Component Issues

### 3.1 **Banner not showing / wrong look on service and about**

- **Cause:** `#banner` on service/about comes from `content-page.scss` (in `local.css`). That block does **not** include `.cs-background::before` (dark overlay). The overlay exists only in `critical.scss`, which is not loaded on those pages.
- **Effect:** Banner image has no overlay → low contrast, text hard to read, or “banner not showing” perception.

**Fix:** Add the same `.cs-background::before` overlay rules to `content-page.scss` inside `#banner` (see Section 5.1).

### 3.2 **Banner vs `main#main`**

- **root.scss:** `main#main .cs-container, main#main .cs-content { max-width: none; margin-left: 0; margin-right: 0 }`.
- **content-page.scss:** `#banner .cs-container { max-width: 112.5rem; ... }`.

Because `#banner` is inside `main#main`, both apply. Specificity is equal; order is root then local, so `#banner .cs-container` from local wins. No change needed unless you add stronger resets later; then consider narrowing the `main#main` reset so it does not target `#banner .cs-container` (e.g. `main#main:not(#banner *) .cs-container` or a utility class).

### 3.3 **No shared banner partial**

- Homepage banner is inline in `index.html`; service/about banners are inline in each page. There is no `_includes/sections/banner.html` (or similar) shared partial.

**Fix:** Extract a single banner include (e.g. `_includes/sections/banner.html`) and use it on homepage and service/about (with parameters for title, image, CTA). Reduces duplication and keeps markup consistent.

---

## 4. Layout Breaks (Service / About)

### 4.1 **Service page typo (landscape-design.html)**

- Line 48: `src="{{ "/assets/images/...webp" }}"` has an extra `"` before `}}`, which can break the attribute.

**Fix:** Use `src="{{ "/assets/images/nice-shrub-and-flower-bed-with-mulch-for-front-house.webp" }}"` (single closing quote for the attribute).

### 4.2 **Content page section ID**

- Service pages use `#content-page-1398`; root/content-page also define `#content-page-713`. Confirm which ID is used where and that all content-page styles apply to the correct section (e.g. one ID or the other, or a class shared by both).

---

## 5. Build & Optimization

### 5.1 **Sass build**

- **Config:** `src/config/processors/sass.js` compiles every non-partial `.scss` in `src/assets/sass/` to `public/assets/css/{name}.css`.
- **Result:** Many top-level files (root, critical, local, about, blog, contact, projects, reviews, services, why-choose) each produce a CSS file. `content-page.scss` is both a partial (imported by `local.scss`) and a top-level file, so it can be compiled twice (standalone + inside local). If no page links to `content-page.css`, the standalone file is unused.

**Fix:** Rename `content-page.scss` to `_content-page.scss` so it is only ever imported (e.g. by `local.scss`) and not compiled as its own file, avoiding duplicate output.

### 5.2 **PostCSS**

- Autoprefixer and cssnano (production) are in use. Good. Ensure cssnano “default” preset is acceptable; consider “lite” if you need to debug and still want some minification.

---

## 6. Prioritized Fix List

### P0 – Do first (banner + duplicates)

1. **Add banner overlay in `content-page.scss`** so service/about banners have `.cs-background::before` (same as critical). Stops “banner not showing” and contrast issues.
2. **Remove duplicate `#steps-585` block** in `local.scss` (second block, ~lines 1666–1838).
3. **Verify landscape-design.html** img `src` in browser (template syntax is valid; fix only if you see a broken image).

### P1 – Performance & consolidation

4. **Single `#banner` source:** Keep full `#banner` (with overlay) in `content-page.scss`; trim or remove `#banner` from `critical.scss` to avoid duplicate rules on homepage.
5. **Make content-page a partial:** Rename `content-page.scss` → `_content-page.scss` and ensure it’s only imported (e.g. in `local.scss`), not built as a separate CSS file.
6. **Reduce `.cs-button-solid` overrides:** Prefer global style in `root.scss`; keep section overrides only where necessary.

### P2 – Further optimization

7. **Conditional scripts:** Load `faq.js`, `gallery-48-lightbox.js`, `touch-interactions.js` only on pages that need them.
8. **Optional CSS split:** Split `local.css` into home-only vs shared so service/about don’t download home-only sections.
9. **Font audit:** Remove Roboto if unused; keep only Oswald + Open Sans (or the set you actually use).
10. **Banner partial:** Create `_includes/sections/banner.html` and reuse on home and service/about pages.

---

## 7. Specific Code Changes

### 7.1 Add banner overlay in `content-page.scss`

In `#banner`, after `.cs-background { z-index: -2; }`, add the same overlay block as in `critical.scss`:

```scss
.cs-background {
    z-index: -2;
    width: 100%;
    height: 100%;
    display: block;
    position: absolute;
    top: 0;
    left: 0;

    &:before {
        content: "";
        width: 100%;
        height: 100%;
        background: #000;
        pointer-events: none;
        opacity: 0.7;
        display: block;
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1;
    }
}

.cs-background,
.cs-background img {
    display: block;
    height: 100%;
    left: 0;
    object-fit: cover;
    position: absolute;
    top: 0;
    width: 100%;
}
```

This matches critical’s banner overlay and fixes service/about banners.

### 7.2 Remove duplicate `#steps-585` in `local.scss`

- Delete the second full block for `#steps-585` (the one that starts around line 1666 and repeats the same section with minor differences). Keep the first block (with `&:before` and background image).

### 7.3 Fix `landscape-design.html` img src

- Change the `src` on the content section image so there is no extra `"` before `}}` (single correct closing quote for the attribute).

---

## 8. Checklist for &lt; 2s and Lighthouse &gt; 90

- [ ] Banner overlay present on all pages (content-page.scss updated).
- [ ] No duplicate `#banner` payload (single source, critical trimmed).
- [ ] Duplicate `#steps-585` removed.
- [ ] Service page img `src` typo fixed.
- [ ] Optional: content-page as partial; conditional scripts; font cleanup; CSS split.

After applying P0 and P1, re-test banner on homepage and service/about, then run Lighthouse (Performance, Best Practices) and measure LCP and load time to confirm &lt; 2s and score &gt; 90.
