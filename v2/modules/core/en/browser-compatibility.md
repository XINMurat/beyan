# Module: Browser Compatibility

**Priority**: P3
**Tokens**: ~1200
**Analysis Time**: Loaded for frontend projects

---

## Purpose
Evaluates cross-browser compatibility strategy, polyfill usage, and identifies features that may fail in target browser environments.

---

## Browser Support Strategy

```yaml
support_definition:
  check: "Is the target browser matrix explicitly defined? (.browserslistrc, package.json browserslist)"
  recommended_default: "last 2 versions, not dead, > 0.5%"
  tools: ["Can I Use (caniuse.com)", "Browserslist"]
```

## Common Compatibility Issues

```yaml
compatibility_risks:
  css_features:
    - "CSS Grid subgrid — limited support in older browsers"
    - "CSS :has() selector — not supported in Firefox < 121"
    - "CSS container queries — check target browser support"
  js_features:
    - "Optional chaining (?.) — needs transpilation for older targets"
    - "Nullish coalescing (??) — needs transpilation"
    - "Top-level await — ESM only"
  web_apis:
    - "Web Bluetooth, WebUSB — Chrome-only"
    - "WebP images — check Safari compatibility if targeting older iOS"
```

## Transpilation & Polyfills

```yaml
build_checks:
  babel: "Is Babel configured with correct @babel/preset-env targets?"
  core_js: "core-js polyfills included for target browsers?"
  postcss_autoprefixer: "CSS autoprefixer adding vendor prefixes for target browsers?"
```

## Testing Matrix

```yaml
test_browsers:
  critical: ["Chrome (latest)", "Firefox (latest)", "Safari (latest)", "Safari iOS (latest)"]
  important: ["Edge (latest)", "Samsung Internet"]
  tools: ["BrowserStack", "Playwright (multi-browser)", "Sauce Labs"]
```

## Scoring

```yaml
scoring:
  excellent: "Browserslist defined, Babel+Autoprefixer configured, tested on all critical browsers."
  good: "Modern browser support works well, minor issues on edge cases."
  attention: "No browserslist config, untested on Safari/iOS."
  critical: "Core features broken on Firefox or Safari — significant user base affected."
```
