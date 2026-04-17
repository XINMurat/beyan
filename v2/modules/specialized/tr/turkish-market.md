# Module: Türkiye Pazarı ve Mevzuat Uyumu

**Priority**: P2 (Yerel Mevzuat ve Pazar)
**Tokens**: ~1500
**Analysis Time**: `turkish`, `turkey`, `kvkk`, `tr` anahtar sözcükleri veya Türkçe proje tespitinde yüklenir

---

## Purpose
Türkiye'de yayınlanan yazılım ürünlerinin KVKK, BTK gereklilikleri, e-ticaret kanunu ve yerel ödeme sistemi entegrasyonlarına uyumluluğunu denetler. Yalnızca teknik kaliteyi değil, yasal riski de ölçer.

---

## KVKK Uyumluluk Kontrolleri

Kişisel Verilerin Korunması Kanunu (KVKK), Türkiye'de faaliyet gösteren tüm yazılımlar için zorunludur.

```yaml
kvkk_checks:
  acik_riza:
    description: "Kullanıcının kişisel verilerini işlemek için açık rızası alınıyor mu?"
    check: "Kayıt formunda veya ilk girişte KVKK onay checkbox'ı mevcut mu?"
  veri_silme:
    description: "Kullanıcı 'Hesabımı Sil' diyebiliyor mu? Veriler sistemden tamamen siliniyor mu?"
    check: "Soft delete yerine KVKK kapsamında hard delete veya anonymize mekanizması var mı?"
  veri_isleme_envanter:
    description: "Hangi kişisel veri, hangi amaçla, ne kadar süre saklanıyor?"
    check: "Privacy Policy / Gizlilik Politikası dokümantasyonu güncel mi?"
  yurt_disi:
    description: "Kişisel veriler yurt dışındaki sunuculara (AWS, GCP, vb.) taşınıyor mu?"
    check: "KVKK 9. Madde kapsamında yurt dışı transfer için yeterli koruma önlemi var mı?"
```

---

## BTK ve E-Ticaret Kanunu Gereklilikleri

*   **E-Ticaret:** Elektronik Ticaretin Düzenlenmesi Hakkında Kanun uyarınca satıcı bilgileri (unvan, adres, vergi no) her sayfada görünür olmalıdır.
*   **Uzaktan Satış Sözleşmesi:** Kullanıcıya ön bilgilendirme formu sunulmalı ve kopyası e-posta ile iletilmelidir.
*   **BTK Bildirimi:** Belirli eşiğin üzerinde kullanıcıya sahip uygulamalar BTK'ya bildirim yapmak zorundadır.

---

## Türk Ödeme Sistemleri

```yaml
payment_systems:
  iyzico:
    security: "3D Secure v2 zorunlu mu? PCI-DSS uyumlu API çağrısı yapılıyor mu?"
    check: "Test/Production API key ayrımı doğru yapılmış mı?"
  paytr:
    security: "Hash doğrulaması (HMAC) server-side mı yapılıyor?"
    check: "Merchant Secret, istemci tarafında (client-side) açık mı?"
  bddk_uyumu:
    description: "Finansal işlemler BDDK denetimine tabi mi? PCI-DSS sertifikasyonu gerekiyor mu?"
```

---

## Yerel Teknik Gereklilikler

*   **Türkçe Karakter Encoding:** Veritabanı ve API yanıtlarının `utf-8` veya `utf-8mb4` (MySQL) kullandığından emin olun.
*   **Türkçe Tarih/Para Formatı:** `31.12.2024` (gün.ay.yıl) ve `₺1.234,56` (nokta binlik, virgül ondalık) formatları kullanılıyor mu?
*   **E-Fatura / E-Arşiv (GİB):** Fatura kesen platformlar GİB entegrasyonu gerektiriyor mu? Logo, Mikro veya QNB Finansbank fintech API'leri entegre mi?
*   **KEP (Kayıtlı Elektronik Posta):** Hukuki bağlayıcı bildirimler için KEP altyapısı gerekiyor mu?

---

## Scoring

```yaml
scoring:
  excellent: "KVKK tam uyumlu, 3D Secure zorunlu, e-fatura entegre, Türkçe format doğru."
  good: "Temel KVKK uyumu var, ödeme sistemi güvenli ancak veri silme mekanizması eksik."
  attention: "KVKK onay checkbox'ı var ama veri envanteri ve silme hakkı uygulanmamış."
  critical: "Kişisel veri açık rıza alınmadan işleniyor, 3D Secure yok, merchant secret client'ta açık."
```

---

## Output Format

```markdown
## 🇹🇷 Türkiye Pazarı Uyumluluk Raporu

### KVKK Değerlendirmesi
- **Açık Rıza:** [Var / Yok]
- **Veri Silme Hakkı:** [Uygulanmış / Eksik]
- **Yurt Dışı Transfer:** [Risk Var / Güvenli]

### Ödeme Sistemi Güvenliği
- **3D Secure:** [Zorunlu / İsteğe Bağlı / Yok]
- **Secret Key Güvenliği:** [Server-side / CLIENT'TA AÇIK - KRİTİK]

### Yerel Teknik Uyum
- **Encoding:** [utf-8 / Sorunlu]
- **E-Fatura:** [Entegre / Gerekli ama Yok]
```
