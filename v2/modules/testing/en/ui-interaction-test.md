# Module: UI Interaction Testing

**Priority**: P1
**Tokens**: ~4500
**Analysis Time**: Loaded when visual_builder, canvas, drag_drop, or UI-heavy project detected

---

## Purpose
Analyzes and improves UI test automation strategy including Cypress vs Playwright selection, canvas/drag-drop testing approaches, accessibility automation, and test data management.

---

## Cypress vs Playwright Selection

```yaml
cypress:
  ideal_for: "JS/TS web projects, simple API mocking, Chrome/Edge testing"
  strengths: "Easy setup, time-travel debugging, large community"
  weaknesses: "Limited multi-tab support, Firefox not fully supported"

playwright:
  ideal_for: "Cross-browser (Chrome, Firefox, WebKit), multi-page scenarios"
  strengths: "True multi-browser, parallel tests, powerful request interception"
  weaknesses: "Steeper learning curve than Cypress"

recommendation:
  single_browser_simple: "Cypress"
  multi_browser_complex: "Playwright"
```

## Drag-and-Drop Testing

```javascript
// Cypress with cypress-drag-drop plugin
cy.get('[data-testid="card-1"]').drag('[data-testid="dropzone-a"]');

// Playwright canvas draw simulation
const canvas = page.locator('canvas');
await canvas.dispatchEvent('mousedown', { clientX: 100, clientY: 100 });
await canvas.dispatchEvent('mousemove', { clientX: 200, clientY: 200 });
await canvas.dispatchEvent('mouseup');
await expect(canvas).toHaveScreenshot('after-draw.png');
```

## Form Test Scenarios

```javascript
describe('Contact Form', () => {
  it('shows validation errors on empty submit', () => {
    cy.visit('/contact');
    cy.get('[data-testid="submit-btn"]').click();
    cy.get('[data-testid="error-email"]').should('be.visible');
  });

  it('submits successfully with valid data', () => {
    cy.intercept('POST', '/api/contact', { statusCode: 200 }).as('submit');
    cy.get('[data-testid="email"]').type('user@example.com');
    cy.get('[data-testid="submit-btn"]').click();
    cy.wait('@submit');
    cy.get('[data-testid="success-message"]').should('be.visible');
  });
});
```

## Accessibility Automation

```javascript
import 'cypress-axe';
it('homepage has no accessibility violations', () => {
  cy.visit('/');
  cy.injectAxe();
  cy.checkA11y(null, { rules: { 'color-contrast': { enabled: true } } });
});
```

## Scoring

```yaml
scoring:
  excellent: "Cypress/Playwright configured, forms tested, axe-core integrated, drag-drop covered."
  good: "Basic UI tests, accessibility missing, some edge cases uncovered."
  attention: "Happy-path only, keyboard navigation untested."
  critical: "No UI test automation at all."
```
