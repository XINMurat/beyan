# Module: Cloud Cost Analysis

**Priority**: P3 (Maliyet Optimizasyonu)
**Tokens**: ~1500
**Analysis Time**: `terraform`, `docker-compose`, `kubernetes`, `serverless.yml` tespit edildiğinde yüklenir

---

## Purpose
Bulut altyapısı (AWS, GCP, Azure) kullanan projelerin gereksiz kaynak tüketimini, aşırı boyutlandırılmış (oversized) instance'ları ve optimize edilebilecek servis konfigürasyonlarını tespit eder.

---

## Yaygın Maliyet Tuzakları

```yaml
cost_traps:
  oversized_instances:
    description: "Geliştirme ortamında production büyüklüğünde EC2/VM instance çalışıyor."
    check: "CPU kullanımı sürekli %20 altındaysa instance küçültülmeli."
    saving_potential: "Yüksek (%30-60 maliyet düşüşü)"

  unused_resources:
    description: "Durdurulan EC2 instance'larına bağlı EBS volume'lar para tükütir."
    check: "Attach edilmemiş (unattached) EBS / Disk volume'lar var mı?"
    tool: "AWS Cost Explorer → Idle Resources"

  data_transfer_costs:
    description: "Aynı cloud içindeki servisler farklı region'daysa veri transferi ücretlendirilir."
    check: "DB ve API sunucuları aynı availability zone'da mı?"

  reserved_vs_on_demand:
    description: "Sürekli çalışan servisler için Reserved Instance, 1 yıllık commit ile %40-60 daha ucuz."
    check: "Production sunucuları hep açık ama On-Demand mı?"
```

---

## Serverless Maliyet Optimizasyonu

```yaml
serverless_optimization:
  cold_start:
    description: "Lambda/Functions uzun başlangıç süresi."
    fix: "Provisioned Concurrency ile sık kullanılan fonksiyonları sıcak tut."
  memory_right_sizing:
    description: "Lambda memory'yi yüksek tutmak CPU'yu da artırır ama maliyet katar."
    fix: "AWS Lambda Power Tuning aracı ile optimal memory boyutunu bul."
```

---

## Output Format

```markdown
## 💰 Cloud Maliyet Analiz Raporu

### Tespit Edilen Savurgan Kaynaklar
- **[Kaynak]:** [Açıklama — Tahmini aylık fazla maliyet: $X]

### Hemen Uygulanabilir Tasarruf Önerileri
1. [Öneri — Tahmini tasarruf: %X]
2. [Öneri — Tahmini tasarruf: $Y/ay]

### Uzun Vadeli Optimizasyon
- [Reserved Instance geçişi — %40 tasarruf potansiyeli]
```