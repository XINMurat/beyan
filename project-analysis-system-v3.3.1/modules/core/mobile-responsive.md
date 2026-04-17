# Module: Mobile & PWA Analysis

**Priority**: P3  
**Tokens**: ~1600  

## Turkish Output

```markdown
# Mobil & PWA Analizi

## Responsive: 8/10 ✅
## PWA: 0/10 ❌ (yok)

### Bulgular

#### 1. 🟡 PWA Özellikleri Yok

**Eksik**:
- Service worker yok
- manifest.json yok
- Offline destek yok
- Install prompt yok

**Eklenmeli**:
```javascript
// service-worker.js
self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
  );
});
```

**Çaba**: 1 hafta (full PWA)
**Güven**: Orta (%70)
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