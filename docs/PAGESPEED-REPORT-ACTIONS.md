# PageSpeed Report (Feb 9, 2026) – Actions Taken & Next Steps

## Your scores (mobile)

| Metric        | Value | Target   |
|---------------|-------|----------|
| Performance   | 76    | 90+      |
| Accessibility | 96    | ✓        |
| Best Practices| 100   | ✓        |
| SEO           | 100   | ✓        |
| **LCP**       | **5.3 s** | &lt; 2.5 s |
| FCP           | 1.9 s | &lt; 1.8 s |
| Element render delay (LCP) | **1,870 ms** | Reduce |

---

## What was slowing LCP

- **LCP element:** Hero image (“Front yard landscaping with shrubs and mulch”).
- **LCP breakdown:** Most of the delay was **element render delay (1,870 ms)**, not network. The browser had the image but couldn’t paint it until it had the **CSS for `#banner`**. That CSS was only in `local.css`, which is **deferred** on the homepage, so the hero stayed hidden until `local.css` loaded.

---

## Fix applied (LCP / element render delay)

**Minimal `#banner` added to `critical.scss`** so the hero can paint as soon as the LCP image is ready, without waiting for deferred `local.css`:

- `critical.css` now includes only what’s needed for the banner **section and image** to render: `#banner` container, `.cs-container`, `.cs-container::before` overlay, `.cs-background` and `.cs-background img` (position/size/object-fit), and `.cs-background::before` (dark overlay).
- Full banner styling (title, buttons, content) still comes from `content-page.scss` in `local.css` when it loads.

**Expected:** Element render delay should drop a lot (ideally under ~500 ms). LCP should improve toward or below 2.5 s after you deploy. Re-run PageSpeed after deploy.

---

## Roboto in the critical chain (report showed it)

The report showed:  
`Initial Navigation → root.css → roboto-v29-latin-700.woff2` (701 ms).

Roboto has been **removed** from the repo (no `@font-face`, no font stack). So either:

- The run was from **before** that change was deployed, or  
- The live site is still serving an **old cached `root.css`** that still references Roboto.

**What to do:** Deploy the current build (with Roboto removed). After deploy, the font request chain should no longer include Roboto, and the “Network dependency tree” in PageSpeed should shorten.

---

## Other report items (optional next steps)

### 1. Render-blocking: root.css (~310 ms)

- **Issue:** `root.css` blocks first paint.
- **Options (later):**
  - Inline a small “above-the-fold” set (e.g. `:root` variables + body + minimal layout) and defer the rest of `root.css`.
  - Or split CSS so a tiny “critical” file loads first and the rest is deferred.
- For now, the **critical #banner** fix is the biggest win; root.css blocking is a follow-up optimization.

### 2. Image delivery (~179 KiB savings)

- **Service card images** (final-grading, hardscaping, residential-overview, lawn-maintenance, sod, snow-removal): report suggests **increasing compression** (e.g. higher compression in your Sharp/build pipeline).
- **Overview / crew images** (about section): “Larger than displayed” – you already use `resize()` and `<picture>`. The report may be seeing built URLs with one size; ensure the **displayed size** (e.g. in the Side-by-Side section) matches the `resize()` dimensions for that breakpoint so the browser doesn’t fetch a larger file than needed.
- **Action:** When you next touch the image pipeline, increase WebP/AVIF compression slightly and double-check that each `<img>` / `<source>` uses a resize close to its displayed size.

### 3. Third-party (GTM, Clarity)

- **GTM:** ~168 KiB, long main-thread tasks (208 ms, 122 ms). You already delay it; could load even later (e.g. after first interaction or after 3–5 s) if you’re okay with slightly delayed analytics.
- **Clarity:** ~28 KiB, 76 ms task. Same idea – already deferred; optional to delay further.
- **Cache:** Clarity has 1d TTL. Not much you can change on your side; optional to leave as-is.

### 4. Preconnect

- Report said “no origins were preconnected.” Your `base.html` has preconnect for GTM and Clarity when `client.isProduction`. If the test ran in production mode, those should be present. If you add more critical third-party origins later, keep preconnect to 2–4 origins.

---

## Additional fixes applied (post-report)

1. **Defer root.css on homepage only** – Homepage now loads `root.css` with `preload` + `onload` so it doesn’t block first paint. Other pages still load `root.css` blocking. Critical.css includes minimal `:root` and `body` so the banner and LCP render correctly while root loads.
2. **Gallery-48-lightbox.js only on homepage** – Removed from base layout; added in `index.html` block head so other pages don’t load this script (~saves one script request on non-home pages).
3. **Image compression on homepage** – All `| webp %}` on `index.html` now use `| webp({ quality: 76 }) %}` and all `| avif %}` use `| avif({ quality: 70 }) %}` to reduce image payload (targeting the ~179 KiB savings PageSpeed suggested).

## Checklist after deploy

- [ ] Deploy current build (critical #banner, Roboto removal, defer root on home, conditional lightbox, image quality).
- [ ] Re-run PageSpeed Insights (mobile) and check **LCP**, **FCP**, **Element render delay**, and **Image delivery**.
- [ ] (Optional) Apply same `webp({ quality: 76 })` / `avif({ quality: 70 })` pattern on other high-traffic pages.
