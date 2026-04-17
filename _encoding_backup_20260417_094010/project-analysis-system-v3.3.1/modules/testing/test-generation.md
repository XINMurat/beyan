# Module: Test Generation & Validation

**Priority**: P1 (High - Critical for Quality Assurance)  
**Module Code**: **TEST-GEN**  
**Tokens**: ~4000  
**Analysis Time**: 30-40 minutes (Phase 1), 20-30 minutes (Phase 2), 10-20 minutes (Phase 3)  

---

## Purpose

Ã–zelliklerden otomatik test senaryolarÄ± oluÅŸturur, bu senaryolardan Ã§alÄ±ÅŸtÄ±rÄ±labilir test kodlarÄ± Ã¼retir ve testleri execute edip kapsamlÄ± raporlar sunar. Feature Gap analizi sonrasÄ± eklenen yeni Ã¶zellikler veya mevcut Ã¶zelliklerin doÄŸru Ã§alÄ±ÅŸÄ±p Ã§alÄ±ÅŸmadÄ±ÄŸÄ±nÄ± BDD-style senaryolarla doÄŸrular.

---

## ðŸŽ¯ Ã‡Ã¶zÃ¼len Problemler

```yaml
common_issues:
  missing_tests:
    - "Yeni Ã¶zellikler ekledim ama test yazmadÄ±m"
    - "Hangi Ã¶zelliklerin test edilmediÄŸini bilmiyorum"
    - "Test coverage %30'un altÄ±nda"
  
  inadequate_tests:
    - "Testler var ama yÃ¼zeysel"
    - "Sadece happy path test edilmiÅŸ"
    - "Edge case'ler eksik"
    - "Integration testleri yok"
  
  unclear_requirements:
    - "Ã–zellik beklendiÄŸi gibi Ã§alÄ±ÅŸmÄ±yor"
    - "DoÄŸru davranÄ±ÅŸÄ± bilmiyorum"
    - "Acceptance criteria belirsiz"
  
  manual_testing_burden:
    - "Her deÄŸiÅŸiklikte manuel test yapÄ±yorum"
    - "Regression testi uzun sÃ¼rÃ¼yor"
    - "Test senaryolarÄ± kafamda"
  
  actor_complexity:
    - "FarklÄ± kullanÄ±cÄ± rolleri iÃ§in test gerekiyor"
    - "Multi-actor senaryolar karmaÅŸÄ±k"
    - "Permission testleri eksik"
```

---

## ðŸ“Š Three-Phase Workflow

### Phase 1: Test Scenario Generation (BDD-Style)

```yaml
input:
  - Feature specifications (from FG analysis)
  - User stories
  - Existing code (API endpoints, components)
  - Actor definitions (Admin, User, Guest)

process:
  step_1_feature_analysis:
    action: "Ã–zellikleri ve kullanÄ±cÄ± hikayelerini analiz et"
    extract:
      - Feature description
      - User roles involved
      - Business rules
      - Expected behavior
      - Edge cases
  
  step_2_actor_identification:
    action: "Actor'larÄ± ve yetkilerini belirle"
    actors:
      admin:
        permissions: "Full access"
        scenarios: "Create, Read, Update, Delete"
      
      user:
        permissions: "Limited access"
        scenarios: "Create (own), Read (own), Update (own)"
      
      guest:
        permissions: "Read only"
        scenarios: "Read (public only)"
      
      custom:
        permissions: "Custom defined"
        scenarios: "Based on role definition"
  
  step_3_scenario_generation:
    format: "Gherkin-style (Given-When-Then)"
    structure: |
      Feature: [Feature Name]
        As a [Actor]
        I want to [Action]
        So that [Benefit]
      
      Scenario: [Scenario Name]
        Given [Precondition]
        And [Additional context]
        When [Action]
        Then [Expected result]
        And [Additional assertion]
      
      Scenario Outline: [Parameterized scenario]
        Given [Precondition with <parameter>]
        When [Action with <parameter>]
        Then [Expected result with <parameter>]
        
        Examples:
          | parameter | expected |
          | value1    | result1  |
          | value2    | result2  |
    
    coverage_types:
      - happy_path: "Normal flow"
      - edge_cases: "Boundary conditions"
      - error_cases: "Invalid inputs, failures"
      - security: "Authorization, authentication"
      - performance: "Load, stress scenarios"
      - integration: "Multiple components"

output:
  - "TEST_SCENARIOS.md" (human-readable)
  - "ACTOR_SCENARIOS.md" (per-actor breakdown)
  - "COVERAGE_MATRIX.md" (what's tested)
```

---

### Phase 2: Executable Test Generation

```yaml
input:
  - TEST_SCENARIOS.md (from Phase 1)
  - Project tech stack (React, .NET, Python, etc.)
  - Test framework preference (Jest, xUnit, Pytest, etc.)

process:
  step_1_framework_detection:
    action: "Detect test framework from project"
    detection:
      javascript:
        - "Jest (package.json)"
        - "Mocha + Chai"
        - "Vitest"
        - "Cypress (E2E)"
        - "Playwright (E2E)"
      
      dotnet:
        - "xUnit"
        - "NUnit"
        - "MSTest"
      
      python:
        - "Pytest"
        - "Unittest"
        - "Robot Framework (BDD)"
      
      go:
        - "testing package"
        - "Ginkgo (BDD)"
  
  step_2_code_generation:
    action: "Gherkin senaryolardan test kodu Ã¼ret"
    
    mapping:
      given: "Setup/Arrange"
      when: "Action/Act"
      then: "Assertion/Assert"
    
    example_jest: |
      describe('Feature: User Registration', () => {
        describe('As a Guest', () => {
          describe('Scenario: Successful registration', () => {
            it('should create user with valid data', async () => {
              // Given: No existing user with email
              const email = 'newuser@example.com';
              
              // When: User submits registration form
              const response = await api.post('/auth/register', {
                name: 'John Doe',
                email: email,
                password: 'SecurePass123!'
              });
              
              // Then: User is created
              expect(response.status).toBe(201);
              expect(response.data).toHaveProperty('id');
              expect(response.data.email).toBe(email);
              
              // And: Confirmation email is sent
              expect(emailService.send).toHaveBeenCalledWith(
                expect.objectContaining({ to: email })
              );
            });
          });
        });
      });
    
    example_xunit: |
      public class UserRegistrationTests
      {
          [Fact]
          public async Task SuccessfulRegistration_CreatesUser()
          {
              // Given: No existing user with email
              var email = "newuser@example.com";
              var request = new RegisterRequest
              {
                  Name = "John Doe",
                  Email = email,
                  Password = "SecurePass123!"
              };
              
              // When: User submits registration form
              var result = await _authService.RegisterAsync(request);
              
              // Then: User is created
              Assert.NotNull(result);
              Assert.Equal(email, result.Email);
              
              // And: Confirmation email is sent
              _emailService.Verify(x => x.SendAsync(
                  It.Is<Email>(e => e.To == email)
              ), Times.Once);
          }
      }
  
  step_3_mock_generation:
    action: "Generate mock data and fixtures"
    
    mock_types:
      - "API responses"
      - "Database records"
      - "External service calls"
      - "User sessions"
      - "File uploads"
    
    example: |
      // Mock data factory
      const mockUser = {
        id: 'uuid-123',
        name: 'Test User',
        email: 'test@example.com',
        role: 'User'
      };
      
      const mockProduct = {
        id: 'prod-456',
        name: 'Test Product',
        price: 99.99,
        stock: 10
      };
  
  step_4_test_utilities:
    action: "Generate helper functions"
    
    helpers:
      - "Authentication helpers (login, logout)"
      - "Database seeders"
      - "Cleanup functions"
      - "Assertion helpers"
      - "Mock factories"
    
    example: |
      // Test utilities
      async function loginAs(role: 'Admin' | 'User' | 'Guest') {
        const credentials = {
          Admin: { email: 'admin@test.com', password: 'admin' },
          User: { email: 'user@test.com', password: 'user' },
          Guest: { email: 'guest@test.com', password: 'guest' }
        };
        
        const response = await api.post('/auth/login', credentials[role]);
        return response.data.token;
      }
      
      async function seedDatabase() {
        await db.users.create(mockUsers);
        await db.products.create(mockProducts);
      }

output:
  - "tests/" folder structure
  - Test files for each feature
  - Mock data files
  - Test utilities/helpers
  - Setup/teardown scripts
```

---

### Phase 3: Test Execution & Validation

```yaml
input:
  - Generated test files (from Phase 2)
  - Existing tests (if any)

process:
  step_1_test_execution:
    action: "Run all tests"
    
    commands:
      jest: "npm test -- --coverage --verbose"
      xunit: "dotnet test --collect:'XPlat Code Coverage'"
      pytest: "pytest --cov=. --cov-report=html"
    
    capture:
      - "Pass/Fail status"
      - "Execution time"
      - "Error messages"
      - "Stack traces"
      - "Coverage data"
  
  step_2_coverage_analysis:
    action: "Analyze test coverage"
    
    metrics:
      line_coverage: "% of lines executed"
      branch_coverage: "% of branches tested"
      function_coverage: "% of functions tested"
      statement_coverage: "% of statements executed"
    
    thresholds:
      excellent: "> 80%"
      good: "60-80%"
      attention: "40-60%"
      critical: "< 40%"
    
    identify:
      - "Untested files"
      - "Untested functions"
      - "Untested branches (if/else)"
      - "Untested edge cases"
  
  step_3_gap_detection:
    action: "Identify missing tests"
    
    detect:
      missing_scenarios:
        - "Features without tests"
        - "API endpoints not tested"
        - "Components without tests"
        - "Critical paths untested"
      
      insufficient_scenarios:
        - "Only happy path tested"
        - "No error handling tests"
        - "No edge case tests"
        - "No integration tests"
      
      actor_coverage:
        - "Admin scenarios: 100%"
        - "User scenarios: 80%"
        - "Guest scenarios: 60%"
  
  step_4_mutation_testing:
    action: "Validate test quality (optional)"
    
    concept: |
      Introduce bugs intentionally, tests should catch them
      - Change operators (> to >=)
      - Remove conditionals
      - Modify constants
    
    tools:
      - "Stryker (JavaScript)"
      - "Stryker.NET (.NET)"
      - "mutmut (Python)"
  
  step_5_regression_detection:
    action: "Compare with previous runs"
    
    track:
      - "New failures"
      - "Performance degradation"
      - "Coverage decrease"
      - "Flaky tests"

output:
  - "TEST_EXECUTION_REPORT.md"
  - "COVERAGE_REPORT.html"
  - "MISSING_TESTS.md"
  - "RECOMMENDATIONS.md"
```

---

## ðŸ“ BDD Scenario Templates

### Template 1: User Authentication

```gherkin
Feature: User Authentication
  As a guest user
  I want to login with my credentials
  So that I can access my account

Scenario: Successful login with valid credentials
  Given I am a guest user
  And I have a registered account with email "user@example.com"
  When I submit login form with valid credentials
  Then I should be redirected to dashboard
  And I should see my profile information
  And I should have an authentication token

Scenario: Failed login with invalid password
  Given I am a guest user
  And I have a registered account with email "user@example.com"
  When I submit login form with incorrect password
  Then I should see error message "Invalid credentials"
  And I should remain on login page
  And I should not have an authentication token

Scenario: Failed login with non-existent email
  Given I am a guest user
  When I submit login form with email "nonexistent@example.com"
  Then I should see error message "User not found"
  And I should remain on login page

Scenario: Login attempt with empty fields
  Given I am a guest user
  When I submit login form with empty email and password
  Then I should see validation errors
  And email field should show "Email is required"
  And password field should show "Password is required"

Scenario Outline: Login with different user roles
  Given I am logged in as <role>
  When I navigate to <page>
  Then I should <access>

  Examples:
    | role  | page            | access                |
    | Admin | /admin/users    | see the page          |
    | User  | /admin/users    | see 403 Forbidden     |
    | Guest | /admin/users    | be redirected to login|
    | Admin | /dashboard      | see the page          |
    | User  | /dashboard      | see the page          |
```

---

### Template 2: E-Commerce Product Purchase

```gherkin
Feature: Product Purchase Flow
  As a registered user
  I want to purchase products
  So that I can receive them

Background:
  Given the following products exist:
    | id   | name        | price | stock |
    | p1   | Laptop      | 999   | 5     |
    | p2   | Mouse       | 29    | 100   |
    | p3   | Keyboard    | 79    | 0     |

Scenario: Successful purchase with sufficient stock
  Given I am logged in as "User"
  And I have "Laptop" in my cart
  And I have a valid payment method
  When I proceed to checkout
  And I confirm the order
  Then the order should be created with status "Pending"
  And the stock for "Laptop" should decrease by 1
  And I should receive an order confirmation email
  And payment should be processed for amount 999

Scenario: Purchase fails with insufficient stock
  Given I am logged in as "User"
  And I have "Keyboard" in my cart
  When I proceed to checkout
  Then I should see error "Product out of stock"
  And order should not be created
  And payment should not be processed

Scenario: Guest user cannot purchase
  Given I am a guest user
  And I have "Mouse" in my cart
  When I proceed to checkout
  Then I should be redirected to login page
  And I should see message "Please login to continue"

Scenario: Admin can view all orders
  Given I am logged in as "Admin"
  When I navigate to "/admin/orders"
  Then I should see all orders from all users

Scenario: User can only view own orders
  Given I am logged in as "User"
  And there are orders from multiple users
  When I navigate to "/orders"
  Then I should only see my own orders
  And I should not see orders from other users
```

---

### Template 3: Multi-Actor Permission Testing

```gherkin
Feature: Product Management Permissions
  As a system administrator
  I want different user roles to have appropriate permissions
  So that data integrity is maintained

Scenario Outline: Create product permissions
  Given I am logged in as <actor>
  When I attempt to create a new product
  Then the action should <result>
  And I should see <message>

  Examples:
    | actor | result  | message                           |
    | Admin | succeed | "Product created successfully"    |
    | User  | fail    | "Insufficient permissions"        |
    | Guest | fail    | "Authentication required"         |

Scenario Outline: Update product permissions
  Given I am logged in as <actor>
  And a product exists with id "p1"
  When I attempt to update product "p1"
  Then the action should <result>

  Examples:
    | actor | result  |
    | Admin | succeed |
    | User  | fail    |
    | Guest | fail    |

Scenario Outline: Delete product permissions
  Given I am logged in as <actor>
  And a product exists with id "p1"
  When I attempt to delete product "p1"
  Then the action should <result>
  And if succeeded, product "p1" should not exist

  Examples:
    | actor | result  |
    | Admin | succeed |
    | User  | fail    |
    | Guest | fail    |

Scenario: User can view all products
  Given I am logged in as <any_role>
  When I navigate to "/products"
  Then I should see the product list
  
  Examples:
    | any_role |
    | Admin    |
    | User     |
    | Guest    |
```

---

## ðŸ”§ Code Generation Examples

### Jest (React/Node.js)

```javascript
// tests/features/authentication.test.js

import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { LoginPage } from '../pages/LoginPage';
import { authService } from '../services/authService';
import { mockUser, mockAuthToken } from './mocks/authMocks';

jest.mock('../services/authService');

describe('Feature: User Authentication', () => {
  beforeEach(() => {
    jest.clearAllMocks();
  });

  describe('As a guest user', () => {
    describe('Scenario: Successful login with valid credentials', () => {
      it('should redirect to dashboard and show profile', async () => {
        // Given: I am a guest user with registered account
        authService.login.mockResolvedValue({
          user: mockUser,
          token: mockAuthToken
        });

        render(<LoginPage />);

        // When: I submit login form with valid credentials
        fireEvent.change(screen.getByLabelText('Email'), {
          target: { value: 'user@example.com' }
        });
        fireEvent.change(screen.getByLabelText('Password'), {
          target: { value: 'ValidPass123!' }
        });
        fireEvent.click(screen.getByRole('button', { name: 'Login' }));

        // Then: I should be redirected to dashboard
        await waitFor(() => {
          expect(window.location.pathname).toBe('/dashboard');
        });

        // And: I should see my profile information
        expect(screen.getByText(mockUser.name)).toBeInTheDocument();

        // And: I should have an authentication token
        expect(localStorage.getItem('authToken')).toBe(mockAuthToken);
      });
    });

    describe('Scenario: Failed login with invalid password', () => {
      it('should show error message and remain on login page', async () => {
        // Given: I am a guest user with registered account
        authService.login.mockRejectedValue({
          message: 'Invalid credentials'
        });

        render(<LoginPage />);

        // When: I submit login form with incorrect password
        fireEvent.change(screen.getByLabelText('Email'), {
          target: { value: 'user@example.com' }
        });
        fireEvent.change(screen.getByLabelText('Password'), {
          target: { value: 'WrongPassword' }
        });
        fireEvent.click(screen.getByRole('button', { name: 'Login' }));

        // Then: I should see error message
        await waitFor(() => {
          expect(screen.getByText('Invalid credentials')).toBeInTheDocument();
        });

        // And: I should remain on login page
        expect(window.location.pathname).toBe('/login');

        // And: I should not have an authentication token
        expect(localStorage.getItem('authToken')).toBeNull();
      });
    });
  });

  describe('Multi-Actor Scenarios', () => {
    const actors = [
      { role: 'Admin', email: 'admin@test.com', password: 'admin' },
      { role: 'User', email: 'user@test.com', password: 'user' },
      { role: 'Guest', email: null, password: null }
    ];

    const accessMatrix = [
      { page: '/admin/users', Admin: true, User: false, Guest: false },
      { page: '/dashboard', Admin: true, User: true, Guest: false },
      { page: '/products', Admin: true, User: true, Guest: true }
    ];

    accessMatrix.forEach(({ page, ...access }) => {
      actors.forEach(({ role, email, password }) => {
        const shouldAccess = access[role];
        
        it(`${role} should ${shouldAccess ? 'access' : 'not access'} ${page}`, async () => {
          // Given: I am logged in as <role>
          if (email) {
            await loginAs(role, email, password);
          }

          // When: I navigate to <page>
          const response = await fetch(`http://localhost:3000${page}`);

          // Then: I should <access>
          if (shouldAccess) {
            expect(response.status).toBe(200);
          } else {
            expect(response.status).toBeIn([401, 403]);
          }
        });
      });
    });
  });
});
```

---

### xUnit (.NET)

```csharp
// Tests/Features/ProductPurchaseTests.cs

using Xunit;
using Moq;
using FluentAssertions;

public class ProductPurchaseTests : IClassFixture<TestFixture>
{
    private readonly TestFixture _fixture;
    private readonly Mock<IPaymentService> _paymentService;
    private readonly Mock<IEmailService> _emailService;

    public ProductPurchaseTests(TestFixture fixture)
    {
        _fixture = fixture;
        _paymentService = new Mock<IPaymentService>();
        _emailService = new Mock<IEmailService>();
    }

    [Fact]
    public async Task SuccessfulPurchase_WithSufficientStock()
    {
        // Given: I am logged in as "User"
        var user = await _fixture.LoginAs("User");
        
        // And: I have "Laptop" in my cart
        var product = _fixture.Products["Laptop"];
        var cart = new Cart { UserId = user.Id };
        cart.AddItem(product, quantity: 1);
        
        // And: I have a valid payment method
        var paymentMethod = new PaymentMethod { Type = "CreditCard" };
        _paymentService
            .Setup(x => x.ProcessPayment(It.IsAny<decimal>()))
            .ReturnsAsync(new PaymentResult { Success = true });

        // When: I proceed to checkout and confirm the order
        var orderService = new OrderService(
            _fixture.DbContext, 
            _paymentService.Object,
            _emailService.Object
        );
        var order = await orderService.CreateOrderAsync(cart, paymentMethod);

        // Then: The order should be created with status "Pending"
        order.Should().NotBeNull();
        order.Status.Should().Be(OrderStatus.Pending);

        // And: The stock for "Laptop" should decrease by 1
        var updatedProduct = await _fixture.DbContext.Products
            .FindAsync(product.Id);
        updatedProduct.Stock.Should().Be(product.Stock - 1);

        // And: I should receive an order confirmation email
        _emailService.Verify(
            x => x.SendOrderConfirmation(user.Email, order.Id),
            Times.Once
        );

        // And: Payment should be processed for amount 999
        _paymentService.Verify(
            x => x.ProcessPayment(999m),
            Times.Once
        );
    }

    [Fact]
    public async Task PurchaseFails_WithInsufficientStock()
    {
        // Given: I am logged in as "User"
        var user = await _fixture.LoginAs("User");
        
        // And: I have "Keyboard" (out of stock) in my cart
        var product = _fixture.Products["Keyboard"];
        product.Stock = 0;
        var cart = new Cart { UserId = user.Id };
        cart.AddItem(product, quantity: 1);

        // When: I proceed to checkout
        var orderService = new OrderService(_fixture.DbContext);
        Func<Task> action = async () => 
            await orderService.CreateOrderAsync(cart, new PaymentMethod());

        // Then: I should see error "Product out of stock"
        await action.Should().ThrowAsync<InvalidOperationException>()
            .WithMessage("Product out of stock");

        // And: Order should not be created
        var orders = await _fixture.DbContext.Orders
            .Where(o => o.UserId == user.Id)
            .ToListAsync();
        orders.Should().BeEmpty();

        // And: Payment should not be processed
        _paymentService.Verify(
            x => x.ProcessPayment(It.IsAny<decimal>()),
            Times.Never
        );
    }

    [Theory]
    [InlineData("Admin", "/admin/orders", true)]
    [InlineData("User", "/orders", true)]
    [InlineData("Guest", "/orders", false)]
    public async Task OrderAccess_BasedOnRole(
        string role, 
        string endpoint, 
        bool shouldAccess)
    {
        // Given: I am logged in as <role>
        var token = role != "Guest" 
            ? await _fixture.LoginAs(role) 
            : null;

        // When: I navigate to <endpoint>
        var client = _fixture.CreateClient();
        if (token != null)
        {
            client.DefaultRequestHeaders.Authorization = 
                new AuthenticationHeaderValue("Bearer", token);
        }
        var response = await client.GetAsync(endpoint);

        // Then: I should <access>
        if (shouldAccess)
        {
            response.StatusCode.Should().Be(HttpStatusCode.OK);
        }
        else
        {
            response.StatusCode.Should().BeOneOf(
                HttpStatusCode.Unauthorized,
                HttpStatusCode.Forbidden
            );
        }
    }
}
```

---

## ðŸ“Š Output Documents

### 1. TEST_SCENARIOS.md

```markdown
# Test Scenarios - E-Commerce Platform

**Generated**: 21 December 2024  
**Features Analyzed**: 8  
**Total Scenarios**: 45  
**Actors**: 3 (Admin, User, Guest)

---

## Feature 1: User Authentication

### Actor: Guest

**Scenario 1.1**: Successful login with valid credentials
- **Given**: Guest user with registered account
- **When**: Submit valid email and password
- **Then**: Redirect to dashboard, show profile, set auth token
- **Priority**: P0 (Critical)
- **Test Type**: Happy Path

**Scenario 1.2**: Failed login with invalid password
- **Given**: Guest user with registered account
- **When**: Submit incorrect password
- **Then**: Show error, remain on login page, no auth token
- **Priority**: P0 (Critical)
- **Test Type**: Error Handling

[... 43 more scenarios ...]

---

## Coverage Matrix

| Feature | Scenarios | Happy Path | Edge Cases | Error Cases | Security |
|---------|-----------|------------|------------|-------------|----------|
| Authentication | 8 | âœ… | âœ… | âœ… | âœ… |
| Product Management | 12 | âœ… | âœ… | âœ… | âœ… |
| Shopping Cart | 10 | âœ… | âœ… | âš ï¸ | âœ… |
| Checkout | 8 | âœ… | âš ï¸ | âš ï¸ | âœ… |
| Payment | 4 | âœ… | âŒ | âŒ | âš ï¸ |

**Legend**: âœ… Complete | âš ï¸ Partial | âŒ Missing
```

---

### 2. TEST_EXECUTION_REPORT.md

```markdown
# Test Execution Report

**Execution Date**: 21 December 2024 14:30:00  
**Framework**: Jest 29.5.0  
**Total Tests**: 127  
**Duration**: 45.3 seconds

---

## Summary

| Metric | Value | Status |
|--------|-------|--------|
| **Tests Passed** | 118 / 127 | âœ… 92.9% |
| **Tests Failed** | 9 / 127 | âš ï¸ 7.1% |
| **Skipped** | 0 | - |
| **Line Coverage** | 78.5% | ðŸŸ¡ Good |
| **Branch Coverage** | 65.2% | ðŸŸ¡ Good |
| **Function Coverage** | 82.1% | âœ… Excellent |

---

## Failed Tests (9)

### 1. Shopping Cart - Remove item updates total
**File**: `tests/features/cart.test.js:145`  
**Error**: `Expected 100, received 129`  
**Stack Trace**:
```
AssertionError: expected 100 to equal 129
    at Context.<anonymous> (cart.test.js:152:32)
```
**Recommendation**: Check cart total calculation logic

### 2. Payment - Process payment with expired card
**File**: `tests/features/payment.test.js:89`  
**Error**: `Expected status 400, received 500`  
**Recommendation**: Add proper error handling for expired cards

[... 7 more failures ...]

---

## Coverage Analysis

### Well-Tested Files (> 80%)
- âœ… `src/services/authService.js` - 95.2%
- âœ… `src/services/productService.js` - 88.7%
- âœ… `src/components/LoginForm.tsx` - 91.3%

### Needs Attention (< 60%)
- âš ï¸ `src/services/paymentService.js` - 45.8%
- âš ï¸ `src/services/emailService.js` - 38.2%
- âŒ `src/utils/encryption.js` - 12.1%

---

## Missing Tests

### Untested Features
1. **Password Reset Flow** - 0% coverage
   - No tests for forgot password
   - No tests for reset token validation
   - No tests for new password submission

2. **Admin Analytics Dashboard** - 0% coverage
   - No tests for data aggregation
   - No tests for chart rendering

### Untested Edge Cases
1. **Concurrent cart updates** - Race conditions
2. **Payment timeout handling** - Network issues
3. **Large file uploads** - Size limits

---

## Recommendations

### Priority 1 (Critical)
1. Fix 9 failing tests
2. Add tests for password reset (0% â†’ 80%)
3. Improve payment service tests (45% â†’ 80%)

### Priority 2 (Important)
1. Add edge case tests for cart
2. Increase encryption utility tests (12% â†’ 80%)
3. Add integration tests for checkout flow

### Priority 3 (Nice to Have)
1. Add performance tests
2. Add mutation testing
3. Set up CI/CD test automation
```

---

## ðŸš€ Usage Examples

### Example 1: Generate Test Scenarios from Features

```markdown
"TEST-GEN koduyla yeni eklenen Ã¶zelliklerin test senaryolarÄ±nÄ± oluÅŸtur.
Mode 1: Test senaryolarÄ± yaz (Markdown/Gherkin).

Ã–zellikler:
- KullanÄ±cÄ± kayÄ±t sistemi (email verification ile)
- ÃœrÃ¼n sepete ekleme
- Ã–deme iÅŸlemi (Stripe)

Actor'lar:
- Admin (tÃ¼m yetkiler)
- User (sÄ±nÄ±rlÄ± yetkiler)
- Guest (sadece gÃ¶rÃ¼ntÃ¼leme)

Her Ã¶zellik iÃ§in:
- Happy path senaryolarÄ±
- Edge case'ler
- Error handling
- Multi-actor permission testleri

TÃ¼rkÃ§e aÃ§Ä±klamalarla, Gherkin formatÄ±nda."
```

---

### Example 2: Generate + Execute Tests

```markdown
"TEST-GEN koduyla Mode 3 - Full test generation + execution.

Proje: React + .NET Core e-ticaret

AdÄ±mlar:
1. Mevcut Ã¶zellikleri analiz et
2. Test senaryolarÄ± oluÅŸtur (Gherkin)
3. Jest testleri generate et (frontend)
4. xUnit testleri generate et (backend)
5. Testleri Ã§alÄ±ÅŸtÄ±r
6. Coverage raporu oluÅŸtur

Eksik testleri tespit et, Ã¶ner.
TÃ¼rkÃ§e rapor."
```

---

### Example 3: Fix Failing Tests

```markdown
"TEST-GEN koduyla failing testleri analiz et ve dÃ¼zelt.

Mevcut durum:
- 9 test fail ediyor
- Shopping cart total hesabÄ± yanlÄ±ÅŸ
- Payment error handling eksik

Yap:
1. Failing testleri analiz et
2. Root cause bul
3. Fix Ã¶nerileri sun
4. Test kodlarÄ±nÄ± gÃ¼ncelle
5. Tekrar Ã§alÄ±ÅŸtÄ±r ve validate et"
```

---

## ðŸ“‹ Deliverables

```yaml
mode_1_scenarios:
  files:
    - "TEST_SCENARIOS.md" (human-readable)
    - "ACTOR_SCENARIOS.md" (per-actor breakdown)
    - "COVERAGE_MATRIX.md" (what needs testing)
  
  content:
    - Gherkin-style scenarios
    - Multi-actor scenarios
    - Edge cases identified
    - Security scenarios

mode_2_generation:
  files:
    - Mode 1 files +
    - "tests/" folder structure
    - "tests/features/*.test.js" (or .cs, .py)
    - "tests/mocks/" (mock data)
    - "tests/helpers/" (test utilities)
  
  content:
    - Executable test code
    - Mock factories
    - Setup/teardown functions
    - Assertion helpers

mode_3_execution:
  files:
    - Mode 2 files +
    - "TEST_EXECUTION_REPORT.md"
    - "COVERAGE_REPORT.html"
    - "MISSING_TESTS.md"
    - "FIX_RECOMMENDATIONS.md"
  
  actions:
    - Tests executed
    - Coverage analyzed
    - Failures reported
    - Gaps identified
```

---

## ðŸ“š Related Modules

- **FG** (Feature Gap): Provides features to test
- **FS** (File Structure): Identifies test file locations
- **API** (API Design): Helps generate API tests
- **UI** (UI/UX): Helps generate UI component tests

---

**Test Generation Complete** | Scenarios: X | Coverage: Y% | Confidence: High (90%)

---

*Module Version: 1.0*  
*Created: December 2024*
