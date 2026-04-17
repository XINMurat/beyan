# Guide: Fixing WCAG 2.1 Accessibility Violations

**Module Type**: Implementation Guide (How-to)
**Priority**: P3

---

## Purpose
Provides concrete before/after code examples for fixing common WCAG 2.1 accessibility violations identified during analysis.

---

## 1. Color Contrast Fix

WCAG 2.1 AA requires 4.5:1 for normal text, 3:1 for large text.

```css
/* ❌ WRONG: Contrast ratio ~2.3:1 */
.button { background-color: #a0a0ff; color: #ffffff; }

/* ✅ CORRECT: Contrast ratio 7.1:1 */
.button { background-color: #3d3db5; color: #ffffff; }
```
**Tool:** WebAIM Contrast Checker or `axe DevTools` extension.

---

## 2. ARIA Label Fix

```html
<!-- ❌ WRONG: Screen reader only hears "button" -->
<button><svg><!-- x icon --></svg></button>

<!-- ✅ CORRECT: Screen reader hears "Close dialog" -->
<button aria-label="Close dialog">
  <svg aria-hidden="true"><!-- x icon --></svg>
</button>
```

---

## 3. Focus Management Fix

When a modal opens, keyboard focus must move inside it:

```javascript
function openModal() {
  const modal = document.getElementById('my-modal');
  modal.removeAttribute('hidden');
  const firstFocusable = modal.querySelector('button, [href], input, select, textarea');
  firstFocusable?.focus();
}

function closeModal(triggerButton) {
  document.getElementById('my-modal').setAttribute('hidden', '');
  triggerButton.focus(); // Return focus to trigger
}
```

---

## Quick Checklist

- [ ] All form inputs have `<label for="...">` or `aria-label`?
- [ ] Color contrast ≥ 4.5:1?
- [ ] Modal focus trapped inside when open?
- [ ] All images have meaningful `alt` text?
- [ ] Site fully navigable with Tab/Shift+Tab/Enter/Escape?
