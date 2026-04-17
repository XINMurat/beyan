# Module: Accessibility Analysis (WCAG 2.1 Detailed)

**Priority**: P2 (Medium - Legal/Compliance)  
**Tokens**: ~2200  
**Analysis Time**: 15-20 minutes  

---

## Purpose

Comprehensive WCAG 2.1 compliance audit including automated testing, manual checks, and legal compliance assessment. More detailed than UI/UX module's accessibility section.

---

## WCAG 2.1 Compliance Levels

```yaml
level_A: "Minimum (25 criteria)"
level_AA: "Recommended for most (13 additional = 38 total)"
level_AAA: "Enhanced (23 additional = 61 total)"

target:
  government: "AA minimum, AAA preferred"
  commercial: "AA sufficient"
  international: "AA required in many countries"
```

---

## Automated Testing (Tools)

```bash
# axe-core (most comprehensive)
npx @axe-core/cli https://localhost:3000 --save results.json

# Lighthouse
lighthouse https://localhost:3000 --only-categories=accessibility

# Pa11y
npx pa11y https://localhost:3000

# Wave (online tool)
# https://wave.webaim.org/
```

---

## Report Example (TURKISH)

```markdown
# EriÅŸilebilirlik (Accessibility) Analizi

## WCAG 2.1 AA Uyumluluk: %72 🟡

### Özet
- ✅ İyi: Klavye navigasyonu çalışıyor
- 🟡 Dikkat: Renk kontrastı sorunları (8 yer)
- 🔴 Kritik: Alt text eksik (12 görsel)
- ⚠️ Uyarı: Ekran okuyucu test edilmemiş

**Yasal Risk**: Orta (WCAG AA %90+ gerekli)

---

## Kritik Bulgular

### 1. 🔴 Eksik Alt Text (12 Görsel)

**Konum**: Ürün listesi sayfası

```html
<!-- ❌ Mevcut -->
<img src="urun1.jpg" />

<!-- ✅ Düzeltme -->
<img src="urun1.jpg" alt="Mavi kot pantolon, slim fit, beden 32" />
```

**Etki**: 
- Görme engelli kullanıcılar görseli anlayamaz
- SEO sorunu (Google görselleri indexleyemez)
- WCAG Level A ihlali

**Çaba**: 1 saat (12 görsel için alt text yaz)
**Güven**: Yüksek (%98)

---

### 2. 🟡 Renk Kontrastı Sorunları (8 Yer)

**Konum**: Butonlar ve linkler

```css
/* ❌ Mevcut: Kontrast 2.8:1 (yetersiz) */
.button-secondary {
  color: #888;  
  background: #fff;
}

/* ✅ Düzeltme: Kontrast 4.6:1 (yeterli) */
.button-secondary {
  color: #595959;  
  background: #fff;
}
```

**WCAG Gerekliliği**: 4.5:1 (normal text), 3:1 (büyük text)

**Çaba**: 2 saat (8 yerde renk değiştir + test)
**Güven**: Yüksek (%95)

---

## Manuel Test Kontrol Listesi

```yaml
klavye_navigasyonu:
  - [ ] Tab ile tüm etkileşimli elemanlara ulaşılabiliyor
  - [ ] Focus göstergesi görünür
  - [ ] Tab sırası mantıklı
  - [ ] Escape ile modal kapatılabiliyor
  - [ ] Enter/Space ile butonlar çalışıyor

ekran_okuyucu:
  - [ ] NVDA ile test edildi (Windows)
  - [ ] VoiceOver ile test edildi (Mac/iOS)
  - [ ] Başlıklar mantıklı sırada
  - [ ] Form alanları doğru etiketli
  - [ ] Hata mesajları duyuruluyor

mobil_eriÅŸilebilirlik:
  - [ ] Dokunma hedefleri 44x44 px
  - [ ] Zoom %200'e kadar çalışıyor
  - [ ] Yatay scroll yok
  - [ ] Ekran döndürme destekleniyor
```

---

## Öncelikli Öneriler

### 🔴 P0 (Bu Hafta)
1. 12 görsele alt text ekle (1 saat)
2. 8 yerde renk kontrastı düzelt (2 saat)
3. Form label'ları ekle (1 saat)

### 🟡 P1 (Bu Sprint)
4. Skip link ekle (30 dakika)
5. ARIA label'ları tamamla (2 saat)
6. Klavye trap'lerini düzelt (1 saat)

**Hedef**: %72 → %92 WCAG AA uyumluluğu

---

**Analiz Tamamlandı** | Erişilebilirlik: %72 | Güven: Yüksek (%88)
```

---

## Automated Report Generation

```yaml
output_language: "Turkish"
format: "Markdown with emoji status indicators"
priority_labels: "P0: Kritik, P1: Yüksek, P2: Orta, P3: Düşük"
```
