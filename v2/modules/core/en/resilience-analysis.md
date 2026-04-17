# Module: Resilience & Fault Tolerance Analysis

**Priority**: P3
**Tokens**: ~1500
**Analysis Time**: Loaded for distributed systems and microservices

---

## Purpose
Analyzes fault tolerance patterns (Circuit Breaker, Retry, Fallback) and evaluates how gracefully the system handles partial failures in distributed environments.

---

## Key Resilience Patterns

### Circuit Breaker
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10)
)
def call_payment_service(payload):
    response = requests.post("http://payment-service/charge", json=payload, timeout=5)
    response.raise_for_status()
    return response.json()
```

### Retry with Exponential Backoff
```yaml
retry_policy:
  max_attempts: 3
  backoff: "1s → 2s → 4s (exponential)"
  retryable: ["503", "429", "NetworkTimeout"]
  non_retryable: ["400", "401", "403", "404"]
```

### Fallback
```javascript
async function getRecommendations(userId) {
  try {
    return await recommendationService.get(userId);
  } catch {
    return cache.get('popular_products') || []; // Graceful degradation
  }
}
```

## Resilience Checklist

```yaml
checks:
  timeout: "Timeout defined on every external service call?"
  circuit_breaker: "Circuit breaker for repeatedly failing services?"
  health_check: "/health endpoint checking all dependencies?"
  graceful_shutdown: "Active requests completed before pod termination?"
  idempotency: "POST endpoints safe to retry without side effects?"
```

## Recommended Libraries
- Python: `tenacity`, `pybreaker`
- .NET: `Polly`
- Node.js: `opossum`
- Java: `Resilience4j`
