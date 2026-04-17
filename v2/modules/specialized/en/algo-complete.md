# Module: Algorithm Verification & Property-Based Testing

**Priority**: P3 (Algorithmic Correctness)
**Tokens**: ~2500
**Analysis Time**: Loaded when critical algorithms, mathematical computations, or data transformation patterns detected

---

## Purpose
Verifies the correctness of mathematically critical algorithms (sorting, encryption, financial calculations, data transformation) not just through hand-written examples, but through **property-based testing** (PBT) and **fuzzing**. Systematically surfaces edge cases that typical unit tests cannot see.

---

## What is Property-Based Testing (PBT)?

Traditional unit tests work on **examples**:
- `add(2, 3)` → expects `5` ✅

Property-based testing works on **rules** and generates hundreds of random inputs:
- `add(a, b) == add(b, a)` — must *always* be true (commutativity)
- `sort(sort(list)) == sort(list)` — must *always* be idempotent

```python
# Example: Hypothesis (Python) for PBT
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sort_idempotency(lst):
    """Sorting a list twice should equal sorting it once."""
    assert sorted(sorted(lst)) == sorted(lst)

@given(st.integers(), st.integers())
def test_addition_commutativity(a, b):
    """Addition must be order-independent."""
    assert add(a, b) == add(b, a)
```

---

## Tools & Ecosystem

```yaml
pbt_tools:
  python:
    primary: "Hypothesis — Most powerful and widely used PBT library"
    install: "pip install hypothesis"
    features: ["Automatic shrinking", "Failure database", "Stateful testing"]

  javascript:
    primary: "fast-check — TypeScript-first PBT"
    install: "npm install fast-check"
    features: ["Jest/Vitest integration", "Custom arbitraries"]

  dotnet:
    primary: "FsCheck — F# and C# support"
    secondary: "CsCheck"

  java:
    primary: "jqwik — Native JUnit 5 integration"
```

---

## Critical Algorithm Detection

The following code types are **strongly recommended** for PBT verification:

```yaml
high_priority_algorithms:
  financial:
    examples:
      - "Currency conversion (rounding errors)"
      - "Tax calculation (precision-sensitive float operations)"
      - "Discount/commission calculation chains"
    risk: "Rounding error → User financial loss or legal liability"

  sorting_searching:
    examples:
      - "Custom sorting algorithms"
      - "Search/filter engines"
    property: "sort(a) + sort(b) == sort(a + b) (merge property)"

  serialization:
    examples:
      - "JSON/XML/YAML serialize/deserialize cycle"
      - "Database ORM mapping"
    property: "deserialize(serialize(obj)) == obj (round-trip property)"

  cryptography:
    examples:
      - "Encrypt/decrypt cycle"
      - "Hash functions"
    property: "decrypt(encrypt(msg, key), key) == msg"
    note: "Always use standard libraries for crypto — never implement your own"
```

---

## Fuzzing

Fuzzing intentionally corrupts (malforms) program input to discover unexpected crashes or security vulnerabilities.

```python
# Python fuzzing with atheris (Coverage-guided)
import atheris
import sys

def fuzz_target(data):
    fdp = atheris.FuzzedDataProvider(data)
    user_input = fdp.ConsumeUnicodeNoSurrogates(100)
    
    # This function must NEVER crash — even on bad input
    try:
        result = parse_user_input(user_input)
        validate_output(result)
    except ValueError:
        pass  # Expected error — fine
    except Exception as e:
        raise  # Unexpected error — fuzzer reports this

atheris.Setup(sys.argv, fuzz_target)
atheris.Fuzz()
```

**Fuzzing vs unit tests:** You don't write "this input is bad" — the tool generates millions of potentially malformed inputs automatically.

---

## When Formal Verification is Needed

Some algorithms require **formal verification**, not just testing:

```yaml
formal_verification:
  use_cases:
    - "Blockchain smart contract logic"
    - "Protocol correctness (consensus algorithms)"
    - "Safety-critical embedded systems"
  tools:
    - "TLA+ — Model checker used by Amazon AWS and Microsoft"
    - "Alloy — Lightweight formal modeling"
    - "Coq / Isabelle — Theorem provers for formal proof"
  note: "PBT is sufficient for most business applications. Formal verification only for life-critical systems."
```

---

## Scoring

```yaml
scoring:
  excellent: "PBT applied to critical algorithms, financial calculations round-trip tested, fuzzing running in CI."
  good: "PBT exists for some algorithms, but financial or cryptographic areas have gaps."
  attention: "Critical algorithms tested only with hand-written examples — edge cases are blind spots."
  critical: "Financial calculations done with float, zero testing — production rounding error risk."
```

---

## Quick Wins

1. **Install Hypothesis:** `pip install hypothesis` — Write your first PBT in 30 minutes.
2. **Add round-trip tests:** Simplest PBT — serialize/deserialize cycle.
3. **Replace float with Decimal:** `decimal.Decimal` is non-negotiable for financial calculations.

---

## Output Format

```markdown
## 🔬 Algorithm Verification Report

### Critical Algorithms Detected
- **`[Function name]` (`[File:Line]`):** [Property that should be PBT-verified]

### Precision/Rounding Risks
- **[Locations]:** Financial calculations using float instead of Decimal

### Current PBT Coverage
- **Tool:** [Hypothesis / fast-check / None]
- **Functions Covered:** [X]

### Suggested Tests
[Project-specific Hypothesis/fast-check code example]
```
