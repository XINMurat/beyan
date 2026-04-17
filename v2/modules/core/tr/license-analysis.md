# Module: License Compliance Analysis

**Priority**: P3 (Hukuki Uyum)
**Tokens**: ~1200
**Analysis Time**: `package.json`, `requirements.txt`, `pom.xml` tespit edildiğinde yüklenir

---

## Purpose
Projede kullanılan üçüncü taraf kütüphanelerin lisans tiplerini tarar, ticari kullanım veya kaynak kodu açma zorunluluğu doğurabilecek uyumsuz lisansları tespit eder.

---

## Lisans Risk Seviyeleri

```yaml
license_risk_matrix:
  low_risk:
    licenses: ["MIT", "Apache 2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC"]
    description: "Ticari kullanım serbesttir. Sadece attribution (kaynak gösterme) gerektirir."

  medium_risk:
    licenses: ["LGPL-2.1", "LGPL-3.0", "MPL-2.0"]
    description: "Dinamik link yapılırsa genellikle sorun çıkmaz. Statik link ve değişiklik yapılırsa kaynak paylaşımı gerekebilir."

  high_risk:
    licenses: ["GPL-2.0", "GPL-3.0", "AGPL-3.0"]
    description: "Projenize entegre edilirse kaynak kodunuzu açık kaynak yapmak zorunda kalabilirsiniz (copyleft). Ticari yazılım için hukuki danışmanlık şart."

  forbidden:
    licenses: ["SSPL", "Commons Clause", "Proprietary"]
    description: "Genellikle ticari kullanımı tamamen kısıtlar. Lisans satın alınmadan kullanılamaz."
```

---

## Tarama Komutları

```bash
# Node.js projeleri için
npx license-checker --summary
npx license-checker --failOn "GPL-2.0;GPL-3.0;AGPL-3.0"

# Python projeleri için
pip-licenses --format=table
pip-licenses --fail-on="GPL"

# Maven (Java) projeleri için
mvn license:aggregate-third-party-report
```

---

## Output Format

```markdown
## ⚖️ Lisans Uyumluluk Raporu

### Risk Özeti
- 🟢 Düşük Risk: X kütüphane (MIT, Apache vb.)
- 🟡 Orta Risk: Y kütüphane (LGPL vb.) — İnceleme Gerekli
- 🔴 Yüksek Risk: Z kütüphane (GPL/AGPL) — Hukuki Danışmanlık Şart

### Yüksek Riskli Kütüphaneler
| Paket | Lisans | Risk | Alternatif |
|-------|--------|------|------------|
| [Paket] | GPL-3.0 | YÜKSEK | [MIT lisanslı alternatif] |
```