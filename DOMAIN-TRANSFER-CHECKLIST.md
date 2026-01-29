# Before Transferring Domain – Checklist

Use this list before pointing your custom domain (e.g. `serenelandscapes.ca`) to Netlify or switching to a new domain.

---

## 1. Single source of truth (update first)

**File: `src/_data/client.js`**

| Field | What to set | Example |
|-------|----------------|--------|
| `domain` | Full site URL **with** `https://`, **no** trailing slash | `https://serenelandscapes.ca` |
| `email` | Contact email (often same as domain) | `info@serenelandscapes.ca` |

This file drives **canonical URLs**, **og:url**, **og:image**, **sitemap**, and **schema** – so getting `domain` right here fixes most links.

---

## 2. Files that use the domain (no change if you use client.js)

These use `{{ client.domain }}` or `client.domain` and stay correct once `client.js` is updated:

- `src/_includes/layouts/base.html` – canonical, og:url, og:image
- `src/_includes/components/post-schema.html` – JSON-LD @id and URLs
- `src/config/plugins/sitemap.js` – sitemap hostname
- `src/robots.html` – Sitemap: URL

No edits needed unless you add new absolute URLs.

---

## 3. Hardcoded links to update if the domain changes

If you **change** to a different domain (not just “going live” on the current one), update:

| File | What to change |
|------|----------------|
| `src/_includes/sections/header.html` | `mailto:info@serenelandscapes.ca` → use `{{ client.email }}` or new email |
| `src/_includes/components/home-schema.html` | `"email": "info@serenelandscapes.ca"` → use `{{ client.email }}` or new email |
| `src/llms.txt` | All `https://serenelandscapes.ca/...` URLs → new domain |

---

## 4. Netlify (dashboard, not code)

After deploy, in **Netlify**:

1. **Domain management**  
   Site → **Domain management** → Add custom domain (e.g. `serenelandscapes.ca` and `www.serenelandscapes.ca` if you use www).

2. **HTTPS**  
   Enable “Force HTTPS” so the site is only served over `https://`.

3. **Form success redirect** (if using Netlify Forms)  
   Forms → your form → Form options → Redirect to:  
   `https://yourdomain.com/contact/#form-success`  
   (use the same domain as in `client.js`.)

4. **DNS**  
   At your registrar, add the records Netlify shows (A/CNAME or Netlify DNS).

---

## 5. Optional: centralize email

So you only change email in one place (`client.js`):

- In **header**: replace `info@serenelandscapes.ca` with `{{ client.email }}`.
- In **home-schema**: replace the hardcoded email with `{{ client.email }}`.

---

## Quick summary

| Task | Where |
|------|--------|
| Set live domain (canonical, sitemap, og, schema) | `src/_data/client.js` → `domain` |
| Set contact email | `src/_data/client.js` → `email` |
| If domain name changes | Update `src/llms.txt` and any remaining hardcoded emails |
| Add domain + HTTPS + form redirect | Netlify dashboard |
| Point domain to Netlify | DNS at your registrar |

After updating `client.js` and redeploying, canonicals, sitemap, and social/share URLs will use the new domain.
