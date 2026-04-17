# Aksiyon PlanÄ± Åžablonu

**Tarih**: [TARÄ°H]  
**Proje**: [PROJE ADI]  
**HazÄ±rlayan**: [ADINIZ]  
**Onaylayan**: [ONAYLAYAN]

---

## ðŸ“Š Genel Durum

**Analiz Tarihi**: [TARÄ°H]  
**Genel Proje Skoru**: [SKOR]/10  
**Toplam Bulunan Sorun**: [SAYI]  
**Toplam Tahmini Ã‡aba**: [SAAT]

---

## ðŸŽ¯ Ã–ncelik Matrisi

### ðŸ”´ P0 - Kritik (Hemen YapÄ±lmalÄ± - Bu Hafta)

**Toplam Ã‡aba**: [SAAT] saat

| # | Sorun | Ã‡Ã¶zÃ¼m | Sorumlu | SÃ¼re | Durum | Tarih |
|---|-------|-------|---------|------|-------|-------|
| 1 | SQL Injection (OrderService.cs) | Parameterized query'ye geÃ§ | Ali | 2h | â¬œ BaÅŸlamadÄ± | - |
| 2 | Exposed secrets (.env in Git) | Rotate secrets, .gitignore ekle | AyÅŸe | 1h | â¬œ BaÅŸlamadÄ± | - |
| 3 | Missing authorization (AdminController) | [Authorize] attribute ekle | Mehmet | 30m | â¬œ BaÅŸlamadÄ± | - |

**Toplam**: 3 kritik sorun

---

### ðŸŸ¡ P1 - YÃ¼ksek (Bu Sprint - 2 Hafta)

**Toplam Ã‡aba**: [SAAT] saat

| # | Sorun | Ã‡Ã¶zÃ¼m | Sorumlu | SÃ¼re | Durum | Tarih |
|---|-------|-------|---------|------|-------|-------|
| 4 | N+1 Query (Orders endpoint) | Eager loading ekle | Ali | 1h | â¬œ BaÅŸlamadÄ± | - |
| 5 | Vulnerable dependencies (12 pkg) | npm audit fix | AyÅŸe | 2h | â¬œ BaÅŸlamadÄ± | - |
| 6 | CORS AllowAnyOrigin | Specific origins ekle | Mehmet | 1h | â¬œ BaÅŸlamadÄ± | - |
| 7 | Build sÃ¼resi Ã§ok uzun (85s) | TypeScript incremental compile | Ahmet | 30m | â¬œ BaÅŸlamadÄ± | - |
| 8 | Weak password hashing (SHA256) | Bcrypt'e geÃ§ + migration | Ali | 4h | â¬œ BaÅŸlamadÄ± | - |

**Toplam**: 5 yÃ¼ksek Ã¶ncelikli sorun

---

### ðŸŸ¢ P2 - Orta (Bu Ay - 4 Hafta)

**Toplam Ã‡aba**: [SAAT] saat

| # | Sorun | Ã‡Ã¶zÃ¼m | Sorumlu | SÃ¼re | Durum | Tarih |
|---|-------|-------|---------|------|-------|-------|
| 9 | Eksik alt text (12 gÃ¶rsel) | Alt text yaz | Fatma | 1h | â¬œ BaÅŸlamadÄ± | - |
| 10 | Renk kontrastÄ± (8 yer) | Renkleri dÃ¼zelt | Zeynep | 2h | â¬œ BaÅŸlamadÄ± | - |
| 11 | Missing security headers | Header middleware ekle | Mehmet | 1h | â¬œ BaÅŸlamadÄ± | - |
| 12 | Zombie code (1,200 satÄ±r) | Sil veya ship | TakÄ±m | 6h | â¬œ BaÅŸlamadÄ± | - |

**Toplam**: 4 orta Ã¶ncelikli sorun

---

### â¬œ P3 - DÃ¼ÅŸÃ¼k (3 Ay Ä°Ã§inde)

**Toplam Ã‡aba**: [SAAT] saat

| # | Ä°yileÅŸtirme | AÃ§Ä±klama | Sorumlu | SÃ¼re | Durum | Tarih |
|---|-------------|----------|---------|------|-------|-------|
| 13 | SEO meta tags | 8 sayfaya meta ekle | Elif | 2h | â¬œ BaÅŸlamadÄ± | - |
| 14 | PWA Ã¶zellikleri | Service worker ekle | Can | 8h | â¬œ BaÅŸlamadÄ± | - |
| 15 | Documentation | Architecture doc yaz | TakÄ±m | 4h | â¬œ BaÅŸlamadÄ± | - |

**Toplam**: 3 dÃ¼ÅŸÃ¼k Ã¶ncelikli iyileÅŸtirme

---

## ðŸ“… Sprint PlanÄ±

### Sprint 1 (Hafta 1)

**Hedef**: P0 sorunlarÄ± Ã§Ã¶z  
**Toplam Ã‡aba**: [SAAT] saat

**GÃ¶revler**:
- [ ] Task #1: SQL Injection dÃ¼zelt (Ali, 2h)
- [ ] Task #2: Secrets rotate et (AyÅŸe, 1h)
- [ ] Task #3: Authorization ekle (Mehmet, 30m)
- [ ] Code review (TakÄ±m, 1h)
- [ ] Test & Deploy (1h)

**BaÅŸarÄ± Kriterleri**:
- [ ] Security scan temiz geÃ§iyor
- [ ] TÃ¼m testler geÃ§iyor
- [ ] Production'da sorunsuz Ã§alÄ±ÅŸÄ±yor

---

### Sprint 2 (Hafta 2)

**Hedef**: P1 sorunlarÄ± Ã§Ã¶z  
**Toplam Ã‡aba**: [SAAT] saat

**GÃ¶revler**:
- [ ] Task #4: N+1 query dÃ¼zelt (Ali, 1h)
- [ ] Task #5: Dependencies gÃ¼ncelle (AyÅŸe, 2h)
- [ ] Task #6: CORS yapÄ±landÄ±rmasÄ± (Mehmet, 1h)
- [ ] Task #7: Build optimize (Ahmet, 30m)
- [ ] Task #8: Password hashing migration (Ali, 4h)
- [ ] Code review (TakÄ±m, 2h)
- [ ] Test & Deploy (1h)

**BaÅŸarÄ± Kriterleri**:
- [ ] API response time <100ms
- [ ] Build sÃ¼resi <30s
- [ ] Zero critical dependencies

---

### Sprint 3-4 (Hafta 3-4)

**Hedef**: P2 iyileÅŸtirmeler  
**Toplam Ã‡aba**: [SAAT] saat

**GÃ¶revler**:
- [ ] Accessibility fixes (Fatma & Zeynep, 3h)
- [ ] Security headers (Mehmet, 1h)
- [ ] Zombie code cleanup (TakÄ±m, 6h)
- [ ] Code review (2h)
- [ ] Test & Deploy (1h)

**BaÅŸarÄ± Kriterleri**:
- [ ] WCAG AA compliance >90%
- [ ] Codebase -1,200 lines (cleanup)
- [ ] All security headers present

---

## ðŸ“ˆ Ä°lerleme Takibi

### HaftalÄ±k Durum (Hafta [N])

**Tarih**: [TARÄ°H]

**Tamamlanan**:
- âœ… [GÃ¶rev adÄ±] (Sorumlu, [TARÄ°H])
- âœ… [GÃ¶rev adÄ±] (Sorumlu, [TARÄ°H])

**Devam Eden**:
- ðŸ”„ [GÃ¶rev adÄ±] (Sorumlu, %[Ä°LERLEME])

**Bloke Olan**:
- ðŸš« [GÃ¶rev adÄ±] (Sebep: [AÃ‡IKLAMA])

**Sonraki Hafta PlanÄ±**:
- [ ] [GÃ¶rev adÄ±]
- [ ] [GÃ¶rev adÄ±]

**Risk ve Sorunlar**:
- âš ï¸ [Risk aÃ§Ä±klamasÄ±]

---

## ðŸŽ¯ Kilometre TaÅŸlarÄ± (Milestones)

### Milestone 1: GÃ¼venlik Kritik SorunlarÄ± Ã‡Ã¶zÃ¼ldÃ¼
**Hedef Tarih**: [TARÄ°H]  
**Durum**: â¬œ BaÅŸlamadÄ±

**Gereksinimler**:
- [ ] TÃ¼m P0 security issues Ã§Ã¶zÃ¼ldÃ¼
- [ ] Security audit temiz geÃ§ti
- [ ] Production'da deploy edildi

---

### Milestone 2: Performance Ä°yileÅŸtirmeleri
**Hedef Tarih**: [TARÄ°H]  
**Durum**: â¬œ BaÅŸlamadÄ±

**Gereksinimler**:
- [ ] Build sÃ¼resi <30s
- [ ] API response time <100ms
- [ ] Bundle size <200KB

---

### Milestone 3: EriÅŸilebilirlik AA StandardÄ±
**Hedef Tarih**: [TARÄ°H]  
**Durum**: â¬œ BaÅŸlamadÄ±

**Gereksinimler**:
- [ ] WCAG AA compliance >90%
- [ ] Axe scan temiz
- [ ] Keyboard navigation Ã§alÄ±ÅŸÄ±yor

---

## ðŸ‘¥ Kaynaklar (TakÄ±m)

| KiÅŸi | Rol | HaftalÄ±k Kapasite | Atanan GÃ¶revler |
|------|-----|-------------------|-----------------|
| Ali | Backend Dev | 40h | #1, #4, #8 |
| AyÅŸe | Security | 30h | #2, #5 |
| Mehmet | Full Stack | 40h | #3, #6, #11 |
| Ahmet | DevOps | 20h | #7 |
| Fatma | Frontend | 30h | #9 |
| Zeynep | UI/UX | 20h | #10 |

**Toplam HaftalÄ±k Kapasite**: [SAAT] saat

---

## ðŸ’° Maliyet & ROI

### Maliyet Tahmini

| Kategori | Ã‡aba (saat) | Saat Ãœcreti | Toplam |
|----------|-------------|-------------|--------|
| P0 (Kritik) | [SAAT] | [TL]/saat | [TOPLAM] TL |
| P1 (YÃ¼ksek) | [SAAT] | [TL]/saat | [TOPLAM] TL |
| P2 (Orta) | [SAAT] | [TL]/saat | [TOPLAM] TL |
| **TOPLAM** | **[SAAT]** | - | **[TOPLAM] TL** |

### Beklenen Fayda (ROI)

| Ä°yileÅŸtirme | Ã–lÃ§Ã¼lebilir Fayda |
|-------------|------------------|
| Security fixes | Risk azaltma: %90, potansiyel kayÄ±p: [TUTAR] TL |
| Performance | KullanÄ±cÄ± kaybÄ± Ã¶nleme: %20 daha az bounce |
| Build optimize | Developer productivity: 78 saat/yÄ±l tasarruf |
| **Toplam Fayda** | **[TUTAR] TL/yÄ±l** |

**ROI**: [ORAN]% (Ä°lk [AY] ayda geri dÃ¶nÃ¼ÅŸ)

---

## ðŸ“‹ ToplantÄ±lar & Checkpoint'ler

### HaftalÄ±k Stand-up
**Ne zaman**: Her Pazartesi 10:00  
**Kim**: TÃ¼m takÄ±m  
**GÃ¼ndem**:
- GeÃ§en hafta tamamlanan
- Bu hafta planlanan
- Blokerlar

### Sprint Review
**Ne zaman**: Her 2 haftada bir Cuma 15:00  
**Kim**: TakÄ±m + Stakeholder'lar  
**GÃ¼ndem**:
- Demo (tamamlanan Ã¶zellikler)
- Metrikler (skor deÄŸiÅŸimi)
- Sonraki sprint planÄ±

### Retrospektif
**Ne zaman**: Sprint bitiminde  
**Kim**: TakÄ±m  
**GÃ¼ndem**:
- Ne iyi gitti?
- Ne daha iyi olabilir?
- Aksiyonlar

---

## ðŸš¨ Risk YÃ¶netimi

### Potansiyel Riskler

| Risk | OlasÄ±lÄ±k | Etki | Ã–nleme | Sorumlu |
|------|----------|------|--------|---------|
| Migration sÄ±rasÄ±nda data loss | Orta | YÃ¼ksek | Backup + dry-run test | Ali |
| Production'da downtime | DÃ¼ÅŸÃ¼k | Kritik | Blue-green deployment | Ahmet |
| TakÄ±m Ã¼yesi hasta/izinli | Orta | Orta | Pair programming, bilgi paylaÅŸÄ±mÄ± | Herkes |
| Scope creep (yeni istekler) | YÃ¼ksek | Orta | Change control process | Proje MÃ¼dÃ¼rÃ¼ |

---

## âœ… Checklist: Her GÃ¶rev Ä°Ã§in

Bir gÃ¶rev "tamamlandÄ±" demek iÃ§in:

- [ ] Kod yazÄ±ldÄ±
- [ ] Unit test yazÄ±ldÄ±
- [ ] Integration test geÃ§ti
- [ ] Code review yapÄ±ldÄ± (en az 1 kiÅŸi)
- [ ] Security check yapÄ±ldÄ± (eÄŸer gÃ¼venlik ile ilgili)
- [ ] Documentation gÃ¼ncellendi
- [ ] Staging'de test edildi
- [ ] Production'a deploy edildi
- [ ] Smoke test geÃ§ti
- [ ] Monitoring alert'leri kontrol edildi

---

## ðŸ“ Notlar

### Ã–ÄŸrenilen Dersler
- [Ders 1]
- [Ders 2]

### Ä°yileÅŸtirme Fikirleri
- [Fikir 1]
- [Fikir 2]

### Referanslar
- [Link 1: Ä°lgili dokÃ¼mantasyon]
- [Link 2: Benzer proje Ã¶rneÄŸi]

---

## ðŸ”„ Versiyon GeÃ§miÅŸi

| Versiyon | Tarih | DeÄŸiÅŸiklik | HazÄ±rlayan |
|----------|-------|------------|------------|
| 1.0 | [TARÄ°H] | Ä°lk oluÅŸturma | [Ä°SÄ°M] |
| 1.1 | [TARÄ°H] | Sprint 1 tamamlandÄ±, Sprint 2 gÃ¼ncellendi | [Ä°SÄ°M] |

---

**Son GÃ¼ncelleme**: [TARÄ°H]  
**Sonraki GÃ¶zden GeÃ§irme**: [TARÄ°H]
