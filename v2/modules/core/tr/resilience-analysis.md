# Module: Resilience & Fault Tolerance Analysis

**Priority**: P3 (Sistem Dayanıklılığı)
**Tokens**: ~1500
**Analysis Time**: `microservices`, `kubernetes`, `distributed` veya API servisi tespit edildiğinde yüklenir

---

## Purpose
Dağıtık sistemlerde ve mikroservis mimarilerinde hata yönetimini (Circuit Breaker, Retry, Fallback) ve sistemin kısmi arızalara karşı dayanıklılığını analiz eder.

---

## Kritik Dayanıklılık Kalıpları

### 1. Circuit Breaker (Devre Kesici)
Bir servis çökmeye başladığında tüm sistemi korumak için çağrıları geçici olarak keser:

```python
# Örnek: Tenacity ile Python Circuit Breaker
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=1, max=10)
)
def call_payment_service(payload):
    response = requests.post("http://payment-service/charge", json=payload)
    response.raise_for_status()
    return response.json()
```

### 2. Retry with Exponential Backoff
Anlık ağ hatalarını yeniden denemek yerine giderek artan bekleme süreleriyle dene:

```yaml
retry_policy:
  max_attempts: 3
  backoff:
    initial: "1 saniye"
    multiplier: 2
    max: "30 saniye"
  retryable_errors: ["503", "429", "NetworkTimeout"]
  non_retryable: ["400", "401", "403", "404"]
```

### 3. Fallback (Yedek Yanıt)
Servis çöktüğünde sıfır yerine makul bir yedek değer dön:

```javascript
async function getProductRecommendations(userId) {
  try {
    return await recommendationService.get(userId);
  } catch (error) {
    // Servis çöktü — cached popüler ürünleri döndür
    return cache.get('popular_products') || [];
  }
}
```

---

## Kontrol Listesi

```yaml
resilience_checks:
  timeout: "Her dış servis çağrısında timeout tanımlı mı?"
  circuit_breaker: "Sürekli başarısız olan servisler için circuit breaker var mı?"
  health_check: "/health endpoint mevcut ve bağımlılıkları kontrol ediyor mu?"
  graceful_shutdown: "Pod/Container kapanırken aktif istekler tamamlanıyor mu?"
  idempotency: "POST/PUT endpoint'leri idempotent mi (tekrar çağrılınca zararsız)?"
```

---

## Output Format

```markdown
## 🛡️ Dayanıklılık Analiz Raporu

### Eksik Koruma Mekanizmaları
- **Timeout:** [X servisi için timeout tanımlı değil — P1]
- **Circuit Breaker:** [Ödeme servisi için CB yok — P0]

### Önerilen Kütüphaneler
- Python: `tenacity`, `pybreaker`
- .NET: `Polly`
- Node.js: `opossum`
- Java: `Resilience4j`
```