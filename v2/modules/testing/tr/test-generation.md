# Module: Test Generation and Strategy

**Priority**: P1 (Testing & Quality)
**Tokens**: ~4000
**Analysis Time**: Kod taraması sonrası otomatik / manuel tetikleme

---

## Purpose
Bu modül, projede bulunan kod tabanından hareketle otomatik BDD (Behavior-Driven Development) test senaryoları üretir, mevcut testlerin kalitesini (Coverage, Flaky Test) analiz eder ve test stratejisini iyileştirmeye yönelik önerilerde bulunur.

---

## BDD / Gherkin Test Senaryoları (Given/When/Then)

Yapay zeka, projedeki iş mantığını kavrayarak her önemli özellik (feature) için standart BDD formatında test senaryoları tasarlamalıdır.

**Örnek Senaryo:**
```gherkin
Feature: User Authentication
  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When they enter valid credentials (email, password)
    And they click the submit button
    Then they should be redirected to the user dashboard
    And a secure session token should be stored

  Scenario: Unsuccessful login with invalid email
    Given the user is on the login page
    When they enter an unregistered email
    Then an error message "Invalid credentials" should be displayed
    And the login form should be cleared
```

---

## Test Türleri ve Araç Değerlendirmesi

Projenin teknolojisine göre aşağıdaki test araçlarının kullanımı aranmalı veya önerilmelidir:

- **Unit Tests:** Jest (JS/TS), pytest (Python), xUnit/NUnit (.NET), JUnit (Java).
- **Integration Tests:** Supertest (Node.js), RestAssured (Java), Testcontainers.
- **E2E Tests:** Cypress, Playwright, Selenium.
- **Coverage Tools:** Istanbul/NYC (JS), pytest-cov (Python), dotCover (.NET).

---

## Test Coverage Analizi

```yaml
coverage_scoring:
  excellent: ">= 80% lines, > 70% branches. Kritik fonksiyonlar %100 kapsanmış."
  good: "70-79% lines. Temel iş mantığı kapsanmış ancak bazı edge-caseler eksik."
  attention: "50-69% lines. Testler var ancak güven vermiyor, branch coverage düşük."
  critical: "< 50% lines. Ciddi bir 'Kör Bölge' (Blind spot) riski var."
```

---

## Kod'dan Test Üretme (Auto-Generation)

Kodu okurken, özellikle karmaşık (Cyclomatic Complexity'si yüksek) fonksiyonlar için aşağıdaki prensiplerle test üretimi sağlanmalıdır:

1.  **Input Boundary Cases:** Maksimum/minimum değerler, boş (null) gönderimler.
2.  **Error Handling Paths:** `try-catch` bloklarının içerisindeki `catch` durumları tetiklenebiliyor mu?
3.  **Happy Path + Edge Cases:** Beklenen normal işleyiş ve en beklenmedik kullanıcı hataları.

---

## Test Kalitesi Değerlendirmesi

Mevcut test dosyaları okunurken aşağıdaki antipattern'ler aranmalıdır:

*   **Flaky Tests:** `sleep(1000)` veya asenkron beklemelerin yanlış yönetildiği rastgele kırılan testler.
*   **Assert Density:** Bir testin içinde çok fazla `assert/expect` olması (Testin sadece bir şeyi doğrulaması kuralının ihlali).
*   **Mock Abuse:** Gerçek mantığı test etmek yerine her şeyin (hatta DB'nin bile gereksizce) mocklanması.

---

## Scoring

```yaml
scoring:
  excellent: "BDD senaryoları tam, coverage mükemmel, E2E testler stabil."
  good: "Coverage makul seviyede, unit testler var ama E2E test eksiği bulunuyor."
  attention: "Testler sadece 'yazılmak için yazılmış', mock'lar yanlış."
  critical: "Test altyapısı hiç kurulamamış veya testler sürekli kırılıyor (Flaky)."
```

---

## Output Format

```markdown
## 🧪 Test Stratejisi & Üretilen Senaryolar

### Mevcut Durum & Coverage Analizi
- **Test Kalitesi:** [Skor ve Değerlendirme]
- **Bulunan Antipattern'ler:** [Flaky test, gereksiz mock vb.]

### 📝 Önerilen BDD Senaryoları (Feature bazlı)
[Gherkin senaryoları]

### 🛠️ Kod İçin Test İskeletleri
[Seçilen spesifik bir fonksiyon için önerilen Jest/pytest/xUnit vb. test kod bloğu]
```
