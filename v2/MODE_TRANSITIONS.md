# Beyan v2.0 — Mode Geçişleri ve Kullanım Senaryoları

Bu doküman, sistemin 3 çalışma modunu, aralarındaki geçişleri ve hangi senaryoda hangisini kullanmanız gerektiğini açıklar.

---

## Mode 1 — Analiz (Analysis)

**Ne yapar?** Projeyi tarar, modülleri yükler, analiz raporunu üretir. Koda dokunmaz.

**Ne zaman kullanılır?**
- Yeni bir projeye bakmaya başlıyorsunuz (ilk keşif).
- Code review öncesinde hızlı kalite kontrolü.
- Teknik borç envanteri çıkarmak istiyorsunuz.
- Bir projeyi başkasına devretmeden önce durum tespiti.

```bash
python cli/analyzer.py --target /path/to/project --mode 1 --lang tr --api anthropic
```

**Çıktı:** `beyan_analysis_result.md` — P0→P3 öncelikli bulgular, skor tablosu, aksiyon önerileri.

---

## Mode 2 — Plan (Planning)

**Ne yapar?** Mode 1'in bulgularını alır ve her bulgu için somut bir `implementation_plan.md` yazar. Önce sizden onay bekler.

**Ne zaman kullanılır?**
- Mode 1'den çıkan P0/P1 sorunlarını bir sprint planına dönüştürmek istiyorsunuz.
- Teknik borç çalışması için kapsamlı bir yol haritası gerekiyor.
- Ekibinize ne yapılacağını net olarak göstermek istiyorsunuz.

```bash
python cli/analyzer.py --target /path/to/project --mode 2 --lang tr --api anthropic
```

**Çıktı:** `implementation_plan.md` — Her bulgu için: Dosya, satır, ne değiştirilmeli, tahmini efor.

---

## Mode 3 — Agentic Fix (Pilot)

**Ne yapar?** Mode 2'nin planını uygular. Her değişiklik öncesinde "Checkpoint" mekanizması ile onay ister, onaylananları bizzat kodlar.

**Ne zaman kullanılır?**
- Kritik P0/P1 bulgularının hızlı kapatılması.
- Test suite genişletme.
- Güvenlik yamaları.

> [!IMPORTANT]
> Mode 3 yarı-otonomdur. Her adımda insan onayı (Human-in-the-loop) zorunludur.

---

## Mode Geçiş Senaryoları

### Senaryo A: Yeni Proje Keşfi
```
Mode 1 → Raporu oku → Kritik bulgular varsa → Mode 2 → Planı onayla → Mode 3 (Dikkatli)
```

### Senaryo B: Düzenli Sağlık Kontrolü (Sprint Başı)
```
Mode 1 → Skoru önceki sprint ile karşılaştır → Regresyon varsa alarm
```

### Senaryo C: Teknik Borç Sprint'i
```
Mode 1 → Mode 2 (Tüm P1/P2'ler için plan) → İnsan onayı → Sprint'e al
```

### Senaryo D: Hızlı Güvenlik Denetimi
```
Mode 1 (sadece security_analysis modülü) → P0 bulgu varsa → Acil → Mode 2 → Uygula
```

---

Her mode geçişinde sistem bir `checkpoint` dosyası yazmayı önerir (veya bellek modülünde tutar). Bu sayede konuşma uzadığında veya context sıfırlandığında kaldığınız yerden devam edebilirsiniz:

1. **Analiz Onayı:** P0 bulgular ve düzeltme stratejisi onayı.
2. **Kod Onayı:** Değişiklik diff'i (❌ Eski vs ✅ Yeni) onayı.
3. **Süreç Onayı:** Commit/Branch onayı.
