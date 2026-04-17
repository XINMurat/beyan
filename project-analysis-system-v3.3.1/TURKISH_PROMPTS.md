# Türkçe Prompt �?rnekleri - v3.2 (3 Mode)

**100+ Türkçe prompt örne�?i - 3 farklı kullanım moduna göre düzenlenmi�?**

---

## �??� Mode Seçimi (Hızlı Ba�?vuru)

| Ne İstiyorsun? | Hangi Mode? | �?rnek Prompt |
|----------------|-------------|--------------|
| Sadece rapor | Mode 1 | "Projeyi analiz et" |
| Rapor + Plan | Mode 2 | "Aksiyon planı olu�?tur" |
| Otomatik fix | Mode 3 | "P0 sorunları düzelt" |

---

## �??? Mode 1: Analyze Only (Sadece Analiz)

**Ne yapar**: Sadece analiz yapar, hiçbir de�?i�?iklik yapmaz  
**Kullanım**: Günlük raporlar, durum de�?erlendirmesi, audit

### Genel Analiz

```markdown
"Projeyi analiz et"
"Proje sa�?lık raporu ver"
"Mevcut durumu de�?erlendir"
"Hızlı bir scan yap"
"Deep analysis yap"
"Comprehensive audit çalı�?tır"
```

### Spesifik Alan Analizi

```markdown
"Security audit yap"
"Performans analizi çalı�?tır"
"Database sorunlarını tespit et"
"UI/UX analizi yap"
"Eri�?ilebilirlik kontrolü yap"
"WCAG compliance kontrol et"
"API design review yap"
"Hidden gem'leri bul"
"Technical debt hesapla"
"Code quality metrics ver"
```

### Türk Piyasası Odaklı

```markdown
"KVKK uyumlulu�?unu kontrol et"
"Türk piyasası için analiz yap"
"e-Devlet entegrasyonunu incele"
"Taksit sistemini de�?erlendir"
"Türkçe deste�?ini kontrol et"
```

### AI-Generated Code Analizi

```markdown
"AI'ın yazdı�?ı kodu incele"
"Mı�? gibi pattern'leri bul"
"AI hallucination'larını tespit et"
"ChatGPT code smell'lerini ara"
```

### �?ncelik Bazlı

```markdown
"Sadece P0 sorunları göster"
"Kritik ve yüksek öncelikli sorunlar"
"Quick win'leri bul"
"En kolay düzeltilebilir sorunlar"
"En kritik 5 sorunu göster"
```

### Açıklayıcı (No Action)

```markdown
"Sadece rapor ver, hiçbir de�?i�?iklik yapma"
"Analiz yap ama kod yazma"
"Read-only mode'da çalı�?"
"De�?erlendirme yap, implementation yapma"
```

---

## �??? Mode 2: Analyze + Plan

**Ne yapar**: Analiz + aksiyon planı + sprint breakdown  
**Kullanım**: Sprint planning, roadmap, task assignment

### Aksiyon Planı

```markdown
"Projeyi analiz et ve aksiyon planı olu�?tur"
"Aksiyon planı hazırla"
"Sprint planning yap"
"Task breakdown olu�?tur"
"Implementation plan hazırla"
"Execution roadmap çıkar"
```

### Sprint Planning

```markdown
"Bu hafta için sprint planı"
"2 haftalık sprint olu�?tur"
"Sprint 1 için task'leri belirle"
"Bu sprint'te ne yapmalıyız?"
"�?ncelikli task'leri sırala"
```

### Roadmap

```markdown
"3 aylık roadmap hazırla"
"Q1 için plan olu�?tur"
"6 aylık teknik strateji"
"Yıllık iyile�?tirme planı"
"Milestone'ları belirle"
```

### Epic & Story Breakdown

```markdown
"Epic'lere ayır"
"Story breakdown yap"
"Task hierarchy olu�?tur"
"Epic �?? Story �?? Task dönü�?ümü"
"Backlog organization yap"
```

### Effort Estimation

```markdown
"Toplam çaba tahmini ver"
"Her task için süre belirle"
"Sprint capacity planning"
"Resource allocation öner"
"Team assignment planı"
```

### �?ncelik Bazlı Planning

```markdown
"Sadece P0 için plan"
"Kritik sorunların aksiyon planı"
"Quick win task'leri planla"
"P0 ve P1 için sprint"
```

### Belirli Sorunlar İçin

```markdown
"Security sorunları için plan"
"Performance iyile�?tirme roadmap'i"
"Technical debt cleanup planı"
"Refactoring stratejisi"
```

### Açıklayıcı (No Code)

```markdown
"Plan olu�?tur ama kod yazma"
"Sadece planlama yap"
"Implementation yapmadan plan"
"Stratejik plan ver, execution yapma"
```

---

## �??? Mode 3: Full Flow (Semi-Autonomous)

**Ne yapar**: Analiz �?? Plan �?? Kod Yaz �?? Test �?? Commit  
**Kullanım**: Otomatik fix, hızlı düzeltme, batch i�?lemler  
**�?�️ DİKKAT**: Kod yazar ve dosya de�?i�?tirir!

### Genel Auto-Fix

```markdown
"P0 sorunları düzelt"
"Kritik sorunları otomatik çöz"
"Security vulnerabilities'i fix et"
"Performans sorunlarını düzelt"
"Tüm otomatik düzeltilebilir sorunları çöz"
```

### Checkpoint Control

```markdown
"P0 düzelt, ama checkpoint'lerde sor"
"Full autonomous mode, ama onayımı al"
"Otomatik düzelt, önemli noktalarda dur"
"Her adımda bana sor"
```

### Spesifik Sorun Fix

```markdown
"SQL injection'ları düzelt"
"Tüm exposed secrets'ı temizle"
"Missing authorization'ları ekle"
"N+1 query'leri optimize et"
"Bundle size'ı küçült"
"Build süresini optimize et"
```

### Scope Limited

```markdown
"Sadece OrderService.cs'i düzelt"
"Backend security sorunlarını çöz"
"Frontend performance'ı optimize et"
"Sadece bu klasörde çalı�?: src/services/"
```

### Batch Operations

```markdown
"Tüm P0 ve P1 sorunları düzelt"
"Security ve performans sorunlarını çöz"
"Frontend ve backend sorunlarını birlikte fix et"
```

### Test-Only Mode

```markdown
"Kod yaz ve test et, ama commit etme"
"Fix'leri hazırla, ben commit edece�?im"
"De�?i�?iklikleri stage'le ama push'lama"
```

### Dry-Run Mode

```markdown
"Ne yapaca�?ını göster ama de�?i�?iklik yapma"
"Simulation mode'da çalı�?"
"Kod yaz ama dosyalara dokunma"
"Preview mode"
```

### Aggressive Mode (�?�️ RİSKLİ)

```markdown
"Tüm checkpoint'leri skip et"
"Sormadan düzelt"
"Full automatic mode"
"Hiç durma, tüm sorunları çöz"
```

**�?�️ Not**: Aggressive mode'u sadece test projelerinde kullan!

---

## �??� Senaryoya Göre �?rnekler

### �??? Yeni Projeye Ba�?lama

**Senaryo**: Yeni bir projeyi devralıyorsun, ne durumda bilmiyorsun

```markdown
# Day 1: Durumu Anla (Mode 1)
"Projeyi kapsamlı analiz et"

# Day 2: Plan Yap (Mode 2)
"İlk 2 hafta için plan olu�?tur"

# Day 3-14: Fix Ba�?lat (Mode 3)
"P0 sorunları düzelt"
```

---

### �?�? Hızlı Bug Fix

**Senaryo**: Production'da kritik bug, hızlı fix gerekiyor

```markdown
# Mode 3: Direct
"SQL injection'ı hemen düzelt"
"Checkpoint'leri skip et, acil durum"
```

---

### �??? Sprint Planning Toplantısı

**Senaryo**: Haftalık sprint planning yapıyorsunuz

```markdown
# Mode 2
"Bu sprint için P0 ve P1 task breakdown yap"
"Her task için çaba tahmini ve sorumlu belirle"
"2 haftalık sprint capacity planning"
```

---

### �??� Technical Debt Sprint

**Senaryo**: 1 sprint'i technical debt temizli�?e ayırdınız

```markdown
# Mode 2 (Planning)
"Technical debt cleanup için 2 haftalık roadmap"

# Mode 3 (Execution)
"Zombie code'ları temizle"
"God file'ları parçala"
"Duplicate code'ları refactor et"
```

---

### �??? Security Audit

**Senaryo**: Güvenlik denetimi yapılacak

```markdown
# Day 1: Mode 1 (Audit)
"Comprehensive security audit"
"OWASP Top 10 kontrolü"

# Day 2: Mode 2 (Planning)
"Security sorunları için fix planı"

# Day 3-10: Mode 3 (Fix)
"Auto-fixable security sorunlarını düzelt"
"Her kritik sorun için bana sor"
```

---

### �?� Performance Optimization Sprint

**Senaryo**: Performance iyile�?tirme hedefi var

```markdown
# Mode 1 (Baseline)
"Mevcut performance metrics"
"Bottleneck'leri tespit et"

# Mode 2 (Planning)
"Performance optimization roadmap"
"Quick win'leri belirle"

# Mode 3 (Implementation)
"Bundle size'ı optimize et"
"N+1 query'leri düzelt"
"Lazy loading ekle"
```

---

### �??? Executive Review

**Senaryo**: CTO'ya proje durumu raporu sunacaksın

```markdown
# Mode 1
"Executive summary ver"
"Proje sa�?lık raporu (dashboard format)"
"Top 5 risk ve top 5 fırsat"
"Metrik trendleri göster"
```

---

### �??? Yeni �?zellik Ekleme

**Senaryo**: Yeni bir feature ekleyeceksin, impact analizi lazım

```markdown
# Mode 1 (Pre-feature)
"Mevcut mimariyi analiz et"
"Yeni feature için uygun noktaları belirle"
"Refactor edilmesi gereken alanlar"

# Mode 2 (Planning)
"Feature implementation planı"
"Hangi dosyalar de�?i�?meli?"
"Test stratejisi ne olmalı?"
```

---

### �??? Production Deploy �?ncesi

**Senaryo**: Production'a deploy öncesi son kontrol

```markdown
# Mode 1 (Pre-deploy checklist)
"Production-ready mi kontrol et"
"Security scan"
"Performance regression check"
"Breaking change var mı?"
"Rollback planı de�?erlendir"
```

---

## �???️ İleri Seviye Kombinasyonlar

### Selective Autonomous

```markdown
"Security sorunlarını otomatik düzelt, ama performance için plan olu�?tur"
�?? Mode 3 for security, Mode 2 for performance
```

### Iterative Refinement

```markdown
Step 1: "Quick scan yap" (Mode 1)
Step 2: "P0 için plan" (Mode 2)  
Step 3: "P0 düzelt" (Mode 3)
Step 4: "Sonuçları analiz et" (Mode 1)
Step 5: "P1 için plan" (Mode 2)
```

### Hybrid Control

```markdown
"Kod yaz ama her dosya de�?i�?ikli�?inde onay al"
�?? Mode 3 with granular checkpoints
```

---

## �??� Tips & Best Practices

### �?? İyi Prompt �?rnekleri

```markdown
�?? "P0 security sorunlarını düzelt"
   �?? Spesifik, net, scope belirli

�?? "Bu sprint için aksiyon planı, task'leri önceliklendir"
   �?? Hem mode hem output formatı belirtilmi�?

�?? "Sadece frontend performance analizi"
   �?? Scope sınırlı, net

�?? "OrderService.cs'i analiz et, SQL injection var mı bak"
   �?? Spesifik dosya, spesifik sorun
```

### �? Kötü Prompt �?rnekleri

```markdown
�? "Düzelt"
   �?? Ne düzeltilecek? Hangi mode?

�? "Bir �?eyler yap"
   �?? Vague, actionable de�?il

�? "Kodları oku"
   �?? Ne amaçla? Mode belirsiz

�? "Fix it"
   �?? İngilizce + vague
```

### �??� Net Olmanın �?nemi

```markdown
Vague: "Performance sorunları var"
Better: "Performance analizi yap" (Mode 1)
Best: "Performance sorunları için sprint planı" (Mode 2)
Perfect: "Bundle size ve N+1 query'leri düzelt" (Mode 3)
```

---

## �??? Mode Geçi�?leri

```markdown
# Sequential (�?nerilen)
1. "Projeyi analiz et" (Mode 1)
   �?? Durumu anla
   
2. "P0 için aksiyon planı" (Mode 2)
   �?? Planı gör
   
3. "Planı uygula" (Mode 3)
   �?? Execute

# Direct (Tecrübeliler için)
"P0 sorunları düzelt" (Mode 3 directly)
```

---

## �??? Ek Kaynaklar

- **Detaylı kullanım**: USAGE_GUIDE.md
- **Güvenlik**: SAFETY_GATES.md
- **Agent entegrasyonu**: AGENTIC_WORKFLOW.md
- **Implementation**: implementation-guides/

---

**100+ örnek, 3 mode, sınırsız kombinasyon!** �???

---

## ? �ZEL: Feature Gap Analysis (�zellik Eksikli?i Analizi)

**Yeni Mod�l!** Projenizi benzer projeler ve industry standartlar? ile kar??la?t?r?r.

### Temel Kullan?m

```markdown
"Projem i�in feature gap analysis yap"
"Eksik �zellikleri tespit et"
"Rakip analizi yap"
"Feature completeness skorunu g�ster"
"Hangi �zellikler eksik?"
```

### Proje Tipi Bazl?

```markdown
"E-ticaret projesi i�in feature gap analysis"
"SaaS dashboard �zellik kar??la?t?rmas? yap"
"Blog sitem i�in eksik �zellikler neler?"
"API projem i�in industry benchmark yap"
```

### Rakip Kar??la?t?rmas?

```markdown
"Trendyol ve Hepsiburada ile kar??la?t?r"
"Notion ile feature comparison yap"
"Rakiplerime g�re hangi �zellikleri eklemeliyim?"
"Benzer projelerde hangi �zellikler var?"
```

### �ncelik Bazl?

```markdown
"Must-have �zellikleri listele"
"Quick win feature'lar? bul"
"Kritik eksiklikler neler?"
"?lk eklemem gereken 5 �zellik"
```

### Roadmap Olu?turma

```markdown
"Feature gap'e g�re 6 ayl?k roadmap"
"Eksik �zellikleri sprint'lere b�l"
"Feature completeness i�in aksiyon plan?"
"MVP i�in hangi �zellikleri eklemeliyim?"
```

### Detayl? Analiz

```markdown
"Feature matrix olu?tur"
"Her kategori i�in eksiklikleri g�ster"
"Industry best practices ile kar??la?t?r"
"Competitive advantage i�in �neriler"
```

### Kombinasyonlar (Di?er Mod�llerle)

```markdown
"Feature gap + aksiyon plan?" (Mode 2)
? Eksiklikleri tespit et + implementation plan? olu?tur

"Feature gap + UI/UX analysis"
? Hangi UX �zelliklerinin eksik oldu?unu g�ster

"Feature gap + performance analysis"
? Eksik performans �zellikleri + mevcut performans durumu

"Full feature audit"
? Teknik kalite + �zellik eksiklikleri birlikte
```

### Sekt�r Odakl?

```markdown
"T�rk e-ticaret piyasas? i�in feature gap"
? T�rkiye'de ba?ar?l? e-ticaret �zellikleri

"SaaS startup i�in MVP feature list"
? SaaS i�in must-have �zellikler

"Fintech projesi i�in compliance features"
? Finans sekt�r� zorunlu �zellikleri
```

### �rnek Tam Prompt

```markdown
"Projemi e-ticaret kategorisinde analiz et.
Trendyol, Hepsiburada ve n11 ile kar??la?t?r.
Hangi �zellikler eksik?
Must-have ve Should-have'leri ayr? g�ster.
Quick wins varsa �ne �?kar.
3 ayl?k implementation plan? olu?tur."
```

### Beklenen �?kt?

```markdown
? Mevcut �zellikler listesi
? Eksik �zellikler (Must/Should/Could/Nice)
? Feature completeness skoru (X/100)
? Rakip kar??la?t?rma tablosu
? Quick wins (h?zl? kazan?mlar)
? Sprint bazl? aksiyon plan?
? Uzun vadeli roadmap �nerileri
```

### Mode Kombinasyonlar?

```markdown
Mode 1 (Analiz):
"Feature gap analysis yap"
? Sadece rapor ver

Mode 2 (Plan):
"Feature gap + implementation plan"
? Rapor + nas?l ekleyece?im plan?

Mode 3 (Execute):
"Feature gap'teki quick wins'i uygula"
? H?zl? eklenebilecek �zellikleri kod olarak yaz
```

---

**G�ncel: v3.3 - Feature Gap Analysis mod�l� eklendi!** ?
