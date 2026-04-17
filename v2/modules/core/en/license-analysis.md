# Module: License Compliance Analysis

**Priority**: P3
**Tokens**: ~1200
**Analysis Time**: Loaded when package.json, requirements.txt, or pom.xml detected

---

## Purpose
Scans third-party library licenses to identify incompatible licenses that may require open-sourcing proprietary code or prohibit commercial use.

---

## License Risk Matrix

```yaml
license_risk_matrix:
  low_risk:
    licenses: ["MIT", "Apache 2.0", "BSD-2-Clause", "BSD-3-Clause", "ISC"]
    description: "Commercial use permitted. Attribution required."
  medium_risk:
    licenses: ["LGPL-2.1", "LGPL-3.0", "MPL-2.0"]
    description: "Dynamic linking generally OK. Static linking or modification may require source disclosure."
  high_risk:
    licenses: ["GPL-2.0", "GPL-3.0", "AGPL-3.0"]
    description: "Copyleft — integrating into commercial software may require releasing your source code. Legal counsel required."
  forbidden:
    licenses: ["SSPL", "Commons Clause", "Proprietary without license"]
    description: "Prohibits commercial use entirely without purchase."
```

## Scan Commands

```bash
# Node.js
npx license-checker --summary
npx license-checker --failOn "GPL-2.0;GPL-3.0;AGPL-3.0"

# Python
pip-licenses --format=table

# Maven
mvn license:aggregate-third-party-report
```

## Output Format

```markdown
## ⚖️ License Compliance Report

### Risk Summary
- 🟢 Low Risk: X packages (MIT, Apache)
- 🟡 Medium Risk: Y packages (LGPL) — Review Required
- 🔴 High Risk: Z packages (GPL/AGPL) — Legal Counsel Required

### High-Risk Packages
| Package | License | Risk | Alternative |
|---------|---------|------|-------------|
| [Package] | GPL-3.0 | HIGH | [MIT-licensed alternative] |
```
