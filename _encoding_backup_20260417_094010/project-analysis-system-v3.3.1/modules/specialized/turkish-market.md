# Module: Turkish Market Specifics

**Priority**: P2 (Specialized - For Turkey-Focused Projects)  
**Tokens**: ~1800  
**Analysis Time**: 10-12 minutes  

---

## Purpose

Evaluate Turkey-specific requirements including Turkish character handling, KVKK (GDPR equivalent) compliance, e-Government integrations, Turkish payment systems, date/currency formatting, and cultural UX considerations.

---

## 1. Turkish Character Handling (Ä°, Åž, Äž, Ãœ, Ã–, Ã‡)

```yaml
common_issues:
  case_conversion:
    problem: "i â†’ I (wrong), should be i â†’ Ä°"
    affected: "Search, sorting, validation"
  
  collation:
    problem: "Turkish alphabetical order: A B C Ã‡ D E F G Äž H I Ä° J K L M N O Ã– P R S Åž T U Ãœ V Y Z"
    sorting: "Must use tr-TR locale"
  
  url_slugification:
    wrong: "TÃ¼rkÃ§e â†’ turkce (missing Ã§, Ã¼)"
    correct: "TÃ¼rkÃ§e â†’ turkce (proper transliteration)"

confidence: "high_92%"
```

### Detection & Fixes

```typescript
// âŒ Wrong: English case conversion
const userInput = "istanbul";
const searchTerm = userInput.toUpperCase();  // "ISTANBUL" âŒ
// Database has "Ä°STANBUL" â†’ No match!

// âœ… Correct: Turkish locale
const searchTerm = userInput.toLocaleUpperCase('tr-TR');  // "Ä°STANBUL" âœ…

// âŒ Wrong: English sorting
const cities = ["Ankara", "Ä°zmir", "Ã‡anakkale"];
cities.sort();  // Incorrect Turkish order

// âœ… Correct: Turkish collation
cities.sort((a, b) => a.localeCompare(b, 'tr-TR'));
// Result: Ankara, Ã‡anakkale, Ä°zmir
```

```csharp
// âŒ Wrong: Invariant culture
string.Compare("i", "Ä°", StringComparison.OrdinalIgnoreCase);  // Not equal

// âœ… Correct: Turkish culture
var turkishCulture = new CultureInfo("tr-TR");
string.Compare("i", "Ä°", turkishCulture, CompareOptions.IgnoreCase);  // Equal
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
  full_name: "KiÅŸisel Verilerin KorunmasÄ± Kanunu"
  effective: "2016-04-07"
  authority: "KiÅŸisel Verilerin KorunmasÄ± Kurumu (KVKK)"
  penalties: "Up to 2% of annual revenue"

requirements:
  consent:
    - Explicit user consent for data collection
    - Clear explanation of data usage
    - "AydÄ±nlatma Metni" (Privacy Notice)
    - "AÃ§Ä±k RÄ±za Metni" (Explicit Consent Text)
  
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

confidence: "high_90%"
```

### Implementation Checklist

```yaml
must_have:
  - [ ] Privacy Policy (Gizlilik PolitikasÄ±) in Turkish
  - [ ] Cookie Consent Banner (Ã‡erez PolitikasÄ±)
  - [ ] User data download (export JSON/CSV)
  - [ ] Account deletion (with data purge)
  - [ ] Consent logs (timestamp, IP, what consented to)
  - [ ] Data encryption (AES-256 at rest, TLS 1.3 in transit)

example_texts:
  privacy_notice: |
    "Åžirketimiz, 6698 sayÄ±lÄ± KiÅŸisel Verilerin KorunmasÄ± Kanunu'na 
    uygun olarak kiÅŸisel verilerinizi iÅŸlemektedir..."
  
  consent_text: |
    "KiÅŸisel verilerimin iÅŸlenmesine aÃ§Ä±k rÄ±za gÃ¶steriyorum.
    â˜ Ticari elektronik ileti almayÄ± kabul ediyorum (isteÄŸe baÄŸlÄ±)"
  
  data_request_response: |
    "Talebiniz 30 gÃ¼n iÃ§erisinde yanÄ±tlanacaktÄ±r.
    Talep sonucu tarafÄ±nÄ±za e-posta ile iletilecektir."
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
    - BKM Express (Bank Association mobile wallet)
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
    - Garanti BankasÄ± Virtual POS
    - Ä°ÅŸ BankasÄ± Virtual POS
    - Akbank Virtual POS

installment_system:
  requirement: "MUST show installment options"
  example: |
    Tek Ã‡ekim: 1,000 TL
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
    { installmentCount: 1, monthlyAmount: amount, totalAmount: amount, bank: "TÃ¼m Bankalar" },
    { installmentCount: 2, monthlyAmount: amount * 1.01 / 2, totalAmount: amount * 1.01, bank: "Ä°ÅŸ BankasÄ±" },
    { installmentCount: 3, monthlyAmount: amount * 1.02 / 3, totalAmount: amount * 1.02, bank: "Garanti" },
    // ... more options
  ];
}
```

---

## 4. E-Government Integration

```yaml
e_devlet:
  login: "e-Devlet KapÄ±sÄ± authentication"
  services:
    - TC Kimlik No verification (ID number)
    - Address lookup (e-Devlet Adres Bilgi Sistemi)
    - Tax information (Vergi records)
  
  integration:
    method: "SOAP Web Services (legacy) or REST API (new)"
    auth: "Certificate-based (institutional e-signature)"
    
  typical_flow: |
    1. User clicks "e-Devlet ile GiriÅŸ"
    2. Redirect to e-Devlet
    3. User authenticates with e-Devlet
    4. Callback with verified ID info
    5. Auto-create/update user profile

mernis:
  full_name: "Merkezi NÃ¼fus Ä°daresi Sistemi"
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
  symbol: "â‚º" or "TL"
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
// âœ… Correct Turkish formatting
const amount = 1234.56;
const formatted = new Intl.NumberFormat('tr-TR', {
  style: 'currency',
  currency: 'TRY'
}).format(amount);
// Result: "â‚¹1.234,56" or "1.234,56 TL"

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
    - Ä°lÃ§e (District)
    - Ä°l (Province/City)
    - Posta Kodu (Postal code - 5 digits)
  
  example: |
    Ã‡ankaya Mahallesi
    AtatÃ¼rk Caddesi No: 45 Daire: 7
    Ã‡ankaya / ANKARA
    06100

validation:
  postal_code: "[0-9]{5}"
  il: "81 provinces (Ä°stanbul, Ankara, Ä°zmir, etc.)"
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
  validation: "Allow Turkish characters (Ä°, Åž, Äž)"
  
holidays:
  religious: "Ramazan BayramÄ±, Kurban BayramÄ± (dates vary)"
  national: "29 Ekim (Cumhuriyet BayramÄ±), 23 Nisan, 19 MayÄ±s"
  
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
# Should be â‚º or TL
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
- [ ] Address form has Mahalle, Ä°lÃ§e, Ä°l fields
- [ ] If e-Gov integration: TC No validation
```

---

## Example Report

```markdown
# Turkish Market Compliance Report

## Overall Score: 6/10 ðŸŸ¡

### Critical Issues

#### 1. ðŸ”´ Turkish Character Sorting Broken
**Location**: Search functionality
```typescript
// âŒ Current: English sorting
users.sort((a, b) => a.name.localeCompare(b.name));

// âœ… Fix: Turkish locale
users.sort((a, b) => a.name.localeCompare(b.name, 'tr-TR'));
```
**Impact**: "Ä°zmir" appears after "Zonguldak" (wrong!)
**Effort**: 30 minutes
**Confidence**: High (95%)

---

#### 2. ðŸŸ¡ KVKK Non-Compliant
**Missing**:
- Privacy policy in Turkish
- Explicit consent mechanism
- Data download feature
- Account deletion

**Effort**: 8 hours
**Risk**: Legal penalties
**Confidence**: High (90%)

---

#### 3. ðŸŸ¢ Currency Format Correct âœ…
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
