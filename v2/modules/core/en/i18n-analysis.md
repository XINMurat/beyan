# Module: i18n / Internationalization Analysis

**Priority**: P2
**Tokens**: ~1400
**Analysis Time**: Loaded when i18n libraries or multiple locale configs detected

---

## Purpose
Evaluates the project's internationalization implementation for correctness, completeness, and future scalability across multiple locales.

---

## i18n Implementation Checklist

```yaml
i18n_checks:
  string_externalization:
    check: "All user-facing strings externalized to translation files? No hardcoded text in JSX/templates?"
    antipattern: "<p>Welcome back!</p>  // Hardcoded — untranslatable"
    correct: "<p>{t('welcome.back')}</p>"

  date_number_formatting:
    check: "Dates/numbers formatted with locale-aware APIs (Intl.DateTimeFormat, Intl.NumberFormat)?"
    antipattern: "new Date().toLocaleDateString() // Uses system locale, not user preference"

  rtl_support:
    check: "Right-to-left (Arabic, Hebrew, Farsi) layout support? dir='rtl' switching?"

  pluralization:
    check: "Plural forms handled correctly? ('1 item' vs '5 items') — not string concatenation"

  missing_keys:
    check: "Are all i18n keys present in all locale files? Missing keys cause [object Object] or empty strings."
    tool: "i18next-parser, babel-plugin-i18next-extract"
```

## Translation File Quality

```yaml
file_quality:
  structure: "Nested keys for context: 'auth.login.button' vs flat 'authLoginButton'"
  fallback: "Fallback locale (usually 'en') configured for missing translations?"
  interpolation: "Variables in strings use safe interpolation: 'Hello, {{name}}' not 'Hello,' + name"
```

## Scoring

```yaml
scoring:
  excellent: "All strings externalized, locale-aware formatting, RTL support, no missing keys in CI."
  good: "Most strings externalized, some hardcoded edge cases, no RTL."
  attention: "Mix of hardcoded and externalized strings, dates formatted inconsistently."
  critical: "No i18n library, all text hardcoded — adding a language requires rewriting the app."
```
