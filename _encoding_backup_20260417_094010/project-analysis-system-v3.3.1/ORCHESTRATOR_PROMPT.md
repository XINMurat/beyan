# AI Orchestrator - ModÃƒÂ¼ler Autonomous System

**Versiyon**: 3.3  
**Tarih**: AralÃ„Â±k 2024  
**Seviye**: Level 3 (Semi-Autonomous)

---

## Ã°Å¸Å½Â¯ ÃƒÅ“ÃƒÂ§ Ãƒâ€¡alÃ„Â±Ã…Å¸ma Modu

Bu sistem **3 farklÃ„Â± modda** ÃƒÂ§alÃ„Â±Ã…Å¸abilir:

### Mode 1: Ã°Å¸â€Â Analyze Only
```
Sadece analiz yapar, hiÃƒÂ§bir deÃ„Å¸iÃ…Å¸iklik yapmaz.
Use case: Mevcut durumu anlamak, rapor almak
```

### Mode 2: Ã°Å¸â€œâ€¹ Analyze + Plan
```
Analiz yapar + Aksiyon planÃ„Â± oluÃ…Å¸turur (kod yazmaz)
Use case: Sprint planning, roadmap hazÃ„Â±rlama
```

### Mode 3: Ã°Å¸Å¡â‚¬ Full Flow (Semi-Autonomous)
```
Analiz Ã¢â€ â€™ Plan Ã¢â€ â€™ Kod Yaz Ã¢â€ â€™ Test Ã¢â€ â€™ Commit
Human checkpoints: 3-5 onay noktasÃ„Â±
Use case: SorunlarÃ„Â± otomatik ÃƒÂ§ÃƒÂ¶z (gÃƒÂ¼venli)
```

---

## Ã°Å¸â€œâ€“ Mode SeÃƒÂ§imi (Prompt Ãƒâ€“rnekleri)

### Mode 1: Analyze Only

**TÃƒÂ¼rkÃƒÂ§e Promptlar**:
```markdown
"Projeyi analiz et"
"Security audit yap"
"Performans sorunlarÃ„Â±nÃ„Â± tespit et"
"WCAG compliance kontrol et"
"Sadece rapor ver, hiÃƒÂ§bir deÃ„Å¸iÃ…Å¸iklik yapma"
```

**AI DavranÃ„Â±Ã…Å¸Ã„Â±**:
- Ã¢Å“â€¦ Analiz yapar
- Ã¢Å“â€¦ TÃƒÂ¼rkÃƒÂ§e rapor verir
- Ã¢Å“â€¦ Ãƒâ€“neri listesi verir
- Ã¢ÂÅ’ Kod yazmaz
- Ã¢ÂÅ’ Dosya deÃ„Å¸iÃ…Å¸tirmez
- Ã¢ÂÅ’ Plan oluÃ…Å¸turmaz

---

### Mode 2: Analyze + Plan

**TÃƒÂ¼rkÃƒÂ§e Promptlar**:
```markdown
"Projeyi analiz et ve aksiyon planÃ„Â± oluÃ…Å¸tur"
"Sprint planning yap"
"3 aylÃ„Â±k roadmap hazÃ„Â±rla"
"P0 sorunlarÃ„Â± iÃƒÂ§in task breakdown yap"
"Plan oluÃ…Å¸tur ama kod yazma"
```

**AI DavranÃ„Â±Ã…Å¸Ã„Â±**:
- Ã¢Å“â€¦ Analiz yapar
- Ã¢Å“â€¦ TÃƒÂ¼rkÃƒÂ§e rapor verir
- Ã¢Å“â€¦ ACTION_PLAN_TEMPLATE doldurur
- Ã¢Å“â€¦ Sprint planÃ„Â± oluÃ…Å¸turur
- Ã¢Å“â€¦ Epic Ã¢â€ â€™ Story Ã¢â€ â€™ Task breakdown
- Ã¢ÂÅ’ Kod yazmaz
- Ã¢ÂÅ’ Dosya deÃ„Å¸iÃ…Å¸tirmez

**Ãƒâ€¡Ã„Â±ktÃ„Â± DosyalarÃ„Â±**:
```
/outputs/
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ analysis-report-20250115.md
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ action-plan-20250115.md
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ sprint-breakdown-20250115.md
Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ roadmap-Q1-2025.md
```

---

### Mode 3: Full Flow (Semi-Autonomous)

**TÃƒÂ¼rkÃƒÂ§e Promptlar**:
```markdown
"Projeyi analiz et ve P0 sorunlarÃ„Â± dÃƒÂ¼zelt"
"Security sorunlarÃ„Â±nÃ„Â± otomatik ÃƒÂ§ÃƒÂ¶z"
"Performans optimizasyonlarÃ„Â±nÃ„Â± uygula"
"TÃƒÂ¼m flow'u ÃƒÂ§alÃ„Â±Ã…Å¸tÃ„Â±r, checkpoint'lerde sor"
"Full autonomous mode, ama onayÃ„Â±mÃ„Â± al"
```

**AI DavranÃ„Â±Ã…Å¸Ã„Â±**:
- Ã¢Å“â€¦ Analiz yapar
- Ã¢Å“â€¦ Plan oluÃ…Å¸turur
- Ã¢Å“â€¦ Kod yazar
- Ã¢Å“â€¦ Dosya deÃ„Å¸iÃ…Å¸tirir
- Ã¢Å“â€¦ Test ÃƒÂ§alÃ„Â±Ã…Å¸tÃ„Â±rÃ„Â±r
- Ã¢Å“â€¦ Git commit yapar
- Ã¢Å¡Â Ã¯Â¸Â 3 checkpoint (Analysis, Code Review, Commit)'te onay ister

**Human Checkpoints**:
1. Ã°Å¸â€Â **After Analysis**: "Plan onaylÃ„Â±yor musun?"
2. Ã°Å¸â€Â **After Code Gen**: "Kod deÃ„Å¸iÃ…Å¸ikliklerini incelemek ister misin?"
3. Ã°Å¸â€Â **Before Commit**: "Commit edilsin mi?"

---

## Ã°Å¸Å½Â¬ Mode 3: Full Flow (DetaylÃ„Â± AkÃ„Â±Ã…Å¸)

### AdÃ„Â±m 1: Analysis Phase

```markdown
Ã°Å¸â€Â **ADIM 1/6: Analiz BaÃ…Å¸lÃ„Â±yor...**

ModÃƒÂ¼ller yÃƒÂ¼klendi:
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ security-analysis.md
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ performance-analysis.md
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ database-analysis.md
Ã¢â€â€Ã¢â€â‚¬ Ã¢Å“â€¦ hidden-gems-deep-scan.md

Analiz devam ediyor...
[Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“â€˜Ã¢â€“â€˜] 85%

Ã¢Å“â€¦ **Analiz TamamlandÃ„Â±**

Bulgular:
Ã¢â€Å“Ã¢â€â‚¬ Ã°Å¸â€Â´ P0 (Kritik): 3 sorun
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬ SQL Injection (OrderService.cs:45)
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬ Exposed secrets (.env in Git)
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬ Missing authorization (AdminController)
Ã¢â€â€š
Ã¢â€Å“Ã¢â€â‚¬ Ã°Å¸Å¸Â¡ P1 (YÃƒÂ¼ksek): 5 sorun
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬ N+1 Query (Orders endpoint)
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬ Vulnerable dependencies (12 packages)
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬ CORS misconfiguration
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬ Weak password hashing (SHA256)
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬ Build time ÃƒÂ§ok uzun (85s)
Ã¢â€â€š
Ã¢â€â€Ã¢â€â‚¬ Ã°Å¸Å¸Â¢ P2 (Orta): 8 sorun
    Ã¢â€â€Ã¢â€â‚¬ [liste...]

Ã°Å¸â€œâ€ž DetaylÃ„Â± rapor: /outputs/analysis-report-20250115.md
```

---

### AdÃ„Â±m 2: Planning Phase

```markdown
Ã°Å¸â€œâ€¹ **ADIM 2/6: Planlama BaÃ…Å¸lÃ„Â±yor...**

Otomatik ÃƒÂ§ÃƒÂ¶zÃƒÂ¼lebilir sorunlar:
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ SQL Injection (auto-fix: parameterized query)
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ Exposed secrets (auto-fix: .gitignore + rotate)
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ Build optimization (auto-fix: tsconfig)
Ã¢â€â€Ã¢â€â‚¬ Ã¢Å¡Â Ã¯Â¸Â Password hashing (requires migration - manual)

Sprint PlanÃ„Â± OluÃ…Å¸turuldu:
Ã¢â€Å“Ã¢â€â‚¬ Sprint 1 (Bu Hafta): P0 sorunlarÃ„Â±
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬ Task 1: SQL Injection (2h, auto)
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬ Task 2: Secrets cleanup (1h, auto)
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬ Task 3: Authorization (30m, auto)
Ã¢â€â€š
Ã¢â€â€Ã¢â€â‚¬ Sprint 2 (Gelecek Hafta): P1 sorunlarÃ„Â±
    Ã¢â€â€Ã¢â€â‚¬ [liste...]

Ã°Å¸â€œâ€ž Aksiyon planÃ„Â±: /outputs/action-plan-20250115.md

Ã°Å¸â€Â **CHECKPOINT #1: Plan OnayÃ„Â±**
Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
3 P0 sorunu otomatik ÃƒÂ§ÃƒÂ¶zÃƒÂ¼lecek.
Tahmini sÃƒÂ¼re: 3.5 saat
DeÃ„Å¸iÃ…Å¸iklik yapÃ„Â±lacak dosyalar: 7 dosya

Devam edilsin mi?
[Evet] [HayÃ„Â±r] [PlanÃ„Â± DÃƒÂ¼zenle] [Sadece GÃƒÂ¶ster]
```

**KullanÃ„Â±cÃ„Â± yanÃ„Â±tÃ„Â± bekleniyor...**

---

### AdÃ„Â±m 3: Implementation Phase (Onaydan sonra)

```markdown
Ã°Å¸â€™Â» **ADIM 3/6: Implementation BaÃ…Å¸lÃ„Â±yor...**

Ã°Å¸â€Â§ Task 1/3: SQL Injection DÃƒÂ¼zeltme
Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
Dosya: src/services/OrderService.cs
SatÃ„Â±r: 45

Ã¢ÂÅ’ Mevcut Kod:
```csharp
var sql = $"SELECT * FROM Orders WHERE CustomerId = {customerId}";
var orders = _context.Database.ExecuteSqlRaw(sql);
```

Ã¢Å“â€¦ DÃƒÂ¼zeltilmiÃ…Å¸ Kod:
```csharp
var orders = _context.Orders
    .Where(o => o.CustomerId == customerId)
    .ToList();
```

Ã°Å¸â€œÂ Test yazÃ„Â±ldÃ„Â±: OrderService.Tests.cs
Ã¢Å“â€¦ Test geÃƒÂ§ti: SQL injection attempt blocked

Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

Ã°Å¸â€Â§ Task 2/3: Secrets Cleanup
Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
Git history taranÃ„Â±yor...
Ã¢â€Å“Ã¢â€â‚¬ Bulundu: .env (3 commit'te)
Ã¢â€Å“Ã¢â€â‚¬ Siliniyor: git filter-branch
Ã¢â€Å“Ã¢â€â‚¬ OluÃ…Å¸turuluyor: .env.example
Ã¢â€â€Ã¢â€â‚¬ GÃƒÂ¼ncelleniyor: .gitignore

Ã¢Å“â€¦ Secrets cleaned from Git history
Ã¢Å¡Â Ã¯Â¸Â NOT: Secrets rotate edilmeli (manuel)

Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

Ã°Å¸â€Â§ Task 3/3: Authorization Ekleme
Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
Dosya: src/controllers/AdminController.cs
Eksik endpoint: DeleteUser, BanUser, ResetPassword

Ã¢Å“â€¦ [Authorize(Roles = "Admin")] eklendi (3 endpoint)
Ã¢Å“â€¦ Logging eklendi
Ã°Å¸â€œÂ Test yazÃ„Â±ldÃ„Â±
Ã¢Å“â€¦ Test geÃƒÂ§ti

Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

Ã°Å¸â€œÅ  **Implementation Ãƒâ€“zeti**
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ 7 dosya deÃ„Å¸iÃ…Å¸tirildi
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ +234 satÃ„Â±r eklendi
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ -156 satÃ„Â±r silindi
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ 9 test yazÃ„Â±ldÃ„Â± (9/9 geÃƒÂ§ti)
Ã¢â€â€Ã¢â€â‚¬ Ã¢Å¡Â Ã¯Â¸Â 1 manuel adÃ„Â±m: Secrets rotation

Ã°Å¸â€Â **CHECKPOINT #2: Kod Ã„Â°nceleme**
Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
Kod deÃ„Å¸iÃ…Å¸ikliklerini gÃƒÂ¶rmek ister misin?
[Diff GÃƒÂ¶ster] [Devam Et] [Rollback] [Dosya Dosya Ã„Â°ncele]
```

---

### AdÃ„Â±m 4: Testing Phase

```markdown
Ã°Å¸Â§Âª **ADIM 4/6: Test BaÃ…Å¸lÃ„Â±yor...**

Unit Tests:
[Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†] 100%
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ OrderService.Tests: 12/12 passed
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ AdminController.Tests: 8/8 passed
Ã¢â€â€Ã¢â€â‚¬ Ã¢Å“â€¦ AuthService.Tests: 15/15 passed

Integration Tests:
[Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†] 100%
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ API Tests: 47/47 passed
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ Database Tests: 12/12 passed
Ã¢â€â€Ã¢â€â‚¬ Ã¢Å“â€¦ Security Tests: 8/8 passed

Build:
[Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†Ã¢â€“Ë†] 100%
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ TypeScript compile: OK (28s)
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ Bundle size: 320 KB (was 847 KB)
Ã¢â€â€Ã¢â€â‚¬ Ã¢Å“â€¦ No errors, 0 warnings

Security Scan:
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ npm audit: 0 vulnerabilities
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ Semgrep: No issues
Ã¢â€â€Ã¢â€â‚¬ Ã¢Å“â€¦ Trivy: Clean

Performance:
Ã¢â€Å“Ã¢â€â‚¬ Build time: 85s Ã¢â€ â€™ 28s Ã¢Å“â€¦ (67% faster)
Ã¢â€Å“Ã¢â€â‚¬ API response: 450ms Ã¢â€ â€™ 95ms Ã¢Å“â€¦
Ã¢â€â€Ã¢â€â‚¬ Bundle size: 847KB Ã¢â€ â€™ 320KB Ã¢Å“â€¦

Ã°Å¸â€œÅ  **Test Ãƒâ€“zeti**
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ 102/102 tests passed
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ Build successful
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ Security clean
Ã¢â€â€Ã¢â€â‚¬ Ã¢Å“â€¦ Performance improved

Ã°Å¸â€Â **CHECKPOINT #3: Test SonuÃƒÂ§larÃ„Â±**
Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
TÃƒÂ¼m testler geÃƒÂ§ti!
Performans %67 iyileÃ…Å¸ti.
Security temiz.

Commit'e hazÃ„Â±r. Devam edilsin mi?
[Evet] [HayÃ„Â±r] [Test DetaylarÃ„Â±nÃ„Â± GÃƒÂ¶ster]
```

---

### AdÃ„Â±m 5: Commit Phase

```markdown
Ã°Å¸â€œÂ **ADIM 5/6: Git Commit**

Branch oluÃ…Å¸turuluyor...
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ Branch: fix/security-p0-issues
Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ 7 dosya staged
Ã¢â€â€Ã¢â€â‚¬ Ã¢Å“â€¦ Ready to commit

Commit Message:
Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
fix: resolve P0 security vulnerabilities

- Fix SQL injection in OrderService (parameterized queries)
- Remove exposed secrets from Git history
- Add authorization to admin endpoints
- Add comprehensive test coverage

Security improvements:
- Security score: 6.5/10 Ã¢â€ â€™ 9.2/10
- Zero critical vulnerabilities
- Test coverage: 78% Ã¢â€ â€™ 82%

Performance improvements:
- Build time: 85s Ã¢â€ â€™ 28s (-67%)
- Bundle size: 847KB Ã¢â€ â€™ 320KB (-62%)
- API response: 450ms Ã¢â€ â€™ 95ms (-79%)

Breaking changes: None
Manual steps required:
- Rotate secrets (DB password, API keys)

Refs: #123, #456
Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

Ã¢Å“â€¦ Committed: abc123def
Ã¢Å“â€¦ Pushed to origin/fix/security-p0-issues

PR oluÃ…Å¸turulsun mu?
[Evet] [HayÃ„Â±r] [PR Template GÃƒÂ¶ster]
```

---

### AdÃ„Â±m 6: Final Report

```markdown
Ã°Å¸â€œÅ  **ADIM 6/6: Final Report**

Ã¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢Â
Ã¢Å“â€¦ BAÃ…Å¾ARIYLA TAMAMLANDI
Ã¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢ÂÃ¢â€¢Â

Ã¢ÂÂ±Ã¯Â¸Â Toplam SÃƒÂ¼re: 3 dakika 42 saniye

Ã°Å¸Å½Â¯ Ãƒâ€¡ÃƒÂ¶zÃƒÂ¼len Sorunlar:
Ã¢â€Å“Ã¢â€â‚¬ Ã°Å¸â€Â´ P0: 3/3 (%100) Ã¢Å“â€¦
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ SQL Injection
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ Exposed Secrets
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬ Ã¢Å“â€¦ Missing Authorization
Ã¢â€â€š
Ã¢â€Å“Ã¢â€â‚¬ Ã°Å¸Å¸Â¡ P1: 2/5 (%40)
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ Build Optimization
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬ Ã¢Å“â€¦ Bundle Size
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬ Ã¢ÂÂ³ 3 sorun backlog'a eklendi
Ã¢â€â€š
Ã¢â€â€Ã¢â€â‚¬ Ã°Å¸Å¸Â¢ P2: 0/8 (kapsam dÃ„Â±Ã…Å¸Ã„Â±)

Ã°Å¸â€œË† Metrik Ã„Â°yileÃ…Å¸tirmeleri:
Ã¢â€Å“Ã¢â€â‚¬ Security Score: 6.5/10 Ã¢â€ â€™ 9.2/10 (+41%)
Ã¢â€Å“Ã¢â€â‚¬ Build Time: 85s Ã¢â€ â€™ 28s (-67%)
Ã¢â€Å“Ã¢â€â‚¬ Bundle Size: 847KB Ã¢â€ â€™ 320KB (-62%)
Ã¢â€Å“Ã¢â€â‚¬ API Response: 450ms Ã¢â€ â€™ 95ms (-79%)
Ã¢â€â€Ã¢â€â‚¬ Test Coverage: 78% Ã¢â€ â€™ 82% (+4%)

Ã°Å¸â€œÂ YapÃ„Â±lan DeÃ„Å¸iÃ…Å¸iklikler:
Ã¢â€Å“Ã¢â€â‚¬ 7 dosya deÃ„Å¸iÃ…Å¸tirildi
Ã¢â€Å“Ã¢â€â‚¬ +234 satÃ„Â±r eklendi
Ã¢â€Å“Ã¢â€â‚¬ -156 satÃ„Â±r silindi
Ã¢â€Å“Ã¢â€â‚¬ 9 yeni test eklendi
Ã¢â€â€Ã¢â€â‚¬ 1 branch oluÃ…Å¸turuldu

Ã°Å¸â€â€” Git Info:
Ã¢â€Å“Ã¢â€â‚¬ Branch: fix/security-p0-issues
Ã¢â€Å“Ã¢â€â‚¬ Commit: abc123def
Ã¢â€Å“Ã¢â€â‚¬ PR: #789 (draft)
Ã¢â€â€Ã¢â€â‚¬ Rollback: git revert abc123def

Ã¢Å¡Â Ã¯Â¸Â Manuel AdÃ„Â±mlar Gerekli:
1. Secrets rotation (DB password, API keys)
   Guide: /IMPLEMENTATION_GUIDES/security-fixes.md
   
2. Code review isteÃ„Å¸i
   Reviewer: @ali, @ayse
   
3. Staging'de test
   Deploy: npm run deploy:staging

Ã°Å¸â€œÂ OluÃ…Å¸turulan Dosyalar:
Ã¢â€Å“Ã¢â€â‚¬ /outputs/analysis-report-20250115.md
Ã¢â€Å“Ã¢â€â‚¬ /outputs/action-plan-20250115.md
Ã¢â€Å“Ã¢â€â‚¬ /outputs/execution-log-20250115.md
Ã¢â€Å“Ã¢â€â‚¬ /outputs/diff-abc123def.patch
Ã¢â€â€Ã¢â€â‚¬ /outputs/test-results-20250115.json

Ã°Å¸Å½Â¯ Sonraki AdÃ„Â±mlar:
1. Ã¢Å“â€¦ Code review (#789)
2. Ã¢ÂÂ³ P1 kalan sorunlar (N+1, password hashing)
3. Ã°Å¸â€œâ€¦ Sprint 2 planning (P2 backlog)

Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬
Ã°Å¸Å½â€° Proje saÃ„Å¸lÃ„Â±Ã„Å¸Ã„Â±: 7.2/10 Ã¢â€ â€™ 8.9/10
Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬Ã¢â€â‚¬

Bir sonraki analiz: 2 hafta sonra (30.01.2025)
```

---

## Ã°Å¸â€ºÂ¡Ã¯Â¸Â Safety Gates (Checkpoint DetaylarÃ„Â±)

### Checkpoint #1: Plan OnayÃ„Â±
**Ne zaman**: Analysis sonrasÃ„Â±  
**Neden**: KullanÃ„Â±cÃ„Â± hangi sorunlarÃ„Â±n ÃƒÂ§ÃƒÂ¶zÃƒÂ¼leceÃ„Å¸ini bilmeli  
**SeÃƒÂ§enekler**:
- Ã¢Å“â€¦ Evet Ã¢â€ â€™ Devam
- Ã¢ÂÅ’ HayÃ„Â±r Ã¢â€ â€™ Dur
- Ã°Å¸â€Â§ PlanÃ„Â± DÃƒÂ¼zenle Ã¢â€ â€™ Interactive edit
- Ã°Å¸â€˜ÂÃ¯Â¸Â Sadece GÃƒÂ¶ster Ã¢â€ â€™ Kod yazma, sadece planÃ„Â± geniÃ…Å¸let

### Checkpoint #2: Kod Ã„Â°nceleme
**Ne zaman**: Implementation sonrasÃ„Â±  
**Neden**: KullanÃ„Â±cÃ„Â± kod deÃ„Å¸iÃ…Å¸ikliklerini gÃƒÂ¶rmeli  
**SeÃƒÂ§enekler**:
- Ã°Å¸â€œâ€ž Diff GÃƒÂ¶ster Ã¢â€ â€™ TÃƒÂ¼m deÃ„Å¸iÃ…Å¸iklikleri gÃƒÂ¶ster
- Ã¢Å“â€¦ Devam Et Ã¢â€ â€™ Test'e geÃƒÂ§
- Ã¢ÂÂª Rollback Ã¢â€ â€™ TÃƒÂ¼m deÃ„Å¸iÃ…Å¸iklikleri geri al
- Ã°Å¸â€œÂ Dosya Dosya Ã„Â°ncele Ã¢â€ â€™ Her dosyayÃ„Â± ayrÃ„Â± gÃƒÂ¶ster

### Checkpoint #3: Commit OnayÃ„Â±
**Ne zaman**: Test sonrasÃ„Â±  
**Neden**: Git'e commit ÃƒÂ¶nemli bir adÃ„Â±m  
**SeÃƒÂ§enekler**:
- Ã¢Å“â€¦ Evet Ã¢â€ â€™ Commit + Push
- Ã¢ÂÅ’ HayÃ„Â±r Ã¢â€ â€™ Commit'siz bÃ„Â±rak
- Ã°Å¸â€œÅ  Test DetaylarÃ„Â± Ã¢â€ â€™ Test log'larÃ„Â±nÃ„Â± gÃƒÂ¶ster

---

## Ã°Å¸Å½Å¡Ã¯Â¸Â Mode Override (Esnek Kontrol)

Prompt'ta ÃƒÂ¶zel direktifler verebilirsin:

```markdown
# Checkpoint'leri devre dÃ„Â±Ã…Å¸Ã„Â± bÃ„Â±rak
"P0 sorunlarÃ„Â± dÃƒÂ¼zelt, tÃƒÂ¼m checkpoint'leri skip et"
Ã¢â€ â€™ HiÃƒÂ§ sormadan tÃƒÂ¼m flow'u ÃƒÂ§alÃ„Â±Ã…Å¸tÃ„Â±rÃ„Â±r (RÃ„Â°SKLÃ„Â°!)

# Sadece belirli dosyalarda ÃƒÂ§alÃ„Â±Ã…Å¸
"Sadece OrderService.cs'i dÃƒÂ¼zelt, diÃ„Å¸erlerine dokunma"
Ã¢â€ â€™ Scope sÃ„Â±nÃ„Â±rlÃ„Â±

# Dry-run mode
"Ne yapacaÃ„Å¸Ã„Â±nÃ„Â± gÃƒÂ¶ster ama deÃ„Å¸iÃ…Å¸iklik yapma"
Ã¢â€ â€™ Kod yazÃ„Â±lÃ„Â±r ama dosyalar deÃ„Å¸iÃ…Å¸tirilmez

# Auto-approve certain types
"Security fix'leri otomatik onayla, ama performance iÃƒÂ§in sor"
Ã¢â€ â€™ Selective checkpoints

# Test-only mode
"Kod yaz ve test et, ama commit etme"
Ã¢â€ â€™ Commit'i manuel yaparsÃ„Â±n
```

---

## Ã°Å¸â€œÅ  Execution Log (Otomatik Kaydedilen)

Her full flow ÃƒÂ§alÃ„Â±Ã…Å¸tÃ„Â±rmasÃ„Â±nda otomatik log:

```markdown
# Execution Log - 15.01.2025 14:30:22

## Metadata
- Mode: Full Flow (Level 3)
- Start: 14:30:22
- End: 14:34:04
- Duration: 3m 42s
- User: dusunceli
- Project: my-project

## Timeline
14:30:22 - Analysis started
14:30:45 - Analysis complete (23s)
14:30:46 - Planning started
14:31:12 - Planning complete (26s)
14:31:12 - CHECKPOINT #1: Approved by user
14:31:13 - Implementation started
14:32:47 - Implementation complete (1m 34s)
14:32:47 - CHECKPOINT #2: Approved (Diff shown)
14:32:48 - Testing started
14:33:52 - Testing complete (1m 4s)
14:33:52 - CHECKPOINT #3: Approved
14:33:53 - Commit started
14:34:04 - Commit complete (11s)

## Results
- Issues resolved: 3/3 P0, 2/5 P1
- Files changed: 7
- Tests written: 9
- Tests passed: 102/102
- Commits: 1 (abc123def)
- Branch: fix/security-p0-issues

## User Interactions
1. [14:31:12] Checkpoint #1: Approved
2. [14:32:47] Checkpoint #2: Approved (viewed diff)
3. [14:33:52] Checkpoint #3: Approved

## Errors: None
## Warnings: 1 (manual step: secrets rotation)
```

---

## Ã°Å¸â€â€ž Rollback KomutlarÃ„Â±

Her zaman rollback mÃƒÂ¼mkÃƒÂ¼n:

```bash
# Son execution'Ã„Â± tamamen geri al
git revert abc123def

# Sadece belirli dosyayÃ„Â± geri al
git checkout HEAD~1 -- src/services/OrderService.cs

# Full rollback (branch'i sil)
git branch -D fix/security-p0-issues
```

---

## Ã°Å¸â€œÅ¡ Dosya YapÃ„Â±sÃ„Â±

```
/outputs/
Ã¢â€Å“Ã¢â€â‚¬ analysis-report-20250115.md        # Mode 1, 2, 3
Ã¢â€Å“Ã¢â€â‚¬ action-plan-20250115.md            # Mode 2, 3
Ã¢â€Å“Ã¢â€â‚¬ execution-log-20250115.md          # Mode 3 only
Ã¢â€Å“Ã¢â€â‚¬ diff-abc123def.patch               # Mode 3 only
Ã¢â€â€Ã¢â€â‚¬ test-results-20250115.json         # Mode 3 only
```

---

## Ã¢Å¡â„¢Ã¯Â¸Â KonfigÃƒÂ¼rasyon

```yaml
# .ai-orchestrator.yml (optional)
default_mode: "analyze_only"  # veya "analyze_plan" veya "full_flow"

checkpoints:
  after_analysis: true
  after_code_gen: true
  before_commit: true
  
auto_approve:
  - "sql_injection_fix"
  - "gitignore_update"
  - "typescript_incremental"
  
never_auto:
  - "database_migration"
  - "password_change"
  - "production_config"

safety:
  max_files_changed: 20
  require_tests: true
  require_backup: true
```

---

**Mode seÃƒÂ§imi kullanÃ„Â±cÃ„Â±ya kalmÃ„Â±Ã…Å¸. Her mode baÃ„Å¸Ã„Â±msÃ„Â±z ÃƒÂ§alÃ„Â±Ã…Å¸abilir!** Ã¢Å“â€¦
