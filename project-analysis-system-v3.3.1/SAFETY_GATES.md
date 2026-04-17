# Safety Gates - Güvenlik Kontrolleri

## 🛡️ Pre-Execution Checks

### 1. Backup Kontrolü
```bash
# Çalıştırmadan önce
git status
└─ Working directory clean? ✅

git log -1
└─ Son commit ne zaman? (güncel mi?)

git remote -v
└─ Origin doğru mu?
```

**Gate**: Eğer uncommitted changes varsa → DURDUR

---

### 2. Test Coverage Kontrolü
```bash
npm test -- --coverage
└─ Coverage >50%? ✅

dotnet test /p:CollectCoverage=true
└─ Coverage >50%? ✅
```

**Gate**: Eğer <50% coverage → UYARI

---

### 3. Branch Kontrolü
```bash
git branch --show-current
└─ main veya master? → ⚠️ UYARI

└─ feature/fix branch? → ✅ OK
```

**Gate**: Main branch'te çalışma → Yeni branch oluştur

---

## 🔍 During Execution Checks

### 1. File Change Limit
```yaml
max_files_changed: 20
```

**Gate**: >20 dosya değişecekse → DURDUR + Manuel review

---

### 2. Line Change Limit
```yaml
max_lines_changed: 500
```

**Gate**: >500 satır değişecekse → Checkpoint

---

### 3. Breaking Change Detection
```typescript
// API signature değişikliği tespit
function detectBreakingChange(oldCode, newCode) {
  if (functionSignatureChanged) {
    return "BREAKING_CHANGE";
  }
}
```

**Gate**: Breaking change → UYARI + Versioning öner

---

### 4. Dependency Update Check
```bash
npm outdated
└─ Major version change? → ⚠️ UYARI
```

**Gate**: Major update → Changelog kontrol et + Test

---

## ✅ Post-Execution Checks

### 1. Test Requirement
```bash
# Tüm testler geçmeli
npm test
└─ Exit code 0? ✅

dotnet test
└─ Exit code 0? ✅
```

**Gate**: Test fail → ROLLBACK

---

### 2. Build Requirement
```bash
npm run build
└─ Exit code 0? ✅

dotnet build
└─ Exit code 0? ✅
```

**Gate**: Build fail → ROLLBACK

---

### 3. Security Scan
```bash
npm audit --audit-level=high
└─ 0 high/critical? ✅

semgrep --config auto
└─ 0 critical? ✅
```

**Gate**: Critical vulnerability → ROLLBACK

---

### 4. Performance Regression Check
```yaml
before:
  build_time: 85s
  bundle_size: 847KB

after:
  build_time: 92s  # ❌ Daha yavaş!
  bundle_size: 320KB  # ✅ Daha hızlı
```

**Gate**: Performance >10% kötüleşme → UYARI

---

## 🚨 Emergency Stop Triggers

### Otomatik Durdurma (Abort)

1. **Test fail >30%**
   ```
   47/102 tests failed → ABORT
   ```

2. **Build error**
   ```
   Compilation error → ABORT
   ```

3. **Git conflict**
   ```
   Merge conflict detected → ABORT
   ```

4. **Disk space <10%**
   ```
   Not enough space → ABORT
   ```

5. **Process timeout**
   ```
   Execution >30 min → ABORT
   ```

---

## 🎛️ Configurable Gates

```yaml
# .ai-safety-gates.yml
gates:
  pre_execution:
    - check: backup
      required: true
      
    - check: test_coverage
      required: false
      minimum: 50%
      
    - check: branch
      required: true
      forbidden_branches: [main, master, production]
  
  during_execution:
    - check: file_limit
      max: 20
      
    - check: line_limit
      max: 500
      
    - check: breaking_change
      action: warn
  
  post_execution:
    - check: tests
      required: true
      
    - check: build
      required: true
      
    - check: security_scan
      required: true
      threshold: high
      
    - check: performance
      regression_tolerance: 10%
```

---

## 📊 Gate Status Dashboard

```markdown
🛡️ Safety Gates Status

Pre-Execution:
├─ ✅ Backup OK
├─ ✅ Test coverage: 82% (>50%)
├─ ✅ Branch: fix/security-issues (OK)
└─ ✅ All pre-execution gates passed

During Execution:
├─ ✅ Files changed: 7 (<20)
├─ ✅ Lines changed: 390 (<500)
├─ ⚠️ Breaking change detected (API signature)
└─ ⚠️ 1 warning

Post-Execution:
├─ ✅ Tests: 102/102 passed
├─ ✅ Build: Success
├─ ✅ Security: Clean
├─ ✅ Performance: +67% improvement
└─ ✅ All post-execution gates passed

Overall: ✅ SAFE TO COMMIT (1 warning)
```

---

## 🔄 Rollback Triggers

Otomatik rollback yapılır:

```yaml
rollback_if:
  - tests_failed: true
  - build_failed: true
  - critical_security: true
  - data_loss_risk: true
  - manual_request: true
```

---

**Güvenlik her şeyden önemli! Gate'ler sistemi korur.** 🛡️
