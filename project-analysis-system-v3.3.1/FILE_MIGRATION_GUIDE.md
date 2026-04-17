# Migration Guide: v3.2 → v3.3
**Versiyon Geçişi**: AI Project Analysis System  
**Tarih**: 20 Aralık 2024  
**Breaking Changes**: Yok (sadece eklemeler)  
**Backward Compatible**: Evet ✅

---

## 📊 Genel Bakış

**v3.2**: 39 dosya  
**v3.3**: 52 dosya (+13 yeni)  
**Silinen**: 0 dosya  
**Güncellenen**: 2 dosya (README, MANIFEST)

---

## 🗑️ SİLİNECEK DOSYALAR

### ❌ Hiçbir dosya silinmiyor!

**Neden**: v3.3 tamamen backward compatible. Mevcut tüm dosyalar korunuyor.

---

## ➕ EKLENECEK YENİ DOSYALAR (13 dosya)

### 📁 1. Root Directory (Ana dizin)

```bash
project-analysis-system/
├── README_V3.3.md                    # ⭐ YENİ - v3.3 release notes
└── FILE_MIGRATION_GUIDE.md           # ⭐ YENİ - Bu dosya
```

**Konum**: `/mnt/project/` (root)

---

### 📁 2. Self-Testing Suite (4 dosya)

```bash
project-analysis-system/
└── testing/                          # ⭐ YENİ KLASÖR
    ├── SELF_TEST_SUITE.md
    ├── VALIDATION_RULES.md
    ├── TEST_SCENARIOS.md
    └── REGRESSION_TESTS.md
```

**Konum**: `/mnt/project/testing/`  
**Not**: Yeni bir `testing/` klasörü oluştur

---

### 📁 3. Setup & Onboarding (4 dosya)

```bash
project-analysis-system/
└── onboarding/                       # ⭐ YENİ KLASÖR
    ├── QUICK_START.md
    ├── SETUP_WIZARD.md
    ├── FILE_SELECTION_GUIDE.md
    └── PROJECT_TYPE_DETECTION.md
```

**Konum**: `/mnt/project/onboarding/`  
**Not**: Yeni bir `onboarding/` klasörü oluştur

---

### 📁 4. AI Validation Layer (4 dosya)

```bash
project-analysis-system/
└── validation/                       # ⭐ YENİ KLASÖR
    ├── AI_VALIDATION_LAYER.md
    ├── CONFIDENCE_SCORING.md
    ├── FACT_CHECKING_RULES.md
    └── UNCERTAINTY_HANDLING.md
```

**Konum**: `/mnt/project/validation/`  
**Not**: Yeni bir `validation/` klasörü oluştur

---

### 📁 5. Planning & Tracking (1 dosya)

```bash
project-analysis-system/
└── planning/                         # ⭐ YENİ KLASÖR (P1'de daha fazlası eklenecek)
    └── SYSTEM_IMPROVEMENT_ACTION_PLAN.md
```

**Konum**: `/mnt/project/planning/`

---

## ✏️ GÜNCELLENECEK DOSYALAR (2 dosya)

### 1. README.md → README.md (güncelle)

**Değişiklikler**:
```diff
- Version: 3.2 AUTONOMOUS
+ Version: 3.3 RELIABLE

+ ## What's New in v3.3
+ - Self-testing suite
+ - AI validation layer
+ - Setup wizard (5-minute start)
+ - Confidence scoring
+ - Module versioning

+ ## New Directories
+ - `/testing/` - Self-test framework
+ - `/onboarding/` - Quick start guides
+ - `/validation/` - AI validation layer
+ - `/planning/` - Roadmaps and plans
```

**Konum**: `/mnt/project/README.md`  
**Aksiyon**: Manuel güncelleme (veya README_V3.3.md'yi README.md ile değiştir)

---

### 2. MANIFEST.yaml → MANIFEST.yaml (güncelle)

**Değişiklikler**:
```diff
- version: "3.0"
+ version: "3.3"

- total_modules: 20
+ total_modules: 24

+ # New modules (v3.3)
+ self_test_suite:
+   path: "testing/SELF_TEST_SUITE.md"
+   priority: P0
+   auto_load: true
+   
+ ai_validation:
+   path: "validation/AI_VALIDATION_LAYER.md"
+   priority: P0
+   auto_load: true
```

**Konum**: `/mnt/project/MANIFEST.yaml`  
**Aksiyon**: Manuel güncelleme (veya P1'de MANIFEST_V2.yaml oluşturacağım)

---

## 📂 YENİ KLASÖR YAPISI

### Önce (v3.2)
```
project-analysis-system/
├── README.md
├── ORCHESTRATOR_PROMPT.md
├── BASE_PROMPT.md
├── MANIFEST.yaml
├── USAGE_GUIDE.md
├── TURKISH_PROMPTS.md
├── MODE_TRANSITIONS.md
├── MISSING_AREAS.md
├── AGENTIC_WORKFLOW.md
├── AUTOMATION_RULES.md
├── SAFETY_GATES.md
├── EXECUTION_LOG_TEMPLATE.md
├── ACTION_PLAN_TEMPLATE.md
├── ROADMAP_GENERATOR.md
├── TASK_BREAKDOWN.md
├── TRACKING_TEMPLATE.md
├── ROLLBACK_PROCEDURES.md
├── EFFECTIVE_PROMPTS.md
└── [24 modül .md dosyası]
```

### Sonra (v3.3)
```
project-analysis-system/
├── README.md                         # GÜNCELLENDİ
├── README_V3.3.md                    # YENİ
├── FILE_MIGRATION_GUIDE.md           # YENİ
├── ORCHESTRATOR_PROMPT.md
├── BASE_PROMPT.md
├── MANIFEST.yaml                     # GÜNCELLENECEK (P1'de)
├── USAGE_GUIDE.md
├── TURKISH_PROMPTS.md
├── MODE_TRANSITIONS.md
├── MISSING_AREAS.md
├── AGENTIC_WORKFLOW.md
├── AUTOMATION_RULES.md
├── SAFETY_GATES.md
├── EXECUTION_LOG_TEMPLATE.md
├── ACTION_PLAN_TEMPLATE.md
├── ROADMAP_GENERATOR.md
├── TASK_BREAKDOWN.md
├── TRACKING_TEMPLATE.md
├── ROLLBACK_PROCEDURES.md
├── EFFECTIVE_PROMPTS.md
│
├── testing/                          # YENİ KLASÖR
│   ├── SELF_TEST_SUITE.md
│   ├── VALIDATION_RULES.md
│   ├── TEST_SCENARIOS.md
│   └── REGRESSION_TESTS.md
│
├── onboarding/                       # YENİ KLASÖR
│   ├── QUICK_START.md
│   ├── SETUP_WIZARD.md
│   ├── FILE_SELECTION_GUIDE.md
│   └── PROJECT_TYPE_DETECTION.md
│
├── validation/                       # YENİ KLASÖR
│   ├── AI_VALIDATION_LAYER.md
│   ├── CONFIDENCE_SCORING.md
│   ├── FACT_CHECKING_RULES.md
│   └── UNCERTAINTY_HANDLING.md
│
├── planning/                         # YENİ KLASÖR
│   └── SYSTEM_IMPROVEMENT_ACTION_PLAN.md
│
└── [24 modül .md dosyası - değişmedi]
```

---

## 🚀 ADIM ADIM MİGRATION

### Adım 1: Backup (Önce yedek al!)
```bash
# Mevcut projeyi yedekle
cp -r /mnt/project /mnt/project-backup-v3.2
cd /mnt/project
```

---

### Adım 2: Yeni Klasörleri Oluştur
```bash
# 4 yeni klasör
mkdir -p testing
mkdir -p onboarding
mkdir -p validation
mkdir -p planning
```

---

### Adım 3: Dosyaları Yerleştir

#### testing/ klasörü
```bash
mv SELF_TEST_SUITE.md testing/
mv VALIDATION_RULES.md testing/
mv TEST_SCENARIOS.md testing/
mv REGRESSION_TESTS.md testing/
```

#### onboarding/ klasörü
```bash
mv QUICK_START.md onboarding/
mv SETUP_WIZARD.md onboarding/
mv FILE_SELECTION_GUIDE.md onboarding/
mv PROJECT_TYPE_DETECTION.md onboarding/
```

#### validation/ klasörü
```bash
mv AI_VALIDATION_LAYER.md validation/
mv CONFIDENCE_SCORING.md validation/
mv FACT_CHECKING_RULES.md validation/
mv UNCERTAINTY_HANDLING.md validation/
```

#### planning/ klasörü
```bash
mv SYSTEM_IMPROVEMENT_ACTION_PLAN.md planning/
```

---

### Adım 4: Root Dosyaları Ekle
```bash
# README_V3.3.md ve bu dosyayı ekle
cp README_V3.3.md /mnt/project/
cp FILE_MIGRATION_GUIDE.md /mnt/project/
```

---

### Adım 5: README.md Güncelle (opsiyonel)
```bash
# Seçenek A: Eski README'yi v3.2 olarak sakla
mv README.md README_V3.2_BACKUP.md
cp README_V3.3.md README.md

# Seçenek B: Manuel olarak README.md'yi güncelle
# (v3.3 değişikliklerini ekle)
```

---

### Adım 6: MANIFEST.yaml Güncelle (P1'de yapılacak)
```bash
# P1'de MANIFEST_V2.yaml oluşturulacak
# O zaman:
mv MANIFEST.yaml MANIFEST_V3.2_BACKUP.yaml
cp MANIFEST_V2.yaml MANIFEST.yaml
```

---

## ✅ DOĞRULAMA

Migration tamamlandıktan sonra kontrol et:

### Checklist
```bash
# 1. Yeni klasörler var mı?
[ -d testing ] && echo "✅ testing/ OK" || echo "❌ testing/ EKSİK"
[ -d onboarding ] && echo "✅ onboarding/ OK" || echo "❌ onboarding/ EKSİK"
[ -d validation ] && echo "✅ validation/ OK" || echo "❌ validation/ EKSİK"
[ -d planning ] && echo "✅ planning/ OK" || echo "❌ planning/ EKSİK"

# 2. Dosya sayısı doğru mu?
find testing -name "*.md" | wc -l    # Beklenen: 4
find onboarding -name "*.md" | wc -l # Beklenen: 4
find validation -name "*.md" | wc -l # Beklenen: 4
find planning -name "*.md" | wc -l   # Beklenen: 1

# 3. README_V3.3.md var mı?
[ -f README_V3.3.md ] && echo "✅ README_V3.3.md OK"

# 4. Eski dosyalar hala var mı?
[ -f ORCHESTRATOR_PROMPT.md ] && echo "✅ Core files intact"
[ -f BASE_PROMPT.md ] && echo "✅ Core files intact"
```

### Beklenen Çıktı
```
✅ testing/ OK
✅ onboarding/ OK
✅ validation/ OK
✅ planning/ OK
4
4
4
1
✅ README_V3.3.md OK
✅ Core files intact
✅ Core files intact
```

---

## 🔄 ROLLBACK (Geri Alma)

Bir sorun olursa:

```bash
# Yedekten geri yükle
rm -rf /mnt/project
cp -r /mnt/project-backup-v3.2 /mnt/project

# Veya sadece yeni dosyaları sil
rm -rf /mnt/project/testing
rm -rf /mnt/project/onboarding
rm -rf /mnt/project/validation
rm -rf /mnt/project/planning
rm /mnt/project/README_V3.3.md
rm /mnt/project/FILE_MIGRATION_GUIDE.md
```

---

## 📊 ÖZET

### Eklenen
- **13 yeni dosya**
- **4 yeni klasör** (testing, onboarding, validation, planning)
- **1 yeni README** (README_V3.3.md)
- **1 migration guide** (bu dosya)

### Kaldırılan
- **0 dosya** (hiçbir şey silinmedi)

### Güncellenen
- **README.md** (opsiyonel - v3.3 notları eklenir)
- **MANIFEST.yaml** (P1'de güncellenir)

### Risk Seviyesi
- **Çok Düşük** 🟢 (sadece eklemeler, silme yok)
- **Backward Compatible** ✅
- **Rollback Mümkün** ✅

---

## 📝 NOTLAR

### P1 Migration (Gelecekte)
P1 iyileştirmelerinde şunlar eklenecek:
- `MANIFEST_V2.yaml` (dependency graph ile)
- `MODULE_VERSIONING.md`
- `TOKEN_BUDGET_MONITOR.md`
- `DEPENDENCY_RESOLVER.md`
- `CHANGELOG_TEMPLATE.md`
- `MIGRATION_GUIDES.md`

Bu dosyalar da aynı şekilde yeni klasörlere yerleştirilecek (breaking change yok).

### Kullanıcılar İçin
Eğer sistemin **kullanıcısıysan** (geliştirici değil):
- Hiçbir şey yapma gerekmez
- Yeni dosyalar otomatik yüklenecek (MANIFEST.yaml sayesinde)
- Eski prompt'lar çalışmaya devam eder

### Geliştiriciler İçin
Eğer sistemi **geliştiriyorsan**:
- Yukarıdaki adımları takip et
- Test et (SELF_TEST_SUITE.md'yi çalıştır)
- MANIFEST.yaml'ı güncelle (P1'de)

---

**Son Güncelleme**: 20 Aralık 2024  
**Sonraki Migration**: v3.3 → v3.4 (P1 iyileştirmeleri sonrası)
