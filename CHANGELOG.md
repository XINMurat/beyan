# Changelog

All notable changes to Beyan are documented here.

---

## [2.0.0] — 2026-04-18
### Added
- **v2.0 Agentic Framework**: A complete autonomous system for repository analysis.
- CLI analyzer with auto-discovery (`discovery.py`).
- MANIFEST-driven modular prompt compilation (`compiler.py`).
- Semi-autonomous agentic loop with human-in-the-loop checkpoints (`orchestrator.py`).
- OpenAI + Anthropic API clients with exception-based error handling (`api_clients.py`).
- Priority-based smart token budget management (Auto-pruning P2/P3 modules).
- Session persistence and resuming capabilities for agentic loops.
- Git safety branching protocol for destructive operations.
- Comprehensive pytest suite (31 tests).
- Professional README and project documentation for v2.

---

## [1.0.0] — 2026-04-16

### Initial Release

**Prompt Family (15 active prompts):**

**Project-Type Prompts (7)**
- Application Analysis (`master_proje_analiz_promptu_v2.3`) — web/mobile/desktop apps with microservice and mobile extensions
- OS / System Software (`os_analiz_promptu_generic_v1.0`) — kernels, firmware, hypervisors
- Research / AI-ML (`research_ai_analiz_promptu_generic_v1.0`) — experimental models, mathematical documentation
- Data & Analytics (`veri_analitik_analiz_promptu_v1.0`) — ETL, pipelines, data quality
- Infrastructure / DevOps (`altyapi_devops_analiz_promptu_v1.0`) — IaC, CI/CD, FinOps
- Legacy / Migration (`legacy_goc_analiz_promptu_v1.0`) — two-system gap analysis, cutover strategy
- Blockchain (`blockchain_analiz_promptu_v1.0`) — smart contract vulnerabilities, tokenomics, economic security

**Focus-Based Prompts (4)**
- Security Audit (`guvenlik_denetim_promptu_v1.0`) — OWASP Top 10, threat modeling
- Performance Audit (`performans_denetim_promptu_v1.0`) — critical path, bottleneck analysis
- API Design Audit (`api_tasarim_denetim_promptu_v1.0`) — contract quality, breaking changes
- Compliance Audit (`uyumluluk_denetim_promptu_v1.0`) — KVKK, GDPR, PCI-DSS, HIPAA

**Cross-Cutting Tools (2)**
- Remediation Plan Generator (`duzeltme_plani_uretici_promptu_v1.0`) — impact-effort matrix, sprint plan
- Project Health Score (`proje_saglik_skoru_promptu_v1.0`) — quantified 1–5 scorecard with project-type calibration

**Entry Point (1)**
- Triage & Routing (`triyaj_yonlendirme_promptu_v1.0`) — unknown project classification, monorepo guide

**Special (1)**
- Meta Audit (`ai_analiz_sistemi_denetim_promptu_v1.0`) — audit the library itself

**Support Files:**
- Navigation Standard — multi-prompt output directory guide, Remediation Plan feed mapping
- Growth Strategy — when to add prompts, update procedure, major/minor versioning thresholds

**Meta-Analysis:**
- Library audited using its own Meta Audit prompt
- Health Score: 2.45 (Before) → 4.75 (After) — +1.75 point improvement (+71%)
- All D-series quick fixes and G-series medium improvements applied
