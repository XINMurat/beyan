# Usage Guide - Project Analysis System v3.3

**Complete guide for all 3 operating modes**

---

## 📖 Table of Contents

1. [Quick Start](#quick-start)
2. [Mode 1: Analyze Only](#mode-1-analyze-only)
3. [Mode 2: Analyze + Plan](#mode-2-analyze--plan)
4. [Mode 3: Full Flow (Semi-Autonomous)](#mode-3-full-flow)
5. [Advanced Usage](#advanced-usage)
6. [Troubleshooting](#troubleshooting)

---

## Quick Start

### Step 1: Upload Files to AI

**Minimum (for Mode 1)**:
```
- ORCHESTRATOR_PROMPT.md
- BASE_PROMPT.md
- Your project files
```

**Recommended (for all modes)**:
```
- ORCHESTRATOR_PROMPT.md
- BASE_PROMPT.md
- MANIFEST.yaml
- modules/ (or let AI auto-load)
- Your project files
```

**For Trae IDE users**:
```
+ AGENTIC_WORKFLOW.md
+ Your agent rules.md files
```

---

### Step 2: Choose Your Mode

Give prompt in Turkish:

| Mode | Prompt Example | What Happens |
|------|---------------|--------------|
| Mode 1 | `"Projeyi analiz et"` | Analysis report only |
| Mode 2 | `"Aksiyon planı oluştur"` | Report + action plan |
| Mode 3 | `"P0 sorunları düzelt"` | Full autonomous fix (with checkpoints) |

---

## Mode 1: Analyze Only

### Use Case
- Daily status reports
- Understanding current project health
- Getting recommendations without changes
- Audit reports for stakeholders

### How to Trigger

**Turkish Prompts**:
```markdown
"Projeyi analiz et"
"Security audit yap"
"Performans sorunlarını tespit et"
"WCAG compliance kontrol et"
"Hidden gem'leri bul"
"Sadece rapor ver, hiçbir değişiklik yapma"
```

### What Happens

```
1. AI loads BASE_PROMPT.md
2. AI selects relevant modules (or you specify)
3. AI analyzes your project files
4. AI generates Turkish report
5. NO code is written
6. NO files are changed
```

### Example Output

```markdown
# Proje Sağlık Raporu
**Tarih**: 15 Ocak 2025  
**Genel Skor**: 7.2/10 🟡

## Özet
├─ 🔴 P0 (Kritik): 3 sorun
├─ 🟡 P1 (Yüksek): 5 sorun
├─ 🟢 P2 (Orta): 8 sorun
└─ ⚪ P3 (Düşük): 4 sorun

## Kritik Bulgular (P0)

### 1. SQL Injection Riski 🔴
**Konum**: `src/services/OrderService.cs:45`  
**Sorgu**: String concatenation kullanılıyor

❌ **Mevcut Kod**:
```csharp
var sql = $"SELECT * FROM Orders WHERE CustomerId = {customerId}";
```

✅ **Önerilen Çözüm**:
```csharp
var orders = _context.Orders
    .Where(o => o.CustomerId == customerId)
    .ToList();
```

**Öncelik**: 🔴 P0 - Hemen yapılmalı  
**Çaba**: 2 saat  
**Etki**: Kritik güvenlik açığı

---

### 2. Exposed Secrets 🔴
**Konum**: `.env` dosyası Git history'de

**Risk**: 
- Database password public
- API key'ler eriÅŸilebilir
- Potansiyel veri ihlali

✅ **Önerilen Adımlar**:
1. Git history'den sil
2. .gitignore'a ekle
3. Secrets'ları rotate et
4. .env.example oluÅŸtur

**Öncelik**: 🔴 P0  
**Çaba**: 1 saat

[... continues with all findings ...]
```

### Customization

**Specific modules**:
```
"Sadece security analizi yap"
→ Loads: security-analysis.md

"Performance ve database analizi"
→ Loads: performance-analysis.md, database-analysis.md
```

**Depth control**:
```
"Quick scan yap"
→ Only P0 and P1

"Deep analysis yap"
→ All priorities (P0, P1, P2, P3)
```

---

## Mode 2: Analyze + Plan

### Use Case
- Sprint planning
- Roadmap creation
- Task breakdown for team
- Estimating effort and timeline

### How to Trigger

**Turkish Prompts**:
```markdown
"Projeyi analiz et ve aksiyon planı oluştur"
"Sprint planning yap"
"3 aylık roadmap hazırla"
"P0 sorunları için task breakdown yap"
"Plan oluÅŸtur ama kod yazma"
"Epic ve story'lere ayır"
```

### What Happens

```
1. Everything from Mode 1 (analysis)
2. AI creates ACTION_PLAN_TEMPLATE
3. AI creates TASK_BREAKDOWN
4. AI creates ROADMAP (if requested)
5. AI creates SPRINT_PLAN
6. NO code is written
7. NO files are changed
```

### Example Output Files

```
/outputs/
├── analysis-report-20250115.md      (from Mode 1)
├── action-plan-20250115.md          (NEW)
├── sprint-breakdown-20250115.md     (NEW)
├── task-breakdown-20250115.md       (NEW)
└── roadmap-Q1-2025.md              (NEW)
```

### Example: action-plan-20250115.md

```markdown
# Aksiyon Planı

**Proje**: MyAwesomeApp  
**Tarih**: 15 Ocak 2025  
**Genel Skor**: 7.2/10 → Hedef: 9.0/10

---

## Sprint 1 (Bu Hafta - 40 saat)
**Hedef**: P0 kritik sorunları çöz

| # | Sorun | Çözüm | Sorumlu | Süre | Durum |
|---|-------|-------|---------|------|-------|
| 1 | SQL Injection | Parameterized query | Ali | 2h | ⬜ |
| 2 | Exposed secrets | Rotate + .gitignore | Ayşe | 1h | ⬜ |
| 3 | Missing auth | [Authorize] ekle | Mehmet | 30m | ⬜ |

**Toplam**: 3.5 saat

---

## Sprint 2 (Gelecek Hafta - 40 saat)
**Hedef**: P1 yüksek öncelikli sorunlar

| # | Sorun | Çözüm | Sorumlu | Süre | Durum |
|---|-------|-------|---------|------|-------|
| 4 | N+1 query | Eager loading | Ali | 1h | ⬜ |
| 5 | Vulnerable deps | npm audit fix | Ayşe | 2h | ⬜ |
| 6 | Build yavaş | TypeScript incremental | Ahmet | 30m | ⬜ |

[... continues ...]
```

### Customization

**Time range**:
```
"Bu haftalık plan yap"
→ Sprint 1 only

"3 aylık roadmap"
→ Q1 breakdown

"Yıllık strateji"
→ 4 quarters
```

**Priority focus**:
```
"Sadece P0 için plan"
→ Critical only

"P0 ve P1 için aksiyon planı"
→ High priority focus

"Full backlog organization"
→ All priorities
```

---

## Mode 3: Full Flow (Semi-Autonomous)

### Use Case
- Automatically fix issues
- Rapid bug fixes
- Batch refactoring
- Technical debt cleanup sprint

### ⚠️ Important: Safety First!

Mode 3 writes code and changes files. **Always**:
1. Work on a separate branch (not main)
2. Have backups
3. Review at checkpoints
4. Have test coverage >50%

### How to Trigger

**Turkish Prompts**:
```markdown
"P0 sorunları düzelt"
"Security vulnerabilities'i otomatik çöz"
"Performans optimizasyonlarını uygula"
"Full flow çalıştır, ama checkpoint'lerde sor"
"Tüm SQL injection'ları fix et"
```

### What Happens

```
STEP 1: Analysis
├─ Load modules
├─ Analyze project
└─ Generate report

STEP 2: Planning
├─ Create action plan
├─ Identify auto-fixable issues
└─ Estimate effort

⚠️ CHECKPOINT #1: Plan Approval
├─ User sees: What will be fixed
├─ User decides: Continue/Stop/Edit
└─ Options: [Evet] [Hayır] [Planı Düzenle]

STEP 3: Implementation
├─ Backend Agent writes code
├─ Frontend Agent writes code
├─ Integration Agent writes code
└─ Architect Guardian coordinates

⚠️ CHECKPOINT #2: Code Review
├─ User sees: Diff of all changes
├─ User decides: Continue/Rollback/Review
└─ Options: [Diff Göster] [Devam Et] [Rollback]

STEP 4: Testing
├─ Run unit tests
├─ Run integration tests
├─ Run build
├─ Security scan
└─ Performance check

STEP 5: Commit
├─ Create commit message
├─ Stage files
└─ Push to branch

⚠️ CHECKPOINT #3: Commit Approval
├─ User sees: Test results, metrics
├─ User decides: Commit/Cancel
└─ Options: [Evet] [Hayır]

STEP 6: Final Report
└─ Execution log with all details
```

### Example: Complete Flow

```
YOU: "P0 sorunları düzelt"

AI:
═══════════════════════════════════════
📊 ADIM 1/6: Analiz Başladı
═══════════════════════════════════════

Modüller yüklendi:
├─ ✅ security-analysis.md
├─ ✅ database-analysis.md
└─ ✅ hidden-gems-deep-scan.md

Analiz tamamlandı (23s)

Bulgular:
├─ 🔴 P0: 3 sorun
│   ├─ SQL Injection (OrderService.cs)
│   ├─ Exposed secrets (.env)
│   └─ Missing authorization (AdminController)
├─ 🟡 P1: 5 sorun
└─ 🟢 P2: 8 sorun

───────────────────────────────────────

═══════════════════════════════════════
📋 ADIM 2/6: Planlama
═══════════════════════════════════════

Otomatik çözülebilir: 3/3 P0 sorunu

Task Breakdown:
1. SQL Injection fix (2h, auto)
2. Secrets cleanup (1h, auto)
3. Authorization add (30m, auto)

Toplam çaba: 3.5 saat
DeÄŸiÅŸecek dosyalar: 7 dosya

───────────────────────────────────────

🔍 CHECKPOINT #1: Plan Onayı
───────────────────────────────────────
3 P0 sorunu otomatik çözülecek
7 dosya deÄŸiÅŸtirilecek
Tahmini süre: 3.5 saat

Devam edilsin mi?
[Evet] [Hayır] [Planı Düzenle] [Sadece Göster]

YOU: "Evet"

═══════════════════════════════════════
💻 ADIM 3/6: Implementation
═══════════════════════════════════════

🔧 Task 1/3: SQL Injection Fix
   Agent: Backend Agent
   File: OrderService.cs
   ✅ Code written
   ✅ Test written
   ✅ Test passed

🔧 Task 2/3: Secrets Cleanup
   Agent: Backend Agent
   Files: .gitignore, .env.example
   ✅ Git history cleaned
   ✅ .gitignore updated

🔧 Task 3/3: Authorization
   Agent: Backend Agent
   File: AdminController.cs
   ✅ [Authorize] added to 3 endpoints
   ✅ Tests passed

Implementation tamamlandı (1m 34s)
├─ 7 dosya değiştirildi
├─ +234 satır eklendi
└─ -156 satır silindi

───────────────────────────────────────

🔍 CHECKPOINT #2: Kod İnceleme
───────────────────────────────────────
Kod değişikliklerini görmek ister misin?
[Diff Göster] [Devam Et] [Rollback] [Dosya Dosya]

YOU: "Devam Et"

═══════════════════════════════════════
🧪 ADIM 4/6: Testing
═══════════════════════════════════════

Unit Tests: 102/102 passed ✅
Build: Success (28s) ✅
Security Scan: Clean ✅
Performance: +67% improvement ✅

Testing tamamlandı (1m 4s)

───────────────────────────────────────

🔍 CHECKPOINT #3: Commit Onayı
───────────────────────────────────────
Tüm testler geçti!
Performans iyileÅŸti (+67%)
Security temiz

Commit edilsin mi?
[Evet] [Hayır] [Test Detaylarını Göster]

YOU: "Evet"

═══════════════════════════════════════
📝 ADIM 5/6: Git Commit
═══════════════════════════════════════

Branch: fix/security-p0-issues
Commit: abc123def456
Pushed: ✅

───────────────────────────────────────

═══════════════════════════════════════
📊 ADIM 6/6: Final Report
═══════════════════════════════════════

✅ BAŞARIYLA TAMAMLANDI

Çözülen Sorunlar:
├─ 🔴 P0: 3/3 (%100)
└─ Toplam süre: 3m 42s

Metrik İyileştirmeleri:
├─ Security: 6.5/10 → 9.2/10 (+41%)
├─ Build: 85s → 28s (-67%)
└─ Bundle: 847KB → 320KB (-62%)

OluÅŸturulan Dosyalar:
├─ /outputs/analysis-report.md
├─ /outputs/action-plan.md
├─ /outputs/execution-log.md
└─ /outputs/diff-abc123def.patch

Git Info:
├─ Branch: fix/security-p0-issues
├─ Commit: abc123def
└─ Rollback: git revert abc123def

Sonraki Adımlar:
1. Code review aç (#789)
2. Staging'de test et
3. Production'a deploy

═══════════════════════════════════════
```

### Safety Features

**Pre-Execution Checks**:
- ✅ Working directory clean?
- ✅ Test coverage >50%?
- ✅ Not on main branch?

**During Execution Limits**:
- Max 20 files changed
- Max 500 lines changed
- Breaking change detection

**Post-Execution Checks**:
- All tests must pass
- Build must succeed
- Security scan clean
- No performance regression

**Auto-Abort Triggers**:
- >30% test failures
- Build errors
- Git conflicts
- Disk space <10%

### Customization

**Selective auto-fix**:
```
"Sadece SQL injection'ı fix et, diğerlerine dokunma"
→ Scope limited

"Security sorunlarını otomatik çöz, ama performance için sor"
→ Selective checkpoints
```

**Checkpoint control**:
```
"Tüm checkpoint'leri skip et"
→ Full automatic (RISKY!)

"Her dosya deÄŸiÅŸikliÄŸinde sor"
→ Maximum control
```

**Dry-run mode**:
```
"Ne yapacağını göster ama değişiklik yapma"
→ Code generated but not applied
```

---

## Advanced Usage

### Trae IDE Agent Integration

If using Trae IDE with agents:

1. **Upload additional file**:
   ```
   AGENTIC_WORKFLOW.md
   ```

2. **Agent coordination**:
   ```
   Orchestrator
   ├─ Architect Guardian (plans & coordinates)
   ├─ Backend Agent (API/DB fixes)
   ├─ Frontend Agent (UI fixes)
   └─ Integration Agent (API integration fixes)
   ```

3. **Example prompt**:
   ```
   "P0 sorunları düzelt, agent'ları koordine et"
   ```

### Custom Configuration

Create `.ai-orchestrator.yml`:

```yaml
default_mode: "analyze_only"

checkpoints:
  after_analysis: true
  after_code_gen: true
  before_commit: true

auto_approve:
  - "sql_injection_fix"
  - "gitignore_update"
  - "eslint_autofix"

never_auto:
  - "database_migration"
  - "password_change"
  - "api_versioning"

safety:
  max_files_changed: 20
  max_lines_changed: 500
  require_tests: true
```

### Combining Modes

**Sequential execution**:
```
Step 1: "Projeyi analiz et"
→ Review report

Step 2: "P0 için aksiyon planı oluştur"
→ Review plan

Step 3: "Planı uygula"
→ Execute with checkpoints
```

---

## Troubleshooting

### "Mode detection failed"

**Problem**: AI doesn't understand which mode to use

**Solution**: Be explicit
```
❌ "Fix the issues"
✅ "P0 sorunları düzelt (Mode 3, full flow)"
```

---

### "Checkpoint skipped"

**Problem**: No human interaction at checkpoint

**Solution**: Check if you have:
```yaml
checkpoints:
  after_analysis: true  # Enable checkpoints
```

---

### "Auto-fix failed"

**Problem**: AI can't automatically fix an issue

**Reason**: Issue requires manual intervention (see AUTOMATION_RULES.md)

**Solution**: Review manual implementation guide:
```
/implementation-guides/[relevant-guide].md
```

---

### "Tests failed after fix"

**Problem**: Auto-fix broke existing tests

**Solution**: Automatic rollback triggered
```bash
# View rollback
git log -1

# Manual rollback if needed
git revert abc123def
```

---

### "Performance regression"

**Problem**: Changes made things slower

**Solution**: Review performance metrics
```
Before: Build 85s
After: Build 92s  # +8% slower = WARNING

Automatic rollback triggered
```

---

## Best Practices

### Mode Selection

```
📊 Need to see current state?
→ Mode 1: Analyze Only

📋 Planning a sprint?
→ Mode 2: Analyze + Plan

🚀 Want automated fixes?
→ Mode 3: Full Flow

🤔 Not sure?
→ Start with Mode 1, then Mode 2, then Mode 3
```

### Safety

```
✅ DO:
- Work on feature branch
- Have backups
- Review at checkpoints
- Test locally first

❌ DON'T:
- Skip checkpoints on main
- Auto-approve in production
- Ignore test failures
- Skip code review
```

### Efficiency

```
🔍 Single issue?
→ Mode 3 with specific scope

📦 Multiple issues?
→ Mode 2 (plan), then batch Mode 3

🏃 Need it fast?
→ Mode 3 with auto-approve (RISKY)

🐢 Need it safe?
→ Mode 2, manual implementation
```

---

## FAQ

**Q: Can I use Mode 3 on production?**  
A: Not recommended. Use on feature branch, test, then merge.

**Q: What if I disagree with a fix?**  
A: At Checkpoint #2, choose "Rollback" or "Edit".

**Q: Can I edit the plan in Mode 2?**  
A: Yes, edit action-plan.md manually, then proceed.

**Q: How do I rollback Mode 3 changes?**  
A: `git revert [commit-sha]` or use ROLLBACK_PROCEDURES.md

**Q: Can agents work in parallel?**  
A: Yes, with AGENTIC_WORKFLOW.md and Trae IDE.

**Q: What if analysis is wrong?**  
A: Provide feedback, AI will adjust. Or manually edit MANIFEST.yaml to change module selection.

---

## Quick Reference

| Task | Prompt | Mode | Time |
|------|--------|------|------|
| Daily status | "Projeyi analiz et" | 1 | 30s |
| Sprint planning | "Sprint planı oluştur" | 2 | 1m |
| Quick fix | "P0 düzelt" | 3 | 3-5m |
| Audit report | "Security audit" | 1 | 30s |
| Roadmap | "3 aylık roadmap" | 2 | 1m |
| Batch fixes | "Tüm P0 ve P1 düzelt" | 3 | 10-15m |

---

For more examples, see `TURKISH_PROMPTS.md`.  
For safety details, see `SAFETY_GATES.md`.  
For agent coordination, see `AGENTIC_WORKFLOW.md`.
