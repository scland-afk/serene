# Serene Landscapes Tools

## Local SEO Site Auditor

Run the auditor with:

```bash
python tools/site_auditor.py --sitemap https://serenelandscapes.ca/sitemap.xml --keywords keywords.txt
```

Optional:

```bash
python tools/site_auditor.py --sitemap <url> --keywords keywords.txt --root-domain https://serenelandscapes.ca
python tools/site_auditor.py --sitemap <url> --keywords keywords.txt --discovery-mode homepage --crawl-depth 3
```

Requirements:

```bash
pip install requests beautifulsoup4 lxml
```

Outputs are written to `reports/`:

- `reports/site_audit.csv`
- `reports/issues_summary.md`
- `reports/redirects_suggestions.txt`
- `reports/sitemap_missing_from_crawl.csv`
- `reports/crawl_missing_from_sitemap.csv`
