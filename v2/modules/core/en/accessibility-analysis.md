# Module: Accessibility Analysis

**Priority**: P2
**Tokens**: ~1800
**Analysis Time**: Loaded for web/frontend projects

---

## Purpose
Performs a systematic WCAG 2.1 compliance audit and identifies barriers for users with disabilities including visual, motor, cognitive, and hearing impairments.

---

## WCAG 2.1 Key Principles (POUR)

```yaml
pour_principles:
  Perceivable:
    checks:
      - "All images have alt text (meaningful, not 'image123.jpg')"
      - "Videos have captions/transcripts"
      - "Color is not the only way to convey information"
      - "Text can be resized to 200% without breaking layout"
  Operable:
    checks:
      - "All functionality reachable via keyboard alone"
      - "No keyboard traps (user can always Tab out)"
      - "Skip navigation link for screen reader users"
      - "No content flashing more than 3 times/second (seizure risk)"
  Understandable:
    checks:
      - "HTML lang attribute set (e.g., lang='en')"
      - "Error messages identify the field and suggest correction"
      - "Consistent navigation across pages"
  Robust:
    checks:
      - "Valid HTML (no duplicate IDs)"
      - "ARIA roles used correctly and not excessively"
      - "Custom components have keyboard support"
```

## Automated vs Manual Testing

```yaml
automated_tools:
  - "axe-core: Catches ~30-40% of WCAG issues automatically"
  - "Lighthouse accessibility audit"
  - "eslint-plugin-jsx-a11y for React projects"
manual_required:
  - "Keyboard navigation walkthrough"
  - "Screen reader testing (NVDA + Firefox, VoiceOver + Safari)"
  - "Cognitive load assessment"
```

## Scoring

```yaml
scoring:
  excellent: "WCAG AA compliant, axe-core clean, keyboard fully functional, screen reader tested."
  good: "Minor contrast issues, most ARIA labels present, keyboard mostly works."
  attention: "Several WCAG violations, keyboard traps present, missing alt text."
  critical: "Site unusable without mouse, no alt text, no focus indicators."
```
