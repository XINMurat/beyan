# Module: Analytics Analysis

**Priority**: P3
**Tokens**: ~1200
**Analysis Time**: Loaded for consumer-facing web/mobile products

---

## Purpose
Evaluates the analytics implementation for data quality, privacy compliance, event tracking completeness, and actionability of collected data.

---

## Analytics Implementation Quality

```yaml
implementation_checks:
  tracking_plan:
    check: "Is there a documented tracking plan defining all events and their properties?"
    antipattern: "Ad-hoc events added by whoever needs them — results in inconsistent data"

  event_naming:
    check: "Consistent naming convention? (snake_case: 'button_clicked', 'page_viewed')"
    antipattern: "Mix of 'ButtonClick', 'button_click', 'clickButton' for the same action"

  user_identification:
    check: "Users identified after login? Anonymous pre-login events linked post-login?"

  data_layer:
    check: "GTM dataLayer or equivalent used to decouple analytics from source code?"
```

## Key Events Checklist

```yaml
essential_events:
  - "Page view (with page title, URL, referrer)"
  - "User registration / Login"
  - "Core conversion event (purchase, subscription, sign-up)"
  - "Error events (form validation failures, API errors)"
  - "Feature usage events (key features tracked)"
```

## Privacy & Compliance

```yaml
privacy_checks:
  pii_in_events: "No personal data (email, name, phone) in event properties?"
  consent: "Analytics only fires after cookie consent on GDPR/KVKK compliant sites?"
  data_retention: "Analytics data retention period configured per privacy policy?"
```

## Scoring

```yaml
scoring:
  excellent: "Tracking plan documented, consistent naming, GTM in use, consent-gated, no PII."
  good: "Core events tracked, mostly consistent, some ad-hoc events."
  attention: "No tracking plan, inconsistent event names, PII potentially in events."
  critical: "No analytics, or analytics fires without consent in GDPR-regulated markets."
```
