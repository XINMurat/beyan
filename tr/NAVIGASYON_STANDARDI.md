# PROMPT AİLESİ — NAVİGASYON VE DİZİN STANDARDI

> **Son Güncelleme:** 2026-04-16
> **Kapsam:** Birden fazla prompt çalıştırıldığında çıktıların nasıl organize edileceği

---

## Çıktı Dizini Referans Kartı

Her prompt kendi alt dizinine yazar. Aynı projede birden fazla prompt çalıştırıldığında bu dizinler aynı proje klasörü altında yan yana durur:

| Prompt | Çıktı Dizini |
|---|---|
| `master_proje_analiz_promptu_v2.3` | `docs/analysis/` |
| `os_analiz_promptu_generic_v1.0` | `docs/analysis/` |
| `research_ai_analiz_promptu_generic_v1.0` | `docs/analysis/` |
| `veri_analitik_analiz_promptu_v1.0` | `docs/analysis/` |
| `altyapi_devops_analiz_promptu_v1.0` | `docs/analysis/` |
| `guvenlik_denetim_promptu_v1.0` | `docs/security-audit/` |
| `api_tasarim_denetim_promptu_v1.0` | `docs/api-audit/` |
| `legacy_goc_analiz_promptu_v1.0` | `docs/migration-analysis/` |
| `performans_denetim_promptu_v1.0` | `docs/performance-audit/` |
| `uyumluluk_denetim_promptu_v1.0` | `docs/compliance-audit/` |
| `blockchain_analiz_promptu_v1.0` | `docs/blockchain-audit/` |
| `ai_analiz_sistemi_denetim_promptu_v1.0` | `docs/meta-analysis/` |
| `triyaj_yonlendirme_promptu_v1.0` | `docs/triage/` |
| `duzeltme_plani_uretici_promptu_v1.0` | `docs/remediation/` |
| `proje_saglik_skoru_promptu_v1.0` | `docs/health-score/` |

---

## Çok Promptlu Proje Yapısı

Aynı projede birden fazla prompt çalıştırıldığında tüm dizinleri birbirine bağlayan bir üst `docs/index.md` oluştur:

```
proje-koku/
└── docs/
    ├── index.md                  ← Üst seviye navigasyon (elle oluştur)
    ├── triage/
    │   └── triage_report.md
    ├── analysis/
    │   └── index.md  ...
    ├── security-audit/
    │   └── index.md  ...
    ├── performance-audit/
    │   └── index.md  ...
    ├── remediation/
    │   └── ...
    └── health-score/
        └── ...
```

### Üst Seviye `docs/index.md` Şablonu

Birden fazla prompt çalıştırıldıktan sonra bu şablonu doldur:

```markdown
# [Proje Adı] — Analiz Merkezi
**Son Güncelleme:** [Tarih]
**Uygulanan Promptlar:** [Hangi promptlar çalıştırıldı]

---

## Triyaj
- [Triyaj Raporu](triage/triage_report.md) — Prompt seçim gerekçesi

## Tanımlayıcı Analizler
- [Teknik Analiz](analysis/index.md)
- [Güvenlik Denetimi](security-audit/index.md) *(varsa)*
- [Performans Denetimi](performance-audit/index.md) *(varsa)*
- [API Denetimi](api-audit/index.md) *(varsa)*
- [Göç Analizi](migration-analysis/index.md) *(varsa)*
- [Uyumluluk Denetimi](compliance-audit/index.md) *(varsa)*

## Değerlendirici Sentez
- [Düzeltme Planı](remediation/index.md)
- [Sağlık Skoru](health-score/index.md)
```

---

## Dizin Adlandırma Prensibi

Mevcut dizin adları bilinçli olarak ayrı tutulmuştur:

- `docs/analysis/` → Proje türü bazlı analizler (birden fazla prompt bu dizini paylaşır)
- `docs/[odak]-audit/` → Odak bazlı denetimler (her biri bağımsız)
- `docs/[işlev]/` → İşlevsel araçlar (remediation, health-score, triage)

Bu ayrım kasıtlıdır: aynı projede hem uygulama analizi hem güvenlik denetimi çalıştırılırsa çıktılar karışmaz. `docs/analysis/` ortak havuz görevi görür; odak bazlı denetimler kendi izole dizinlerinde kalır.

---

## `duzeltme_plani_uretici` Beslenme Rehberi

Düzeltme Planı Üretici farklı promptların farklı isimlendirilmiş çıktı dosyalarını bekler. Eşleme tablosu:

| Kaynak Prompt | Ürettiği Anahtar Dosya | Düzeltme Planına Besle |
|---|---|---|
| Tüm analiz promptları | `completeness_report.md` | ✅ Her zaman |
| `guvenlik_denetim` | `risk_matrix.md` | ✅ |
| Tüm analiz promptları | `fragility_report.md` | ✅ Varsa |
| `legacy_goc` | `gap_analysis.md` | ✅ |
| `ai_analiz_denetim` | `gap_and_conflict_analysis.md` | ✅ |
| Tüm promptlar | `tech_debt_audit.md` | ✅ Varsa |
