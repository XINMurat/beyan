# Module: UI Interaction Testing

**Priority**: P1 (Testing — UI Otomasyonu)
**Tokens**: ~4500
**Analysis Time**: `visual_builder`, `canvas`, `drag_drop` veya UI yoğun proje tespit edildiğinde yüklenir

---

## Purpose
Kullanıcı arayüzü (UI) etkileşimlerini otomatize eden test stratejisini analiz eder ve geliştirir. Cypress ile Playwright arasında doğru seçimi yapmanıza yardımcı olur, kanvas/drag-drop gibi zor test edilebilen senaryolar için özel yaklaşımlar sunar ve accessibility (erişilebilirlik) testlerini otomasyona dahil eder.

---

## Cypress vs Playwright Seçimi

```yaml
cypress:
  ideal_for: "JavaScript/TypeScript tabanlı web projeleri, basit API mock'lama, Chrome/Edge testleri."
  strengths: "Kolay kurulum, Time-travel debugging (test snapshot'larını geçmişe alarak inceleme), Büyük community."
  weaknesses: "Çoklu sekme (Multi-tab) testi yetersiz, Firefox tam desteği sınırlı."

playwright:
  ideal_for: "Cross-browser (Chrome, Firefox, WebKit) testler, çoklu sayfa/sekme senaryoları."
  strengths: "Gerçek multi-browser, paralel test, interceptor API çok güçlü."
  weaknesses: "Cypress'e göre daha dik öğrenme eğrisi."

recommendation_matrix:
  single_browser_simple_ui: "Cypress"
  multi_browser_complex_scenarios: "Playwright"
  legacy_project_selenium: "Playwright (Daha modern, Selenium'un halefi)"
```

---

## Drag-and-Drop ve Canvas Testleri

UI'da en zor test edilen bileşenler sürükle-bırak (Drag & Drop) ve Canvas elementleridir.

### Cypress ile Drag-and-Drop
```javascript
// cypress-drag-drop plugin'i ile
cy.get('[data-testid="card-1"]').drag('[data-testid="dropzone-a"]');

// Native HTML5 Drag Events (plugin olmadan)
cy.get('[data-testid="source"]')
  .trigger('dragstart')
  .get('[data-testid="target"]')
  .trigger('drop');
```

### Playwright ile Canvas Test (Snapshot)
```javascript
// Canvas elementi için snapshot testi
await page.goto('/whiteboard');
const canvas = await page.locator('canvas');
await expect(canvas).toHaveScreenshot('empty-canvas.png');

// Canvas üzerinde çizim simülasyonu
await canvas.dispatchEvent('mousedown', { clientX: 100, clientY: 100 });
await canvas.dispatchEvent('mousemove', { clientX: 200, clientY: 200 });
await canvas.dispatchEvent('mouseup');
await expect(canvas).toHaveScreenshot('after-draw.png');
```

---

## Form Test Senaryoları

Formlar, UI testlerinin en kritik ve en yaygın bölümüdür:

```javascript
// Cypress ile kapsamlı form testi
describe('Contact Form', () => {
  it('shows validation errors on empty submit', () => {
    cy.visit('/contact');
    cy.get('[data-testid="submit-btn"]').click();
    cy.get('[data-testid="error-email"]').should('be.visible');
    cy.get('[data-testid="error-message"]').should('contain', 'Bu alan zorunludur');
  });

  it('submits successfully with valid data', () => {
    cy.intercept('POST', '/api/contact', { statusCode: 200 }).as('submitContact');
    cy.get('[data-testid="email"]').type('user@example.com');
    cy.get('[data-testid="submit-btn"]').click();
    cy.wait('@submitContact');
    cy.get('[data-testid="success-message"]').should('be.visible');
  });
});
```

---

## Accessibility Otomasyonu (axe-core)

WCAG 2.1 uyumluluğunu el ile kontrol etmek yerine testlere entegre edin:

```javascript
// Cypress ile axe-core entegrasyonu
import 'cypress-axe';

it('homepage has no accessibility violations', () => {
  cy.visit('/');
  cy.injectAxe();
  cy.checkA11y(null, {
    rules: { 'color-contrast': { enabled: true } }
  });
});

// Klavye navigasyonu testi
it('user can navigate form using only keyboard', () => {
  cy.get('[data-testid="name"]').focus().type('Test');
  cy.realPress('Tab');
  cy.get('[data-testid="email"]').should('be.focused');
  cy.realPress('Tab');
  cy.get('[data-testid="submit-btn"]').should('be.focused');
  cy.realPress('Enter');
});
```

---

## Test Data Yönetimi

*   **Fixtures:** Statik test verilerini `cypress/fixtures/users.json` gibi ayrı dosyalarda tutun.
*   **Mock API Responses:** `cy.intercept()` veya Playwright'ın `page.route()` ile ağ isteklerini yakalayıp sahte veri döndürün.
*   **Database Seeding:** E2E testleri başlamadan önce `cy.task('seedDatabase')` ile veritabanını temiz, bilinen bir duruma getirin.

---

## Scoring

```yaml
scoring:
  excellent: "Cypress/Playwright kurulu, form testleri tam, axe-core entegre, drag-drop senaryoları var."
  good: "Temel UI testleri var ama accessibility testleri yok, bazı form validasyonları test edilmemiş."
  attention: "Sadece happy-path testler var, hata senaryoları ve keyboard navigation testlenmemiş."
  critical: "UI test altyapısı hiç kurulmamış, tüm testler elle yapılıyor."
```

---

## Output Format

```markdown
## 🖱️ UI Etkileşim Test Raporu

### Mevcut Test Altyapısı
- **Araç:** [Cypress / Playwright / Hiçbiri]
- **Kapsanan Senaryo Sayısı:** [Tahmini]

### Boşluklar (Test Edilmeyen Alanlar)
- [Form validasyonları test edilmemiş]
- [Accessibility kontrolleri yok]
- [Drag-and-drop için test senaryosu yok]

### Önerilen Test Senaryoları
[Projeye özgü kod örneği]
```
