# Fact Checking Rules - Olgu Do�?rulama Kuralları

**Version**: 1.0  
**Purpose**: AI'ın somut iddialarını do�?rulama  
**Philosophy**: "Güven ama do�?rula" (Trust but verify)

---

## �??� Fact Checking Nedir?

**Fact**: Somut, do�?rulanabilir iddia  
**Fiction/Hallucination**: Do�?rulanamayan, yanlı�? iddia

```yaml
�?? FACT: "package.json'da react@18.2.0 var"
  �?? Do�?rulanabilir (dosyayı kontrol et)

�? OPINION: "React en iyi framework'tür"
  �?? Do�?rulanamaz (subjektif)

�? HALLUCINATION: "src/NonExistent.ts:45'te hata var"
  �?? Do�?rulanabilir ama YANLI�? (dosya yok)
```

---

## �??? Fact Categories

### Category 1: File & Code Facts

#### Rule FC-001: File Existence
```yaml
rule_id: FC-001
name: "Referenced files must exist"
category: critical
auto_verify: true

check: |
  For each file path mentioned in output:
    1. Verify file exists in project
    2. If line number given, check it's within range
    3. If code snippet given, verify it matches

examples:
  �?? PASS:
    claim: "Found in src/App.tsx:15"
    verification: "File exists, has 150 lines"
    
  �? FAIL:
    claim: "Found in src/Deleted.ts:30"
    verification: "File not found"
    action: "Flag as hallucination"

severity: high
auto_fix: false  # Can't auto-fix missing files
```

#### Rule FC-002: Code Syntax Validity
```yaml
rule_id: FC-002
name: "Code examples must be syntactically valid"
category: high
auto_verify: true

check: |
  For each code block in output:
    1. Extract language (typescript, python, etc.)
    2. Parse with language parser
    3. Verify no syntax errors

examples:
  �?? PASS:
    code: "const x = 5;"
    language: "typescript"
    verification: "Valid syntax"
    
  �? FAIL:
    code: "const x = ;"
    language: "typescript"
    verification: "SyntaxError: Unexpected token ;"
    action: "Fix or remove code example"

severity: high
auto_fix: true  # Can attempt to fix simple errors
```

#### Rule FC-003: Import Statements
```yaml
rule_id: FC-003
name: "Imports must match actual dependencies"
category: medium
auto_verify: true

check: |
  For code examples with imports:
    1. Extract import statements
    2. Check package.json for dependency
    3. Verify version compatibility

examples:
  �?? PASS:
    code: "import React from 'react'"
    package.json: "dependencies: { react: ^18.0.0 }"
    verification: "Dependency exists"
    
  �? FAIL:
    code: "import Vue from 'vue'"
    package.json: "dependencies: { react: ^18.0.0 }"
    verification: "Vue not in dependencies"
    action: "Flag as potential error"

severity: medium
auto_fix: false
```

---

### Category 2: Dependency Facts

#### Rule FC-010: Package Versions
```yaml
rule_id: FC-010
name: "Package versions must exist"
category: critical
auto_verify: true
external_check: true

check: |
  For each package version mentioned:
    1. Query NPM/NuGet registry
    2. Verify version exists
    3. Check if it's latest/deprecated

examples:
  �?? PASS:
    claim: "React 18.2.0"
    verification: "NPM registry confirms"
    
  �? FAIL:
    claim: "React 18.5.2"
    verification: "Version doesn't exist (latest: 18.2.0)"
    action: "Correct to actual version"

severity: critical
auto_fix: true  # Can auto-correct to actual version
```

#### Rule FC-011: Dependency Vulnerabilities
```yaml
rule_id: FC-011
name: "Vulnerability counts must be accurate"
category: high
auto_verify: true
external_check: true

check: |
  If claiming "X vulnerabilities found":
    1. Run npm audit or similar
    2. Count actual vulnerabilities
    3. Compare with claim

examples:
  �?? PASS:
    claim: "12 vulnerabilities found"
    verification: "npm audit shows 12"
    
  �? FAIL:
    claim: "25 critical vulnerabilities"
    verification: "npm audit shows 2 critical, 23 total"
    action: "Correct the count and severity"

severity: high
auto_fix: true
```

---

### Category 3: Metric Facts

#### Rule FC-020: Score Ranges
```yaml
rule_id: FC-020
name: "Scores must be within valid range"
category: critical
auto_verify: true

check: |
  For all scores (X/10 format):
    1. Score must be 0-10
    2. Decimals allowed (8.5/10)
    3. No negative or >10

examples:
  �?? PASS:
    score: "8.5/10"
    verification: "Within 0-10 range"
    
  �? FAIL:
    score: "12/10"
    verification: "Exceeds maximum"
    action: "Clamp to 10/10"

severity: critical
auto_fix: true  # Auto-clamp to valid range
```

#### Rule FC-021: Performance Metrics
```yaml
rule_id: FC-021
name: "Performance metrics must be realistic"
category: high
auto_verify: true

check: |
  For performance claims:
    - Bundle size: 1KB - 50MB (realistic range)
    - Load time: 0.1s - 60s
    - API response: 1ms - 30s
    - FCP, LCP: realistic web vitals

examples:
  �?? PASS:
    claim: "Bundle size: 847KB"
    verification: "Within realistic range"
    
  �? FAIL:
    claim: "Bundle size: 5GB"
    verification: "Unrealistic for web app"
    action: "Flag as likely error"

severity: high
auto_fix: false
```

---

### Category 4: Project Structure Facts

#### Rule FC-030: Directory Existence
```yaml
rule_id: FC-030
name: "Mentioned directories must exist"
category: medium
auto_verify: true

check: |
  For directory references:
    1. Verify directory exists
    2. Check it's not empty (if relevant)

examples:
  �?? PASS:
    claim: "src/components/ contains 15 files"
    verification: "Directory exists, 15 files found"
    
  �? FAIL:
    claim: "Found issues in controllers/ folder"
    verification: "Directory not found"
    action: "Flag as potential hallucination"

severity: medium
auto_fix: false
```

---

### Category 5: Historical Facts

#### Rule FC-040: Git History
```yaml
rule_id: FC-040
name: "Git history claims must be verifiable"
category: low
auto_verify: true

check: |
  If mentioning git history:
    1. Run git log
    2. Verify claims about commits, dates

examples:
  �?? PASS:
    claim: "Last commit: 2 days ago"
    verification: "git log shows commit 2 days ago"
    
  �?�️ SKIP:
    claim: "File hasn't been touched in 6 months"
    verification: "Cannot verify (no git access)"
    action: "Skip check, add disclaimer"

severity: low
auto_fix: false
```

---

## �??� Verification Methods

### Method 1: Local Verification
```python
def verify_file_existence(file_path):
    """Dosya var mı kontrol et"""
    
    import os
    
    if not os.path.exists(file_path):
        return {
            'verified': False,
            'method': 'local_filesystem',
            'error': f'File not found: {file_path}',
            'confidence': 0.0
        }
    
    # Line number check if provided
    if line_number:
        with open(file_path) as f:
            max_lines = sum(1 for _ in f)
        
        if line_number > max_lines:
            return {
                'verified': False,
                'error': f'Line {line_number} exceeds file length ({max_lines})'
            }
    
    return {
        'verified': True,
        'method': 'local_filesystem',
        'confidence': 1.0
    }
```

### Method 2: External API Verification
```python
def verify_package_version(package, version):
    """NPM registry'den do�?rula"""
    
    import requests
    
    url = f'https://registry.npmjs.org/{package}'
    response = requests.get(url)
    
    if response.status_code != 200:
        return {
            'verified': False,
            'method': 'npm_registry',
            'error': 'Package not found',
            'confidence': 0.0
        }
    
    data = response.json()
    versions = list(data.get('versions', {}).keys())
    
    if version in versions:
        return {
            'verified': True,
            'method': 'npm_registry',
            'latest': data.get('dist-tags', {}).get('latest'),
            'confidence': 1.0
        }
    
    return {
        'verified': False,
        'method': 'npm_registry',
        'error': f'Version {version} not found',
        'available_versions': versions[-5:],  # Last 5
        'confidence': 0.0
    }
```

### Method 3: Code Parser Verification
```python
def verify_code_syntax(code, language):
    """Kod syntax'ını kontrol et"""
    
    parsers = {
        'typescript': parse_typescript,
        'python': compile_python,
        'csharp': roslyn_parse
    }
    
    if language not in parsers:
        return {
            'verified': None,
            'error': f'No parser for {language}',
            'confidence': 0.5  # Neutral
        }
    
    try:
        parsers[language](code)
        return {
            'verified': True,
            'method': f'{language}_parser',
            'confidence': 1.0
        }
    except SyntaxError as e:
        return {
            'verified': False,
            'method': f'{language}_parser',
            'error': str(e),
            'confidence': 0.0
        }
```

---

## �??? Fact Check Report

```markdown
# Fact Check Report

**Analysis**: analysis-report-20241220.md  
**Checked**: 2024-12-20 15:45  
**Total Claims**: 47  
**Verified**: 42 (89%)  
**Failed**: 3 (6%)  
**Skipped**: 2 (4%)

---

## �?? Verified Claims (42)

### File References (18/20)
�?? src/App.tsx:15 �?? File exists, line valid
�?? src/components/Header.tsx:42 �?? Valid
�? src/old-service.ts:30 �?? **File not found**
�? public/legacy.html:5 �?? **File not found**

### Package Versions (10/10)
�?? react@18.2.0 �?? NPM verified
�?? typescript@5.0.4 �?? NPM verified
[... all verified ...]

### Metrics (12/12)
�?? Security: 8.5/10 �?? Valid range
�?? Bundle: 847KB �?? Realistic
[... all verified ...]

### Code Examples (2/3)
�?? TypeScript snippet #1 �?? Valid syntax
�?? C# snippet #2 �?? Valid syntax
�? Python snippet #3 �?? **SyntaxError: unexpected EOF**

---

## �? Failed Verifications (3)

### 1. File Reference Hallucination
**Claim**: "Found SQL injection in src/old-service.ts:30"
**Issue**: File not found  
**Severity**: High  
**Action**: Remove from report or mark as "historical reference"

### 2. File Reference Hallucination
**Claim**: "Missing meta tags in public/legacy.html:5"
**Issue**: File not found  
**Severity**: Medium  
**Action**: Verify if file was recently deleted

### 3. Invalid Code Example
**Claim**: [Code example in Python]
**Issue**: SyntaxError: unexpected EOF while parsing  
**Severity**: Medium  
**Action**: Fix code example or remove

---

## ⏭️ Skipped Checks (2)

### 1. Git History Claim
**Claim**: "File last modified 6 months ago"
**Reason**: No git access in verification environment  
**Action**: Manual verification if important

### 2. External API Claim
**Claim**: "Production has 50K daily users"
**Reason**: Cannot verify external analytics  
**Action**: Trust user's data

---

## �??� Overall Fact Check Score

**89% verified** (42/47)

**Recommendation**: High confidence, address 3 failed verifications

**Impact on Confidence Score**: -11 points (3 failures * high severity)
```

---

## �??� Configuration

```yaml
# .ai-fact-check-config.yml

fact_checking:
  enabled: true
  
  auto_verify:
    file_existence: true
    code_syntax: true
    package_versions: true
    score_ranges: true
    
  external_apis:
    npm_registry: true
    github_api: false  # Requires token
    
  skip_categories:
    - git_history  # No git access
    - external_metrics  # Can't verify analytics
    
  severity_weights:
    critical: -20  # Points deduction
    high: -10
    medium: -5
    low: -2
    
  auto_fix:
    enabled: true
    fix_types:
      - score_clamping
      - version_correction
      - simple_syntax_fixes
```

---

## �??? Related Documents

- `AI_VALIDATION_LAYER.md` - Overall validation
- `CONFIDENCE_SCORING.md` - How failures affect score
- `UNCERTAINTY_HANDLING.md` - What to do with unverified claims

---

**Facts don't care about feelings. Verify everything!** �??�
