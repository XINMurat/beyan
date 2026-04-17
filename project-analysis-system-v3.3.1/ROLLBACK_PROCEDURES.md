# Rollback (Geri Alma) Prosedürleri

## Ne Zaman Rollback Yapılır?

- ✅ Production'da kritik hata
- ✅ Performans ciddi düştü
- ✅ Kullanıcılar etkilendi
- ✅ Data corruption riski

❌ Minor bug'lar için rollback yapma, hotfix yap!

---

## 1. Kod Rollback

### Git ile Rollback

```bash
# Son commit'i geri al
git revert HEAD
git push origin main

# Belirli commit'e geri dön
git revert abc123
git push origin main

# Acil durum: Force reset (DİKKAT!)
git reset --hard HEAD~1
git push origin main --force
```

### CI/CD ile Rollback

```bash
# GitHub Actions: Previous version'a deploy
gh workflow run deploy.yml -f version=previous

# Veya tag'e geri dön
git checkout v1.2.3
# Yeniden deploy
```

---

## 2. Database Rollback

### Migration Geri Alma

```bash
# Son migration'ı geri al
dotnet ef database update PreviousMigration

# Belirli migration'a geri dön
dotnet ef database update AddIndexCustomerId
```

### Manuel Rollback

```sql
-- Önce backup'tan restore et
pg_restore -d production_db backup.sql

-- VEYA sadece son değişikliği geri al
DROP INDEX IX_Orders_CustomerId;
```

---

## 3. Rollback Checklist

### Deploy Öncesi
- [ ] Backup alındı
- [ ] Rollback planı hazır
- [ ] Test edildi (staging)
- [ ] Takım bilgilendirildi

### Rollback Sırasında
- [ ] Kullanıcılara bildirim gönder
- [ ] Monitoring'i izle
- [ ] Rollback adımlarını dokümante et
- [ ] Root cause'u belirle

### Rollback Sonrası
- [ ] Sistem normal çalışıyor
- [ ] Smoke test geçti
- [ ] Postmortem yap
- [ ] Fix planla

---

## 4. Rollback Stratejileri

### A) Blue-Green Deployment

```yaml
# Instant rollback
# Blue (old): %0 traffic
# Green (new): %100 traffic

# Sorun çıkarsa:
# Blue: %100 traffic (geri dön)
# Green: %0 traffic
```

**Avantaj**: Instant rollback (30 saniye)

### B) Canary Deployment

```yaml
# Kademeli deploy
# v1.0: %90 traffic
# v1.1: %10 traffic

# Sorun çıkarsa:
# v1.1'i durdur, herkesi v1.0'a yönlendir
```

**Avantaj**: Sorun erken tespit

### C) Feature Flag

```typescript
// Feature flag ile rollback
if (featureFlags.newCheckout) {
  return <NewCheckout />;
} else {
  return <OldCheckout />;  // Geri dön
}
```

**Avantaj**: Kod değişikliği yok, hızlı

---

## 5. Acil Durum Senaryoları

### Senaryo 1: Database Migration Başarısız

**Sorun**: Migration yarıda kaldı, production down.

**Çözüm**:
```bash
# 1. Backup'tan restore
pg_restore -d production_db backup.sql

# 2. Migration'ı fix et
# 3. Test et (staging)
# 4. Tekrar dene
```

---

### Senaryo 2: Memory Leak, Sistem Yavaşladı

**Sorun**: Yeni kod memory leak yapıyor.

**Çözüm**:
```bash
# 1. Hızlı rollback (önceki version)
git revert HEAD
git push

# 2. Redeploy
npm run deploy

# 3. Monitoring'i izle
# 4. Memory usage düşmeli
```

---

### Senaryo 3: API Breaking Change

**Sorun**: Frontend hata veriyor, API değişikliği yüzünden.

**Çözüm**:
```bash
# Option A: Rollback (hızlı)
git revert abc123

# Option B: Hotfix (daha iyi)
# Backward compatible hale getir
# Eski API'yi destekle
```

---

### Senaryo 4: Data Corruption

**Sorun**: Migration veri bozdu.

**Çözüm**:
```bash
# 1. Hemen production'ı readonly'e al
# 2. Backup'tan restore
# 3. Data fix script'i yaz
# 4. Test et
# 5. Production'a uygula
```

---

## 6. Postmortem Template

### Olay Özeti
- **Tarih**: [TARİH]
- **Süre**: [DAKIKA] downtime
- **Etki**: [KULLANıCI SAYISI] kullanıcı
- **Root Cause**: [SEBEP]

### Timeline
- 14:00 - Deploy başladı
- 14:05 - Error rate arttı
- 14:10 - Rollback kararı
- 14:15 - Rollback tamamlandı
- 14:20 - Sistem normal

### Ne İyi Gitti?
- Hızlı tespit (5 dakika)
- Rollback planı hazırdı

### Ne Daha İyi Olabilir?
- Staging'de tespit edilmeliydi
- Canary deploy kullanmalıyız

### Aksiyonlar
- [ ] Integration test ekle
- [ ] Canary deployment kur
- [ ] Monitoring alert'leri iyileştir

---

## 7. Rollback Komutları (Hızlı Referans)

```bash
# Git rollback
git revert HEAD && git push

# Docker rollback
docker pull myapp:previous
docker-compose up -d

# Kubernetes rollback
kubectl rollout undo deployment/myapp

# Database rollback
dotnet ef database update PreviousMigration

# Feature flag toggle
curl -X POST api.com/feature-flags/newCheckout/disable

# Traffic routing (nginx)
# Yük dengeleyiciyi eski version'a yönlendir
```

---

**Acil Durum İletişim**:
- DevOps: [TELEFON]
- Backend Lead: [TELEFON]
- CTO: [TELEFON]

**Postmortem**: Her rollback sonrası zorunlu!
