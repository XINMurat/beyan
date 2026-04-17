# Module: Mobile Responsive Analysis

**Priority**: P2
**Tokens**: ~1400
**Analysis Time**: Loaded for web/frontend projects

---

## Purpose
Evaluates responsive design implementation, touch interaction quality, and cross-device compatibility for web applications.

---

## Responsive Design Evaluation

```yaml
responsive_checks:
  viewport_meta:
    check: "<meta name='viewport' content='width=device-width, initial-scale=1'> present?"
  breakpoint_strategy:
    check: "Mobile-first CSS (min-width) or desktop-first (max-width)?"
    preferred: "Mobile-first — design for smallest screen first, enhance upward"
  flexbox_grid:
    check: "Modern layout using CSS Flexbox/Grid? Or legacy float-based layouts?"
  overflow:
    check: "Horizontal scrollbar appearing on mobile? Content overflowing?"
    tool: "Chrome DevTools → Toggle device toolbar"
```

## Touch Interaction

```yaml
touch_checks:
  tap_targets:
    check: "Interactive elements >= 44×44px? (Apple HIG and WCAG 2.5.5)"
    antipattern: "Small icon buttons or links with insufficient spacing"
  hover_states:
    check: "Hover-only interactions available as alternative on touch?"
    note: "Touch devices don't fire hover events reliably"
  scroll:
    check: "-webkit-overflow-scrolling: touch for smooth scroll on iOS?"
```

## Cross-Browser / Cross-Device Testing

```yaml
testing_matrix:
  browsers: ["Chrome", "Firefox", "Safari (iOS)", "Samsung Internet"]
  devices: ["iPhone SE (smallest)", "iPhone 14 Pro", "iPad", "Desktop 1920px"]
  tools: ["BrowserStack", "Chrome DevTools", "Responsively App (free)"]
```

## Scoring

```yaml
scoring:
  excellent: "Mobile-first, all tap targets 44px+, no overflow, tested on real devices."
  good: "Responsive layout works, minor touch target issues, tested in DevTools."
  attention: "Desktop-first, some overflow on mobile, hover-only features."
  critical: "No responsive design, fixed-width layout, unusable on mobile."
```
