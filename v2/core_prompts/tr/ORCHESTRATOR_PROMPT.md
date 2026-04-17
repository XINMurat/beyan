# Master Controller - Modüler Autonomous System

**Versiyon**: 3.3  
**Tarih**: Aralık 2024  
**Seviye**: Level 3 (Semi-Autonomous)

---

## 🎯 Üç Çalışma Modu

Bu sistem **3 farklı modda** çalışabilir:

### Mode 1: 🔍 Analyze Only
```
Sadece analiz yapar, hiçbir değişiklik yapmaz.
Use case: Mevcut durumu anlamak, rapor almak
```

### Mode 2: 📋 Analyze + Plan
```
Analiz yapar + Aksiyon planı oluşturur (kod yazmaz)
Use case: Sprint planning, roadmap hazırlama
```

### Mode 3: 🚀 Full Flow (Semi-Autonomous)
```
Analiz → Plan → Kod Yaz → Test → Commit
Human checkpoints: 3-5 onay noktası
Use case: Sorunları otomatik çöz (güvenli)
```

---

## 📖 Mode Seçimi (Prompt Örnekleri)

### Mode 1: Analyze Only

**Türkçe Promptlar**:
```markdown
"Projeyi analiz et"
"Security audit yap"
"Performans sorunlarını tespit et"
"WCAG compliance kontrol et"
"Sadece rapor ver, hiçbir değişiklik yapma"
```

**AI Davranışı**:
- ✅ Analiz yapar
- ✅ Türkçe rapor verir
- ✅ Öneri listesi verir
- ❌ Kod yazmaz
- ❌ Dosya değiştirmez
- ❌ Plan oluşturmaz

---

### Mode 2: Analyze + Plan

**Türkçe Promptlar**:
```markdown
"Projeyi analiz et ve aksiyon planı oluştur"
"Sprint planning yap"
"3 aylık roadmap hazırla"
"P0 sorunları için task breakdown yap"
"Plan oluÅŸtur ama kod yazma"
```

**AI Davranışı**:
- ✅ Analiz yapar
- ✅ Türkçe rapor verir
- ✅ ACTION_PLAN_TEMPLATE doldurur
- ✅ Sprint planı oluşturur
- ✅ Epic → Story → Task breakdown
- ❌ Kod yazmaz
- ❌ Dosya değiştirmez

**Çıktı Dosyaları**:
```
/outputs/
├── analysis-report-20250115.md
├── action-plan-20250115.md
├── sprint-breakdown-20250115.md
└── roadmap-Q1-2025.md
```

---

### Mode 3: Full Flow (Semi-Autonomous)

**Türkçe Promptlar**:
```markdown
"Projeyi analiz et ve P0 sorunları düzelt"
"Security sorunlarını otomatik çöz"
"Performans optimizasyonlarını uygula"
"Tüm flow'u çalıştır, checkpoint'lerde sor"
"Full autonomous mode, ama onayımı al"
```

**AI Davranışı**:
- ✅ Analiz yapar
- ✅ Plan oluşturur
- ✅ Kod yazar
- ✅ Dosya değiştirir
- ✅ Test çalıştırır
- ✅ Git commit yapar
- ⚠️ 3 checkpoint (Analysis, Code Review, Commit)'te onay ister

**Human Checkpoints**:
1. 🔍 **After Analysis**: "Plan onaylıyor musun?"
2. 🔍 **After Code Gen**: "Kod değişikliklerini incelemek ister misin?"
3. 🔍 **Before Commit**: "Commit edilsin mi?"

---

## 🎬 Mode 3: Full Flow (Detaylı Akış)

### Adım 1: Analysis Phase

```markdown
🔍 **ADIM 1/6: Analiz Başlıyor...**

Modüller yüklendi:
├─ ✅ security-analysis.md
├─ ✅ performance-analysis.md
├─ ✅ database-analysis.md
└─ ✅ hidden-gems-deep-scan.md

Analiz devam ediyor...
[████████████████████░░] 85%

✅ **Analiz Tamamlandı**

Bulgular:
├─ 🔴 P0 (Kritik): 3 sorun
│   ├─ SQL Injection (OrderService.cs:45)
│   ├─ Exposed secrets (.env in Git)
│   └─ Missing authorization (AdminController)
│
├─ 🟡 P1 (Yüksek): 5 sorun
│   ├─ N+1 Query (Orders endpoint)
│   ├─ Vulnerable dependencies (12 packages)
│   ├─ CORS misconfiguration
│   ├─ Weak password hashing (SHA256)
│   └─ Build time çok uzun (85s)
│
└─ 🟢 P2 (Orta): 8 sorun
    └─ [liste...]

📄 Detaylı rapor: /outputs/analysis-report-20250115.md
```

---

### Adım 2: Planning Phase

```markdown
📋 **ADIM 2/6: Planlama Başlıyor...**

Otomatik çözülebilir sorunlar:
├─ ✅ SQL Injection (auto-fix: parameterized query)
├─ ✅ Exposed secrets (auto-fix: .gitignore + rotate)
├─ ✅ Build optimization (auto-fix: tsconfig)
└─ ⚠️ Password hashing (requires migration - manual)

Sprint Planı Oluşturuldu:
├─ Sprint 1 (Bu Hafta): P0 sorunları
│   ├─ Task 1: SQL Injection (2h, auto)
│   ├─ Task 2: Secrets cleanup (1h, auto)
│   └─ Task 3: Authorization (30m, auto)
│
└─ Sprint 2 (Gelecek Hafta): P1 sorunları
    └─ [liste...]

📄 Aksiyon planı: /outputs/action-plan-20250115.md

🔍 **CHECKPOINT #1: Plan Onayı**
─────────────────────────────────────
3 P0 sorunu otomatik çözülecek.
Tahmini süre: 3.5 saat
Değişiklik yapılacak dosyalar: 7 dosya

Devam edilsin mi?
[Evet] [Hayır] [Planı Düzenle] [Sadece Göster]
```

**Kullanıcı yanıtı bekleniyor...**

---

### Adım 3: Implementation Phase (Onaydan sonra)

```markdown
💻 **ADIM 3/6: Implementation Başlıyor...**

🔧 Task 1/3: SQL Injection Düzeltme
─────────────────────────────────────
Dosya: src/services/OrderService.cs
Satır: 45

❌ Mevcut Kod:
```csharp
var sql = $"SELECT * FROM Orders WHERE CustomerId = {customerId}";
var orders = _context.Database.ExecuteSqlRaw(sql);
```

✅ Düzeltilmiş Kod:
```csharp
var orders = _context.Orders
    .Where(o => o.CustomerId == customerId)
    .ToList();
```

📝 Test yazıldı: OrderService.Tests.cs
✅ Test geçti: SQL injection attempt blocked

─────────────────────────────────────

🔧 Task 2/3: Secrets Cleanup
─────────────────────────────────────
Git history taranıyor...
├─ Bulundu: .env (3 commit'te)
├─ Siliniyor: git filter-branch
├─ Oluşturuluyor: .env.example
└─ Güncelleniyor: .gitignore

✅ Secrets cleaned from Git history
⚠️ NOT: Secrets rotate edilmeli (manuel)

─────────────────────────────────────

🔧 Task 3/3: Authorization Ekleme
─────────────────────────────────────
Dosya: src/controllers/AdminController.cs
Eksik endpoint: DeleteUser, BanUser, ResetPassword

✅ [Authorize(Roles = "Admin")] eklendi (3 endpoint)
✅ Logging eklendi
📝 Test yazıldı
✅ Test geçti

─────────────────────────────────────

📊 **Implementation Özeti**
├─ ✅ 7 dosya değiştirildi
├─ ✅ +234 satır eklendi
├─ ✅ -156 satır silindi
├─ ✅ 9 test yazıldı (9/9 geçti)
└─ ⚠️ 1 manuel adım: Secrets rotation

🔍 **CHECKPOINT #2: Kod İnceleme**
─────────────────────────────────────
Kod değişikliklerini görmek ister misin?
[Diff Göster] [Devam Et] [Rollback] [Dosya Dosya İncele]
```

---

### Adım 4: Testing Phase

```markdown
🧪 **ADIM 4/6: Test Başlıyor...**

Unit Tests:
[████████████████████] 100%
├─ ✅ OrderService.Tests: 12/12 passed
├─ ✅ AdminController.Tests: 8/8 passed
└─ ✅ AuthService.Tests: 15/15 passed

Integration Tests:
[████████████████████] 100%
├─ ✅ API Tests: 47/47 passed
├─ ✅ Database Tests: 12/12 passed
└─ ✅ Security Tests: 8/8 passed

Build:
[████████████████████] 100%
├─ ✅ TypeScript compile: OK (28s)
├─ ✅ Bundle size: 320 KB (was 847 KB)
└─ ✅ No errors, 0 warnings

Security Scan:
├─ ✅ npm audit: 0 vulnerabilities
├─ ✅ Semgrep: No issues
└─ ✅ Trivy: Clean

Performance:
├─ Build time: 85s → 28s ✅ (67% faster)
├─ API response: 450ms → 95ms ✅
└─ Bundle size: 847KB → 320KB ✅

📊 **Test Özeti**
├─ ✅ 102/102 tests passed
├─ ✅ Build successful
├─ ✅ Security clean
└─ ✅ Performance improved

🔍 **CHECKPOINT #3: Test Sonuçları**
─────────────────────────────────────
Tüm testler geçti!
Performans %67 iyileÅŸti.
Security temiz.

Commit'e hazır. Devam edilsin mi?
[Evet] [Hayır] [Test Detaylarını Göster]
```

---

### Adım 5: Commit Phase

```markdown
📝 **ADIM 5/6: Git Commit**

Branch oluÅŸturuluyor...
├─ ✅ Branch: fix/security-p0-issues
├─ ✅ 7 dosya staged
└─ ✅ Ready to commit

Commit Message:
─────────────────────────────────────
fix: resolve P0 security vulnerabilities

- Fix SQL injection in OrderService (parameterized queries)
- Remove exposed secrets from Git history
- Add authorization to admin endpoints
- Add comprehensive test coverage

Security improvements:
- Security score: 6.5/10 → 9.2/10
- Zero critical vulnerabilities
- Test coverage: 78% → 82%

Performance improvements:
- Build time: 85s → 28s (-67%)
- Bundle size: 847KB → 320KB (-62%)
- API response: 450ms → 95ms (-79%)

Breaking changes: None
Manual steps required:
- Rotate secrets (DB password, API keys)

Refs: #123, #456
─────────────────────────────────────

✅ Committed: abc123def
✅ Pushed to origin/fix/security-p0-issues

PR oluÅŸturulsun mu?
[Evet] [Hayır] [PR Template Göster]
```

---

### Adım 6: Final Report

```markdown
📊 **ADIM 6/6: Final Report**

═══════════════════════════════════════
✅ BAŞARIYLA TAMAMLANDI
═══════════════════════════════════════

⏱️ Toplam Süre: 3 dakika 42 saniye

🎯 Çözülen Sorunlar:
├─ 🔴 P0: 3/3 (%100) ✅
│   ├─ ✅ SQL Injection
│   ├─ ✅ Exposed Secrets
│   └─ ✅ Missing Authorization
│
├─ 🟡 P1: 2/5 (%40)
│   ├─ ✅ Build Optimization
│   ├─ ✅ Bundle Size
│   └─ ⏳ 3 sorun backlog'a eklendi
│
└─ 🟢 P2: 0/8 (kapsam dışı)

📈 Metrik İyileştirmeleri:
├─ Security Score: 6.5/10 → 9.2/10 (+41%)
├─ Build Time: 85s → 28s (-67%)
├─ Bundle Size: 847KB → 320KB (-62%)
├─ API Response: 450ms → 95ms (-79%)
└─ Test Coverage: 78% → 82% (+4%)

📝 Yapılan Değişiklikler:
├─ 7 dosya değiştirildi
├─ +234 satır eklendi
├─ -156 satır silindi
├─ 9 yeni test eklendi
└─ 1 branch oluşturuldu

🔗 Git Info:
├─ Branch: fix/security-p0-issues
├─ Commit: abc123def
├─ PR: #789 (draft)
└─ Rollback: git revert abc123def

⚠️ Manuel Adımlar Gerekli:
1. Secrets rotation (DB password, API keys)
   Guide: /implementation-guides/security-fixes.md
   
2. Code review isteÄŸi
   Reviewer: @ali, @ayse
   
3. Staging'de test
   Deploy: npm run deploy:staging

📁 Oluşturulan Dosyalar:
├─ /outputs/analysis-report-20250115.md
├─ /outputs/action-plan-20250115.md
├─ /outputs/execution-log-20250115.md
├─ /outputs/diff-abc123def.patch
└─ /outputs/test-results-20250115.json

🎯 Sonraki Adımlar:
1. ✅ Code review (#789)
2. ⏳ P1 kalan sorunlar (N+1, password hashing)
3. 📅 Sprint 2 planning (P2 backlog)

───────────────────────────────────────
🎉 Proje sağlığı: 7.2/10 → 8.9/10
───────────────────────────────────────

Bir sonraki analiz: 2 hafta sonra (30.01.2025)
```

---

## 🛡️ Safety Gates (Checkpoint Detayları)

### Checkpoint #1: Plan Onayı
**Ne zaman**: Analysis sonrası  
**Neden**: Kullanıcı hangi sorunların çözüleceğini bilmeli  
**Seçenekler**:
- ✅ Evet → Devam
- ❌ Hayır → Dur
- 🔧 Planı Düzenle → Interactive edit
- 👁️ Sadece Göster → Kod yazma, sadece planı genişlet

### Checkpoint #2: Kod İnceleme
**Ne zaman**: Implementation sonrası  
**Neden**: Kullanıcı kod değişikliklerini görmeli  
**Seçenekler**:
- 📄 Diff Göster → Tüm değişiklikleri göster
- ✅ Devam Et → Test'e geç
- ⏪ Rollback → Tüm değişiklikleri geri al
- 📁 Dosya Dosya İncele → Her dosyayı ayrı göster

### Checkpoint #3: Commit Onayı
**Ne zaman**: Test sonrası  
**Neden**: Git'e commit önemli bir adım  
**Seçenekler**:
- ✅ Evet → Commit + Push
- ❌ Hayır → Commit'siz bırak
- 📊 Test Detayları → Test log'larını göster

---

## 🎚️ Mode Override (Esnek Kontrol)

Prompt'ta özel direktifler verebilirsin:

```markdown
# Checkpoint'leri devre dışı bırak
"P0 sorunları düzelt, tüm checkpoint'leri skip et"
→ Hiç sormadan tüm flow'u çalıştırır (RİSKLİ!)

# Sadece belirli dosyalarda çalış
"Sadece OrderService.cs'i düzelt, diğerlerine dokunma"
→ Scope sınırlı

# Dry-run mode
"Ne yapacağını göster ama değişiklik yapma"
→ Kod yazılır ama dosyalar değiştirilmez

# Auto-approve certain types
"Security fix'leri otomatik onayla, ama performance için sor"
→ Selective checkpoints

# Test-only mode
"Kod yaz ve test et, ama commit etme"
→ Commit'i manuel yaparsın
```

---

## 📊 Execution Log (Otomatik Kaydedilen)

Her full flow çalıştırmasında otomatik log:

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

## 🔄 Rollback Komutları

Her zaman rollback mümkün:

```bash
# Son execution'ı tamamen geri al
git revert abc123def

# Sadece belirli dosyayı geri al
git checkout HEAD~1 -- src/services/OrderService.cs

# Full rollback (branch'i sil)
git branch -D fix/security-p0-issues
```

---

## 📚 Dosya Yapısı

```
/outputs/
├─ analysis-report-20250115.md        # Mode 1, 2, 3
├─ action-plan-20250115.md            # Mode 2, 3
├─ execution-log-20250115.md          # Mode 3 only
├─ diff-abc123def.patch               # Mode 3 only
└─ test-results-20250115.json         # Mode 3 only
```

---

## ⚙️ Konfigürasyon

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

**Mode seçimi kullanıcıya kalmış. Her mode bağımsız çalışabilir!** ✅
