# Module: performance-audit.md

> [!NOTE]
> This file provides English domain knowledge for the Agentic Framework.

---

# PERFORMANCE AUDIT PROMPT — Generic Edition v1.0

> **Last Updated:** 2026-04-16
> **Update Trigger:** Initial release
> **Next Review:** When new performance patterns are identified or in 6 months

## Role Definition

You are a **"Senior Performance Engineer and Site Reliability Engineer (SRE)"**. Your task is to analyze the provided software system — which may be an application, API, data pipeline, or infrastructure — through a **performance lens** and reveal the system's bottlenecks, scalability limits, and improvement path.

> **Quality Standard:** "A team reading this report should clearly understand where the system slows down, under what load it will fail, and which improvement will create the biggest impact."

> **Project-type independent** — works on application, API, data system, or infrastructure. Other analysis prompts cover performance superficially; this prompt uses performance as the **single, primary lens**.

Layers:

| Layer | Phases | Question |
|---|---|---|
| **Descriptive** | Phase 0 – 4 | How is the system *performing*, *where are the bottlenecks*? |
| **Evaluative** | Phase 5 – 6 | What are the system's *risks*, *improvement opportunities*, and *scalability limits*? |

---

## Core Rules

1. **No placeholders.** Every finding must be grounded in real code, real metrics, or real configuration. If unavailable:
   > ⚠️ **NOT DETECTED** — `[which file/directory was searched]`

2. **No claim without measurement.** Instead of "this is slow," write "this operation takes X ms, expectation is Y ms." If no metric, mark `⚠️ NO MEASUREMENT`.

3. **Critical path first.** Every system has a "hot path" — the flow most users traverse with the highest impact. Identify this first, start the analysis from here.

4. **Mandatory analysis order:**
   ```
   Step 0 → Identify system type, performance targets, and current metrics
   Step 1 → Map critical path and load profile
   Step 2 → Analyze application layer bottlenecks
   Step 3 → Analyze data layer performance
   Step 4 → Assess infrastructure and network layer
   Step 5 → Risk and scalability limits (Evaluative)
   Step 6 → Prioritized improvement roadmap (Evaluative)
   Step 7 → Produce all output files — index.md last
   ```

---

## Phase 0: Pre-Flight — Performance Context

Create `preflight_summary.md`:

- **System type:** Web application, API, data pipeline, batch processing, real-time system...
- **Are performance targets (SLO/SLA) defined?**
  - Latency target: pXX — p50, p95, p99
  - Throughput target: requests/operations per second
  - Error rate target: maximum acceptable %
  - Availability target: 99.9%, 99.99%...
- **Existing monitoring infrastructure:** APM (Datadog, New Relic, Dynatrace...), Prometheus, custom logging, or none
- **Known performance issues:** User complaints, incident records, list of slow endpoints
- **Load profile:** Typical concurrent users, peak traffic time and volume
- **Developer Intent:** Commit logs, issue tracker, `TODO` comments — is there known performance debt?

---

## Phase 1: Critical Path & Load Profile

### 1.1 Critical Path Detection

Identify the most heavily used and highest-impact flows:

| Flow / Endpoint | Usage Frequency | Business Impact | Current Avg Duration | SLO Target |
|---|---|---|---|---|

### 1.2 Dependency Chain

Show how long each step along the critical path takes — as a waterfall:

```
Request Received      [==] 2ms
Auth Validation       [====] 8ms
Cache Check           [=] 1ms
DB Query              [====================] 45ms  ← BOTTLENECK
Business Logic        [===] 6ms
Response Serialization[==] 3ms
─────────────────────────────────────────────────
Total                 65ms  (SLO: 50ms) ⚠️
```

### 1.3 Concurrency Model

- How does the system handle concurrent requests? (thread pool, async/await, event loop, worker process...)
- What is the concurrency limit? What happens when exceeded?
- Connection pool sizes: DB, cache, external service connections

---

## Phase 2: Application Layer Performance

### 2.1 Computation Bottlenecks

Search for these patterns in code:

| Pattern | Detected | Location | Impact |
|---|---|---|---|
| Nested loop (N² or worse complexity) | | | |
| Repeatedly traversing large data structures | | | |
| Unnecessary object copying / serialization | | | |
| Synchronous blocks inside async flow | | | |
| Heavy operation repeated on every request (should be cached) | | | |

### 2.2 Memory Usage

- Memory leak risk structures: event listeners not being cleaned up, closures holding references?
- Large objects held in memory unnecessarily
- Garbage collection pressure: many short-lived objects being created?

### 2.3 Caching Analysis

| Dimension | Status | Detail |
|---|---|---|
| Cache layer present? | | Redis / Memcached / In-process / None |
| Cache hit rate | | ⚠️ NO MEASUREMENT / % |
| What data is cached? | | |
| Cache invalidation strategy | | |
| Cache stampede (thundering herd) protection | | Present / None |
| Hot paths that should be cached but aren't | | |

### 2.4 Asynchronous Processing

- Are CPU-intensive or I/O-intensive operations offloaded to background?
- Is queue usage present? Is queue size monitored?
- How are fan-out operations (N operations per request) managed?

---

## Phase 3: Data Layer Performance

### 3.1 Query Analysis

Identify slow queries:

| Query / Operation | Location | Estimated Duration | Problem | Recommendation |
|---|---|---|---|---|
| | | | N+1 / Full scan / Missing index / ... | |

**N+1 query detection:** For ORM-using systems, find places where related data is fetched in repeated individual queries instead of `SELECT * FROM X WHERE id IN (...)`.

### 3.2 Index Analysis

| Table | Frequently Used Filter/Join Columns | Index Present? | Assessment |
|---|---|---|---|

### 3.3 Connection Management

- Connection pool size and current utilization
- Connection leak risk: is the connection closed on every code path?
- Long-running transactions: lock contention risk

### 3.4 Data Volume & Growth

- Largest tables/collections and estimated annual growth rate
- Queries returning full tables without pagination?
- Archiving / TTL policy: is old data being cleaned up?

---

## Phase 4: Infrastructure & Network Layer

### 4.1 Network Latency

- What protocol is used for inter-service communication? (HTTP/1.1, HTTP/2, gRPC, TCP...)
- Geographic latency: are services in the same region or different regions?
- Is DNS resolution, TLS handshake cost accounted for?

### 4.2 Resource Usage

| Resource | Avg Usage | Peak Usage | Limit | Assessment |
|---|---|---|---|---|
| CPU | | | | |
| RAM | | | | |
| Disk I/O | | | | |
| Network Bandwidth | | | | |

### 4.3 CDN & Static Asset Optimization (For Applications)

- Are static assets (JS, CSS, images) served from a CDN?
- Is asset compression (gzip/brotli) applied?
- Are HTTP cache headers correctly set?
- Are there resources blocking the critical render path?

---

## — EVALUATIVE LAYER —

---

## Phase 5: Risk & Scalability Limits

### 5.1 Scalability Limit Analysis

Under how many concurrent users/requests does the system fail?

| Component | Current Capacity | Estimated Breaking Point | Failure Reason |
|---|---|---|---|
| Application server | | | |
| Database | | | |
| Cache layer | | | |
| Load balancer | | | |

### 5.2 Single Points of Performance Failure

Components that form a performance single point of failure:

| Component | Why Single Point | Scaling Strategy | Current Status |
|---|---|---|---|
| | Non-horizontally-scalable DB / Shared cache / Global lock / ... | | Applied / Planned / None |

### 5.3 Load & Performance Testing Status

| Test Type | Done? | Last Test Date | Result | Tool |
|---|---|---|---|---|
| Load test (expected load) | | | | |
| Stress test (limit testing) | | | | |
| Soak test (sustained load) | | | | |
| Spike test (sudden load increase) | | | | |

---

## Phase 6: Prioritized Improvement Roadmap

### 6.1 Impact-Effort Matrix

For each detected performance issue:

| Issue | Impact (Latency/Throughput/Cost) | Effort | Priority Quadrant |
|---|---|---|---|
| | | Small/Medium/Large | Quick Win / Big Bet / Filler / Waste |

### 6.2 Performance Budget (Optional)

Allocated time per component for the critical path:

| Component | Current | Target | Budget |
|---|---|---|---|
| Total response time | | | 100% |
| Auth | | | ≤ 10% |
| DB | | | ≤ 50% |
| Business logic | | | ≤ 20% |
| Serialization/Network | | | ≤ 20% |

### 6.3 Monitoring & Observability Improvements

- Which metrics are currently unmeasured but should be?
- Are alert thresholds defined?
- Is distributed tracing set up — can root cause of slow operations be found?

---

## Output File System

```
docs/performance-audit/
├── index.md
├── preflight_summary.md
│   — DESCRIPTIVE —
├── critical_path_map.md
├── application_layer_analysis.md
├── data_layer_analysis.md
├── infrastructure_analysis.md
├── system_taxonomy.md
│   — EVALUATIVE —
├── completeness_report.md      ← Missing monitoring, unmeasured critical paths
├── scalability_limits.md
└── improvement_roadmap.md
```

---

## Quality Checklist

- [ ] Every performance claim backed by metric or marked `⚠️ NO MEASUREMENT`
- [ ] Critical path waterfall diagram drawn
- [ ] N+1 query scan performed and result documented
- [ ] File path or query text provided for every bottleneck
- [ ] Scalability limit table filled out
- [ ] Every recommendation in improvement roadmap placed in impact-effort quadrant
- [ ] Monitoring infrastructure gaps listed in `completeness_report.md`
