# Module: SEO Analysis

**Priority**: P3
**Tokens**: ~1500
**Analysis Time**: Loaded for public-facing web/frontend projects

---

## Purpose
Evaluates technical SEO implementation including metadata, structured data, Core Web Vitals, crawlability, and indexability for public web applications.

---

## Technical SEO Checklist

```yaml
meta_tags:
  required:
    - "Unique <title> tag per page (50-60 chars)"
    - "Meta description (150-160 chars) — not duplicate across pages"
    - "Open Graph tags for social sharing (og:title, og:description, og:image)"
    - "Canonical URL to prevent duplicate content"
  check: "Title and description are unique for EVERY page — not just homepage"

structured_data:
  schema_org:
    check: "JSON-LD structured data for breadcrumbs, articles, products, FAQs?"
    tool: "Google Rich Results Test"

robots_sitemap:
  check: "robots.txt correctly allows/disallows crawlers?"
  check2: "XML sitemap submitted to Google Search Console?"
  check3: "Sitemap kept up-to-date automatically?"
```

## Core Web Vitals (SEO Ranking Factor)

```yaml
cwv_thresholds:
  LCP: "< 2.5s Good | 2.5-4.0s Needs Improvement | > 4.0s Poor"
  FID: "< 100ms Good | 100-300ms Needs Improvement | > 300ms Poor"
  CLS: "< 0.1 Good | 0.1-0.25 Needs Improvement | > 0.25 Poor"
tool: "Google PageSpeed Insights, Search Console Core Web Vitals report"
```

## Crawlability

*   **JavaScript rendering:** Is critical content server-side rendered (SSR/SSG) or only in client-side JS? Google may miss JS-only content.
*   **Pagination:** Proper `rel="prev"` and `rel="next"` or `?page=` parameter handling.
*   **404 Handling:** Broken links return proper 404, not redirect to homepage.

## Scoring

```yaml
scoring:
  excellent: "Unique meta per page, structured data, Core Web Vitals green, SSR/SSG, sitemap current."
  good: "Most meta tags present, CWV mostly green, some structured data missing."
  attention: "Duplicate titles, no structured data, slow LCP, content JS-only."
  critical: "No meta tags, pages not indexed, CWV all red, no sitemap."
```
