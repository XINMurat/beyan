# Module: Monitoring & Observability

**Priority**: P2  
**Tokens**: ~1600  

## Purpose

Evaluate application monitoring, logging, alerting, and observability practices.

## Key Checks

```yaml
logging:
  structured: "JSON logs (not plain text)"
  centralized: "ELK, Splunk, CloudWatch"
  levels: "ERROR, WARN, INFO, DEBUG"
  sensitive_data: "No PII in logs"

monitoring:
  apm: "Application Performance Monitoring"
  metrics: "Request rate, error rate, duration"
  dashboards: "Real-time visibility"

alerting:
  critical: "Error rate > 5%"
  performance: "Response time > 1s"
  availability: "Uptime < 99.9%"
```

## Turkish Output

```markdown
# Monitoring & Observability Analizi

## Genel Skor: 5/10 ðŸŸ¡

### Bulgular

#### 1. ðŸ”´ Log Toplama Yok

**Sorun**: Loglar sadece sunucuda (SSH gerekli)

**Ã‡Ã¶zÃ¼m**: Centralized logging
```javascript
// Winston + CloudWatch
const logger = winston.createLogger({
  transports: [
    new winston.transports.CloudWatch({
      logGroupName: 'app-logs',
      logStreamName: 'production'
    })
  ]
});

logger.error('Payment failed', { 
  userId: '123',
  amount: 100,
  error: err.message 
});
```

**Ã‡aba**: 4 saat
**GÃ¼ven**: YÃ¼ksek (%90)

---

#### 2. ðŸŸ¡ Alert Sistemi Yok

**Eksik**:
- Error rate spike bildirimi yok
- Slow response warning yok
- Disk dolma alert'i yok

**Ã‡Ã¶zÃ¼m**: Alert rules
```yaml
# Prometheus Alert Rules
groups:
  - name: app_alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status="500"}[5m]) > 0.05
        annotations:
          summary: "Error rate >5%"
          
      - alert: SlowResponse
        expr: http_request_duration_seconds > 1
        annotations:
          summary: "Response time >1s"
```

**Ã‡aba**: 2 gÃ¼n
**GÃ¼ven**: Orta (%75)

---

## Ã–neriler

### ðŸ”´ P0
1. Centralized logging ekle (4 saat)
2. Basic health check endpoint (30 dk)

### ðŸŸ¡ P1
3. Alert sistemi kur (2 gÃ¼n)
4. Grafana dashboard (1 gÃ¼n)

**Hedef**: Proaktif sorun tespiti

---

**Analiz TamamlandÄ±** | Observability: 5/10
```
