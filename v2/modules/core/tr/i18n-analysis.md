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
    t('items', { count: 5 })  → "5 items"
    t('items', { count: 1 })  → "1 item"

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
# Çoklu Dil Desteği Analizi

## Genel Skor: 6/10 🟡

### Bulgular

#### 1. 🟡 Eksik Çeviriler (23 anahtar)

**Sorun**: İngilizce metinler Türkçe arayüzde görünüyor

```json
// en-US.json
{
  "welcome": "Welcome",
  "login": "Login"
}

// tr-TR.json (eksik)
{
  "welcome": "HoÅŸ geldiniz"
  // "login" anahtarı eksik!
}
```

**Çözüm**:
```bash
# Eksik anahtarları bul
i18next-scanner --scan src/ --output locales/
```

**Çaba**: 2 saat (23 anahtar çevir)
**Güven**: Yüksek (%95)

---

#### 2. 🔴 Tarih Formatı Sabit Kodlanmış

```javascript
// ❌ Yanlış: Tüm diller için MM/DD/YYYY
const formatted = `${month}/${day}/${year}`;

// ✅ Doğru: Locale'e göre
const formatted = date.toLocaleDateString(locale);
// tr-TR: 15.12.2024
// en-US: 12/15/2024
```

**Çaba**: 1 saat
**Güven**: Yüksek (%92)

---

## Öneriler

### 🔴 P0
1. Eksik 23 çeviriyi tamamla (2 saat)
2. Tarih formatını locale'e göre yap (1 saat)

### 🟡 P1
3. Çoğul formları düzelt (2 saat)
4. Para birimi formatını ekle (1 saat)

**Hedef**: Tam Türkçe destek + İngilizce fallback

---

**Analiz Tamamlandı** | i18n Skoru: 6/10
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