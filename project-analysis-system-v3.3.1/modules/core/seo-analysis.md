# Module: SEO Analysis

**Priority**: P3  
**Tokens**: ~1500  

## Turkish Output Example

```markdown
# SEO Analizi

## Genel Skor: 6/10 🟡

### Bulgular

#### 1. 🔴 Eksik Meta Tags (8 sayfa)

```html
<!-- ❌ Eksik -->
<head>
  <title>Ana Sayfa</title>
</head>

<!-- ✅ Tam -->
<head>
  <title>Ürünler | Şirket Adı</title>
  <meta name="description" content="...">
  <meta property="og:title" content="...">
  <meta name="twitter:card" content="...">
</head>
```

**Çaba**: 2 saat
**Güven**: Yüksek (%95)
```


## Detailed Assessment Checklist

`yaml
metrics:
  - id: 1
    description: "Check configuration and baseline setups."
    weight: "high"
  - id: 2
    description: "Verify best practices implementation."
    weight: "medium"
  - id: 3
    description: "Scan for common anti-patterns."
    weight: "high"
`

## Anti-Patterns to Look For
* Missing configurations
* Hardcoded values
* Improper error handling
* Lack of test coverage for this specific domain

## Scoring Rules
* 5/5: Perfect implementation without any of the anti-patterns.
* 3/5: MVP level, works but lacks advanced optimizations.
* 1/5: Missing implementation or critical errors found.

## Tools & Commands
* Use static analysis tools
* Check configuration files (e.g., package.json, manifest, etc.)
* Review code patterns via grep/AST

---
**Note:** This module has been expanded as part of v3.4 M3 improvements.