# Module: Project Intelligence & Auto-Analyst

**Priority**: P0 (Critical - Master Orchestrator)  
**Module Code**: **PROJECT-INTEL** (or **AUTO-ANALYST**)  
**Tokens**: ~5000  
**Analysis Time**: 15-20 minutes (Discovery), 5-10 minutes (Planning), Variable (Execution)  

---

## Purpose

Projeyi otomatik analiz eden, ihtiyaç duyulan tüm modülleri tespit eden, kullanıcıya öneriler sunan ve onaylandıktan sonra modülleri sıralı şekilde çalıştırıp final rapor oluşturan **Meta-Orchestrator** modülü. Tüm diğer modüllerin üzerinde çalışan bir "Project Intelligence" sistemi.

---

## 🎯 Çözülen Problem

```yaml
without_project_intel:
  confusion: "Hangi modülleri çalıştırmalıyım?"
  overwhelm: "66 tane modül var, nereden başlayacağım?"
  inefficiency: "Gereksiz modülleri de çalıştırıyorum"
  manual: "Her modülü tek tek çağırmam gerekiyor"
  time_waste: "Sıralama ve bağımlılıkları ben yönetiyorum"

with_project_intel:
  smart: "Proje otomatik analiz ediliyor"
  focused: "Sadece gerekli modüller öneriliyor"
  efficient: "En önemli modüller önce çalışıyor"
  automated: "Tek komutla tüm analiz tamamlanıyor"
  guided: "Adım adım ilerleme takibi"
```

---

## 🔍 Phase 1: Project Discovery & Analysis

### Step 1: Quick Project Scan (5 minutes)

```yaml
scan_project_structure:
  action: "Proje dosya yapısını ve temel bilgileri topla"
  
  detect:
    project_type:
      method: "File patterns, package.json, *.csproj, etc."
      options:
        - "Frontend Only (React, Vue, Angular)"
        - "Backend Only (.NET, Node.js, Python)"
        - "Full-Stack"
        - "Mobile (React Native, Flutter)"
        - "Desktop (Electron)"
        - "Library/Package"
        - "Unknown/Mixed"
    
    tech_stack:
      frontend: "React, Vue, Angular, Svelte, Next.js, etc."
      backend: ".NET, Node.js, Python, Go, Java, etc."
      database: "PostgreSQL, MongoDB, MySQL, Redis, etc."
      testing: "Jest, xUnit, Pytest, Cypress, etc."
      infra: "Docker, Kubernetes, CI/CD configs"
    
    project_size:
      total_files: "Count all code files"
      total_lines: "Sum of all LOC"
      complexity_score: "Average cyclomatic complexity"
      file_types: "Distribution (.ts, .cs, .py, etc.)"
    
    existing_docs:
      count: "Number of .md files"
      types: "README, API docs, architecture, etc."
      quality_score: "0-10 based on completeness"
    
    existing_tests:
      count: "Number of test files"
      coverage: "If coverage report exists, extract %"
      frameworks: "Jest, xUnit, Pytest detected"
    
    git_info:
      commits: "Total commit count"
      contributors: "Number of contributors"
      branches: "Active branches"
      last_commit: "Days since last commit"
      activity: "Commits per month (trend)"
    
    special_features:
      visual_builder: "Detect canvas, drag-drop patterns"
      collaboration: "Detect WebSocket, SignalR"
      e_commerce: "Detect cart, checkout, payment"
      admin_panel: "Detect CRUD, user management"
      authentication: "Detect JWT, OAuth, sessions"
      api: "Detect REST, GraphQL endpoints"

output:
  project_profile: "Comprehensive project metadata"
  confidence: "High (95%)"
```

---

### Step 2: Needs Analysis (10 minutes)

```yaml
analyze_needs:
  action: "Her modülün gerekli olup olmadığını değerlendir"
  
  scoring_framework:
    relevance_score:
      calculation: "0-10 scale"
      factors:
        - "Project type match"
        - "Tech stack compatibility"
        - "Detected features"
        - "Existing gaps"
    
    priority_score:
      calculation: "P0 (Critical) to P3 (Optional)"
      factors:
        - "Impact on project success"
        - "Common issues detected"
        - "Best practices adherence"
    
    urgency_score:
      calculation: "0-10 scale"
      factors:
        - "Production readiness"
        - "Security vulnerabilities potential"
        - "Performance issues potential"
    
    combined_score:
      formula: "(relevance * 0.4) + (priority * 0.4) + (urgency * 0.2)"
      threshold: "> 6.0 = Recommended"

module_evaluation_examples:
  file_structure_FS:
    relevance: 10 # Always relevant
    priority: 10 # P0 - Critical
    urgency: 8 # Usually important
    combined: 9.2
    recommendation: "MUST RUN"
    reason: "Every project needs file structure analysis"
  
  security_SEC:
    relevance: 10 # Always relevant
    priority: 10 # P0 - Critical
    urgency: 10 # Security is always urgent
    combined: 10.0
    recommendation: "MUST RUN"
    reason: "Security vulnerabilities can be critical"
  
  turkish_market_TR:
    relevance_check: |
      IF project has:
        - KVKK mentions
        - Turkish language files
        - Turkish payment systems
      THEN relevance = 10
      ELSE relevance = 0
    recommendation: "CONDITIONAL"
    reason: "Only relevant for Turkish market projects"
  
  collaboration_COLLAB_TEST:
    relevance_check: |
      IF project has:
        - WebSocket/SignalR
        - Real-time features
        - Multi-user editing
      THEN relevance = 10
      ELSE relevance = 1
    recommendation: "CONDITIONAL"
    reason: "Only for collaborative applications"
  
  documentation_DOCS:
    relevance_check: |
      IF docs_count > 10:
        relevance = 10 (needs consolidation)
      ELIF docs_count < 3:
        relevance = 2 (DOCGEN better choice)
      ELSE:
        relevance = 5
    recommendation: "SMART CHOICE"
  
  documentation_DOCGEN:
    relevance_check: |
      IF docs_count < 3:
        relevance = 10 (missing docs)
      ELIF docs_count > 10:
        relevance = 1 (DOCS better choice)
      ELSE:
        relevance = 3
    recommendation: "SMART CHOICE"
  
  test_generation_TEST_GEN:
    relevance_check: |
      IF test_coverage < 40%:
        relevance = 10
        urgency = 9
      ELIF test_coverage < 70%:
        relevance = 7
        urgency = 6
      ELSE:
        relevance = 3
        urgency = 2
    recommendation: "COVERAGE-BASED"
  
  ui_interaction_UI_TEST:
    relevance_check: |
      IF visual_builder OR canvas_detected OR drag_drop_patterns:
        relevance = 10
        priority = 10
      ELIF frontend_only:
        relevance = 7
      ELSE:
        relevance = 2
    recommendation: "FEATURE-BASED"

output:
  recommended_modules: "List with scores and reasons"
  optional_modules: "Lower priority suggestions"
  skipped_modules: "Not relevant, with explanation"
```

---

### Step 3: Dependency & Sequencing

```yaml
determine_execution_order:
  action: "Modüllerin çalışma sırasını belirle"
  
  dependencies:
    PROJECT_TYPE_DETECTION:
      must_run_before: "ALL modules"
      reason: "Other modules need project type info"
    
    FS_file_structure:
      must_run_before:
        - "HG (Hidden Gems)"
        - "REFACTOR"
        - "AI (AI Code Quality)"
      reason: "Structure analysis needed for code quality checks"
    
    FG_feature_gap:
      must_run_before:
        - "TEST-GEN"
        - "UI-TEST"
      reason: "Test scenarios based on features"
    
    DOCS_or_DOCGEN:
      run_order: "Late (after analysis complete)"
      reason: "Documentation created/updated based on findings"
  
  sequencing_strategy:
    phase_1_foundation:
      modules:
        - "PROJECT_TYPE_DETECTION"
        - "FS (File Structure)"
        - "SEC (Security)"
        - "PERF (Performance)"
      reason: "Critical baseline analysis"
      duration: "~20 minutes"
    
    phase_2_deep_dive:
      modules:
        - "API (if backend)"
        - "DB (if database detected)"
        - "UI (if frontend)"
        - "HG (Hidden Gems)"
        - "AI (AI Code Quality)"
      reason: "Detailed component analysis"
      duration: "~30 minutes"
    
    phase_3_specialized:
      modules:
        - "FG (Feature Gap)"
        - "TR (if Turkish market)"
        - "COLLAB-TEST (if collaborative)"
        - "UI-TEST (if visual builder)"
      reason: "Domain-specific analysis"
      duration: "~25 minutes"
    
    phase_4_testing:
      modules:
        - "TEST-GEN"
        - "TEST (Testing Strategy)"
      reason: "Generate and validate tests"
      duration: "~20 minutes"
    
    phase_5_documentation:
      modules:
        - "DOCS (if > 10 docs)"
        - "DOCGEN (if < 3 docs)"
      reason: "Finalize documentation"
      duration: "~15 minutes"
    
    phase_6_final_report:
      modules:
        - "PROJECT_INTEL (self - final report)"
      reason: "Aggregate all findings"
      duration: "~5 minutes"
  
  total_estimated_time: "~115 minutes (for full suite)"
```

---

## 📋 Phase 2: User Interaction & Confirmation

### Interactive Recommendation Report

```markdown
# Project Intelligence Report - [Project Name]

**Analysis Date**: December 21, 2024 17:30:00  
**Project Type**: Full-Stack E-Commerce  
**Tech Stack**: React 18 + .NET 8 + PostgreSQL  
**Project Size**: 18,500 LOC across 247 files  
**Team Size**: 5 contributors  

---

## 📊 Quick Assessment

| Aspect | Score | Status |
|--------|-------|--------|
| **Code Structure** | 6.5/10 | 🟡 Needs Attention |
| **Security** | 4.2/10 | 🔴 Critical Issues |
| **Performance** | 7.8/10 | 🟢 Good |
| **Documentation** | 3.1/10 | 🔴 Poor |
| **Test Coverage** | 28% | 🔴 Critical |
| **Overall Health** | 5.9/10 | 🟡 Below Average |

---

## 🎯 Recommended Analysis Modules (12 modules)

### 🔴 Critical Priority (Must Run - 4 modules)

**1. FS (File Structure Analysis)** - Score: 9.2/10
- **Why**: God files detected, circular dependencies likely
- **Duration**: ~8 minutes
- **Impact**: High - Foundation for other analyses
- **Run**: ✅ YES

**2. SEC (Security Analysis)** - Score: 10.0/10  
- **Why**: No security headers, potential SQL injection, missing auth checks
- **Duration**: ~12 minutes
- **Impact**: CRITICAL - Production vulnerability risk
- **Run**: ✅ YES

**3. TEST-GEN (Test Generation)** - Score: 9.5/10
- **Why**: Only 28% coverage, 45+ untested features
- **Duration**: ~15 minutes
- **Impact**: High - Quality assurance
- **Run**: ✅ YES

**4. DOCGEN (Documentation Generation)** - Score: 9.0/10
- **Why**: Only README exists (50 lines), no API docs, no setup guide
- **Duration**: ~10 minutes
- **Impact**: High - Onboarding and maintainability
- **Run**: ✅ YES

---

### 🟠 High Priority (Strongly Recommended - 5 modules)

**5. PERF (Performance Analysis)** - Score: 8.5/10
- **Why**: N+1 queries detected, bundle size 2.4MB, slow initial load
- **Duration**: ~10 minutes
- **Impact**: High - User experience
- **Run**: ✅ RECOMMENDED

**6. API (API Design Analysis)** - Score: 8.2/10
- **Why**: 21 endpoints, inconsistent status codes, missing validation
- **Duration**: ~8 minutes
- **Impact**: Medium-High - API quality
- **Run**: ✅ RECOMMENDED

**7. HG (Hidden Gems)** - Score: 8.0/10
- **Why**: Likely zombie code, bus factor risks, "mış gibi" patterns
- **Duration**: ~10 minutes
- **Impact**: Medium - Technical debt
- **Run**: ✅ RECOMMENDED

**8. UI-TEST (UI Interaction Testing)** - Score: 9.8/10 ⭐
- **Why**: Visual builder detected, property binding issues reported, drag-drop needs testing
- **Duration**: ~20 minutes
- **Impact**: CRITICAL - Core feature validation
- **Run**: ✅ HIGHLY RECOMMENDED

**9. FG (Feature Gap Analysis)** - Score: 7.5/10
- **Why**: Comparison with Trendyol/Hepsiburada, missing competitive features
- **Duration**: ~12 minutes
- **Impact**: Medium - Product strategy
- **Run**: ⚠️ OPTIONAL (but valuable)

---

### 🟡 Medium Priority (Optional - 3 modules)

**10. DB (Database Analysis)** - Score: 7.0/10
- **Why**: PostgreSQL detected, potential optimization opportunities
- **Duration**: ~8 minutes
- **Impact**: Medium - Performance
- **Run**: ⚠️ OPTIONAL

**11. TR (Turkish Market)** - Score: 6.8/10
- **Why**: Turkish language files detected, but no KVKK compliance yet
- **Duration**: ~6 minutes
- **Impact**: Medium - Compliance
- **Run**: ⚠️ OPTIONAL

**12. DOCS (Documentation Analysis)** - Score: 3.0/10
- **Why**: Too few docs (only 2 files), DOCGEN is better choice
- **Duration**: ~5 minutes
- **Impact**: Low - Not applicable
- **Run**: ❌ SKIP (use DOCGEN instead)

---

## ⏱️ Execution Plan

### Recommended Execution (9 modules)

**Total Estimated Time**: ~85 minutes

#### Phase 1: Foundation (30 min)
1. FS (File Structure) - 8 min
2. SEC (Security) - 12 min
3. PERF (Performance) - 10 min

#### Phase 2: Deep Dive (38 min)
4. API (API Design) - 8 min
5. HG (Hidden Gems) - 10 min
6. UI-TEST (UI Testing) - 20 min ⭐

#### Phase 3: Quality (25 min)
7. TEST-GEN (Test Generation) - 15 min
8. DOCGEN (Documentation) - 10 min

#### Phase 4: Optional Extras (20 min)
9. FG (Feature Gap) - 12 min
10. DB (Database) - 8 min

---

## 🚀 Quick Actions

**Option A: Run All Recommended (9 modules)**
```
Estimated Time: 85 minutes
Modules: FS + SEC + PERF + API + HG + UI-TEST + TEST-GEN + DOCGEN + FG
```
✅ **CONFIRM & RUN**

**Option B: Critical Only (4 modules)**
```
Estimated Time: 45 minutes
Modules: FS + SEC + TEST-GEN + DOCGEN
```
⚡ **QUICK START**

**Option C: Custom Selection**
```
Select individual modules below
```
🎛️ **CUSTOMIZE**

**Option D: View Detailed Recommendations First**
```
See full analysis for each module
```
📊 **MORE INFO**

---

## 💬 Interactive Prompts

**User Response Expected**:

> **PROJECT-INTEL**: I've analyzed your project and found several critical areas that need attention. 
> 
> Your project has:
> - 🔴 **Low test coverage** (28%) - 45 features untested
> - 🔴 **Security vulnerabilities** - Missing auth checks, no CSRF protection
> - 🔴 **Poor documentation** - Only basic README
> - 🟡 **UI testing needed** - Visual builder property binding issues
>
> I recommend running **9 modules** in **~85 minutes** to get a comprehensive analysis.
>
> **What would you like to do?**
> 
> A) Run all 9 recommended modules (comprehensive)
> B) Run only 4 critical modules (quick scan)
> C) Let me customize the selection
> D) Show me more details first

[WAIT FOR USER RESPONSE]
```

---

## 🔄 Phase 3: Execution & Progress Tracking

### Sequential Execution Engine

```yaml
execution_flow:
  step_1_confirmation:
    action: "User selects option (A, B, C, or D)"
    validation: "Confirm module list and time estimate"
  
  step_2_initialization:
    action: "Prepare execution environment"
    tasks:
      - "Load selected module prompts"
      - "Initialize progress tracker"
      - "Create execution log"
      - "Set up checkpoints"
  
  step_3_sequential_run:
    for_each_module:
      pre_execution:
        - "Display: 'Starting [Module Name]...'"
        - "Show: Progress [3/9]"
        - "Estimate: '~12 minutes remaining for this module'"
      
      execution:
        - "Load module prompt"
        - "Run analysis"
        - "Capture output"
      
      post_execution:
        - "Display: '✅ [Module Name] Complete'"
        - "Show: Key findings summary (3-5 bullet points)"
        - "Save: Full report to file"
      
      checkpoint:
        - "Ask: 'Continue to next module? (Y/n)'"
        - "If critical issue found: 'ALERT: Critical security vulnerability detected. Review now? (Y/n)'"
  
  step_4_aggregation:
    action: "Combine all module reports"
    tasks:
      - "Generate executive summary"
      - "Create unified action plan"
      - "Prioritize findings (P0 → P3)"
      - "Estimate fix efforts"
      - "Create roadmap"

progress_tracking:
  real_time_display: |
    ┌─────────────────────────────────────────────────────┐
    │  PROJECT INTELLIGENCE - Analysis in Progress        │
    ├─────────────────────────────────────────────────────┤
    │  Phase: 2/4 - Deep Dive Analysis                    │
    │  Module: API Design Analysis (5/9)                  │
    │  Progress: ████████░░░░░░░░ 56%                     │
    │  Elapsed: 42 minutes                                │
    │  Remaining: ~33 minutes                             │
    ├─────────────────────────────────────────────────────┤
    │  Completed:                                         │
    │  ✅ File Structure (8 min) - 12 issues found        │
    │  ✅ Security (12 min) - 🔴 7 CRITICAL issues!       │
    │  ✅ Performance (10 min) - 5 optimizations          │
    │  ✅ Hidden Gems (10 min) - 23 zombie files          │
    │  ⏳ API Design (in progress...)                     │
    │                                                     │
    │  Pending:                                           │
    │  ⏸️ UI Testing                                      │
    │  ⏸️ Test Generation                                 │
    │  ⏸️ Documentation Generation                        │
    │  ⏸️ Feature Gap                                     │
    └─────────────────────────────────────────────────────┘
  
  live_updates:
    format: "Real-time console/UI updates"
    frequency: "Every 30 seconds or on significant events"
```

---

## 📊 Phase 4: Final Unified Report

```markdown
# Project Intelligence - Final Report

**Project**: Visual Builder E-Commerce  
**Analysis Date**: December 21, 2024  
**Modules Executed**: 9 of 66 available  
**Total Duration**: 1 hour 23 minutes  
**Findings**: 127 issues identified  

---

## 🎯 Executive Summary

Your project has been comprehensively analyzed across 9 critical dimensions. Here are the key findings:

### Critical Issues (Require Immediate Action) - 18 found

1. **🔴 Security - SQL Injection Vulnerability** (SEC module)
   - **Location**: `src/api/products/ProductController.cs:45`
   - **Risk**: High - Production data exposure
   - **Fix**: Use parameterized queries
   - **Effort**: 30 minutes
   - **Priority**: P0

2. **🔴 UI - Property Binding Broken** (UI-TEST module)
   - **Location**: `src/components/PropertiesPanel.tsx:145`
   - **Impact**: Core feature not working
   - **Fix**: Add `updateComponent` call in onChange
   - **Effort**: 15 minutes
   - **Priority**: P0

3. **🔴 Testing - 45 Features Untested** (TEST-GEN module)
   - **Coverage**: 28% (target: 80%)
   - **Missing**: Checkout flow, admin panel, user registration
   - **Fix**: Generated 127 test scenarios (ready to implement)
   - **Effort**: 12 hours
   - **Priority**: P0

[... 15 more critical issues ...]

---

### High Priority Issues - 34 found

[... list of P1 issues ...]

---

### Medium Priority Issues - 47 found

[... list of P2 issues ...]

---

### Low Priority Issues - 28 found

[... list of P3 issues ...]

---

## 📈 Module-by-Module Summary

### ✅ File Structure (FS) - 12 issues
- 3 God files detected (> 1000 lines)
- 5 circular dependencies
- 4 orphaned files
- **Action**: Refactor UserService.cs, split into smaller modules

### ✅ Security (SEC) - 7 CRITICAL issues  
- SQL injection vulnerability
- Missing CSRF protection
- Weak password hashing
- **Action**: Fix SQL queries, add anti-forgery tokens, upgrade to bcrypt

### ✅ Performance (PERF) - 5 optimizations
- N+1 queries in products listing
- Bundle size 2.4MB (target: < 1MB)
- Slow initial load (3.2s)
- **Action**: Add eager loading, code splitting, lazy load images

### ✅ API Design (API) - 8 issues
- Inconsistent status codes (200 vs 201 vs 204)
- Missing request validation
- No rate limiting
- **Action**: Standardize responses, add FluentValidation, implement rate limiting

### ✅ Hidden Gems (HG) - 23 zombie files
- 15 unused components
- 8 dead code sections
- Bus factor risk (3 critical files only 1 dev knows)
- **Action**: Remove unused files, document critical code

### ✅ UI Testing (UI-TEST) - 7 CRITICAL bugs detected! ⭐
- Property binding not working
- Resize handles missing event listeners
- Drop position calculation wrong
- **Action**: Fix property panel, add resize handlers, correct drop math

### ✅ Test Generation (TEST-GEN) - 127 scenarios generated
- 45 features completely untested
- 82 edge cases missing
- **Action**: Implement generated tests (12 hours estimated)

### ✅ Documentation Generation (DOCGEN) - 8 docs created
- README (comprehensive, 300 lines)
- API_REFERENCE (21 endpoints)
- SETUP guide
- ARCHITECTURE diagram
- **Action**: Review and customize generated docs

### ✅ Feature Gap (FG) - 12 missing features
- Compared with Trendyol: 8 missing features
- Compared with Hepsiburada: 4 missing features
- **Action**: Prioritize wishlist, advanced filters, live chat

---

## 🗺️ Recommended Roadmap

### Sprint 1 (This Week) - Fix Critical Issues

**Security Fixes** (4 hours)
- [ ] Fix SQL injection (30 min)
- [ ] Add CSRF protection (1 hour)
- [ ] Upgrade password hashing (30 min)
- [ ] Add input validation (2 hours)

**UI Fixes** (2 hours)
- [ ] Fix property binding (15 min)
- [ ] Add resize event listeners (30 min)
- [ ] Fix drop position calc (20 min)
- [ ] Test all fixes (55 min)

**Total**: 6 hours

---

### Sprint 2 (Next Week) - Test Coverage

**Implement Generated Tests** (12 hours)
- [ ] Setup test framework (if needed)
- [ ] Implement unit tests (4 hours)
- [ ] Implement integration tests (4 hours)
- [ ] Implement E2E tests (4 hours)

**Goal**: 28% → 80% coverage

---

### Sprint 3 (Week 3) - Performance & Documentation

**Performance Optimizations** (6 hours)
- [ ] Fix N+1 queries (2 hours)
- [ ] Code splitting (2 hours)
- [ ] Image optimization (2 hours)

**Documentation** (4 hours)
- [ ] Review generated docs (2 hours)
- [ ] Add business-specific details (2 hours)

---

### Sprint 4 (Week 4) - Feature Gaps

**New Features** (20 hours)
- [ ] Wishlist functionality (6 hours)
- [ ] Advanced filters (8 hours)
- [ ] Live chat widget (6 hours)

---

## 📊 Impact Analysis

### Before Analysis
```yaml
code_quality: 5.9/10
security: 🔴 Vulnerable
test_coverage: 28%
documentation: 🔴 Poor
feature_completeness: 67%
```

### After Implementing Recommendations
```yaml
code_quality: 8.5/10 (+2.6)
security: 🟢 Secure (+5.8)
test_coverage: 80% (+52%)
documentation: 🟢 Excellent (+6.9)
feature_completeness: 92% (+25%)
```

**Estimated Improvement**: +47% overall project health

---

## 💾 Generated Artifacts

All module reports and generated files are available:

```
/project-analysis/
├── final-report.md (this file)
├── executive-summary.md
├── action-plan.md
├── roadmap.md
│
├── /module-reports/
│   ├── file-structure-report.md
│   ├── security-analysis.md
│   ├── performance-analysis.md
│   ├── api-design-report.md
│   ├── hidden-gems-report.md
│   ├── ui-test-report.md
│   ├── test-scenarios.md
│   ├── documentation-generated/
│   └── feature-gap-report.md
│
├── /generated-tests/
│   ├── unit-tests/ (127 test files)
│   ├── integration-tests/
│   └── e2e-tests/
│
└── /generated-docs/
    ├── README.md
    ├── API_REFERENCE.md
    ├── SETUP.md
    ├── ARCHITECTURE.md
    └── CONTRIBUTING.md
```

---

## 🎯 Next Steps

1. **Review this report** (15 minutes)
2. **Start Sprint 1** - Fix critical security & UI issues (6 hours)
3. **Implement generated tests** - Boost coverage to 80% (12 hours)
4. **Deploy with confidence** 🚀

---

**Questions or need clarification?** Ask PROJECT-INTEL for details on any finding.

**Want to re-run analysis?** Say "Re-analyze [module name]" to update specific areas.

**Ready to start?** Say "Start Sprint 1" to begin implementation.
```

---

## 🚀 Usage Examples

### Example 1: Auto-Discover & Run

```markdown
"PROJECT-INTEL koduyla projeyi analiz et.

Mode: Full Auto-Discovery

Yap:
1. Projeyi tara ve ihtiyaçları tespit et
2. Önerileri sun
3. Onayımı bekle
4. Onaylandıktan sonra modülleri çalıştır
5. Final rapor oluştur

Türkçe interaktif mesajlar."
```

**Expected Flow**:
```
[PROJECT-INTEL] 📊 Projenizi tarıyorum...

✅ Analiz tamamlandı!

Proje: React + .NET E-Ticaret
Durum: 🟡 İyileştirme Gerekiyor (5.9/10)

Kritik Sorunlar:
- 🔴 Güvenlik açıkları (7 adet)
- 🔴 Test coverage düşük (28%)
- 🔴 UI property binding çalışmıyor

Öneri: 9 modül çalıştıralım (~85 dakika)

A) Tümünü çalıştır (9 modül)
B) Sadece kritik modüller (4 modül)  
C) Özelleştir

Seçiminiz?
```

[User: A]

```
[PROJECT-INTEL] ✅ Başlıyorum!

Modül 1/9: File Structure Analysis
⏳ Tahmini süre: 8 dakika...

[8 minutes later]

✅ File Structure Complete!
Özet:
- 3 God file bulundu (> 1000 satır)
- 5 circular dependency
- Öneri: UserService.cs'i böl

Devam? (Y/n)
```

---

### Example 2: Quick Critical Scan

```markdown
"PROJECT-INTEL koduyla sadece kritik sorunları tara.

Mode: Quick Scan

Çıktı: Sadece P0 sorunlar ve hızlı fix önerileri"
```

---

### Example 3: Specific Focus

```markdown
"PROJECT-INTEL koduyla visual builder özelliklerime odaklan.

Özel İstek:
- UI-TEST modülünü mutlaka çalıştır
- Property binding sorununu tespit et
- Collaboration features'ı test et
- Diğerleri için otomatik öneri

Interaktif çalış."
```

---

## 🔧 Module Detection Logic

```yaml
detection_rules:
  FS_file_structure:
    always_run: true
    reason: "Foundation for all analyses"
  
  SEC_security:
    always_run: true
    reason: "Security is critical for all projects"
  
  PERF_performance:
    run_if: "project_size > 5000 LOC OR frontend_detected"
  
  UI_TEST_ui_interaction:
    run_if: |
      canvas_detected OR 
      drag_drop_patterns OR 
      visual_builder_keywords OR
      user_reported_ui_issues
  
  COLLAB_TEST_collaboration:
    run_if: |
      websocket_detected OR
      signalr_detected OR
      real_time_keywords OR
      multi_user_features
  
  TR_turkish_market:
    run_if: |
      turkish_language_files OR
      kvkk_mentions OR
      turkish_payment_systems OR
      tr_currency_usage
  
  DOCS_documentation_analysis:
    run_if: "doc_count > 10"
  
  DOCGEN_documentation_generation:
    run_if: "doc_count < 3"
  
  TEST_GEN_test_generation:
    run_if: "test_coverage < 70% OR test_files == 0"
  
  FG_feature_gap:
    run_if: |
      competitor_analysis_requested OR
      e_commerce_detected OR
      saas_product
```

---

## 📋 Deliverables

```yaml
phase_1_discovery:
  files:
    - "project-profile.md"
    - "needs-analysis.md"
    - "recommended-modules.md"
  
  duration: "15-20 minutes"

phase_2_planning:
  files:
    - "execution-plan.md"
    - "time-estimate.md"
    - "user-confirmation-prompt.md"
  
  duration: "5-10 minutes"

phase_3_execution:
  files:
    - "progress-log.txt" (real-time)
    - "module-reports/" (individual reports)
    - "checkpoint-logs.md"
  
  duration: "Variable (45-120 minutes)"

phase_4_final:
  files:
    - "final-report.md" (comprehensive)
    - "executive-summary.md"
    - "action-plan.md"
    - "roadmap.md"
    - "all-generated-artifacts/" (tests, docs, etc.)
  
  duration: "5 minutes"
```

---

## 🎓 Smart Features

### 1. Adaptive Recommendations

```yaml
scenario_1_new_project:
  detected: "< 1 month old, < 10 commits"
  recommendation:
    - "DOCGEN (setup documentation)"
    - "FS (establish structure)"
    - "TEST-GEN (TDD approach)"
    - "Skip: DOCS, HG, REFACTOR (too early)"

scenario_2_legacy_project:
  detected: "> 2 years old, > 1000 commits, no tests"
  recommendation:
    - "HG (find technical debt)"
    - "SEC (legacy security issues)"
    - "TEST-GEN (add tests to legacy)"
    - "REFACTOR (modernize)"

scenario_3_pre_production:
  detected: "deploy_config exists, no production yet"
  recommendation:
    - "SEC (critical!)"
    - "PERF (user experience)"
    - "TEST-GEN (quality assurance)"
    - "DOCS (operational docs)"

scenario_4_visual_builder_focus:
  detected: "canvas elements, drag-drop, property panels"
  recommendation:
    - "UI-TEST (top priority!)"
    - "COLLAB-TEST (if multi-user)"
    - "PERF (canvas rendering)"
    - "A11Y (accessibility)"
```

---

### 2. Cost-Benefit Analysis

```yaml
show_roi:
  module: "TEST-GEN"
  cost: "12 hours to implement generated tests"
  benefit:
    - "Prevent 5-10 production bugs"
    - "Save 20+ hours of manual testing"
    - "Increase deployment confidence"
  roi: "167% time savings + quality improvement"

show_roi:
  module: "UI-TEST"
  cost: "20 minutes to run + 2 hours to fix detected bugs"
  benefit:
    - "Fix 7 critical UI bugs"
    - "Prevent user frustration"
    - "Improve conversion rate (estimated +15%)"
  roi: "🚀 High business impact"
```

---

### 3. Checkpoint Intelligence

```yaml
intelligent_pausing:
  scenario: "Critical security vulnerability found in SEC module"
  
  action:
    - "Pause execution immediately"
    - "Display: '🔴 CRITICAL: SQL Injection found!'"
    - "Ask: 'This is a production security risk. Fix now before continuing? (Y/n)'"
    - "If Y: Show fix suggestion, wait for implementation"
    - "If n: Log as P0, continue analysis"
  
  benefit: "Immediate action on critical findings"
```

---

## 🔄 Self-Improvement

```yaml
learning_system:
  track_metrics:
    - "Which modules found most issues"
    - "Which recommendations user accepted"
    - "Which modules user skipped"
    - "Execution time vs estimate accuracy"
  
  optimize:
    - "Refine module recommendations"
    - "Improve time estimates"
    - "Adjust priority scores"
    - "Learn project-specific patterns"
  
  feedback_loop:
    - "After analysis: 'Was this helpful? Rate 1-5'"
    - "Track: Which findings led to action"
    - "Improve: Detection accuracy over time"
```

---

## 📚 Related Modules

**PROJECT-INTEL manages ALL modules:**
- All 24 analysis modules (FS, SEC, PERF, API, DB, UI, etc.)
- All specialized modules (HG, AI, FG, TR, etc.)
- All testing modules (TEST-GEN, UI-TEST, COLLAB-TEST, etc.)
- All documentation modules (DOCS, DOCGEN, etc.)

**PROJECT-INTEL is the master orchestrator!**

---

**Project Intelligence Complete** | Modules Orchestrated: 66 | Confidence: High (95%)

---

*Module Version: 1.0*  
*Created: December 2024*  
*The Brain of Your Analysis System*
