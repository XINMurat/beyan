# Module: Cost Analysis

**Priority**: P3
**Tokens**: ~1500
**Analysis Time**: Loaded when cloud infrastructure detected

---

## Purpose
Identifies unnecessary cloud spending, oversized resources, and optimization opportunities for AWS, GCP, and Azure deployments.

---

## Common Cost Traps

```yaml
cost_traps:
  oversized_instances:
    check: "CPU utilization consistently below 20%? Instance is likely oversized."
    fix: "Downsize to next smaller instance type — 30-60% cost reduction possible"
  unattached_resources:
    check: "EBS volumes, Elastic IPs, Load Balancers with no attached instances"
    tool: "AWS Trusted Advisor → Underutilized Resources"
  data_transfer:
    check: "Services in different regions? Cross-region transfer fees add up fast."
    fix: "Colocate services in same availability zone"
  on_demand_vs_reserved:
    check: "Always-on production servers on On-Demand pricing?"
    fix: "1-year Reserved Instance commitment → 40-60% savings"
```

## Serverless Cost Optimization

```yaml
serverless:
  memory_right_sizing: "AWS Lambda Power Tuning tool to find optimal memory/cost balance"
  cold_starts: "Provisioned Concurrency for latency-sensitive functions"
  invocation_batching: "SQS batch processing to reduce invocation count"
```

## Output Format

```markdown
## 💰 Cloud Cost Analysis Report

### Wasteful Resources Detected
- **[Resource]:** [Description — Estimated monthly overspend: $X]

### Immediate Savings Opportunities
1. [Action — Estimated saving: X% or $Y/month]

### Long-Term Optimization
- [Reserved Instance migration — ~40% savings potential]
```
