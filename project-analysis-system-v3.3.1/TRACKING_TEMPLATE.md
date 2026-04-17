# Manuel Takip Şablonu

## Haftalık İlerleme (Hafta [N])

**Tarih**: [GÜN]-[GÜN] [AY] 2025

### Tamamlanan ✅

| Task ID | Görev | Sorumlu | Tamamlanma Tarihi |
|---------|-------|---------|-------------------|
| #1 | SQL injection düzelt | Ali | 15.01.2025 |
| #2 | Alt text ekle (12 görsel) | Ayşe | 16.01.2025 |

### Devam Eden 🔄

| Task ID | Görev | Sorumlu | İlerleme | Bloker? |
|---------|-------|---------|----------|---------|
| #3 | N+1 query optimize | Ali | %70 | Hayır |
| #4 | Build optimize | Mehmet | %30 | Test ortamı yok |

### Bloke Olan 🚫

| Task ID | Görev | Sorumlu | Bloker Sebep | Çözüm |
|---------|-------|---------|--------------|-------|
| #5 | Redis kurulumu | DevOps | Prod erişim yok | Ticket açıldı (#1234) |

### Sonraki Hafta Planı 📅

- [ ] #6: CORS yapılandırması (Mehmet, 1h)
- [ ] #7: Security headers (Mehmet, 1h)
- [ ] #8: Password hashing migration (Ali, 4h)

---

## Sprint Burndown

**Sprint**: Sprint 2 (Hafta 3-4)  
**Başlangıç**: 40 saat  
**Kalan**: 28 saat

```
Gün     | İdeal | Gerçek
--------|-------|--------
Pzt (1) |  36h  |  38h
Sal (2) |  32h  |  34h
Çar (3) |  28h  |  30h
Per (4) |  24h  |  28h  ← (Şu an)
Cum (5) |  20h  |  ?
Pzt (8) |  16h  |  ?
```

**Analiz**: Plandan 4 saat geride, bloker yüzünden.

---

## Sorun Takibi

### Aktif Sorunlar

| ID | Sorun | Etki | Durum | Çözüm Sahibi |
|----|-------|------|-------|--------------|
| #101 | Test ortamı down | Yüksek | Açık | DevOps |
| #102 | Code review bekliyor | Orta | Açık | Mehmet |

### Çözülen Sorunlar

| ID | Sorun | Çözüm | Çözüm Tarihi |
|----|-------|-------|--------------|
| #100 | Git conflict | Pair programming | 14.01.2025 |

---

## Metrikler

### Bu Hafta
- Tamamlanan task: 2
- Eklenen task: 1 (scope creep!)
- Velocity: 16 SP / hafta
- Bug count: 3 yeni, 5 fixed

### Trend (4 Hafta)
```
Hafta | Velocity | Bug Ratio
------|----------|----------
  1   |   12 SP  |   40%
  2   |   14 SP  |   35%
  3   |   16 SP  |   30%  ← İyileşme
  4   |   ?      |   ?
```

---

## Retrospektif Notları

### Ne İyi Gitti? 😊
- Pair programming iyi sonuç verdi
- Test coverage arttı

### Ne Daha İyi Olabilir? 🤔
- Code review daha hızlı olmalı (24h hedef)
- Bloker'lar daha erken escalate edilmeli

### Aksiyonlar
- [ ] Code review SLA: 24 saat (Takım)
- [ ] Daily stand-up'ta bloker öncelik (Scrum Master)
