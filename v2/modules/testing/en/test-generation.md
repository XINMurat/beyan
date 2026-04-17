# Module: Test Generation and Strategy

**Priority**: P1 (Testing & Quality)
**Tokens**: ~4000
**Analysis Time**: Loaded after code scan / manual trigger

---

## Purpose
Generates automated BDD test scenarios from the existing codebase, analyzes test quality (coverage, flaky tests), and provides targeted recommendations to improve the overall testing strategy.

---

## BDD / Gherkin Test Scenarios (Given/When/Then)

The AI should design test scenarios in standard BDD format for each key feature:

```gherkin
Feature: User Authentication
  Scenario: Successful login with valid credentials
    Given the user is on the login page
    When they enter valid credentials (email, password)
    And they click the submit button
    Then they should be redirected to the user dashboard
    And a secure session token should be stored

  Scenario: Failed login with invalid email
    Given the user is on the login page
    When they enter an unregistered email
    Then an error message "Invalid credentials" should be displayed
    And the login form should be cleared
```

---

## Test Types and Tool Evaluation

| Test Type | JS/TS | Python | .NET | Java |
|-----------|-------|--------|------|------|
| Unit | Jest | pytest | xUnit/NUnit | JUnit |
| Integration | Supertest | pytest + httpx | WebApplicationFactory | RestAssured |
| E2E | Cypress/Playwright | Selenium/Playwright | Playwright | Selenium |
| Coverage | Istanbul/NYC | pytest-cov | dotCover | JaCoCo |

---

## Test Coverage Analysis

```yaml
coverage_scoring:
  excellent: ">= 80% lines, > 70% branches. Critical functions at 100%."
  good: "70-79% lines. Core business logic covered, some edge cases missing."
  attention: "50-69% lines. Tests exist but reliability is questionable, low branch coverage."
  critical: "< 50% lines. Serious blind spot risk."
```

---

## Auto-Generation from Code

When reading the codebase, especially functions with high Cyclomatic Complexity, test generation follows these principles:

1. **Input Boundary Cases:** Max/min values, null/undefined submissions.
2. **Error Handling Paths:** Are `catch` blocks in try-catch reachable?
3. **Happy Path + Edge Cases:** Expected normal flow and the most unexpected user errors.

---

## Test Quality Assessment

Antipatterns to detect in existing test files:

*   **Flaky Tests:** Tests with `sleep(1000)` or poorly managed async waits that randomly fail.
*   **Assert Density:** Too many `expect` calls in a single test (violates "test one thing" rule).
*   **Mock Abuse:** Mocking everything including the DB instead of testing real logic.

---

## Scoring

```yaml
scoring:
  excellent: "BDD scenarios complete, coverage excellent, E2E tests stable, no flaky tests."
  good: "Coverage adequate, unit tests present but E2E gap exists."
  attention: "Tests written only for happy paths, mocks are excessive."
  critical: "No test infrastructure, or tests are constantly breaking (flaky)."
```

---

## Output Format

```markdown
## 🧪 Test Strategy & Generated Scenarios

### Current State & Coverage Analysis
- **Test Quality:** [Score and Assessment]
- **Antipatterns Found:** [Flaky tests, excessive mocks, etc.]

### 📝 Suggested BDD Scenarios (Feature-based)
[Gherkin scenarios]

### 🛠️ Test Skeletons for Key Functions
[Jest/pytest/xUnit test code block for a specific function]
```
