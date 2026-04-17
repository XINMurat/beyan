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
# EriÃƒâ€¦Ã…Â¸ilebilirlik (Accessibility) Analizi

## WCAG 2.1 AA Uyumluluk: %72 ÃƒÂ°Ã…Â¸Ã…Â¸Ã‚Â¡

### ÃƒÆ’Ã¢â‚¬â€œzet
- ÃƒÂ¢Ã…â€œÃ¢â‚¬Â¦ Ãƒâ€žÃ‚Â°yi: Klavye navigasyonu ÃƒÆ’Ã‚Â§alÃƒâ€žÃ‚Â±Ãƒâ€¦Ã…Â¸Ãƒâ€žÃ‚Â±yor
- ÃƒÂ°Ã…Â¸Ã…Â¸Ã‚Â¡ Dikkat: Renk kontrastÃƒâ€žÃ‚Â± sorunlarÃƒâ€žÃ‚Â± (8 yer)
- ÃƒÂ°Ã…Â¸Ã¢â‚¬ÂÃ‚Â´ Kritik: Alt text eksik (12 gÃƒÆ’Ã‚Â¶rsel)
- ÃƒÂ¢Ã…Â¡Ã‚Â ÃƒÂ¯Ã‚Â¸Ã‚Â UyarÃƒâ€žÃ‚Â±: Ekran okuyucu test edilmemiÃƒâ€¦Ã…Â¸

**Yasal Risk**: Orta (WCAG AA %90+ gerekli)

---

## Kritik Bulgular

### 1. ÃƒÂ°Ã…Â¸Ã¢â‚¬ÂÃ‚Â´ Eksik Alt Text (12 GÃƒÆ’Ã‚Â¶rsel)

**Konum**: ÃƒÆ’Ã…â€œrÃƒÆ’Ã‚Â¼n listesi sayfasÃƒâ€žÃ‚Â±

```html
<!-- ÃƒÂ¢Ã‚ÂÃ…â€™ Mevcut -->
<img src="urun1.jpg" />

<!-- ÃƒÂ¢Ã…â€œÃ¢â‚¬Â¦ DÃƒÆ’Ã‚Â¼zeltme -->
<img src="urun1.jpg" alt="Mavi kot pantolon, slim fit, beden 32" />
```

**Etki**: 
- GÃƒÆ’Ã‚Â¶rme engelli kullanÃƒâ€žÃ‚Â±cÃƒâ€žÃ‚Â±lar gÃƒÆ’Ã‚Â¶rseli anlayamaz
- SEO sorunu (Google gÃƒÆ’Ã‚Â¶rselleri indexleyemez)
- WCAG Level A ihlali

**ÃƒÆ’Ã¢â‚¬Â¡aba**: 1 saat (12 gÃƒÆ’Ã‚Â¶rsel iÃƒÆ’Ã‚Â§in alt text yaz)
**GÃƒÆ’Ã‚Â¼ven**: YÃƒÆ’Ã‚Â¼ksek (%98)

---

### 2. ÃƒÂ°Ã…Â¸Ã…Â¸Ã‚Â¡ Renk KontrastÃƒâ€žÃ‚Â± SorunlarÃƒâ€žÃ‚Â± (8 Yer)

**Konum**: Butonlar ve linkler

```css
/* ÃƒÂ¢Ã‚ÂÃ…â€™ Mevcut: Kontrast 2.8:1 (yetersiz) */
.button-secondary {
  color: #888;  
  background: #fff;
}

/* ÃƒÂ¢Ã…â€œÃ¢â‚¬Â¦ DÃƒÆ’Ã‚Â¼zeltme: Kontrast 4.6:1 (yeterli) */
.button-secondary {
  color: #595959;  
  background: #fff;
}
```

**WCAG GerekliliÃƒâ€žÃ…Â¸i**: 4.5:1 (normal text), 3:1 (bÃƒÆ’Ã‚Â¼yÃƒÆ’Ã‚Â¼k text)

**ÃƒÆ’Ã¢â‚¬Â¡aba**: 2 saat (8 yerde renk deÃƒâ€žÃ…Â¸iÃƒâ€¦Ã…Â¸tir + test)
**GÃƒÆ’Ã‚Â¼ven**: YÃƒÆ’Ã‚Â¼ksek (%95)

---

## Manuel Test Kontrol Listesi

```yaml
klavye_navigasyonu:
  - [ ] Tab ile tÃƒÆ’Ã‚Â¼m etkileÃƒâ€¦Ã…Â¸imli elemanlara ulaÃƒâ€¦Ã…Â¸Ãƒâ€žÃ‚Â±labiliyor
  - [ ] Focus gÃƒÆ’Ã‚Â¶stergesi gÃƒÆ’Ã‚Â¶rÃƒÆ’Ã‚Â¼nÃƒÆ’Ã‚Â¼r
  - [ ] Tab sÃƒâ€žÃ‚Â±rasÃƒâ€žÃ‚Â± mantÃƒâ€žÃ‚Â±klÃƒâ€žÃ‚Â±
  - [ ] Escape ile modal kapatÃƒâ€žÃ‚Â±labiliyor
  - [ ] Enter/Space ile butonlar ÃƒÆ’Ã‚Â§alÃƒâ€žÃ‚Â±Ãƒâ€¦Ã…Â¸Ãƒâ€žÃ‚Â±yor

ekran_okuyucu:
  - [ ] NVDA ile test edildi (Windows)
  - [ ] VoiceOver ile test edildi (Mac/iOS)
  - [ ] BaÃƒâ€¦Ã…Â¸lÃƒâ€žÃ‚Â±klar mantÃƒâ€žÃ‚Â±klÃƒâ€žÃ‚Â± sÃƒâ€žÃ‚Â±rada
  - [ ] Form alanlarÃƒâ€žÃ‚Â± doÃƒâ€žÃ…Â¸ru etiketli
  - [ ] Hata mesajlarÃƒâ€žÃ‚Â± duyuruluyor

mobil_eriÃƒâ€¦Ã…Â¸ilebilirlik:
  - [ ] Dokunma hedefleri 44x44 px
  - [ ] Zoom %200'e kadar ÃƒÆ’Ã‚Â§alÃƒâ€žÃ‚Â±Ãƒâ€¦Ã…Â¸Ãƒâ€žÃ‚Â±yor
  - [ ] Yatay scroll yok
  - [ ] Ekran dÃƒÆ’Ã‚Â¶ndÃƒÆ’Ã‚Â¼rme destekleniyor
```

---

## ÃƒÆ’Ã¢â‚¬â€œncelikli ÃƒÆ’Ã¢â‚¬â€œneriler

### ÃƒÂ°Ã…Â¸Ã¢â‚¬ÂÃ‚Â´ P0 (Bu Hafta)
1. 12 gÃƒÆ’Ã‚Â¶rsele alt text ekle (1 saat)
2. 8 yerde renk kontrastÃƒâ€žÃ‚Â± dÃƒÆ’Ã‚Â¼zelt (2 saat)
3. Form label'larÃƒâ€žÃ‚Â± ekle (1 saat)

### ÃƒÂ°Ã…Â¸Ã…Â¸Ã‚Â¡ P1 (Bu Sprint)
4. Skip link ekle (30 dakika)
5. ARIA label'larÃƒâ€žÃ‚Â± tamamla (2 saat)
6. Klavye trap'lerini dÃƒÆ’Ã‚Â¼zelt (1 saat)

**Hedef**: %72 ÃƒÂ¢Ã¢â‚¬Â Ã¢â‚¬â„¢ %92 WCAG AA uyumluluÃƒâ€žÃ…Â¸u

---

**Analiz TamamlandÃƒâ€žÃ‚Â±** | EriÃƒâ€¦Ã…Â¸ilebilirlik: %72 | GÃƒÆ’Ã‚Â¼ven: YÃƒÆ’Ã‚Â¼ksek (%88)
```

---

## Automated Report Generation

```yaml
output_language: "Turkish"
format: "Markdown with emoji status indicators"
priority_labels: "P0: Kritik, P1: YÃƒÆ’Ã‚Â¼ksek, P2: Orta, P3: DÃƒÆ’Ã‚Â¼Ãƒâ€¦Ã…Â¸ÃƒÆ’Ã‚Â¼k"
```
