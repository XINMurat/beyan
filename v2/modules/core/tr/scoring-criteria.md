# Module: Scoring Criteria and Formulas

**Priority**: P0 (Core System Module)
**Tokens**: ~1500
**Analysis Time**: Otomatik (tüm modüller tamamlandıktan sonra)

---

## Purpose

Tüm modüllerden gelen alt skorları birleştirerek projenin genel sağlık skorunu (0–10) hesaplar. Ağırlıklı ortalama formülü, her boyutun proje tipine göre farklı ağırlığa sahip olmasını sağlar.

---

## Ağırlık Tablosu (Proje Tipine Göre)

```yaml
weights_by_project_type:
  web_app:
    architecture: 0.20
    code_quality:  0.20
    security:      0.20
    performance:   0.15
    testing:       0.15
    documentation: 0.10

  api_backend:
    architecture: 0.25
    code_quality:  0.20
    security:      0.25
    performance:   0.15
    testing:       0.15
    documentation: 0.00  # ağırlık sıfır değil, baseline

  mobile_app:
    architecture: 0.20
    code_quality:  0.20
    security:      0.15
    performance:   0.20
    testing:       0.15
    documentation: 0.10

  data_pipeline:
    architecture: 0.15
    code_quality:  0.15
    security:      0.10
    performance:   0.30
    testing:       0.20
    documentation: 0.10
```

## Hesaplama Formülü

```
Overall Score (O) = Σ (boyut_skoru × boyut_ağırlığı)
Final Score       = min(10, max(0, O))
```

**Örnek:**
- Architecture: 8.0 × 0.20 = 1.60
- Code Quality:  7.0 × 0.20 = 1.40
- Security:      6.0 × 0.20 = 1.20
- Performance:   8.5 × 0.15 = 1.28
- Testing:       5.0 × 0.15 = 0.75
- Documentation: 7.0 × 0.10 = 0.70
- **Toplam: 6.93 / 10**

---

## Skor Aralıkları ve Anlamları

```yaml
score_ranges:
  9.0 - 10.0:
    status: "🟢 Mükemmel"
    meaning: "Production-ready, minimal risk"
    action: "Periyodik takip yeterli"

  7.0 - 8.9:
    status: "🟡 İyi"
    meaning: "Birkaç iyileştirme noktası var"
    action: "P1 sorunları bu sprint ele al"

  5.0 - 6.9:
    status: "🟠 Orta"
    meaning: "Dikkat gerektiren sorunlar mevcut"
    action: "P0 ve P1 sorunları acilen çöz"

  0.0 - 4.9:
    status: "🔴 Kritik"
    meaning: "Production'a çıkma riski yüksek"
    action: "Acil müdahale gerekli, deployment durdur"
```

---

## Kritik Override Kuralları

Genel skor ne olursa olsun, şu durumlar skoru otomatik olarak düşürür:

```yaml
critical_overrides:
  any_p0_finding:
    description: "Herhangi bir P0 bulgu varsa"
    cap_score_at: 6.0
    reason: "P0 = production outage veya güvenlik açığı riski"

  security_score_below_5:
    description: "Security skoru 5'in altındaysa"
    cap_score_at: 5.5
    reason: "Güvenlik açığı tüm sistemi tehdit eder"

  test_coverage_below_20:
    description: "Test coverage %20'nin altındaysa"
    deduct: 1.0
    reason: "Kör bölge riski çok yüksek"

  no_readme:
    description: "README.md yoksa"
    deduct: 0.5
    reason: "Onboarding imkansız"
```

---

## Output Format

```markdown
## Proje Sağlık Skoru: X.X / 10 [STATUS_EMOJI]

| Boyut | Skor | Ağırlık | Katkı |
|-------|------|---------|-------|
| Architecture | X.X | %20 | X.XX |
| Code Quality | X.X | %20 | X.XX |
| Security | X.X | %20 | X.XX |
| Performance | X.X | %15 | X.XX |
| Testing | X.X | %15 | X.XX |
| Documentation | X.X | %10 | X.XX |
| **TOPLAM** | | | **X.XX** |

[Varsa override açıklamaları]
```