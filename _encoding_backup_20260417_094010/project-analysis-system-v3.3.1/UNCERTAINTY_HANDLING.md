# Uncertainty Handling - Belirsizlik YÃ¶netimi

**Module**: AI Validation Layer  
**Priority**: P0 (Critical)  
**Version**: 1.0  
**Last Updated**: 20 AralÄ±k 2024

---

## ðŸŽ¯ AmaÃ§

AI sisteminin **ne bilmediÄŸini bilmesi** ve belirsizliÄŸi aÃ§Ä±kÃ§a ifade etmesi. Hallucination'Ä±n Ã§oÄŸu, sistemin emin olmadÄ±ÄŸÄ± ÅŸeylerde aÅŸÄ±rÄ± gÃ¼venli konuÅŸmasÄ±ndan gelir.

**Prensip**: "Bilmiyorum" demek, yanlÄ±ÅŸ bilgi vermekten iyidir.

---

## ðŸ“Š Belirsizlik Seviyeleri

### Level 1: Kesin Bilgi âœ…
```yaml
confidence: 95-100%
indicator: "Kesin olarak tespit edildi"
action: Direct statement
example: "SQL injection gÃ¼venlik aÃ§Ä±ÄŸÄ± var (OrderService.cs:45)"
```

### Level 2: YÃ¼ksek OlasÄ±lÄ±k ðŸŸ¢
```yaml
confidence: 75-94%
indicator: "BÃ¼yÃ¼k olasÄ±lÄ±kla"
action: State with caveat
example: "N+1 query sorunu olabilir (eager loading eksik gÃ¶rÃ¼nÃ¼yor)"
```

### Level 3: Orta Belirsizlik ðŸŸ¡
```yaml
confidence: 50-74%
indicator: "Potansiyel olarak"
action: Suggest investigation
example: "Bundle size yÃ¼ksek olabilir, production build'ini analiz etmek gerekir"
```

### Level 4: DÃ¼ÅŸÃ¼k GÃ¼ven ðŸŸ 
```yaml
confidence: 25-49%
indicator: "Tam emin deÄŸilim ama"
action: Mark as speculation
example: "God class pattern'i olabilir, ancak business domain analizi gerekli"
```

### Level 5: Bilinmiyor âŒ
```yaml
confidence: 0-24%
indicator: "Bu konuda yeterli bilgim yok"
action: Recommend expert consultation
example: "Performans hedefleriniz hakkÄ±nda bilgi sahibi deÄŸilim, belirtebilir misiniz?"
```

---

## ðŸ” Belirsizlik KaynaklarÄ±

### 1. Eksik BaÄŸlam
```markdown
âŒ HatalÄ±: "Bu API yavaÅŸ"
âœ… DoÄŸru: "Bu API 500ms'de cevap veriyor. Kabul edilebilir bir sÃ¼re mi, 
           performans hedeflerinize baÄŸlÄ± - belirtebilir misiniz?"

Neden: "YavaÅŸ" subjektif, hedef SLA bilinmiyor
Belirsizlik: High
Aksiyon: KullanÄ±cÄ±dan context iste
```

### 2. GÃ¶rÃ¼nmez FaktÃ¶rler
```markdown
âŒ HatalÄ±: "Test coverage %78, bu yeterli"
âœ… DoÄŸru: "Test coverage %78. Industry standard %80, ancak critical 
           path'leriniz hangileri bilmiyorum - bunlar test edilmiÅŸse yeterli olabilir"

Neden: Hangi kod kritik bilinmiyor
Belirsizlik: Medium
Aksiyon: Qualify the statement
```

### 3. Teknik SÄ±nÄ±rlamalar
```markdown
âŒ HatalÄ±: "Database migration sorunsuz Ã§alÄ±ÅŸÄ±r"
âœ… DoÄŸru: "Migration script doÄŸru gÃ¶rÃ¼nÃ¼yor ANCAK production data 
           hacmini bilmiyorum. BÃ¼yÃ¼k tablolarda lock riski olabilir - 
           Ã¶nce staging'de test edilmeli"

Neden: Production scale bilinmiyor
Belirsizlik: High
Aksiyon: Risk disclaimer + recommendation
```

### 4. Domain Bilgisi EksikliÄŸi
```markdown
âŒ HatalÄ±: "Bu fonksiyon gereksiz, silin"
âœ… DoÄŸru: "Bu fonksiyon gÃ¶rÃ¼nÃ¼rde kullanÄ±lmÄ±yor, ancak business logic'i 
           tam bilmiyorum. GerÃ§ekten gereksizse silinebilir - domain 
           expert'e danÄ±ÅŸÄ±n"

Neden: Business context eksik
Belirsizlik: Very High
Aksiyon: Recommend domain expert review
```

---

## ðŸ“ Ä°fade ÅžablonlarÄ±

### Kesin Bulgu
```
"[SORUN] tespit edildi"
"Kesin olarak [X] durumu var"
"[METRIC] Ã¶lÃ§Ã¼ldÃ¼: [VALUE]"
```

### YÃ¼ksek OlasÄ±lÄ±k
```
"BÃ¼yÃ¼k olasÄ±lÄ±kla [SORUN]"
"[X] pattern'i gÃ¶rÃ¼nÃ¼yor"
"[Y] olmasÄ± muhtemel"
```

### Orta Belirsizlik
```
"Potansiyel olarak [SORUN]"
"[X] olabilir"
"Daha fazla analiz gerekli: [Y]"
```

### DÃ¼ÅŸÃ¼k GÃ¼ven
```
"Tam emin deÄŸilim ama [X] olabilir"
"[Y] hakkÄ±nda yeterli bilgi yok"
"[Z]'yi varsayÄ±yorum, doÄŸru mu?"
```

### Bilinmiyor
```
"Bu konuda bilgim yok"
"[X] hakkÄ±nda veri eksik"
"Domain expert danÄ±ÅŸmanÄ±zÄ± Ã¶neririm"
```

---

## ðŸŽ¯ Kontrol Listesi: Her Ã–neri Ä°Ã§in

Bir Ã¶neri yapmadan Ã¶nce:

- [ ] **KanÄ±t var mÄ±?** (kod, metrik, log)
- [ ] **BaÄŸlam yeterli mi?** (business context, requirements)
- [ ] **VarsayÄ±mlar neler?** (aÃ§Ä±kÃ§a belirt)
- [ ] **Confidence level nedir?** (0-100%)
- [ ] **YanlÄ±ÅŸsam etkisi ne?** (risk assessment)

EÄŸer 5'inden biri net deÄŸilse â†’ **BelirsizliÄŸi belirt**

---

## ðŸš¨ Anti-Patterns (YAPMA!)

### âŒ Anti-Pattern 1: AÅŸÄ±rÄ± GÃ¼venlenen Tahmin
```markdown
BAD: "Bu god class, mutlaka 3 ayrÄ± class'a bÃ¶lÃ¼n"

GOOD: "Bu class 800+ satÄ±r ve 15 farklÄ± sorumluluk var. 
       Tipik god class pattern'i. ANCAK domain logic'i bilmiyorum -
       nasÄ±l bÃ¶lÃ¼neceÄŸi business context'e baÄŸlÄ±. 
       Domain expert ile beraber refactor planÄ± yapÄ±lmalÄ±."
```

### âŒ Anti-Pattern 2: BelirsizliÄŸi Gizleme
```markdown
BAD: "Performans sorunlarÄ± var" (hangi metrik, ne kadar kÃ¶tÃ¼, kabul edilebilir mi?)

GOOD: "LCP 4.2s (hedef <2.5s iÃ§in yavaÅŸ). Ancak sizin performans 
       SLA'nÄ±zÄ± bilmiyorum - bu kabul edilebilir mi belirtin lÃ¼tfen."
```

### âŒ Anti-Pattern 3: VarsayÄ±mlarÄ± Gizli Tutma
```markdown
BAD: "Database index ekleyin"

GOOD: "Orders tablosunda CustomerId'ye index yok, bu N+1 soruna yol aÃ§abilir.
       ANCAK tablo boyutunu bilmiyorum - bÃ¼yÃ¼k tabloda (>10M rows) CONCURRENT 
       index gerekir, kÃ¼Ã§Ã¼k tabloda direkt eklenebilir."
```

### âŒ Anti-Pattern 4: Binary Cevap Zorla
```markdown
BAD: "Bu kod kÃ¶tÃ¼, yeniden yazÄ±n"

GOOD: "Bu kod ÅŸu problemleri iÃ§eriyor: [liste]
       Yeniden yazmak mÄ± yoksa refactor mu daha iyi?
       Bu kod ne kadar kritik, team bandwidth'iniz ne kadar - bunlara baÄŸlÄ±."
```

---

## ðŸ’¡ Pratik Ã–rnekler

### Ã–rnek 1: Test Coverage
```markdown
ðŸ“Š Analiz:
Test coverage: 78%

âŒ KÃ¶tÃ¼ Rapor:
"Test coverage dÃ¼ÅŸÃ¼k, %80'e Ã§Ä±karÄ±n"

âœ… Ä°yi Rapor:
"Test coverage %78 (industry standard ~%80)
 
Belirsizlik: 
- Hangi kod kritik path, bilmiyorum
- Bu %78'in iÃ§inde kritik fonksiyonlar test edilmiÅŸse yeterli olabilir
- EÄŸer kritik kod test edilmemiÅŸse, %78 yanÄ±ltÄ±cÄ± olabilir

Ã–neri:
1. Critical path'leri belirleyin
2. OnlarÄ±n coverage'Ä±nÄ± ayrÄ±ca Ã¶lÃ§Ã¼n
3. O %100 ise, genel %78 kabul edilebilir"
```

### Ã–rnek 2: API Performance
```markdown
ðŸ“Š Analiz:
GET /api/orders â†’ 450ms average

âŒ KÃ¶tÃ¼ Rapor:
"API yavaÅŸ, optimize edin"

âœ… Ä°yi Rapor:
"GET /api/orders â†’ 450ms average response time

Belirsizlik:
- Sizin SLA hedefleriniz nedir? (bilinmiyor)
- Bu endpoint ne kadar kritik? (bilinmiyor)
- N+1 query var gibi gÃ¶rÃ¼nÃ¼yor (%75 confidence - profiling gerekli)

Context sorgularÄ±:
1. Kabul edilebilir response time nedir?
2. Bu endpoint gÃ¼nde kaÃ§ kere Ã§aÄŸrÄ±lÄ±yor?
3. Kritik kullanÄ±cÄ± flow'unda mÄ±?

EÄŸer:
- SLA <200ms ise â†’ Kritik problem âœ… Mutlaka fix
- SLA <1s ise â†’ Ä°yileÅŸtirilebilir ðŸŸ¡ P2
- Nadiren kullanÄ±lÄ±yor ise â†’ DÃ¼ÅŸÃ¼k Ã¶ncelik ðŸŸ¢ P3"
```

### Ã–rnek 3: Architecture Decision
```markdown
ðŸ“Š Analiz:
Monolith structure (tek repo, 85K LOC)

âŒ KÃ¶tÃ¼ Rapor:
"Microservices'e geÃ§in"

âœ… Ä°yi Rapor:
"Mevcut: Monolith (85K LOC)

Belirsizlik:
- Team size? (bilinmiyor)
- Deployment frequency? (bilinmiyor)  
- Domain boundaries? (net deÄŸil)
- Ops expertise? (bilinmiyor)

Monolithìž¥ì :
- Tek deployment (basit)
- Tek codebase (kolay search)
- Local development (hÄ±zlÄ±)

Microservicesìž¥ì :
- Independent scaling
- Team autonomy
- Technology diversity

Karar iÃ§in gerekli:
1. Team >20 kiÅŸi mi? â†’ Microservices dÃ¼ÅŸÃ¼nÃ¼lebilir
2. FarklÄ± scale ihtiyaÃ§larÄ± var mÄ±? â†’ Microservices
3. Ops ekibi K8s deneyimli mi? â†’ Yoksa monolith devam

Ã–nerim:
Åžimdilik monolith iÃ§inde modularity artÄ±rÄ±n (hexagonal architecture),
gerektiÄŸinde extraction daha kolay olur"
```

---

## ðŸ”„ Belirsizlik Azaltma AkÄ±ÅŸÄ±

```mermaid
graph TD
    A[Ã–neri yapacaksÄ±n] --> B{Yeterli bilgi var mÄ±?}
    B -->|Evet| C[Confidence %95+]
    B -->|HayÄ±r| D{VarsayÄ±mla devam edilir mi?}
    
    D -->|Evet| E[VarsayÄ±mÄ± aÃ§Ä±kla]
    D -->|HayÄ±r| F[KullanÄ±cÄ±dan bilgi iste]
    
    C --> G[Kesin ifade kullan]
    E --> H[BelirsizliÄŸi belirt]
    F --> I[Soru sor]
    
    G --> J[Ã–neriyi yaz]
    H --> J
    I --> K[Cevap bekle]
    K --> A
```

---

## ðŸ“Š Belirsizlik MetriÄŸi (Her Raporda)

```markdown
## ðŸŽ¯ Rapor GÃ¼venilirlik Ã–zeti

**Kesin Bulgular**: 15 Ã¶neri (confidence >90%)
**YÃ¼ksek OlasÄ±lÄ±k**: 8 Ã¶neri (confidence 75-90%)
**VarsayÄ±mlarla**: 4 Ã¶neri (confidence 50-75%)
**Belirsiz**: 2 Ã¶neri (daha fazla bilgi gerekli)

**Toplam GÃ¼venilirlik**: 83% (weighted average)

**VarsayÄ±mlar listesi**:
1. Production SLA <500ms (belirtilmedi)
2. Critical path: Login â†’ Dashboard (varsayÄ±m)
3. Team size <10 kiÅŸi (repository'den tahmin)
```

---

## ðŸŽ“ EÄŸitim: BelirsizliÄŸi Fark Et

### Quiz: Hangi ifade daha iyi?

**Soru 1**:
- A) "Bu kod kÃ¶tÃ¼, yeniden yaz"
- B) "Bu kod ÅŸu sorunlarÄ± iÃ§eriyor: [X,Y,Z]. Business context'i bilmiyorum, yeniden yazmak mÄ± refactor mu daha iyi domain expert'e sorun"

**Cevap**: B âœ… (Belirsizlik aÃ§Ä±k, seÃ§im kullanÄ±cÄ±da)

**Soru 2**:
- A) "Test coverage %78, yeterli"
- B) "Test coverage %78. Industry standard ~%80, ancak kritik path'leriniz test edilmiÅŸse kabul edilebilir"

**Cevap**: B âœ… (Context eksikliÄŸi belirtilmiÅŸ)

**Soru 3**:
- A) "API 450ms, yavaÅŸ"
- B) "API 450ms. SLA hedefleriniz nedir? <200ms ise kritik, <1s ise kabul edilebilir olabilir"

**Cevap**: B âœ… (Subjektif yargÄ± vermemiÅŸ, context sormuÅŸ)

---

## ðŸ›¡ï¸ Hallucination Ã–nleme Checklist

Bir rapor yazmadan Ã¶nce:

### âœ… Do (Yap)
- [ ] KanÄ±tÄ± gÃ¶ster (dosya:satÄ±r, metrik, log)
- [ ] VarsayÄ±mlarÄ± listele
- [ ] Confidence level belirt
- [ ] Alternative scenarios dÃ¼ÅŸÃ¼n
- [ ] "Bilmiyorum" de (gerÃ§ekten bilmiyorsan)
- [ ] KullanÄ±cÄ±dan eksik bilgiyi iste
- [ ] Risk seviyesini belirt

### âŒ Don't (Yapma)
- [ ] Kesin konuÅŸ (emin deÄŸilsen)
- [ ] VarsayÄ±mlarÄ± gizle
- [ ] Binary choice zorla
- [ ] Domain expert olmadan mimari karar ver
- [ ] Subjektif ifadeler (yavaÅŸ, kÃ¶tÃ¼, karmaÅŸÄ±k) - Ã¶lÃ§Ã¼lebilir metrikler kullan
- [ ] Speculation'Ä± fact gibi sun
- [ ] Worst-case'i default gibi gÃ¶ster

---

## ðŸ’¬ Ä°fade DÃ¶nÃ¼ÅŸÃ¼mleri

### DÃ¶nÃ¼ÅŸÃ¼m 1: Kesin â†’ Qualified
```
Ã–nce: "Bu gÃ¼venlik aÃ§Ä±ÄŸÄ±"
Sonra: "Bu SQL injection pattern'i gÃ¼venlik riski taÅŸÄ±yor (parameterized query eksik)"
```

### DÃ¶nÃ¼ÅŸÃ¼m 2: Subjektif â†’ Objective
```
Ã–nce: "Kod karmaÅŸÄ±k"
Sonra: "Cyclomatic complexity 45 (threshold 10). Fonksiyon 280 satÄ±r (Ã¶nerilen <50)"
```

### DÃ¶nÃ¼ÅŸÃ¼m 3: VarsayÄ±m â†’ AÃ§Ä±k
```
Ã–nce: "Database migrasyonu kolay"
Sonra: "Migration script doÄŸru gÃ¶rÃ¼nÃ¼yor. Ancak production data hacmini bilmiyorum - 
        kÃ¼Ã§Ã¼k tablolarda (<100K rows) sorunsuz, bÃ¼yÃ¼k tablolarda lock riski var"
```

### DÃ¶nÃ¼ÅŸÃ¼m 4: Binary â†’ Spectrum
```
Ã–nce: "Microservices'e geÃ§"
Sonra: "Monolith vs Microservices tradeoff:
        - Team <10: Monolith devam
        - Team >20: Microservices dÃ¼ÅŸÃ¼nÃ¼lebilir
        - Sizin team size'Ä±nÄ±z nedir?"
```

---

## ðŸŽ¯ BaÅŸarÄ± Kriterleri

Belirsizlik yÃ¶netimi baÅŸarÄ±lÄ± ise:

### Metrikler
- [ ] Her raporda confidence distribution var
- [ ] VarsayÄ±mlar aÃ§Ä±kÃ§a listeleniyor
- [ ] "Bilmiyorum" ifadeleri var (uygun yerlerde)
- [ ] KullanÄ±cÄ± follow-up sorularÄ± soruyor (iyi iÅŸaret!)
- [ ] False positive rate dÃ¼ÅŸÃ¼k (<5%)

### KullanÄ±cÄ± Feedback
- [ ] "Rapor ÅŸeffaf"
- [ ] "Nerelerde emin olmadÄ±ÄŸÄ±nÄ±z belli"
- [ ] "KararÄ± bana bÄ±rakÄ±yorsunuz, iyi"
- [ ] "Overconfident deÄŸil"

### Anti-Metrik (Bunlar KÃ–TÃœ)
- [ ] %100 confidence everywhere (gerÃ§ekÃ§i deÄŸil)
- [ ] HiÃ§ "bilmiyorum" yok (tehlikeli)
- [ ] TÃ¼m Ã¶neriler kesin (hallucination riski)
- [ ] KullanÄ±cÄ± soru sormuyor (engagement dÃ¼ÅŸÃ¼k)

---

## ðŸ“š Referanslar

### Ä°lgili ModÃ¼ller
- `CONFIDENCE_SCORING.md` - Skorlama sistemi
- `FACT_CHECKING_RULES.md` - DoÄŸrulama kurallarÄ±
- `AI_VALIDATION_LAYER.md` - Genel validation

### Best Practices
- Humble AI: "I don't know" is better than hallucination
- Transparent assumptions
- User empowerment (let them decide)
- Measurable over subjective

---

**Ã–zet**: BelirsizliÄŸi saklamak deÄŸil, aÃ§Ä±kÃ§a ifade etmek gÃ¼ven oluÅŸturur. ðŸŽ¯

---

**Version**: 1.0  
**Next Review**: v3.3 release  
**Feedback**: KullanÄ±cÄ± belirsizlik ifadelerini nasÄ±l karÅŸÄ±lÄ±yor, tracking yapÄ±lmalÄ±
