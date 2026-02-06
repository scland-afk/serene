# Changes Summary
Date: February 5, 2026

## Core fixes
- Fixed broken Sherwood Park hardscaping links by switching to /services/hardscaping/.
- Replaced deleted grading images with existing assets:
  - before-final-grading.webp -> progress-picture-grading.webp
  - sod-installation-after-final-grading.webp -> sod-installation-edmonton.webp
- Replaced missing construction image on contact page with commercial-landscape-installation.webp.
- Added missing lightbox alt text placeholders.

## Meta tags
- Updated titles and descriptions across core, service, city, and blog pages.
- All descriptions are now 150-160 characters.

## Content expansion
- Expanded thin pages to meet word count targets:
  - final-grading/sherwood-park
  - hardscaping/st-albert
  - final-grading/st-albert
  - sod-installation/sherwood-park
  - services/artificial-grass
  - services/final-grading
  - services/paving-stones
  - locations/edmonton
  - locations/sherwood-park
  - homepage trimmed to target

## Duplicate content reductions
- Added distinct Sherwood Park vs St. Albert sections and project details for sod pages.
- Differentiated hardscaping vs paving stones content focus.

## Sitemap
- Excluded blog posts and commercial subpages from sitemap.
- Final sitemap URL count: 25.

## Files touched (high level)
- Layouts/components:
  - src/_includes/layouts/base.html
  - src/_includes/sections/header.html
  - src/_includes/sections/footer.html
- Redirects:
  - src/_redirects
- Content pages:
  - src/index.html
  - src/content/pages/*.html (about/contact/portfolio/residential/commercial and services/city pages)
  - src/content/pages/services/*.html
  - src/content/pages/locations/*.html
  - src/content/pages/*/st-albert.html and sherwood-park.html
- Blog:
  - src/content/blog/*.md
  - src/content/blog/blog.json
- Report:
  - reports/audit-remediation-report-2026-02-05.md

## Artifacts
- Full diff: reports/changes.diff
