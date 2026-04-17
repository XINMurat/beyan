# Module: Refactoring Guide

**Priority**: P3
**Tokens**: ~1500
**Analysis Time**: Loaded when high complexity or tech debt detected

---

## Purpose
Provides structured refactoring strategies for identified code quality issues, with safe step-by-step approaches to modernize legacy patterns without breaking functionality.

---

## The Strangler Fig Pattern (Large Refactors)

For legacy systems, never rewrite everything at once. Use the Strangler Fig pattern:

```yaml
strangler_fig:
  concept: "New functionality is built in the new way. Old code is gradually replaced — never all at once."
  steps:
    1: "Identify one high-traffic or high-risk module to refactor first"
    2: "Write tests for existing behavior BEFORE touching any code"
    3: "Build new implementation alongside old (feature flag gated)"
    4: "Switch traffic to new implementation, monitor"
    5: "Delete old implementation only when confident"
```

## Extract Function Refactoring

```python
# ❌ BEFORE: Long function doing many things
def process_order(order_id):
    order = db.get(order_id)
    # 20 lines of validation
    # 15 lines of price calculation
    # 10 lines of inventory check
    # 25 lines of payment processing
    # 10 lines of notification sending

# ✅ AFTER: Each responsibility in its own function
def process_order(order_id):
    order = db.get(order_id)
    validate_order(order)
    price = calculate_price(order)
    check_inventory(order)
    process_payment(order, price)
    send_confirmation(order)
```

## Safe Refactoring Rules

```yaml
safe_refactoring:
  golden_rule: "Never refactor without tests. Write tests first, refactor second."
  small_steps: "Commit after each small, working refactor — not after the entire task"
  boy_scout_rule: "Leave code cleaner than you found it — small improvements in every PR"
  preserve_behavior: "Refactoring = same behavior, better code. Not adding features."
```

## Common Quick Wins

1. **Rename for clarity:** `d` → `discountAmount`, `u` → `currentUser`
2. **Extract constants:** `if (type === 3)` → `if (type === PaymentType.CREDIT_CARD)`
3. **Remove dead code:** Delete commented-out blocks over 2 weeks old
4. **Replace magic strings:** `'pending'` → `OrderStatus.PENDING`

## Scoring

```yaml
scoring:
  excellent: "Refactoring done incrementally with test coverage, no regressions."
  good: "Some cleanup happening, but no systematic approach."
  attention: "Tech debt acknowledged but no action plan."
  critical: "Codebase too fragile to refactor safely — test coverage needed first."
```
