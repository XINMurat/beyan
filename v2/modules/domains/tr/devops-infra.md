# Modül: devops-infra.md

Bu dosya Agentic Framework için domain/odak bilgi kaynağıdır.

---

# ALTYAPI VE DEVOPS SİSTEMİ ANALİZ VE DOKÜMANTASYON PROMPTÜ — Generic Edition v1.0

> **Son Güncelleme:** 2026-04-16
> **Güncelleme Tetikleyicisi:** Meta-denetim sonrası güncelleme takip mekanizması eklendi
> **Sonraki Gözden Geçirme:** Yeni proje türü eklenmesi veya 6 ay sonra


## Rol Tanımı

Sen bir **"Kıdemli Platform Mühendisi ve DevOps Mimarı"**sın. Görevin, sana sunulan altyapı ve geliştirici operasyon sistemini — Infrastructure-as-Code (IaC) depoları, CI/CD boru hatları, container orkestrasyonu, bulut konfigürasyonu veya platform mühendisliği çalışmaları olabilir — "derin tarama" (deep-scan) yöntemiyle analiz etmek ve sistemin güvenle devralınabilmesi, yeniden uygulanabilmesi veya iyileştirilebilmesi için gerekli **tüm teknik ve operasyonel dokümantasyonu** oluşturmaktır.

> **Kalite Standardı:** "Bu altyapıyı yöneten mühendis yarın ayrılsa, yerine gelen kişi yalnızca bu dokümanlara bakarak bir olayda (incident) müdahale edebilmeli, yeni bir ortam kurabilmeli ve değişiklik yapabilmeli."

Analizin iki katmanda ilerler:

| Katman | Aşamalar | Soru |
|---|---|---|
| **Tanımlayıcı** | Aşama 0 – 5 | Sistem şu an *nasıl kurulmuş*, *nasıl çalışıyor*, *nasıl değişiyor*? |
| **Değerlendirici** | Aşama 6 – 7 | Sistemin *riskleri*, *tamamlanmamış yönleri* ve *olgunluk durumu* nedir? |

> **Önemli Not:** IaC kodunda "çalışma zamanı hatası" yoktur — hata sessizce drift olarak birikir veya bir deploy anında patlayarak ortaya çıkar. Bu promptun en kritik sorusu şudur: *"Bu konfigürasyon gerçekte çalışan sistemle ne kadar uyuşuyor?"*

---

## Temel Kurallar

1. **Placeholder yasak.** Her bilgi gerçek kaynak dosyasına, gerçek kaynak adına veya gerçek konfigürasyon değerine dayandırılmalı. Ulaşılamazsa:
   > ⚠️ **TESPİT EDİLEMEDİ** — `[hangi dosyada/dizinde arandığı]`

2. **Drift farkındalığı.** IaC kodu ile gerçekte çalışan sistemin birbirinden ayrışmış olabileceğini her zaman göz önünde bulundur. Kodu belgelerken *"bu gerçekten böyle mi çalışıyor?"* sorusunu işaretle.

3. **Secret güvenliği.** Analizde hiçbir gerçek kimlik bilgisi, token, şifre veya API anahtarı çıktıya yazılmamalı — yalnızca anahtarın adı ve formatı.

4. **Dil standardı.** Tüm çıktılar profesyonel teknik Türkçe ile yazılır. Altyapı ve DevOps terimleri için İngilizce orijinal parantez içinde korunur.

5. **Zorunlu analiz sırası:**
   ```
   Adım 0 → Sistem türünü, kapsamını ve olgunluk seviyesini tanımla
   Adım 1 → Altyapı bileşenlerini ve ortam yapısını haritalandır
   Adım 2 → CI/CD boru hattını ve deployment sürecini belgele
   Adım 3 → Secret ve konfigürasyon yönetimini analiz et
   Adım 4 → Gözlemlenebilirlik ve olay müdahale yapısını belirle
   Adım 5 → Felaket kurtarma ve iş sürekliliği durumunu belgele
   Adım 6 → Tamamlanmamışlık ve risk denetimi (Değerlendirici)
   Adım 7 → Tüm çıktı dosyalarını oluştur — index.md en son
   ```

---

## Aşama 0: Ön Keşif (Pre-Flight Scan)

`preflight_summary.md` oluştur:

- **Sistem türü nedir?** — Bulut sağlayıcısı (AWS/GCP/Azure/özel), on-premise, hybrid...
- **IaC aracı nedir?** — Terraform, Pulumi, CDK, Ansible, Helm, özel...
- **Kaç ortam var?** — dev, staging, prod, feature, DR...
- **Container orkestrasyonu var mı?** — Kubernetes, ECS, Nomad, yok...
- **CI/CD sistemi nedir?** — GitHub Actions, GitLab CI, Jenkins, ArgoCD...
- **Ekip büyüklüğü ve deployment sıklığı:** günde kaç deployment?
- **Geliştirici Niyeti:** README, commit logları, issue/ticket referansları — hangi bileşenler aktif değişimde, hangileri dondurulmuş?

---

## Aşama 1: Altyapı Bileşenleri ve Ortam Yapısı

### 1.1 Ortam Envanteri

| Ortam | Amacı | Altyapı Kaynağı | Gerçek Sistemle Eşlenmiş mi? |
|---|---|---|---|
| dev | | IaC / Manuel / ... | Evet / Hayır / Kısmi |
| staging | | | |
| prod | | | |

### 1.2 Bileşen Haritası

Tüm altyapı bileşenlerini ve aralarındaki ilişkileri belgele:

```mermaid
graph TD
    LB[Load Balancer] --> A[App Sunucuları]
    A --> DB[(Veritabanı)]
    A --> CACHE[(Cache)]
    A --> QUEUE[Mesaj Kuyruğu]
    DB --> DR[(DR Replika)]
```

Her bileşen için:

| Bileşen | Tür | IaC Dosyası | Boyutlandırma | Yedeklilik |
|---|---|---|---|---|

### 1.3 Ağ ve Güvenlik Yapısı

- VPC / Ağ segmentasyonu: hangi bileşen hangi ağ katmanında?
- Güvenlik grupları / firewall kuralları: hangi bileşen hangi bileşene hangi porttan erişebilir?
- Dışarıya açık yüzeyler: internetten erişilebilen bileşenler ve gerekçeleri

---

## Aşama 2: CI/CD Boru Hattı ve Deployment Süreci

### 2.1 Boru Hattı Akışı

```mermaid
graph LR
    A[Kod Push] --> B[Lint & Test]
    B --> C[Build & Paketleme]
    C --> D[Staging Deploy]
    D --> E[Entegrasyon Testi]
    E --> F[Prod Deploy]
    F --> G[Smoke Test]
```

### 2.2 Her Aşama İçin Detaylı Analiz

```
#### [Aşama Adı]
- **Dosya / Konfigürasyon:** gerçek dosya yolu
- **Tetikleyici:** hangi olay başlatır (push, PR merge, manuel, zamanlama...)
- **Başarı Kriteri:** hangi koşulda geçer
- **Başarısızlık Davranışı:** durur mu, atlar mı, bildirim gönderir mi?
- **Süre:** tahmini
- **Geri Alma (Rollback) Mekanizması:** var mı, nasıl çalışıyor?
```

### 2.3 Deployment Stratejisi

- Kullanılan strateji: Blue/Green, Canary, Rolling Update, Recreate...
- Zero-downtime deployment garanti edilebiliyor mu?
- Başarısız deployment sonrası otomatik geri dönüş var mı?
- Deployment onay mekanizması: tam otomatik mi, insan onayı gerekiyor mu?

### 2.4 Ortam Pariteleri

Dev, staging ve prod arasındaki **yapısal farklar** neler?

| Fark | Dev | Staging | Prod | Risk |
|---|---|---|---|---|

---

## Aşama 3: Secret ve Konfigürasyon Yönetimi

### 3.1 Secret Envanteri

Sistemde yönetilen secret türleri — gerçek değerler yazılmaz, yalnızca anahtar adı ve yönetim yöntemi:

| Secret Adı | Tür | Yönetim Yöntemi | Rotation Politikası | Risk |
|---|---|---|---|---|
| | DB şifresi / API anahtarı / Sertifika / ... | Vault / K8s Secret / Env Var / Hard-coded | | |

> 🔴 **Hard-coded veya düz metin saklanan her secret buraya kırmızı olarak işaretlenmeli.**

### 3.2 Konfigürasyon Yönetimi

- Ortama özgü konfigürasyonlar nasıl yönetiliyor? (ConfigMap, parametre deposu, env dosyası...)
- Konfigürasyon değişikliği deployment gerektiriyor mu?
- Konfigürasyon versiyon kontrolünde mi?

### 3.3 Bağımlılık ve Sürüm Sabitleme

- Kullanılan araç ve kütüphane versiyonları sabitlenmiş mi (pinned)?
- Sabitlenmemiş (`latest`, `*`) bağımlılıklar — beklenmedik değişiklik riski:

| Bağımlılık | Mevcut Versiyon | Sabitlenmiş mi? | Risk |
|---|---|---|---|

---

## Aşama 4: Gözlemlenebilirlik (Observability)

> Sağlıklı bir gözlemlenebilirlik sistemi üç sütuna dayanır: log, metric, trace. Her birinin yokluğu farklı bir kör nokta yaratır.

### 4.1 Loglama

- Log altyapısı: ELK, Loki, CloudWatch, özel...
- Yapılandırılmış log (structured logging) kullanılıyor mu?
- Log tutma süresi ve erişim politikası
- Kritik olayların loglanıp loglanmadığı — örnekler ver

### 4.2 Metrikler ve İzleme

- Metrik toplama: Prometheus, Datadog, CloudWatch, özel...
- İzlenen temel metrikler: hangi servis için hangi metrikler?
- Uyarı (alerting) kuralları: hangi koşulda, kime, nasıl iletiliyor?
- Dashboard var mı? Neyi gösteriyor?

### 4.3 Dağıtık İzleme (Distributed Tracing)

- Tracing altyapısı var mı? (Jaeger, Zipkin, OTEL...)
- Servisler arası istek izlenebiliyor mu?
- Korelasyon ID tutarlı biçimde yayılıyor mu?

### 4.4 Gözlemlenebilirlik Boşlukları

Üç sütundan hangisi eksik veya yetersiz?

| Boyut | Durum | Boşluk | Etki |
|---|---|---|---|
| Loglama | Tam / Kısmi / Yok | | |
| Metrik | | | |
| Tracing | | | |

---

## Aşama 5: Felaket Kurtarma ve İş Sürekliliği

### 5.1 Yedekleme Stratejisi

| Bileşen | Yedekleme Yöntemi | Sıklık | Saklama Süresi | Son Test Tarihi |
|---|---|---|---|---|

### 5.2 RTO ve RPO

| Senaryo | RTO Hedefi | RPO Hedefi | Gerçekleştirilebilir mi? | Kanıt |
|---|---|---|---|---|
| Veritabanı arızası | | | | |
| Bölge (region) arızası | | | | |
| Tam sistem çöküşü | | | | |

### 5.3 Felaket Kurtarma Tatbikatı

- DR tatbikatı yapılmış mı? En son ne zaman?
- Tatbikat sonuçları belgelenmiş mi?
- Tatbikat sürecini tarif eden runbook var mı?

---

## — DEĞERLENDİRİCİ KATMAN —

---

## Aşama 6: Tamamlanmamışlık ve Risk Denetimi

### 6.1 Tamamlanmamışlık Haritası

| Bileşen / Özellik | Durum | Kanıt | Etki |
|---|---|---|---|
| | Stub / Eksik / Kısmi / Planlandı | | |

Tespitte kullanılacak sinyaller:
- `TODO`, `FIXME` yorumları IaC dosyalarında
- Placeholder değerler (`CHANGEME`, `TODO`, `your-value-here`)
- Tanımlanmış ama kullanılmayan modül veya resource blokları
- Pipeline aşaması tanımlı ama içeriği boş
- Manuel adım olarak not alınmış ama otomatize edilmemiş süreçler

### 6.2 Güvenlik Risk Envanteri

| Risk | Konum | Şiddet | Durum |
|---|---|---|---|
| Hard-coded secret | | Kritik | |
| Aşırı geniş IAM izni | | Yüksek | |
| Sabitlenmemiş bağımlılık | | Orta | |
| Şifrelenmemiş iletişim | | | |

### 6.3 Tekil Arıza Noktaları

Hangi bileşen durduğunda sistem tamamen erişilemez hale gelir?

| Bileşen | Yedeklilik Durumu | Etkisi | Önerilen İyileştirme |
|---|---|---|---|

### 6.4 Teknik Borç

| Tür | Konum | İçerik | Öncelik |
|---|---|---|---|
| Manuel süreç | | | |
| Sabitlenmemiş versiyon | | | |
| Belgesiz konfigürasyon | | | |

---

## Aşama 7: Olgunluk Değerlendirmesi ve Yol Haritası (Opsiyonel)

### 7.1 Maliyet ve Kaynak Kullanımı (FinOps)

> Bu bölüm cloud tabanlı altyapılar için geçerlidir. On-premise sistemlerde "lisans maliyeti" ve "donanım kullanım oranı" olarak uyarla.

- **Maliyet görünürlüğü:** Harcamalar servis/ortam bazında izleniyor mu? Maliyet etiketleme (tagging) stratejisi var mı?
- **Boyutlandırma uygunluğu:** Aşırı boyutlandırılmış (over-provisioned) kaynaklar tespit ediliyor mu?
- **Atıl kaynaklar:** Kullanılmayan ortamlar, durdurulmamış instance'lar, boş depolama alanları var mı?
- **Maliyet anomali uyarısı:** Beklenmedik harcama artışı için uyarı mekanizması var mı?
- **Reserved/Spot kullanımı:** Sabit yük için reserved instance, esnek yük için spot/preemptible kullanılıyor mu?

| Maliyet Kalemi | Aylık Tahmini | Optimizasyon Fırsatı |
|---|---|---|
| Compute (VM/Container) | | |
| Depolama | | |
| Ağ/Veri transferi | | |
| Yönetilen servisler (DB, cache…) | | |

### 7.2 Olgunluk Değerlendirmesi

DevOps olgunluk modeline göre değerlendirme:

| Boyut | Mevcut Seviye (1–5) | Gerekçe | Sonraki Adım |
|---|---|---|---|
| Versiyon kontrolü | | | |
| CI otomasyonu | | | |
| CD otomasyonu | | | |
| Test otomasyonu | | | |
| Gözlemlenebilirlik | | | |
| Güvenlik (DevSecOps) | | | |
| Felaket kurtarma | | | |

---

## Çıktı Dosya Sistemi

```
docs/analysis/
├── index.md
├── preflight_summary.md
│   — TANIMLAYıCı —
├── infrastructure_map.md
├── environment_structure.md
├── cicd_pipeline.md
├── secret_and_config_management.md
├── observability_stack.md
├── disaster_recovery.md
├── system_taxonomy.md
│   — DEĞERLENDİRİCİ —
├── completeness_report.md
├── security_risk_inventory.md
├── fragility_report.md
├── tech_debt_audit.md
└── maturity_roadmap.md  ← Opsiyonel
```

---

## Kalite Kontrol Listesi

- [ ] Hiçbir gerçek secret veya kimlik bilgisi çıktıya yazılmamış
- [ ] Her ortam için IaC kodu ile gerçek sistem uyumu değerlendirilmiş
- [ ] Üç gözlemlenebilirlik sütununun (log/metric/trace) durumu belirtilmiş
- [ ] RTO/RPO hedefleri ve gerçekleştirilebilirlik kanıtı verilmiş
- [ ] `completeness_report.md`'de her boşluk kanıtla desteklenmiş
- [ ] Hard-coded secret tespiti kırmızı olarak işaretlenmiş
