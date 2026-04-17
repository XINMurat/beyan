# Guide: WCAG 2.1 Erişilebilirlik İhlallerini Düzeltme

**Modül Türü**: Uygulama Rehberi (How-to Guide)
**Priority**: P3
**Hedef Kitle**: Frontend Geliştiriciler

---

## Purpose
Bu rehber, erişilebilirlik analizi sonucunda tespit edilen WCAG 2.1 ihlallerini nasıl düzelteceğinizi somut kod örnekleriyle açıklar. Analiz bulgusu → düzeltme kodu formatında ilerler.

---

## 1. Renk Kontrastı (Color Contrast) Düzeltmesi

WCAG 2.1 AA seviyesi için normal metin **4.5:1**, büyük metin ise **3:1** kontrast oranı gerektirir.

```css
/* ❌ YANLIŞ: Kontrast oranı yetersiz (~2.3:1) */
.button {
  background-color: #a0a0ff;
  color: #ffffff;
}

/* ✅ DOĞRU: Kontrast oranı yeterli (7.1:1) */
.button {
  background-color: #3d3db5;
  color: #ffffff;
}
```

**Araç:** [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) veya `axe DevTools` tarayıcı eklentisi.

---

## 2. ARIA Label Eksikliği Düzeltmesi

Ekran okuyucuların (Screen Reader) anlayamayacağı ikonlar veya soyut butonlar için `aria-label` zorunludur.

```html
<!-- ❌ YANLIŞ: Ekran okuyucu sadece "button" duyar -->
<button>
  <svg><!-- x ikonu --></svg>
</button>

<!-- ✅ DOĞRU: Ekran okuyucu "Dialogu kapat" duyar -->
<button aria-label="Dialogu kapat">
  <svg aria-hidden="true"><!-- x ikonu --></svg>
</button>
```

---

## 3. Klavye Navigasyonu (Focus Management) Düzeltmesi

Modal dialog açıldığında klavye odağı (focus) modal içine taşınmazsa, kullanıcı Tab tuşuyla sayfanın arkasındaki elemanlara geçer.

```javascript
// ✅ DOĞRU: Modal açılınca odağı modal'a taşı
function openModal() {
  const modal = document.getElementById('my-modal');
  modal.removeAttribute('hidden');
  
  // İlk odaklanabilir elemana fokus ver
  const firstFocusable = modal.querySelector('button, [href], input, select, textarea');
  firstFocusable?.focus();
}

// ✅ DOĞRU: Modal kapanınca odağı tetikleyen butona geri ver
function closeModal(triggerButton) {
  const modal = document.getElementById('my-modal');
  modal.setAttribute('hidden', '');
  triggerButton.focus(); // Kullanıcı kaldığı yerden devam eder
}
```

---

## Hızlı Kontrol Listesi

- [ ] Tüm form alanlarında `<label for="...">` veya `aria-label` var mı?
- [ ] Renk kontrastı ≥ 4.5:1 mi?
- [ ] Modal/drawer açılınca odak içine taşınıyor mu?
- [ ] Tüm resimler için anlamlı `alt` metni var mı?
- [ ] Klavye ile site tamamen dolaşılabiliyor mu (Tab/Shift+Tab/Enter/Escape)?