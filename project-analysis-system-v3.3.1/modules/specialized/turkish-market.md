# Module: Turkish Market Specifics

**Priority**: P2 (Specialized - For Turkey-Focused Projects)  
**Tokens**: ~1800  
**Analysis Time**: 10-12 minutes  

---

## Purpose

Evaluate Turkey-specific requirements including Turkish character handling, KVKK (GDPR equivalent) compliance, e-Government integrations, Turkish payment systems, date/currency formatting, and cultural UX considerations.

---

## 1. Turkish Character Handling (İ, �₺, �₺, �₺, �₺, �₺)

```yaml
common_issues:
  case_conversion:
    problem: "i �₺₺ I (wrong), should be i �₺₺ İ"
    affected: "Search, sorting, validation"
  
  collation:
    problem: "Turkish alphabetical order: A B C �₺ D E F G �₺ H I İ J K L M N O �₺ P R S �₺ T U �₺ V Y Z"
    sorting: "Must use tr-TR locale"
  
  url_slugification:
    wrong: "Türkçe �₺₺ turkce (missing ç, ü)"
    correct: "Türkçe �₺₺ turkce (proper transliteration)"

confidence: "high_92%"
```

### Detection & Fixes

```typescript
// �₺ Wrong: English case conversion
const userInput = "istanbul";
const searchTerm = userInput.toUpperCase();  // "ISTANBUL" �₺
// Database has "İSTANBUL" �₺₺ No match!

// �₺₺ Correct: Turkish locale
const searchTerm = userInput.toLocaleUpperCase('tr-TR');  // "İSTANBUL" �₺₺

// �₺ Wrong: English sorting
const cities = ["Ankara", "İzmir", "�Çanakkale"];
cities.sort();  // Incorrect Turkish order

// �₺₺ Correct: Turkish collation
cities.sort((a, b) => a.localeCompare(b, 'tr-TR'));
// Result: Ankara, �Çanakkale, İzmir
```

```csharp
// �₺ Wrong: Invariant culture
string.Compare("i", "İ", StringComparison.OrdinalIgnoreCase);  // Not equal

// �₺₺ Correct: Turkish culture
var turkishCulture = new CultureInfo("tr-TR");
string.Compare("i", "İ", turkishCulture, CompareOptions.IgnoreCase);  // Equal
```

**Database Collation**:
```sql
-- SQL Server: Use Turkish collation
CREATE TABLE Users (
    Name NVARCHAR(100) COLLATE Turkish_CI_AS  -- Case-insensitive, accent-sensitive
);

-- PostgreSQL: Use tr_TR locale
CREATE COLLATION turkish (provider = icu, locale = 'tr-TR');
```

---

## 2. KVKK Compliance (Turkish GDPR)

```yaml
kvkk_basics:
  full_name: "Ki�₺isel Verilerin Korunması Kanunu"
  effective: "2016-04-07"
  authority: "Ki�₺isel Verilerin Korunması Kurumu (KVKK)"
  penalties:
    system: "Kategorik sabit ceza (GDPR gibi yüzde bazlı DEĞİL)"
    administrative_2024: "1.813 TL - 3.625.732 TL (yeniden değerleme ile)"
    criminal: "Madde 17 kapsamında hapis cezası riski"
    note: "GDPR'dan farklıdır — AB yüzde bazlı cezalarla karıştırılmamalı"

requirements:
  consent:
    - Explicit user consent for data collection
    - Clear explanation of data usage
    - "Aydınlatma Metni" (Privacy Notice)
    - "Açık Rıza Metni" (Explicit Consent Text)
  
  user_rights:
    - Right to access personal data
    - Right to correction
    - Right to deletion
    - Right to object to processing
    - Right to data portability
  
  technical:
    - Encrypt personal data (at rest, in transit)
    - Audit logging (who accessed what, when)
    - Data breach notification (72 hours)
    - DPO (Data Protection Officer) if needed

  verbis_registry:
    required_if: "Yıllık ciro > 10M TL VEYA çalışan sayısı > 50"
    registration_url: "https://verbis.kvkk.gov.tr"
    deadline: "Yeni veri sorumluları için faaliyet başlangıcında"
    penalty: "KVKK Madde 18 — kayıt yaptırmama idari para cezası"

  international_data_transfer:
    law: "KVKK Madde 9"
    requirement: "Yurt dışına veri aktarımı için KVKK Kurulu onayı VEYA açık rıza zorunlu"
    common_services_affected:
      - "Google Analytics (ABD) — IP adresi kişisel veri sayılır"
      - "AWS, Azure, GCP (ABD/AB sunucu) — veri depolama"
      - "SendGrid / Mailchimp (ABD) — e-posta adresi aktarımı"
    solutions:
      - "Türkiye'deki sunuculara taşı (veri yerelleştirme)"
      - "GA4 IP anonimleştirme + consent mode aktif et"
      - "Standart Sözleşme Maddeleri (SCCs) + açık rıza"
    kurul_kararlar: "https://www.kvkk.gov.tr/Icerik/6908"

confidence: "high_90%"
```

### Implementation Checklist

```yaml
must_have:
  - [ ] Privacy Policy (Gizlilik Politikası) in Turkish
  - [ ] Cookie Consent Banner (�Çerez Politikası)
  - [ ] User data download (export JSON/CSV)
  - [ ] Account deletion (with data purge)
  - [ ] Consent logs (timestamp, IP, what consented to)
  - [ ] Data encryption (AES-256 at rest, TLS 1.3 in transit)
  - [ ] VERBİS kaydı (yıllık ciro > 10M TL veya çalışan > 50 ise zorunlu)
  - [ ] Yurt dışı veri aktarımı için KVKK Madde 9 uyumluluğu

example_texts:
  privacy_notice: |
    "�Şirketimiz, 6698 sayılı Ki�₺isel Verilerin Korunması Kanunu'na 
    uygun olarak ki�₺isel verilerinizi i�₺lemektedir..."
  
  consent_text: |
    "Ki�₺isel verilerimin i�₺lenmesine açık rıza gösteriyorum.
    �₺� Ticari elektronik ileti almayı kabul ediyorum (iste�₺e ba�₺lı)"
  
  data_request_response: |
    "Talebiniz 30 gün içerisinde yanıtlanacaktır.
    Talep sonucu tarafınıza e-posta ile iletilecektir."
```

---

## 3. Turkish Payment Systems

```yaml
local_payment_methods:
  credit_cards:
    - Troy (Turkish card network)
    - Visa, Mastercard (common)
    - Installment options (Taksit) - MUST support
  
  digital_wallets:
    - Tosla (BKM'nin güncel mobil cüzdanı — BKM Express'in halefi)
    - PayFix, Papara (popular Turkish fintechs)
  
  bank_transfers:
    - EFT (Electronic Fund Transfer)
    - FAST (instant 7/24 transfer)
    - Havale (wire transfer)

payment_gateways:
  popular:
    - iyzico (most popular for SMEs)
    - PayTR
    - Param
    - PayU Turkey
  
  bank_pos:
    - Garanti Bankası Virtual POS
    - İ�₺ Bankası Virtual POS
    - Akbank Virtual POS

installment_system:
  requirement: "MUST show installment options"
  example: |
    Tek �₺ekim: 1,000 TL
    2 Taksit: 2 x 505 TL (Total: 1,010 TL)
    3 Taksit: 3 x 340 TL (Total: 1,020 TL)
    6 Taksit: 6 x 175 TL (Total: 1,050 TL)
  
  banks_vary: "Each bank offers different installment rates"
  
confidence: "high_88%"
```

### Example Integration

```typescript
// Turkish installment display
interface InstallmentOption {
  installmentCount: number;
  monthlyAmount: number;
  totalAmount: number;
  bank: string;
}

function displayInstallments(amount: number): InstallmentOption[] {
  return [
    { installmentCount: 1, monthlyAmount: amount, totalAmount: amount, bank: "Tüm Bankalar" },
    { installmentCount: 2, monthlyAmount: amount * 1.01 / 2, totalAmount: amount * 1.01, bank: "İ�₺ Bankası" },
    { installmentCount: 3, monthlyAmount: amount * 1.02 / 3, totalAmount: amount * 1.02, bank: "Garanti" },
    // ... more options
  ];
}
```

---

## 4. E-Government Integration

```yaml
e_devlet:
  login: "e-Devlet Kapısı authentication"
  services:
    - TC Kimlik No verification (ID number)
    - Address lookup (e-Devlet Adres Bilgi Sistemi)
    - Tax information (Vergi records)
  
  integration:
    method: "SOAP Web Services (legacy) or REST API (new)"
    auth: "Certificate-based (institutional e-signature)"
    
  typical_flow: |
    1. User clicks "e-Devlet ile Giri�₺"
    2. Redirect to e-Devlet
    3. User authenticates with e-Devlet
    4. Callback with verified ID info
    5. Auto-create/update user profile

mernis:
  full_name: "Merkezi Nüfus İdaresi Sistemi"
  purpose: "Verify TC Kimlik No and personal info"
  validation: "Name, surname, birthdate, TC No match"

confidence: "medium_75%"  # Requires institutional setup
```

---

## 5. Date, Time & Currency Formatting

```yaml
date_format:
  common: "DD.MM.YYYY (e.g., 15.12.2024)"
  wrong: "12/15/2024 (American format confuses users)"

time:
  format_24h: "15:30 (preferred)"
  format_12h: "03:30 PM (understood but less common)"

currency:
  symbol: "�₺�" or "TL"
  position: "After amount (1.000,50 TL)"
  thousands_separator: "." (dot)
  decimal_separator: "," (comma)
  
  examples:
    correct: "1.234,56 TL"
    wrong: "TL 1,234.56 (English format)"

confidence: "high_95%"
```

### Implementation

```typescript
// �₺₺ Correct Turkish formatting
const amount = 1234.56;
const formatted = new Intl.NumberFormat('tr-TR', {
  style: 'currency',
  currency: 'TRY'
}).format(amount);
// Result: "�₺�1.234,56" or "1.234,56 TL"

// Dates
const date = new Date('2024-12-15');
const formattedDate = date.toLocaleDateString('tr-TR');
// Result: "15.12.2024"
```

---

## 6. Address Format

```yaml
turkish_address:
  components:
    - Mahalle (Neighborhood)
    - Sokak/Cadde (Street/Avenue)
    - Bina No (Building number)
    - Daire No (Apartment number)
    - İlçe (District)
    - İl (Province/City)
    - Posta Kodu (Postal code - 5 digits)
  
  example: |
    �₺ankaya Mahallesi
    Atatürk Caddesi No: 45 Daire: 7
    �₺ankaya / ANKARA
    06100

validation:
  postal_code: "[0-9]{5}"
  il: "81 provinces (İstanbul, Ankara, İzmir, etc.)"
  ilce: "~970 districts"

confidence: "high_92%"
```

---

## 7. Cultural UX Considerations

```yaml
language:
  default: "Turkish (tr-TR)"
  fallback: "English for international users"
  
naming:
  turkish_names: "Single surname (no middle name)"
  validation: "Allow Turkish characters (İ, �₺, �₺)"
  
holidays:
  religious: "Ramazan Bayramı, Kurban Bayramı (dates vary)"
  national: "29 Ekim (Cumhuriyet Bayramı), 23 Nisan, 19 Mayıs"
  
business_hours:
  typical: "09:00 - 18:00 weekdays"
  lunch: "12:00 - 13:00 (common lunch break)"
  weekend: "Saturday half-day, Sunday closed (traditional)"

confidence: "high_85%"
```

---

## Analysis Protocol

### Quick Check (5 min)

```bash
# Turkish character handling
grep -r "toUpperCase()\|toLowerCase()" src/ | wc -l
# Should use toLocaleUpperCase('tr-TR')

# Date formatting
grep -r "MM/DD/YYYY\|MM-DD-YYYY" src/
# Wrong format for Turkey

# Currency
grep -r "\$\|USD" src/ | grep -v node_modules
# Should be �₺� or TL
```

### Checklist

```yaml
- [ ] Turkish characters work in search/sort
- [ ] KVKK-compliant privacy policy exists (in Turkish)
- [ ] Cookie consent banner (Turkish + English)
- [ ] User can download their data (KVKK right)
- [ ] User can delete account (KVKK right)
- [ ] Payment supports installments (Taksit)
- [ ] Dates formatted DD.MM.YYYY
- [ ] Currency formatted 1.234,56 TL
- [ ] Address form has Mahalle, İlçe, İl fields
- [ ] If e-Gov integration: TC No validation
```

---

## Example Report

```markdown
# Turkish Market Compliance Report

## Overall Score: 6/10 �₺₺�

### Critical Issues

#### 1. �₺₺� Turkish Character Sorting Broken
**Location**: Search functionality
```typescript
// �₺ Current: English sorting
users.sort((a, b) => a.name.localeCompare(b.name));

// �₺₺ Fix: Turkish locale
users.sort((a, b) => a.name.localeCompare(b.name, 'tr-TR'));
```
**Impact**: "İzmir" appears after "Zonguldak" (wrong!)
**Effort**: 30 minutes
**Confidence**: High (95%)

---

#### 2. �₺₺� KVKK Non-Compliant
**Missing**:
- Privacy policy in Turkish
- Explicit consent mechanism
- Data download feature
- Account deletion

**Effort**: 8 hours
**Risk**: Legal penalties
**Confidence**: High (90%)

---

#### 3. �₺₺� Currency Format Correct �₺₺
```typescript
// Already using tr-TR locale
new Intl.NumberFormat('tr-TR', { 
  style: 'currency', 
  currency: 'TRY' 
})
```

---

## Recommendations

### P0 (This Week)
1. Fix Turkish character sorting (30 min)
2. Add KVKK privacy policy (2 hours)

### P1 (This Month)
3. Implement KVKK user rights (8 hours)
4. Add installment options to checkout (4 hours)

### P2 (Quarter)
5. e-Devlet integration (if needed) (40 hours)
```

---

**Analysis Complete** | Turkish Compliance: 6/10 | Confidence: High (88%)
