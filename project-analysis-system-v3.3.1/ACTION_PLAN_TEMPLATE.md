# Aksiyon Planı �?ablonu

**Tarih**: [TARİH]  
**Proje**: [PROJE ADI]  
**Hazırlayan**: [ADINIZ]  
**Onaylayan**: [ONAYLAYAN]

---

## �??? Genel Durum

**Analiz Tarihi**: [TARİH]  
**Genel Proje Skoru**: [SKOR]/10  
**Toplam Bulunan Sorun**: [SAYI]  
**Toplam Tahmini �?aba**: [SAAT]

---

## �??� �?ncelik Matrisi

### �??� P0 - Kritik (Hemen Yapılmalı - Bu Hafta)

**Toplam �?aba**: [SAAT] saat

| # | Sorun | �?özüm | Sorumlu | Süre | Durum | Tarih |
|---|-------|-------|---------|------|-------|-------|
| 1 | SQL Injection (OrderService.cs) | Parameterized query'ye geç | Ali | 2h | �? Ba�?lamadı | - |
| 2 | Exposed secrets (.env in Git) | Rotate secrets, .gitignore ekle | Ay�?e | 1h | �? Ba�?lamadı | - |
| 3 | Missing authorization (AdminController) | [Authorize] attribute ekle | Mehmet | 30m | �? Ba�?lamadı | - |

**Toplam**: 3 kritik sorun

---

### �??� P1 - Yüksek (Bu Sprint - 2 Hafta)

**Toplam �?aba**: [SAAT] saat

| # | Sorun | �?özüm | Sorumlu | Süre | Durum | Tarih |
|---|-------|-------|---------|------|-------|-------|
| 4 | N+1 Query (Orders endpoint) | Eager loading ekle | Ali | 1h | �? Ba�?lamadı | - |
| 5 | Vulnerable dependencies (12 pkg) | npm audit fix | Ay�?e | 2h | �? Ba�?lamadı | - |
| 6 | CORS AllowAnyOrigin | Specific origins ekle | Mehmet | 1h | �? Ba�?lamadı | - |
| 7 | Build süresi çok uzun (85s) | TypeScript incremental compile | Ahmet | 30m | �? Ba�?lamadı | - |
| 8 | Weak password hashing (SHA256) | Bcrypt'e geç + migration | Ali | 4h | �? Ba�?lamadı | - |

**Toplam**: 5 yüksek öncelikli sorun

---

### �??� P2 - Orta (Bu Ay - 4 Hafta)

**Toplam �?aba**: [SAAT] saat

| # | Sorun | �?özüm | Sorumlu | Süre | Durum | Tarih |
|---|-------|-------|---------|------|-------|-------|
| 9 | Eksik alt text (12 görsel) | Alt text yaz | Fatma | 1h | �? Ba�?lamadı | - |
| 10 | Renk kontrastı (8 yer) | Renkleri düzelt | Zeynep | 2h | �? Ba�?lamadı | - |
| 11 | Missing security headers | Header middleware ekle | Mehmet | 1h | �? Ba�?lamadı | - |
| 12 | Zombie code (1,200 satır) | Sil veya ship | Takım | 6h | �? Ba�?lamadı | - |

**Toplam**: 4 orta öncelikli sorun

---

### �? P3 - Dü�?ük (3 Ay İçinde)

**Toplam �?aba**: [SAAT] saat

| # | İyile�?tirme | Açıklama | Sorumlu | Süre | Durum | Tarih |
|---|-------------|----------|---------|------|-------|-------|
| 13 | SEO meta tags | 8 sayfaya meta ekle | Elif | 2h | �? Ba�?lamadı | - |
| 14 | PWA özellikleri | Service worker ekle | Can | 8h | �? Ba�?lamadı | - |
| 15 | Documentation | Architecture doc yaz | Takım | 4h | �? Ba�?lamadı | - |

**Toplam**: 3 dü�?ük öncelikli iyile�?tirme

---

## �??? Sprint Planı

### Sprint 1 (Hafta 1)

**Hedef**: P0 sorunları çöz  
**Toplam �?aba**: [SAAT] saat

**Görevler**:
- [ ] Task #1: SQL Injection düzelt (Ali, 2h)
- [ ] Task #2: Secrets rotate et (Ay�?e, 1h)
- [ ] Task #3: Authorization ekle (Mehmet, 30m)
- [ ] Code review (Takım, 1h)
- [ ] Test & Deploy (1h)

**Ba�?arı Kriterleri**:
- [ ] Security scan temiz geçiyor
- [ ] Tüm testler geçiyor
- [ ] Production'da sorunsuz çalı�?ıyor

---

### Sprint 2 (Hafta 2)

**Hedef**: P1 sorunları çöz  
**Toplam �?aba**: [SAAT] saat

**Görevler**:
- [ ] Task #4: N+1 query düzelt (Ali, 1h)
- [ ] Task #5: Dependencies güncelle (Ay�?e, 2h)
- [ ] Task #6: CORS yapılandırması (Mehmet, 1h)
- [ ] Task #7: Build optimize (Ahmet, 30m)
- [ ] Task #8: Password hashing migration (Ali, 4h)
- [ ] Code review (Takım, 2h)
- [ ] Test & Deploy (1h)

**Ba�?arı Kriterleri**:
- [ ] API response time <100ms
- [ ] Build süresi <30s
- [ ] Zero critical dependencies

---

### Sprint 3-4 (Hafta 3-4)

**Hedef**: P2 iyile�?tirmeler  
**Toplam �?aba**: [SAAT] saat

**Görevler**:
- [ ] Accessibility fixes (Fatma & Zeynep, 3h)
- [ ] Security headers (Mehmet, 1h)
- [ ] Zombie code cleanup (Takım, 6h)
- [ ] Code review (2h)
- [ ] Test & Deploy (1h)

**Ba�?arı Kriterleri**:
- [ ] WCAG AA compliance >90%
- [ ] Codebase -1,200 lines (cleanup)
- [ ] All security headers present

---

## �??? İlerleme Takibi

### Haftalık Durum (Hafta [N])

**Tarih**: [TARİH]

**Tamamlanan**:
- �?? [Görev adı] (Sorumlu, [TARİH])
- �?? [Görev adı] (Sorumlu, [TARİH])

**Devam Eden**:
- �??? [Görev adı] (Sorumlu, %[İLERLEME])

**Bloke Olan**:
- �??� [Görev adı] (Sebep: [A�?IKLAMA])

**Sonraki Hafta Planı**:
- [ ] [Görev adı]
- [ ] [Görev adı]

**Risk ve Sorunlar**:
- �?�️ [Risk açıklaması]

---

## �??� Kilometre Ta�?ları (Milestones)

### Milestone 1: Güvenlik Kritik Sorunları �?özüldü
**Hedef Tarih**: [TARİH]  
**Durum**: �? Ba�?lamadı

**Gereksinimler**:
- [ ] Tüm P0 security issues çözüldü
- [ ] Security audit temiz geçti
- [ ] Production'da deploy edildi

---

### Milestone 2: Performance İyile�?tirmeleri
**Hedef Tarih**: [TARİH]  
**Durum**: �? Ba�?lamadı

**Gereksinimler**:
- [ ] Build süresi <30s
- [ ] API response time <100ms
- [ ] Bundle size <200KB

---

### Milestone 3: Eri�?ilebilirlik AA Standardı
**Hedef Tarih**: [TARİH]  
**Durum**: �? Ba�?lamadı

**Gereksinimler**:
- [ ] WCAG AA compliance >90%
- [ ] Axe scan temiz
- [ ] Keyboard navigation çalı�?ıyor

---

## �??� Kaynaklar (Takım)

| Ki�?i | Rol | Haftalık Kapasite | Atanan Görevler |
|------|-----|-------------------|-----------------|
| Ali | Backend Dev | 40h | #1, #4, #8 |
| Ay�?e | Security | 30h | #2, #5 |
| Mehmet | Full Stack | 40h | #3, #6, #11 |
| Ahmet | DevOps | 20h | #7 |
| Fatma | Frontend | 30h | #9 |
| Zeynep | UI/UX | 20h | #10 |

**Toplam Haftalık Kapasite**: [SAAT] saat

---

## �??� Maliyet & ROI

### Maliyet Tahmini

| Kategori | �?aba (saat) | Saat �?creti | Toplam |
|----------|-------------|-------------|--------|
| P0 (Kritik) | [SAAT] | [TL]/saat | [TOPLAM] TL |
| P1 (Yüksek) | [SAAT] | [TL]/saat | [TOPLAM] TL |
| P2 (Orta) | [SAAT] | [TL]/saat | [TOPLAM] TL |
| **TOPLAM** | **[SAAT]** | - | **[TOPLAM] TL** |

### Beklenen Fayda (ROI)

| İyile�?tirme | �?lçülebilir Fayda |
|-------------|------------------|
| Security fixes | Risk azaltma: %90, potansiyel kayıp: [TUTAR] TL |
| Performance | Kullanıcı kaybı önleme: %20 daha az bounce |
| Build optimize | Developer productivity: 78 saat/yıl tasarruf |
| **Toplam Fayda** | **[TUTAR] TL/yıl** |

**ROI**: [ORAN]% (İlk [AY] ayda geri dönü�?)

---

## �??? Toplantılar & Checkpoint'ler

### Haftalık Stand-up
**Ne zaman**: Her Pazartesi 10:00  
**Kim**: Tüm takım  
**Gündem**:
- Geçen hafta tamamlanan
- Bu hafta planlanan
- Blokerlar

### Sprint Review
**Ne zaman**: Her 2 haftada bir Cuma 15:00  
**Kim**: Takım + Stakeholder'lar  
**Gündem**:
- Demo (tamamlanan özellikler)
- Metrikler (skor de�?i�?imi)
- Sonraki sprint planı

### Retrospektif
**Ne zaman**: Sprint bitiminde  
**Kim**: Takım  
**Gündem**:
- Ne iyi gitti?
- Ne daha iyi olabilir?
- Aksiyonlar

---

## �??� Risk Yönetimi

### Potansiyel Riskler

| Risk | Olasılık | Etki | �?nleme | Sorumlu |
|------|----------|------|--------|---------|
| Migration sırasında data loss | Orta | Yüksek | Backup + dry-run test | Ali |
| Production'da downtime | Dü�?ük | Kritik | Blue-green deployment | Ahmet |
| Takım üyesi hasta/izinli | Orta | Orta | Pair programming, bilgi payla�?ımı | Herkes |
| Scope creep (yeni istekler) | Yüksek | Orta | Change control process | Proje Müdürü |

---

## �?? Checklist: Her Görev İçin

Bir görev "tamamlandı" demek için:

- [ ] Kod yazıldı
- [ ] Unit test yazıldı
- [ ] Integration test geçti
- [ ] Code review yapıldı (en az 1 ki�?i)
- [ ] Security check yapıldı (e�?er güvenlik ile ilgili)
- [ ] Documentation güncellendi
- [ ] Staging'de test edildi
- [ ] Production'a deploy edildi
- [ ] Smoke test geçti
- [ ] Monitoring alert'leri kontrol edildi

---

## �??� Notlar

### �?�?renilen Dersler
- [Ders 1]
- [Ders 2]

### İyile�?tirme Fikirleri
- [Fikir 1]
- [Fikir 2]

### Referanslar
- [Link 1: İlgili dokümantasyon]
- [Link 2: Benzer proje örne�?i]

---

## �??? Versiyon Geçmi�?i

| Versiyon | Tarih | De�?i�?iklik | Hazırlayan |
|----------|-------|------------|------------|
| 1.0 | [TARİH] | İlk olu�?turma | [İSİM] |
| 1.1 | [TARİH] | Sprint 1 tamamlandı, Sprint 2 güncellendi | [İSİM] |

---

**Son Güncelleme**: [TARİH]  
**Sonraki Gözden Geçirme**: [TARİH]
