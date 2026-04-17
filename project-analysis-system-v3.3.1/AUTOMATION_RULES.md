# Automation Rules - Hangi Sorunlar Otomatik Çözülür?

## 🤖 Otomatik Çözülebilir (Auto-Fix)

### ✅ Güvenlik

| Sorun | Auto-Fix | Risk | Checkpoint |
|-------|----------|------|------------|
| SQL Injection | ✅ Evet | Düşük | After code gen |
| .gitignore eksik | ✅ Evet | Yok | Otomatik |
| Hardcoded secrets (tespit) | ⚠️ Git'ten sil | Orta | Before commit |
| CORS AllowAnyOrigin | ✅ Evet | Düşük | After code gen |
| Missing [Authorize] | ✅ Evet | Düşük | After code gen |

### ✅ Performans

| Sorun | Auto-Fix | Risk | Checkpoint |
|-------|----------|------|------------|
| Moment.js → date-fns | ✅ Evet | Düşük | After test |
| Lodash → lodash-es | ✅ Evet | Düşük | After test |
| TypeScript incremental | ✅ Evet | Yok | Otomatik |
| Lazy loading eksik | ✅ Evet | Düşük | After test |
| Bundle optimization | ✅ Evet | Düşük | After test |

### ✅ Code Quality

| Sorun | Auto-Fix | Risk | Checkpoint |
|-------|----------|------|------------|
| ESLint errors | ✅ Evet | Yok | Otomatik |
| Prettier formatting | ✅ Evet | Yok | Otomatik |
| Unused imports | ✅ Evet | Yok | Otomatik |
| Missing types (TypeScript) | ✅ Evet | Düşük | After test |

### ✅ Erişilebilirlik

| Sorun | Auto-Fix | Risk | Checkpoint |
|-------|----------|------|------------|
| Alt text eksik (basit) | ✅ Evet | Yok | Manual review |
| Renk kontrastı | ✅ Evet | Düşük | After code gen |
| Missing ARIA labels | ✅ Evet | Düşük | After code gen |

---

## ❌ Otomatik Çözülemez (Manual)

### ❌ Güvenlik

| Sorun | Neden Manuel? | Gerekli Adımlar |
|-------|---------------|-----------------|
| Password hashing change | Migration gerekli | DB backup + migrate + test |
| Secrets rotation | External service | API key'leri yenile |
| SSL certificate | Infrastructure | Certificate provider |

### ❌ Database

| Sorun | Neden Manuel? | Gerekli Adımlar |
|-------|---------------|-----------------|
| Schema migration | Data loss riski | Backup + migrate + verify |
| Index ekleme (büyük tablo) | Lock riski | Maintenance window |
| Data migration | Business logic | Manuel verification |

### ❌ Architecture

| Sorun | Neden Manuel? | Gerekli Adımlar |
|-------|---------------|-----------------|
| Monolith → Microservices | Büyük refactor | Architecture planning |
| God class bölme | Business context | Domain expertise |
| API versioning | Breaking change | Backward compatibility plan |

---

## ⚠️ Conditional Auto-Fix (Şartlı)

### Küçük Projeler (<10K LOC)
```yaml
auto_fix:
  - bundle_optimization: true
  - dependency_updates: true  # Breaking change riski düşük
  - refactoring: true  # Impact küçük
```

### Büyük Projeler (>100K LOC)
```yaml
auto_fix:
  - bundle_optimization: true
  - dependency_updates: false  # Breaking change riski yüksek
  - refactoring: false  # Impact büyük, manuel review şart
```

### Production vs Development
```yaml
development:
  auto_fix_level: high
  checkpoints: minimal
  
staging:
  auto_fix_level: medium
  checkpoints: standard
  
production:
  auto_fix_level: low  # Sadece güvenli değişiklikler
  checkpoints: all
```

---

## 🎛️ Configuration

```yaml
# .ai-orchestrator.yml
automation_rules:
  # Always auto-fix
  always_auto:
    - sql_injection_fix
    - gitignore_update
    - eslint_autofix
    - prettier_format
    
  # Never auto-fix
  never_auto:
    - database_migration
    - password_hashing_change
    - api_versioning
    - architecture_change
    
  # Conditional (by file count)
  conditional:
    dependency_update:
      condition: "files_changed < 5"
      auto: true
    
    refactoring:
      condition: "lines_changed < 100"
      auto: true
  
  # Risk-based
  risk_levels:
    high_risk:  # Never auto
      - production_config
      - payment_logic
      - auth_system
    
    medium_risk:  # Checkpoint required
      - api_endpoints
      - database_queries
      - business_logic
    
    low_risk:  # Auto-fix OK
      - ui_styling
      - logging
      - error_messages
```

---

## 📊 Decision Tree

```
Sorun tespit edildi
│
├─ Risk level?
│  ├─ High → ❌ Manuel
│  ├─ Medium → ⚠️ Checkpoint
│  └─ Low → Devam
│
├─ Auto-fix mümkün?
│  ├─ Hayır → ❌ Manuel
│  └─ Evet → Devam
│
├─ Test coverage yeterli?
│  ├─ <50% → ⚠️ Checkpoint
│  └─ >80% → Devam
│
├─ Breaking change?
│  ├─ Evet → ⚠️ Checkpoint
│  └─ Hayır → Devam
│
└─ ✅ Auto-fix uygula
```

---

## ✅ Örnek: SQL Injection (Auto-Fix)

```markdown
Tespit: SQL Injection (OrderService.cs:45)
├─ Risk: High (ama fix basit)
├─ Auto-fix: Mümkün ✅
├─ Breaking change: Hayır ✅
├─ Test: Yazılabilir ✅
└─ Karar: Auto-fix + Checkpoint

Akış:
1. Test yaz
2. Kodu düzelt
3. Test çalıştır
4. ✅ Geçti
5. Checkpoint: "Kod değişikliğini göster"
6. Kullanıcı onayla
7. Commit
```

---

## ❌ Örnek: Database Migration (Manuel)

```markdown
Tespit: Missing index (Orders.CustomerId)
├─ Risk: Medium (büyük tabloda lock riski)
├─ Auto-fix: Teknik olarak mümkün
├─ Breaking change: Hayır
├─ ANCAK: Production'da maintenance window gerekli
└─ Karar: Manuel ❌

Manuel Adımlar:
1. Migration script hazırla
2. Backup al
3. Maintenance window planla
4. Staging'de test et
5. Production'da uygula (CONCURRENT index)
```

---

**Sistem akıllı seçim yapar: Güvenli olanlar otomatik, riskli olanlar manuel!** ✅
