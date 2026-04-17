# Module: Turkish Market Compliance

**Priority**: P2
**Tokens**: ~1500
**Analysis Time**: Loaded when Turkish language, KVKK, or .tr TLD detected

---

## Purpose
Evaluates compliance with Turkish data protection law (KVKK), BTK regulations, local payment system security, and Turkish-specific technical requirements for software deployed in Turkey.

---

## KVKK Compliance

KVKK (Personal Data Protection Law) is mandatory for all software operating in Turkey.

```yaml
kvkk_checks:
  explicit_consent:
    check: "Explicit consent obtained before processing personal data? Checkbox on registration?"
  right_to_erasure:
    check: "Can users delete their accounts and have data fully removed? Hard delete or anonymization?"
  data_inventory:
    check: "Privacy Policy documenting what data is collected, for what purpose, how long retained?"
  cross_border:
    check: "Personal data transferred to servers outside Turkey (AWS, GCP)? Adequate safeguards per KVKK Art. 9?"
```

## BTK & E-Commerce Law

*   **E-Commerce:** Merchant information (company name, address, tax ID) must be visible on all pages.
*   **Distance Selling:** Pre-information form required before purchase, copy sent via email.
*   **BTK Notification:** Apps above certain user thresholds must register with BTK.

## Turkish Payment Systems

```yaml
payment_security:
  3d_secure: "3D Secure v2 mandatory for all card transactions?"
  merchant_secret: "Payment provider secret key server-side only? Not exposed client-side?"
  pci_dss: "Financial operations subject to BDDK oversight require PCI-DSS compliance?"
```

## Local Technical Requirements

*   **Encoding:** Database and API responses using `utf-8` or `utf-8mb4` (MySQL)?
*   **Date/Currency Format:** `31.12.2024` (DD.MM.YYYY) and `₺1.234,56` (period=thousands, comma=decimal)?
*   **E-Invoice (GİB):** Revenue-generating platforms may need GIB e-invoice integration.

## Scoring

```yaml
scoring:
  excellent: "KVKK fully compliant, 3D Secure mandatory, e-invoice integrated, UTF-8 throughout."
  good: "Basic KVKK consent, payment secure, minor gaps in data erasure."
  attention: "KVKK checkbox present but no data deletion mechanism, missing privacy inventory."
  critical: "Personal data processed without consent, merchant secret exposed client-side."
```
