# Module: Algoritma Doğrulama ve Property-Based Testing

**Priority**: P3 (Algoritmik Güvenilirlik)
**Tokens**: ~2500
**Analysis Time**: Kritik algoritma, matematiksel hesaplama veya veri dönüşümü tespit edildiğinde yüklenir

---

## Purpose
Matematiksel olarak kritik algoritmaların (sıralama, şifreleme, finansal hesaplama, veri dönüşümü) doğruluğunu yalnızca elle yazılan örneklerle değil, **property-based testing** (özellik tabanlı test) ve **fuzzing** ile otomatik olarak doğrular. Tipik birim testlerinin göremeyeceği köşe durumlarını (edge cases) sistematik olarak açığa çıkarır.

---

## Property-Based Testing (PBT) Nedir?

Geleneksel birim testleri "örnekler" üzerinden çalışır:
- `add(2, 3)` → `5` beklenir ✅

Property-based testing ise **kurallar** üzerinden çalışır ve yüzlerce rastgele girdi üretir:
- `add(a, b) == add(b, a)` — *her zaman* doğru olmalı (komütatiflik)
- `sort(sort(liste)) == sort(liste)` — *her zaman* idempotent olmalı

```python
# Örnek: Hypothesis (Python) ile PBT
from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_sort_idempotency(lst):
    """Bir listeyi iki kez sıralamak, bir kez sıralamakla aynı sonucu vermelidir."""
    assert sorted(sorted(lst)) == sorted(lst)

@given(st.integers(), st.integers())
def test_addition_commutativity(a, b):
    """Toplama işlemi sıra bağımsız olmalıdır."""
    assert add(a, b) == add(b, a)
```

---

## Araçlar ve Ekosistem

```yaml
pbt_tools:
  python:
    primary: "Hypothesis — En güçlü ve en yaygın PBT kütüphanesi"
    usage: "pip install hypothesis"
    features: ["Otomatik küçültme (shrinking)", "Başarısız örnekleri hafıza", "Stateful testing"]

  javascript:
    primary: "fast-check — TypeScript destekli PBT"
    usage: "npm install fast-check"
    features: ["Jest/Vitest entegrasyonu", "Arbitraries (özel veri üreticileri)"]

  dotnet:
    primary: "FsCheck — F# ve C# destekli"
    secondary: "CsCheck"

  java:
    primary: "jqwik — JUnit 5 ile doğal entegrasyon"
```

---

## Kritik Algoritma Tespiti

Aşağıdaki türde kodlar PBT ile doğrulanması **şiddetle önerilen** alanlardır:

```yaml
high_priority_algorithms:
  financial:
    examples:
      - "Para birimi dönüşümleri (yuvarlama hataları)"
      - "Vergi hesaplama (kesinlik gerektiren float işlemleri)"
      - "İndirim/komisyon hesaplama zincirleri"
    risk: "Yuvarlama hatası → Kullanıcı zararı veya yasal yükümlülük"

  sorting_searching:
    examples:
      - "Özel sıralama algoritmaları"
      - "Arama/filtreleme motorları"
    property: "sort(a) + sort(b) == sort(a + b) (merge özelliği)"

  serialization:
    examples:
      - "JSON/XML/YAML serialize/deserialize döngüsü"
      - "Veritabanı ORM mapping"
    property: "deserialize(serialize(obj)) == obj (yuvarlak-trip özelliği)"

  cryptography:
    examples:
      - "Şifreleme/şifre çözme döngüsü"
      - "Hash fonksiyonları"
    property: "decrypt(encrypt(msg, key), key) == msg"
    note: "Şifreleme için standart kütüphane kullanın, asla kendiniz yazmayın"
```

---

## Fuzzing (Bulanık Test)

Fuzzing, programın girdisini kasıtlı olarak bozarak (malformed input) beklenmedik çöküşleri veya güvenlik açıklarını tespit eder.

```python
# Python'da atheris ile Coverage-guided fuzzing
import atheris
import sys

def fuzz_target(data):
    fdp = atheris.FuzzedDataProvider(data)
    user_input = fdp.ConsumeUnicodeNoSurrogates(100)
    
    # Bu fonksiyon asla çökmemeli — hatta kötü girdide bile
    try:
        result = parse_user_input(user_input)
        validate_output(result)
    except ValueError:
        pass  # Beklenen hata — sorun yok
    except Exception as e:
        raise  # Beklenmeyen hata — fuzzer bunu rapor eder

atheris.Setup(sys.argv, fuzz_target)
atheris.Fuzz()
```

**Fuzzing'in birim testlerden farkı:** Siz "bu girdi hatalı" diye yazmaz; araç milyonlarca olası hatalı girdiyi sizin yerinize üretir.

---

## Matematiksel İspat Gerektiren Alanlar

Bazı algoritmalar test değil, **formal verification** gerektirir:

```yaml
formal_verification:
  use_cases:
    - "Blockchain akıllı kontrat mantığı"
    - "Protokol doğruluğu (consensus algoritmaları)"
    - "Güvenlik-kritik embedded sistemler"
  tools:
    - "TLA+ — Amazon AWS ve Microsoft'un kullandığı model checker"
    - "Alloy — Hafif formal modelleme"
    - "Coq / Isabelle — Teoremler için formal ispat"
  note: "Çoğu iş uygulaması için PBT yeterlidir. Formal verification sadece hayati sistemler için."
```

---

## Scoring

```yaml
scoring:
  excellent: "PBT kritik algoritmalar için uygulanmış, finansal hesaplamalar round-trip test edilmiş, fuzzing CI'da çalışıyor."
  good: "Bazı algoritmalar için PBT var, ancak finansal veya şifreleme alanları eksik."
  attention: "Kritik algoritmalar sadece elle yazılmış örneklerle test ediliyor, köşe durumları kör nokta."
  critical: "Finansal hesaplamalar float ile yapılıyor ve hiç test edilmemiş — production'da yuvarlama hatası riski var."
```

---

## Quick Wins (Hızlı Kazanımlar)

1. **Hypothesis kurun:** `pip install hypothesis` — İlk PBT'yi 30 dakikada yazabilirsiniz.
2. **Round-trip testi ekleyin:** En basit PBT — serialize/deserialize döngüsü.
3. **Float yerine Decimal kullanın:** Finansal hesaplamalarda `decimal.Decimal` kaçınılmaz.

---

## Output Format

```markdown
## 🔬 Algoritma Doğrulama Raporu

### Tespit Edilen Kritik Algoritmalar
- **`[Fonksiyon adı]` (`[Dosya:Satır]`):** [PBT ile doğrulanması gereken özellik]

### Yuvarlama/Kesinlik Riskleri
- **[Yerler]:** float kullanıldığı finansal hesaplamalar

### Mevcut PBT Kapsamı
- **Araç:** [Hypothesis / fast-check / Yok]
- **Kapsanan Fonksiyon Sayısı:** [X]

### Önerilen Testler
[Projeye özgü Hypothesis/fast-check örneği]
```
