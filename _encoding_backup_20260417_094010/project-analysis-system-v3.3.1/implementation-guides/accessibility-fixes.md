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
