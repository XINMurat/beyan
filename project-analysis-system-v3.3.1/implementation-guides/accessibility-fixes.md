# Erişilebilirlik Düzeltme Rehberi

## 1. Alt Text Ekleme

### Görev
12 görsele alt text ekle

### Adım Adım
```html
<!-- ❌ Öncesi -->
<img src="product1.jpg" />

<!-- ✅ Sonrası -->
<img src="product1.jpg" alt="Mavi kot pantolon, slim fit, beden 32" />
```

**İyi Alt Text Yazma**:
- Görseli açıkla (renk, şekil, içerik)
- SEO için keyword ekle (ama spam yapma)
- Dekoratif görsellerde alt="" (boş)

## 2. Renk Kontrastı Düzeltme

### Araç
https://webaim.org/resources/contrastchecker/

### Düzeltme
```css
/* ❌ Kontrast 2.8:1 */
.button { color: #888; background: #fff; }

/* ✅ Kontrast 4.6:1 */
.button { color: #595959; background: #fff; }
```

## 3. Keyboard Navigation

### Test
```
Tab: İleri git
Shift+Tab: Geri git
Enter/Space: Butona tıkla
Escape: Modal kapat
```

### Düzeltme
```tsx
// Focus indicator ekle
button:focus {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}

// Tab sırası
<div tabIndex={0}>Fokuslanabilir</div>
```

**Checklist**:
- [ ] Tüm görsellere alt text
- [ ] Renk kontrastları WCAG AA
- [ ] Keyboard navigation çalışıyor
- [ ] ARIA labels eklendi


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