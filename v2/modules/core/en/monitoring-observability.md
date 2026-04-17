# Module: Monitoring & Observability

**Priority**: P2
**Tokens**: ~1800
**Analysis Time**: Loaded for production/mature projects

---

## Purpose
Evaluates the system's observability posture: logging quality, metrics collection, distributed tracing, alerting, and incident response readiness.

---

## The Three Pillars of Observability

```yaml
pillars:
  logs:
    checks:
      - "Structured logging (JSON) vs plain text strings?"
      - "Log levels used correctly (DEBUG/INFO/WARN/ERROR)?"
      - "Sensitive data (passwords, tokens) NOT in logs?"
      - "Centralized log aggregation (ELK, Datadog, CloudWatch)?"
    antipattern: "console.log('user:', user) — prints entire user object including password hash"

  metrics:
    checks:
      - "RED metrics: Rate, Errors, Duration for all services"
      - "Business metrics: Order count, revenue, conversion rate"
      - "Infrastructure metrics: CPU, memory, disk, connection pool"
    tools: "Prometheus + Grafana, Datadog, CloudWatch"

  traces:
    checks:
      - "Distributed tracing for cross-service requests? (Jaeger, Zipkin, X-Ray)"
      - "Trace IDs propagated through all service calls?"
      - "Slow trace detection configured?"
```

## Alerting

```yaml
alerting_checks:
  on_call: "Is there an on-call rotation? PagerDuty/OpsGenie configured?"
  alert_fatigue: "Are alerts actionable? Too many non-critical alerts = alert fatigue"
  slo_based: "Alerts based on SLO burn rate rather than arbitrary thresholds?"
```

## Scoring

```yaml
scoring:
  excellent: "Structured logs, RED metrics, distributed tracing, SLO-based alerting, runbooks."
  good: "Logs present, basic metrics, but no tracing, alert thresholds somewhat arbitrary."
  attention: "console.log only, no metrics, alerts go unnoticed."
  critical: "Zero observability — production issues discovered by users, not the team."
```
