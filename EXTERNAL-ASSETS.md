# External assets (icons/images) – move to local

These assets are currently loaded from **csimg.nyc3.cdn.digitaloceanspaces.com**. To avoid extra requests and improve load time, save each file into `src/assets/svgs/` with the name below, then the site will use the local copies.

| Save as (in `src/assets/svgs/`) | Download URL |
|---------------------------------|--------------|
| `diamond.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Icons/diamond.svg |
| `trophy-white.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Icons/trophy-white.svg |
| `building-white.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Icons/building-white.svg |
| `yellow-stars.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Graphics/yellow-stars.svg |
| `gray-quote.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Graphics/gray-quote.svg |
| `white-arrow-up.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Icons/white-arrow-up.svg |
| `sheild.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Why-Choose/sheild.svg |
| `toolbox.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Why-Choose/toolbox.svg |
| `ribbon.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Why-Choose/ribbon.svg |
| `grey-call.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Icons/grey-call.svg |
| `grey-mail.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Icons/grey-mail.svg |
| `facebook-1a.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Icons/facebook-1a.svg |
| `instagram1a.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Icons/instagram1a.svg |
| `arrow-dwon2.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Icons/arrow-dwon2.svg |
| `white-chev.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Icons/white-chev.svg |
| `red-check.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Pricing/red-check.svg |
| `large-waves.svg` | https://csimg.nyc3.cdn.digitaloceanspaces.com/Images/Graphics/large-waves.svg |

**Footer social icons** – The code now uses your existing local files: `google.svg`, `facebook.svg`, `instagram.svg`. If the footer social icons look wrong, replace those files in `src/assets/svgs/` with the CDN versions:

- https://csimg.nyc3.digitaloceanspaces.com/Social/google.svg → `google.svg`
- https://csimg.nyc3.digitaloceanspaces.com/Social/Facebook.svg → `facebook.svg`
- https://csimg.nyc3.digitaloceanspaces.com/Social/instagram.svg → `instagram.svg`

**Not changed (admin / analytics):**

- `src/admin/config.yml`: `logo_url` for Decap CMS (admin only).
- `src/admin/index.html`: Decap CMS script from unpkg (admin only).
- `base.html`: Google Tag Manager and Clarity (analytics).

After saving the SVGs above into `src/assets/svgs/`, the site will no longer request these from the CDN.
