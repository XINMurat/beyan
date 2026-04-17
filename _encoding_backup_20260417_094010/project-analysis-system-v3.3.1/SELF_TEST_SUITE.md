# Self-Test Suite - Sistem Kendi DoÄŸrulama MekanizmasÄ±

**Version**: 1.0  
**Purpose**: AI Analysis System'in kendi Ã§Ä±ktÄ±larÄ±nÄ± doÄŸrulamasÄ±  
**Priority**: P0 (GÃ¼venilirlik iÃ§in kritik)

---

## ðŸŽ¯ AmaÃ§

Bu framework, sistemin Ã¼rettiÄŸi analizlerin, Ã¶nerilerin ve planlarÄ±n **otomatik olarak doÄŸrulanmasÄ±nÄ±** saÄŸlar. AI hallucination riskini azaltÄ±r ve Ã§Ä±ktÄ± kalitesini garanti eder.

---

## ðŸ“‹ Test Kategorileri

### 1. Syntax Validation (SÃ¶zdizimi KontrolÃ¼)
**Ne kontrol eder**: Ãœretilen dosyalarÄ±n format doÄŸruluÄŸu

```yaml
test_syntax_validation:
  name: "Markdown syntax kontrolÃ¼"
  
  checks:
    - valid_markdown: true
      reason: "TÃ¼m baÅŸlÄ±klar # ile baÅŸlamalÄ±"
      
    - code_blocks_closed: true
      reason: "AÃ§Ä±lan ``` kapatÄ±lmalÄ±"
      
    - table_syntax: true
      reason: "Tablolar doÄŸru formatlanmalÄ±"
      
    - yaml_valid: true
      reason: "YAML bloklarÄ± parse edilebilir olmalÄ±"
  
  auto_fix: true
  severity: "medium"
```

**Ã–rnek Test**:
```python
def test_markdown_syntax(output_file):
    """Markdown dosyasÄ±nÄ±n geÃ§erli olduÄŸunu kontrol et"""
    
    with open(output_file) as f:
        content = f.read()
    
    # Test 1: Her ``` aÃ§Ä±lÄ±ÅŸÄ±nÄ±n kapanÄ±ÅŸÄ± var mÄ±?
    code_blocks = content.count("```")
    assert code_blocks % 2 == 0, "AÃ§Ä±k code block var!"
    
    # Test 2: BaÅŸlÄ±klar # ile mi baÅŸlÄ±yor?
    lines = content.split('\n')
    for line in lines:
        if line.startswith('#'):
            assert line[1] == ' ' or line[1] == '#', "BaÅŸlÄ±k formatÄ± hatalÄ±"
    
    return "PASS"
```

---

### 2. Content Validation (Ä°Ã§erik DoÄŸrulama)
**Ne kontrol eder**: Analizin iÃ§eriÄŸinin mantÄ±klÄ± olmasÄ±

```yaml
test_content_validation:
  name: "Ä°Ã§erik tutarlÄ±lÄ±ÄŸÄ± kontrolÃ¼"
  
  checks:
    - priority_consistency:
        rule: "P0 sorunlar P1'den fazla olmalÄ± (severity)"
        example: "P0: 3 sorun, P1: 15 sorun â†’ UYARI"
    
    - score_range:
        rule: "Skorlar 0-10 arasÄ±nda olmalÄ±"
        example: "Security: 12/10 â†’ HATA"
    
    - file_references:
        rule: "Referans verilen dosyalar mevcut olmalÄ±"
        example: "src/missing.ts:45 â†’ Dosya yok â†’ UYARI"
    
    - recommendation_feasibility:
        rule: "Ã–neriler uygulanabilir olmalÄ±"
        example: "Delete production DB â†’ RÄ°SKLÄ° â†’ FLAG"
  
  auto_fix: false
  severity: "high"
```

**Ã–rnek Test**:
```python
def test_priority_consistency(analysis_json):
    """P0 sorunlarÄ±n gerÃ§ekten kritik olduÄŸunu kontrol et"""
    
    p0_issues = analysis_json['findings']['P0']
    p1_issues = analysis_json['findings']['P1']
    
    # Test: P0'da 10+ sorun varsa ÅŸÃ¼pheli
    if len(p0_issues) > 10:
        return {
            "status": "WARNING",
            "message": "10+ P0 sorun nadir, priority inflation olabilir"
        }
    
    # Test: P0'larÄ±n hepsi security/performance ile ilgili mi?
    critical_tags = ['security', 'data-loss', 'performance-critical']
    for issue in p0_issues:
        if not any(tag in issue['tags'] for tag in critical_tags):
            return {
                "status": "FAIL",
                "message": f"P0 issue '{issue['title']}' kritik deÄŸil"
            }
    
    return {"status": "PASS"}
```

---

### 3. Logic Validation (MantÄ±k KontrolÃ¼)
**Ne kontrol eder**: Ã–nerilerin mantÄ±ksal tutarlÄ±lÄ±ÄŸÄ±

```yaml
test_logic_validation:
  name: "MantÄ±k tutarlÄ±lÄ±ÄŸÄ±"
  
  checks:
    - contradiction_detection:
        rule: "Ã‡eliÅŸen Ã¶neriler olmamalÄ±"
        example: "Sorun: 'Bundle Ã§ok bÃ¼yÃ¼k' + Ã–neri: 'Daha fazla library ekle' â†’ Ã‡ELÄ°ÅžKÄ°"
    
    - dependency_order:
        rule: "BaÄŸÄ±mlÄ± tasklar doÄŸru sÄ±rada"
        example: "Task 3: 'Test yaz' BEFORE Task 1: 'Kodu dÃ¼zelt' â†’ YANLIÅž SIRA"
    
    - effort_estimation:
        rule: "SÃ¼re tahminleri gerÃ§ekÃ§i"
        example: "'Database migration: 5 minutes' â†’ ÅžÃœPHELÄ°"
    
    - resource_allocation:
        rule: "AynÄ± kiÅŸiye Ã§ok iÅŸ verilmemiÅŸ"
        example: "Ali: 80 saat/hafta â†’ Ä°MKANSIZ"
  
  auto_fix: false
  severity: "high"
```

**Ã–rnek Test**:
```python
def test_contradiction_detection(recommendations):
    """Ã‡eliÅŸen Ã¶nerileri tespit et"""
    
    contradictions = []
    
    for i, rec1 in enumerate(recommendations):
        for rec2 in recommendations[i+1:]:
            # Ã‡eliÅŸki 1: Bundle kÃ¼Ã§Ã¼lt vs bÃ¼yÃ¼t
            if ('reduce bundle' in rec1['text'].lower() and 
                'add library' in rec2['text'].lower()):
                contradictions.append({
                    "pair": [rec1['id'], rec2['id']],
                    "reason": "Bundle optimization vs library addition"
                })
            
            # Ã‡eliÅŸki 2: AynÄ± dosyada farklÄ± deÄŸiÅŸiklikler
            if (rec1['file'] == rec2['file'] and 
                rec1['action'] == 'delete' and rec2['action'] == 'modify'):
                contradictions.append({
                    "pair": [rec1['id'], rec2['id']],
                    "reason": "Cannot modify deleted file"
                })
    
    if contradictions:
        return {"status": "FAIL", "contradictions": contradictions}
    
    return {"status": "PASS"}
```

---

### 4. Output Quality (Ã‡Ä±ktÄ± Kalitesi)
**Ne kontrol eder**: Raporun okunabilirliÄŸi ve faydalÄ±lÄ±ÄŸÄ±

```yaml
test_output_quality:
  name: "Rapor kalitesi"
  
  checks:
    - language_consistency:
        rule: "TÃ¼m rapor TÃ¼rkÃ§e olmalÄ± (eÄŸer belirtilmiÅŸse)"
        check: "Ä°ngilizce kelime oranÄ± < %10"
    
    - actionable_recommendations:
        rule: "Her Ã¶neri somut adÄ±mlar iÃ§ermeli"
        bad_example: "PerformansÄ± artÄ±r" âŒ
        good_example: "Bundle size'Ä± 847KB'dan 320KB'a dÃ¼ÅŸÃ¼r: lodash â†’ lodash-es" âœ…
    
    - code_examples:
        rule: "Ã–nemli Ã¶neriler kod Ã¶rneÄŸi iÃ§ermeli"
        threshold: "P0 ve P1 sorunlarÄ±n %80+i"
    
    - readability_score:
        rule: "Flesch reading ease > 60 (kolay okunur)"
        tool: "textstat.flesch_reading_ease()"
  
  auto_fix: true
  severity: "medium"
```

**Ã–rnek Test**:
```python
def test_actionable_recommendations(recommendations):
    """Ã–nerilerin somut olup olmadÄ±ÄŸÄ±nÄ± kontrol et"""
    
    vague_keywords = [
        'improve', 'optimize', 'enhance', 'better',
        'geliÅŸtir', 'iyileÅŸtir', 'dÃ¼zelt', 'yap'
    ]
    
    actionable_count = 0
    vague_recs = []
    
    for rec in recommendations:
        text = rec['text'].lower()
        
        # Somutluk kontrolleri
        has_numbers = any(char.isdigit() for char in text)
        has_file_ref = 'src/' in text or '.ts' in text
        has_code = 'code' in rec and len(rec['code']) > 0
        
        # Vague kelimeler var ama somut bilgi yok
        if (any(kw in text for kw in vague_keywords) and 
            not (has_numbers or has_file_ref or has_code)):
            vague_recs.append(rec['id'])
        else:
            actionable_count += 1
    
    ratio = actionable_count / len(recommendations)
    
    return {
        "status": "PASS" if ratio > 0.8 else "FAIL",
        "actionable_ratio": f"{ratio*100:.1f}%",
        "vague_recommendations": vague_recs
    }
```

---

## ðŸ”„ Test Execution Flow

```mermaid
graph TD
    A[Analysis Complete] --> B{Run Self-Tests}
    B --> C[Syntax Validation]
    C --> D{Pass?}
    D -->|No| E[Auto-fix if possible]
    E --> C
    D -->|Yes| F[Content Validation]
    F --> G{Pass?}
    G -->|No| H[Flag Issues]
    G -->|Yes| I[Logic Validation]
    I --> J{Pass?}
    J -->|No| K[Human Review Required]
    J -->|Yes| L[Output Quality]
    L --> M{Pass?}
    M -->|No| N[Improve & Re-test]
    M -->|Yes| O[âœ… Validation Complete]
    O --> P[Attach Confidence Score]
```

---

## ðŸ“Š Confidence Scoring

Her analiz bir **gÃ¼ven skoru** alÄ±r:

```yaml
confidence_score:
  calculation: |
    base_score = 100
    
    # Deductions
    - syntax_errors: -5 per error
    - content_warnings: -10 per warning
    - logic_failures: -20 per failure
    - quality_issues: -5 per issue
    
    # Bonuses
    + all_tests_pass: +10
    + has_code_examples: +5
    + references_real_files: +5
  
  interpretation:
    90-100: "Ã‡ok YÃ¼ksek - GÃ¼venle kullanÄ±labilir"
    70-89:  "YÃ¼ksek - Ä°nceleme sonrasÄ± kullan"
    50-69:  "Orta - Dikkatle kullan"
    0-49:   "DÃ¼ÅŸÃ¼k - Manuel review gerekli"
```

**Ã–rnek Ã‡Ä±ktÄ±**:
```markdown
## ðŸŽ¯ Validation Results

âœ… Syntax: PASS (0 errors)
âœ… Content: PASS (2 warnings)
âš ï¸ Logic: WARNING (1 contradiction detected)
âœ… Quality: PASS (readability: 72)

**Confidence Score**: 82/100 (YÃ¼ksek)

**Warnings**:
- Contradiction: Task 5 ve Task 8 aynÄ± dosyayÄ± deÄŸiÅŸtiriyor
- P0 issue count (12) normalden yÃ¼ksek

**Recommendation**: Ä°nceleme sonrasÄ± kullan âœ…
```

---

## ðŸŽ›ï¸ Configuration

```yaml
# .ai-self-test.yml
self_test:
  enabled: true
  
  run_on:
    - after_analysis: true
    - before_mode3_execution: true
    - on_demand: true
  
  test_suites:
    syntax:
      enabled: true
      auto_fix: true
      
    content:
      enabled: true
      auto_fix: false
      
    logic:
      enabled: true
      auto_fix: false
      
    quality:
      enabled: true
      auto_fix: true
  
  thresholds:
    minimum_confidence: 70  # Mode 3 iÃ§in
    warning_threshold: 50
    
  actions:
    if_fail_syntax: "auto_fix"
    if_fail_content: "warn_user"
    if_fail_logic: "block_mode3"
    if_fail_quality: "suggest_improvements"
```

---

## ðŸš¨ Integration with Modes

### Mode 1 (Analyze)
```
Analysis â†’ Self-Test â†’ Confidence Score â†’ Report
```
- Test fails â†’ Raporda uyarÄ± ekle
- Confidence score her zaman gÃ¶ster

### Mode 2 (Plan)
```
Analysis â†’ Self-Test â†’ Plan Generation â†’ Plan Validation â†’ Report
```
- Plan'da logic test Ã¶nemli
- Dependency order kontrolÃ¼

### Mode 3 (Execute)
```
Analysis â†’ Self-Test â†’ Confidence Check â†’ Execute (if >70)
```
- **BLOCKER**: Confidence <70 ise Mode 3 Ã§alÄ±ÅŸmaz
- User override seÃ§eneÄŸi

---

## âœ… Example: Full Test Run

```bash
# Self-test Ã§alÄ±ÅŸtÄ±rma
$ ai-analysis self-test analysis-report.md

Running Self-Test Suite v1.0...

[1/4] Syntax Validation
  âœ… Markdown syntax: PASS
  âœ… Code blocks: PASS
  âœ… YAML blocks: PASS
  âœ… Table format: PASS
  
[2/4] Content Validation
  âœ… Priority consistency: PASS
  âœ… Score ranges: PASS
  âš ï¸  File references: 2 warnings
      - src/old-file.ts not found (mentioned in line 45)
  âœ… Recommendations: PASS

[3/4] Logic Validation
  âœ… No contradictions: PASS
  âœ… Dependency order: PASS
  âš ï¸  Effort estimation: 1 warning
      - "Database migration: 30 min" might be underestimated
  âœ… Resource allocation: PASS

[4/4] Output Quality
  âœ… Language (Turkish): PASS (96% TR)
  âœ… Actionable recs: PASS (87%)
  âœ… Code examples: PASS (P0: 100%, P1: 80%)
  âœ… Readability: PASS (score: 68)

â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”

ðŸ“Š FINAL RESULTS

Tests Run: 16
Passed: 14
Warnings: 2
Failures: 0

Confidence Score: 88/100 â­ (YÃ¼ksek)

Recommendation: âœ… GÃ¼venle kullanÄ±labilir
(Warnings gÃ¶zden geÃ§irilebilir ama bloke edici deÄŸil)

â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”â”
```

---

## ðŸ”§ Extending Tests

Yeni test eklemek iÃ§in:

```python
# custom_tests.py

from self_test_suite import TestCase

class CustomTest(TestCase):
    """Ã–zel test senaryosu"""
    
    name = "My Custom Check"
    severity = "medium"
    
    def run(self, analysis_data):
        # Test logic burada
        if some_condition:
            return self.PASS()
        else:
            return self.FAIL("Reason here")
```

Sonra config'e ekle:
```yaml
custom_tests:
  - name: "CustomTest"
    enabled: true
    auto_fix: false
```

---

## ðŸ“š Related Documents

- `VALIDATION_RULES.md` - DetaylÄ± validation kurallarÄ±
- `TEST_SCENARIOS.md` - Ã–rnek test senaryolarÄ±
- `REGRESSION_TESTS.md` - Regresyon test suite'i
- `CONFIDENCE_SCORING.md` - GÃ¼ven skoru hesaplama

---

**Ã–nemli**: Self-testing sistemi %100 hatasÄ±zlÄ±k garantisi vermez, ama **risk seviyesini Ã¶lÃ§er** ve **ÅŸeffaflÄ±k saÄŸlar**. AI'a gÃ¼ven + doÄŸrulama = gÃ¼Ã§lÃ¼ sistem! ðŸ›¡ï¸
