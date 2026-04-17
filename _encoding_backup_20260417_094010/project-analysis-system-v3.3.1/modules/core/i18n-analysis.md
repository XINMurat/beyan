# Module: Internationalization (i18n) Analysis

**Priority**: P2 (Medium)  
**Tokens**: ~1500  
**Analysis Time**: 8-10 minutes  

---

## Purpose

Evaluate multi-language support, translation quality, locale handling, and RTL support.

---

## Key Checks

```yaml
i18n_framework:
  react: "react-intl, i18next, react-i18next"
  detection: "Check package.json for i18n libraries"

translation_files:
  structure:
    - locales/en-US.json
    - locales/tr-TR.json
    - locales/de-DE.json
  
  missing_keys:
    command: "i18next-scanner --scan"
    issue: "Keys in code but not in translation files"

pluralization:
  check: "Does framework handle plural forms?"
  example: |
    // Good
    t('items', { count: 5 })  Ã¢â€ â€™ "5 items"
    t('items', { count: 1 })  Ã¢â€ â€™ "1 item"

date_formatting:
  check: "Use Intl.DateTimeFormat with locale"
  wrong: "hardcoded DD/MM/YYYY"
  correct: "date.toLocaleDateString(locale)"

rtl_support:
  languages: ["Arabic", "Hebrew", "Persian"]
  css: "Check for dir='rtl' support"
```

---

## Turkish Output Example

```markdown
# Ãƒâ€¡oklu Dil DesteÃ„Å¸i Analizi

## Genel Skor: 6/10 Ã°Å¸Å¸Â¡

### Bulgular

#### 1. Ã°Å¸Å¸Â¡ Eksik Ãƒâ€¡eviriler (23 anahtar)

**Sorun**: Ã„Â°ngilizce metinler TÃƒÂ¼rkÃƒÂ§e arayÃƒÂ¼zde gÃƒÂ¶rÃƒÂ¼nÃƒÂ¼yor

```json
// en-US.json
{
  "welcome": "Welcome",
  "login": "Login"
}

// tr-TR.json (eksik)
{
  "welcome": "HoÃ…Å¸ geldiniz"
  // "login" anahtarÃ„Â± eksik!
}
```

**Ãƒâ€¡ÃƒÂ¶zÃƒÂ¼m**:
```bash
# Eksik anahtarlarÃ„Â± bul
i18next-scanner --scan src/ --output locales/
```

**Ãƒâ€¡aba**: 2 saat (23 anahtar ÃƒÂ§evir)
**GÃƒÂ¼ven**: YÃƒÂ¼ksek (%95)

---

#### 2. Ã°Å¸â€Â´ Tarih FormatÃ„Â± Sabit KodlanmÃ„Â±Ã…Å¸

```javascript
// Ã¢ÂÅ’ YanlÃ„Â±Ã…Å¸: TÃƒÂ¼m diller iÃƒÂ§in MM/DD/YYYY
const formatted = `${month}/${day}/${year}`;

// Ã¢Å“â€¦ DoÃ„Å¸ru: Locale'e gÃƒÂ¶re
const formatted = date.toLocaleDateString(locale);
// tr-TR: 15.12.2024
// en-US: 12/15/2024
```

**Ãƒâ€¡aba**: 1 saat
**GÃƒÂ¼ven**: YÃƒÂ¼ksek (%92)

---

## Ãƒâ€“neriler

### Ã°Å¸â€Â´ P0
1. Eksik 23 ÃƒÂ§eviriyi tamamla (2 saat)
2. Tarih formatÃ„Â±nÃ„Â± locale'e gÃƒÂ¶re yap (1 saat)

### Ã°Å¸Å¸Â¡ P1
3. Ãƒâ€¡oÃ„Å¸ul formlarÃ„Â± dÃƒÂ¼zelt (2 saat)
4. Para birimi formatÃ„Â±nÃ„Â± ekle (1 saat)

**Hedef**: Tam TÃƒÂ¼rkÃƒÂ§e destek + Ã„Â°ngilizce fallback

---

**Analiz TamamlandÃ„Â±** | i18n Skoru: 6/10
```
