# CSS Conflicts & Exact Fixes

## 1. Specific CSS rules that are conflicting

### Conflict A: `#banner` (duplicate full blocks)

| Source | Selector | Loaded on | Conflict |
|--------|----------|-----------|----------|
| **critical.scss** lines 12–119 | `#banner`, `#banner .cs-container`, `#banner .cs-container::before`, `#banner .cs-content`, `#banner .cs-title`, `#banner .cs-background`, `#banner .cs-button-solid` | Homepage only (critical.css) | Same rules again in content-page → duplicate payload on homepage; later file wins. |
| **content-page.scss** lines 99–180 | Same selectors | Every page that loads local.css (service, about, contact, etc.) | Same rules; was missing `.cs-background::before` (now fixed). |

**Conflicting properties (same selector, different files):**
- `#banner` → `padding`, `padding-bottom`, `padding-top`, `position`, `overflow`
- `#banner .cs-container` → `max-width: 112.5rem`, `padding-top`, etc.
- `#banner .cs-container::before` → `background` (gradient)
- `#banner .cs-button-solid` → `border-radius: 0.25rem` (critical) vs global `0.5rem` (root)

**Winner on homepage:** `local.css` (content-page) wins because it loads after critical.css. So you’re shipping the same #banner rules twice on the home page.

---

### Conflict B: `main#main` vs `#banner .cs-container`

| Source | Selector | Rule | Conflict |
|--------|----------|------|----------|
| **root.scss** lines 346–353 | `main#main .cs-container, main#main .cs-content` | `max-width: none; margin-left: 0; margin-right: 0` | Resets every section’s container inside `<main>`. |
| **content-page.scss** (in local.css) | `#banner .cs-container` | `max-width: 112.5rem; ...` | More specific (ID + class). Loads after root. |

**Result:** On pages that load local.css, `#banner .cs-container` wins (same specificity as `main#main .cs-container`, but comes later). So banner is correct. If you ever reorder or remove local’s #banner block, the banner would stretch full width.

---

### Conflict C: `.cs-button-solid` (many overrides)

| File | Context | Conflicting / overriding properties |
|------|----------|--------------------------------------|
| **root.scss** 194–243 | Global `.cs-button-solid` | `border-radius: 0.5rem`, `padding: 1rem 2rem`, `min-width: 11.25rem`, `:before` hover |
| **critical.scss** 96–112 | `#banner .cs-button-solid` | `border-radius: 0.25rem`, `min-width: 12.5rem`, `padding: 0.75rem 1.5rem`, no `:before` |
| **content-page.scss** 259+ | `#content-page-713 .cs-button-solid` | Different font-size, margin, etc. |
| **local.scss** | Inside #gallery-48, #reviews-67, #faq-489, #cs-contact-485, #pricing-1769, #cs-contact-485, etc. | Various padding, width, border-radius overrides |

**Result:** Buttons look different in banner vs elsewhere (e.g. 0.25rem vs 0.5rem radius). Many sections re-declare the same button styles.

---

## 2. Which files to delete / consolidate

### Do not delete whole files

Keep all SCSS files; the issue is **what’s inside them**, not the file list.

### Consolidate by changing content

| Action | File | What to do |
|--------|------|------------|
| **Remove duplicate #banner** | `critical.scss` | Delete the entire `#banner` block (lines 8–120) so `#banner` exists only in `content-page.scss` (loaded via local.css). Homepage will get banner styles from local.css; LCP may parse slightly later but you remove duplicate CSS. |
| **Make content-page a partial (optional)** | `content-page.scss` | Rename to `_content-page.scss` so the build doesn’t output a separate `content-page.css`. Only `local.scss` should `@import "content-page"`. If no page links to `content-page.css`, this just avoids an unused file. |
| **Already done** | `local.scss` | Duplicate `#steps-585` block was already removed. |

### Files that are safe to keep as-is (no delete)

- `root.scss` → keep (global, nav, footer, variables).
- `critical.scss` → keep file; remove only the `#banner` block to consolidate.
- `local.scss`, `content-page.scss`, `about.scss`, `blog.scss`, `contact.scss`, `services.scss`, `why-choose.scss`, `projects.scss`, `reviews.scss` → keep; optionally trim `.cs-button-solid` overrides later.

---

## 3. Exact code changes to fix the banner issue

### 3.1 Banner fix (already applied)

The missing overlay on service/about banners is **already fixed** in `content-page.scss`: the `.cs-background::before` block (dark overlay) is present at lines 148–160. No further change needed for the overlay.

Current `content-page.scss` `#banner` snippet (what you should have):

```scss
/*  content-page.scss – #banner (keep as single source of truth)  */
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

If your `content-page.scss` doesn’t have the `&:before` block inside `#banner .cs-background`, add the block above inside `#banner` (after `.cs-title` and before the `.cs-background, .cs-background img` rule).

---

### 3.2 Remove duplicate `#banner` from critical.scss (exact edit)

**File:** `src/assets/sass/critical.scss`

**Delete** from the top of the file through the end of the `#banner .cs-container::before` media query (so the next section is “Hero”). That is, remove this entire block:

```scss
/*-- -------------------------- -->
<---     #banner (LCP hero)     -->
<--- -------------------------- -*/
@media only screen and (min-width: 0rem) {
    #banner {
        padding: var(--sectionPadding);
        padding-bottom: 3.75rem;
        padding-top: clamp(8rem, 12vw, 9.3125rem);
        position: relative;
        overflow: hidden;

        .cs-container {
            margin: auto;
            max-width: 112.5rem;
            padding-top: clamp(8rem, 45vw, 12rem);
            position: relative;
            width: 100%;
            z-index: 1;
        }

        .cs-container::before {
            background: linear-gradient(180deg, transparent 0, rgba(0, 0, 0, 0.92));
            content: "";
            display: block;
            height: 100%;
            left: 0;
            opacity: 1;
            position: absolute;
            top: 0;
            width: 100%;
            z-index: -1;
        }

        .cs-content {
            box-sizing: border-box;
            display: flex;
            flex-direction: column;
            padding: clamp(1.5rem, 4vw, 2.5rem) clamp(1rem, 4vw, 2.5rem);
            row-gap: 1rem;
        }

        .cs-title {
            color: var(--bodyTextColorWhite);
            font-size: clamp(2.4375rem, 6vw, 4.625rem);
            margin-bottom: 0;
        }

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

        .cs-button-group {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
        }

        .cs-button-solid {
            font-size: 1rem;
            font-weight: 700;
            line-height: 1.2;
            text-align: center;
            text-decoration: none;
            min-width: 12.5rem;
            margin: 0;
            box-sizing: border-box;
            padding: 0.75rem 1.5rem;
            background-color: var(--primary);
            color: var(--bodyTextColorWhite);
            border-radius: 0.25rem;
            display: inline-block;
            position: relative;
            z-index: 1;
        }
    }
}

@media only screen and (min-width: 48rem) {
    #banner .cs-container::before {
        background: linear-gradient(180deg, transparent 0, rgba(0, 0, 0, 0.8) 90%, rgba(0, 0, 0, 0.92));
    }
}

```

**Leave** the next comment and section in place (Hero):

```scss
/*-- -------------------------- -->
<---           Hero             -->
<--- -------------------------- -*/
```

After this, `#banner` exists only in `content-page.scss` (via local.css), so the banner issue is fixed with one source of truth and no duplicate banner CSS on the homepage.

**Note:** On the homepage, `local.css` is loaded deferred in production (preload + onload). So the banner is styled when local.css runs. If you see a brief unstyled banner on first paint, you can either (a) load `local.css` blocking on the homepage only, or (b) add back a minimal `#banner` block in critical.scss (e.g. just layout + `.cs-background::before` overlay, ~30 lines) for LCP and keep the rest in content-page. The change above was applied; you can revert it and use (b) if you prefer fastest LCP.
