# Internal Linking Strategy (Local SEO)

This doc summarizes how we use internal links to support local SEO: one city + one service = one target keyword, silos linked with keyword-rich text, and limited high-value links per page.

## Principles (from guides)

- **Internal link each silo with text links.** Use keyword-rich anchor text (e.g. “final grading in Sherwood Park”), not generic “click here.”
- **Link to home with search-rich keywords.** Use phrases like “Serene Landscaping in Edmonton” or “landscaping in Sherwood Park” linking to `/`, not only the business name.
- **Don’t overlink.** Every extra link in the body dilutes value. Link best pages to best pages; keep silos clear.

## What’s in place

### Home (/) links

- **Edmonton** (`locations/edmonton.html`): One link “Serene Landscaping in Edmonton” → `/`.
- **St. Albert** (`locations/st-albert.html`): One link “Serene Landscaping in St. Albert” → `/`.
- **Sherwood Park** (`locations/sherwood-park.html`): One link “landscaping in Sherwood Park” → `/` (in “Where We Work”).
- **Final grading overview** (`services/final-grading.html`): One link “Serene Landscaping in Edmonton” → `/`.
- **Sod installation overview** (`services/sod-installation.html`): One link “Serene Landscaping in Edmonton” → `/`.

### City cross-links (keyword text)

- **St. Albert**: Paragraph before FAQ linking “landscaping in Edmonton” → `/locations/edmonton/`, “landscaping in Sherwood Park” → `/locations/sherwood-park/`.
- **Sherwood Park**: “Where We Work” links “landscaping in Sherwood Park” → `/`, “landscaping in Edmonton” → `/locations/edmonton/`, “landscaping in St. Albert” → `/locations/st-albert/`.

### Sherwood Park silo (city-specific service pages)

- **Location page**: In-body “Sod installation in Sherwood Park” → `/sod-installation/sherwood-park/`, “final grading in Sherwood Park” → `/final-grading/sherwood-park/`.
- **Catalogue cards**: “Sod Installation in Sherwood Park” → `/sod-installation/sherwood-park/`, “Final Grading in Sherwood Park” → `/final-grading/sherwood-park/`.
- **Service overviews**: Final grading and sod installation overviews link to “final grading in Sherwood Park” and “sod installation in Sherwood Park” for city-specific details.

### Footer “Popular Searches”

- Landscaping Edmonton → `/`
- Landscaping Sherwood Park → `/locations/sherwood-park/`
- Final Grading Edmonton → `/services/final-grading/`
- Final Grading St. Albert → `/final-grading/st-albert/`
- Final Grading Sherwood Park → `/final-grading/sherwood-park/`
- Sod Installation Edmonton → `/services/sod-installation/`
- Sod Installation St. Albert → `/sod-installation/st-albert/`
- Sod Installation Sherwood Park → `/sod-installation/sherwood-park/`

## Keywords (for anchor text and content)

Use these naturally in links and copy where they fit:

- Paving stones Edmonton, final grade/grading Edmonton, commercial lawn care Edmonton, final grading Edmonton, edmonton final grading
- Landscape grading contractors near me, paving contractor St. Albert, sod installation Edmonton, patio installers near me
- Synthetic turf Edmonton, artificial grass Edmonton, lawn installation, pavers Edmonton, best landscaping company
- Hardscaping services, lawn installation near me, edmonton artificial turf, hardscape companies near me
- Landscape design Edmonton, landscaping Sherwood Park, sod installation companies near me, sod installation near me

## Protected pages (do not edit for internal links)

Final grading city pages and service pages that are designated “do not edit” in the project—confirm with the project owner before changing their body copy or link structure.

## Adding new pages

- **New city page:** Add one link to home with “Serene Landscaping in [City]” or “landscaping in [City]”; add cross-links to other city pages with “landscaping in [City]” anchor text.
- **New city+service page (e.g. sod installation in X):** Link from that city’s location page and from the main service overview with “sod installation in [City]”; add to footer Popular Searches if it’s a target keyword.
- **New blog/post:** Link to 1–2 relevant service or location pages with keyword-rich anchor text; optionally one link to home with search-rich text. Avoid stuffing links.
