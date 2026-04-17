# Module: .NET Core & ASP.NET Analysis

**Priority**: P1
**Tokens**: ~1800
**Analysis Time**: Loaded when .csproj or *.sln detected

---

## Purpose
Analyzes ASP.NET Core architecture, Entity Framework Core query efficiency, .NET-specific security configuration, and async/await correctness.

---

## Layered Architecture Checks

```yaml
layer_structure:
  expected:
    - "Controller → HTTP request/response only"
    - "Service Layer → Business logic"
    - "Repository Layer → Data access"
  antipatterns:
    - "DbContext used directly in Controllers"
    - "Business logic inside Repository"
    - "SQL queries inside View/Razor"
```

## Entity Framework Core — N+1 Detection

```csharp
// ❌ WRONG: N+1 — separate SELECT per order
var orders = context.Orders.ToList();
foreach (var order in orders)
    Console.WriteLine(order.Customer.Name); // Lazy load = N extra queries!

// ✅ CORRECT: Single JOIN
var orders = context.Orders.Include(o => o.Customer).ToList();
```

## .NET Security Checklist

```yaml
security_checks:
  authorization: "[Authorize] missing on controllers/actions?"
  anti_forgery: "[ValidateAntiForgeryToken] on form POST endpoints?"
  cors: "AllowAnyOrigin() in production = critical vulnerability"
  secrets: "Connection strings in appsettings.json? Use Secret Manager or Key Vault."
```

## Async Antipatterns

*   **`.Result` or `.Wait()`:** Synchronous blocking on async → potential Deadlock.
*   **`async void`:** Unhandleable exceptions outside event handlers.

## Scoring

```yaml
scoring:
  excellent: "Clean layers, no N+1, DI correct, no .Result deadlocks, CORS restricted."
  good: "Mostly good, minor DI issues or occasional lazy loading."
  attention: "Fat controllers, N+1 detected, some endpoints not authorized."
  critical: ".Result deadlock risk, AllowAnyOrigin in production, DbContext as Singleton."
```
