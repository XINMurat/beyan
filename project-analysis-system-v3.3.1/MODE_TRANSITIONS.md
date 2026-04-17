# Mode Transitions - Dosyalar Arası Geçiş Rehberi

**Mode'lar arasında output'ları nasıl kullanırsın?**

---

## 🔄 Problem

```
Mode 1 çalıştırdın → analysis-report.md aldın
Mode 2'de bu raporu kullanmak istiyorsun
Mode 3'te planı execute etmek istiyorsun
```

**Nasıl yapacaksın?** 👇

---

## 🎯 Çözüm: 3 Yöntem

### Yöntem 1: 📎 Dosya Referansı (Önerilen ✅)

**En kolay ve en etkili yöntem**

#### Mode 1 → Mode 2

```markdown
# Adım 1: Mode 1 çalıştır
YOU: "Projeyi analiz et"
AI: [analysis-report-20250116.md oluşturur]

# Adım 2: Dosyayı AI'ya tekrar yükle + Mode 2 prompt
YOU: [analysis-report-20250116.md'yi AI'ya yükle]
     "Bu analiz raporunu kullanarak aksiyon planı oluştur"

AI: [Raporu okur, action-plan-20250116.md oluşturur]
```

#### Mode 2 → Mode 3

```markdown
# Adım 1: Mode 2'den gelen dosyalar
- analysis-report-20250116.md
- action-plan-20250116.md

# Adım 2: Dosyaları AI'ya yükle + Mode 3 prompt
YOU: [Her iki dosyayı da yükle]
     "Bu aksiyon planını uygula"

AI: [Planı okur, kod yazar, execute eder]
```

**Avantaj**: 
- ✅ Her şey explicit
- ✅ AI tam context'i görüyor
- ✅ Herhangi bir mode'dan başlayabilirsin

---

### Yöntem 2: 💬 Prompt İçinde Referans

**Dosya yüklemeden, prompt ile referans ver**

```markdown
# Mode 1 çıktısı:
"3 P0 sorun var: SQL injection, exposed secrets, missing auth"

# Mode 2 prompt'u:
YOU: "Bu 3 P0 sorun için aksiyon planı:
      1. SQL injection (OrderService.cs)
      2. Exposed secrets (.env)
      3. Missing authorization (AdminController)
      
      Bunlar için sprint planı oluştur"

AI: [Planı oluşturur]
```

**Avantaj**: Hızlı  
**Dezavantaj**: Manuel kopyala-yapıştır gerekiyor

---

### Yöntem 3: 🔗 Conversation History (Aynı Chat'te)

**Aynı conversation içinde devam et**

```markdown
# Aynı chat window'da:

YOU: "Projeyi analiz et"
AI: [Analiz yapar, rapor verir]

YOU: "Şimdi bu analiz için aksiyon planı oluştur"
AI: [Önceki mesajları hatırlayarak plan oluşturur]

YOU: "Planı uygula"
AI: [Mode 3 execute eder]
```

**Avantaj**: 
- ✅ En seamless
- ✅ Manuel işlem minimum

**Dezavantaj**: 
- ⚠️ Uzun conversation'larda context kaybolabilir
- ⚠️ Yeni chat'te kullanamazsın

---

## 📋 Detaylı Örnek: Full Flow

### Senaryo: Mode 1 → Mode 2 → Mode 3

```markdown
═══════════════════════════════════════
🔍 ADIM 1: MODE 1 (Analyze Only)
═══════════════════════════════════════

YOU: "Projeyi analiz et"

AI: 
# Proje Sağlık Raporu

## P0 (Kritik)
1. SQL Injection (OrderService.cs:45)
2. Exposed secrets (.env)
3. Missing authorization (AdminController)

## P1 (Yüksek)
4. N+1 Query (Orders endpoint)
5. Vulnerable deps (12 packages)
...

[Dosya kaydedildi: analysis-report-20250116.md]

───────────────────────────────────────

═══════════════════════════════════════
📋 ADIM 2: MODE 2 (Analyze + Plan)
═══════════════════════════════════════

# Yöntem 1a: Dosya yükle
YOU: [analysis-report-20250116.md'yi yükle]
     "Bu rapor için aksiyon planı oluştur"

# Yöntem 1b: Aynı chat'te devam
YOU: "Bu analiz için aksiyon planı oluştur"

AI:
# Aksiyon Planı

## Sprint 1 (Bu Hafta - 40h)

| # | Sorun | Çözüm | Sorumlu | Süre |
|---|-------|-------|---------|------|
| 1 | SQL Injection | Parameterized query | Ali | 2h |
| 2 | Secrets | Rotate + .gitignore | Ayşe | 1h |
| 3 | Authorization | [Authorize] ekle | Mehmet | 30m |

[Dosya kaydedildi: action-plan-20250116.md]

───────────────────────────────────────

═══════════════════════════════════════
🚀 ADIM 3: MODE 3 (Full Flow)
═══════════════════════════════════════

# Yöntem 1: Her iki dosyayı yükle
YOU: [analysis-report.md + action-plan.md yükle]
     "Bu planı uygula"

# Yöntem 2: Sadece plan'ı yükle
YOU: [action-plan-20250116.md yükle]
     "Bu aksiyon planını execute et"

# Yöntem 3: Aynı chat'te
YOU: "Bu planı şimdi uygula"

AI:
📊 ADIM 1/6: Analiz (Skip - zaten var)
📋 ADIM 2/6: Plan (Skip - zaten var)

🔍 CHECKPOINT #1: Plan Onayı
3 P0 sorun çözülecek. Devam? [Evet/Hayır]

YOU: "Evet"

💻 ADIM 3/6: Implementation
✅ SQL Injection düzeltildi
✅ Secrets temizlendi
✅ Authorization eklendi

[... continues ...]
```

---

## 🎛️ Hangi Yöntemi Kullanmalısın?

### Durum 1: Aynı Gün, Aynı Proje
```
→ Yöntem 3: Aynı chat'te devam et
→ En hızlı, minimum effort
```

### Durum 2: Farklı Günler, Aynı Proje
```
→ Yöntem 1: Dosya yükle
→ Context kaybolmaz, güvenli
```

### Durum 3: Başka Biri İçin Plan Oluşturuyorsun
```
→ Yöntem 1: Dosyaları export et
→ Diğer kişi dosyaları yükleyip execute edebilir
```

### Durum 4: Hızlı Iterasyon
```
→ Yöntem 3: Aynı chat
→ "Şimdi P1'leri de ekle planına"
```

---

## 🔀 Partial Flow Örnekleri

### Mode 1 → Mode 3 (Plan Skip)

```markdown
YOU: "Projeyi analiz et"
AI: [Rapor verir]

YOU: "P0 sorunlarını direkt düzelt (plan oluşturmadan)"
AI: [Mode 3 çalışır, ama plan adımını otomatik yapar]
```

---

### Mode 2 → Mode 1 (Re-analysis)

```markdown
YOU: "Aksiyon planı oluştur"
AI: [Plan verir]

# Planı uyguladın (manuel veya Mode 3 ile)
# Şimdi sonucu görmek istiyorsun

YOU: "Projeyi tekrar analiz et"
AI: [Yeni analiz, metrik iyileşmelerini gösterir]
```

---

### Mode 3 → Mode 1 (Verification)

```markdown
YOU: "P0 sorunları düzelt"
AI: [Execute eder, 3/3 sorun çözülür]

YOU: "Sonuçları doğrula, tekrar analiz et"
AI: [Verification analysis yapar]
     Security: 6.5/10 → 9.2/10 ✅
```

---

## 📊 Output Dosya Formatları

### Mode 1 Output

```
/outputs/
└── analysis-report-20250116.md
    ├─ Genel skor
    ├─ P0, P1, P2, P3 sorunlar
    ├─ Metrikler
    └─ Öneriler
```

### Mode 2 Output

```
/outputs/
├── analysis-report-20250116.md (from Mode 1)
├── action-plan-20250116.md
│   ├─ Sprint breakdown
│   ├─ Task assignments
│   └─ Effort estimates
│
├── roadmap-Q1-2025.md (optional)
└── task-breakdown-20250116.md (optional)
```

### Mode 3 Output

```
/outputs/
├── analysis-report-20250116.md
├── action-plan-20250116.md
├── execution-log-20250116.md ⭐ NEW
│   ├─ Timeline
│   ├─ Changes made
│   ├─ Test results
│   └─ Metrics
│
├── diff-abc123def.patch ⭐ NEW
└── test-results-20250116.json ⭐ NEW
```

---

## 🎯 Best Practices

### ✅ DO

**1. Dosyaları İsimlendir**
```
✅ analysis-report-20250116-security.md
✅ action-plan-20250116-P0-fixes.md
✅ execution-log-20250116-sprint1.md
```

**2. Versiyonla**
```
✅ analysis-report-v1.md
✅ analysis-report-v2-after-fixes.md
```

**3. Context Ver**
```
✅ "Bu analiz raporunu kullanarak aksiyon planı oluştur"
❌ "Plan oluştur" (hangi analiz?)
```

---

### ❌ DON'T

**1. Eski Dosyaları Kullanma**
```
❌ 2 hafta önceki analysis ile plan oluşturma
✅ Güncel analiz yap, sonra planla
```

**2. Incomplete Context**
```
❌ Sadece "P0: SQL Injection" diye not alıp plan isteme
✅ Tam raporu yükle veya detaylı bilgi ver
```

**3. Mode Karıştırma**
```
❌ "Analiz et ve düzelt" (hangi mode?)
✅ "Analiz et" sonra "Planı uygula" (explicit)
```

---

## 🔄 Iterative Workflow

### Döngüsel Kullanım (Önerilen)

```markdown
Week 1:
├─ Mode 1: Initial analysis
│   └─ Skor: 6.5/10
│
├─ Mode 2: Create roadmap
│   └─ 3 sprint plan
│
└─ Mode 3: Execute Sprint 1 (P0)
    └─ 3/3 sorun çözüldü

Week 3:
├─ Mode 1: Re-analysis
│   └─ Skor: 7.8/10 ✅ (+1.3)
│
├─ Mode 2: Plan Sprint 2 (P1)
│
└─ Mode 3: Execute Sprint 2
    └─ 4/5 sorun çözüldü

Week 5:
├─ Mode 1: Final analysis
│   └─ Skor: 9.1/10 ✅ (+2.6 total)
│
└─ Executive Report
    └─ 3 sprint, 12 issue, +41% improvement
```

---

## 🎬 Pratik Örnekler

### Örnek 1: Daily Standup

```markdown
# Her gün sabah
Mode 1: "Quick scan yap"
→ Yeni sorun var mı?
→ Metrikler nasıl?

# Hafta başı
Mode 2: "Bu haftalık plan"
→ Sprint tasks

# Her gün
Mode 3: "Bugünkü task'leri yap"
→ Incremental progress
```

---

### Örnek 2: Sprint Cycle

```markdown
# Sprint Planning (Pazartesi)
Mode 1: "Detaylı analiz"
Mode 2: "2 haftalık sprint planı"

# Sprint Execution (Salı-Cuma)
Mode 3: "Task 1'i yap"
Mode 3: "Task 2'yi yap"
...

# Sprint Review (Cuma)
Mode 1: "Sprint sonuçlarını analiz et"
→ Metrik iyileşmesi göster
```

---

### Örnek 3: Quarterly Planning

```markdown
# Q1 Start (Ocak 1)
Mode 1: "Baseline analysis"
Mode 2: "3 aylık roadmap"

# Monthly Check (Her ayın 1'i)
Mode 1: "Progress analysis"
Mode 2: "Roadmap update"

# Q1 End (Mart 31)
Mode 1: "Final Q1 analysis"
→ Metrics: Başlangıç vs Bitiş
→ ROI: Çaba vs İyileşme
```

---

## 🛠️ Teknik Detaylar

### Dosya Formatları

**Markdown (.md)**
```markdown
✅ Human-readable
✅ AI-friendly
✅ Git-friendly
✅ Diff'lenebilir
```

**JSON (.json)**
```json
✅ Structured data
✅ Programmatic use
✅ Integration ready
```

**YAML (.yaml)**
```yaml
✅ Configuration
✅ Human-readable
✅ Nested structures
```

---

### File Naming Convention

```
[type]-[date]-[description].[ext]

Örnekler:
analysis-report-20250116.md
analysis-report-20250116-security-focus.md
action-plan-20250116-sprint1.md
execution-log-20250116-p0-fixes.md
roadmap-Q1-2025.md
```

---

## 📚 Referanslar

**İlgili Dosyalar**:
- `ORCHESTRATOR_PROMPT.md` → Mode definitions
- `USAGE_GUIDE.md` → Detailed usage for each mode
- `TURKISH_PROMPTS.md` → 100+ prompt examples

**Workflow Örnekleri**:
- Daily standup workflow
- Sprint cycle workflow  
- Quarterly planning workflow

---

## ❓ FAQ

**Q: Mode 1 output'unu Mode 3'te kullanabilir miyim?**  
A: Evet! Mode 3 otomatik olarak planlamayı da yapar.

**Q: Eski analizi yeni plana kullanabilir miyim?**  
A: Kullanabilirsin ama güncel analiz önerilir.

**Q: Chat history yeterli mi?**  
A: Kısa conversation'larda evet, uzunsa dosya yükle.

**Q: Başka biri Mode 2 output'umu kullanabilir mi?**  
A: Evet, action-plan.md'yi export et, yüklesin.

**Q: Mode 3'ü çalıştırdıktan sonra Mode 1 gerekli mi?**  
A: Verification için önerilir (metrik iyileşmesi görmek için).

---

**Mode'lar arası geçiş artık çok kolay!** 🔄✅
