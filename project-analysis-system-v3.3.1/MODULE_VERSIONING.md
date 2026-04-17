# Module Versioning Policy

**System**: Project Analysis System  
**Version**: 1.0  
**Last Updated**: 20 Aralık 2024

---

## �??� Semantic Versioning

Tüm modüller [Semantic Versioning 2.0.0](https://semver.org/) kullanır:

```
MAJOR.MINOR.PATCH

Example: 1.4.2
```

### MAJOR (Breaking Changes)
```yaml
When: Module çıktı formatı de�?i�?ti
Example: 
  v1.x.x �?? Report format: Markdown
  v2.0.0 �?? Report format: JSON (BREAKING!)
  
Action Required: Kullananlar kodlarını güncellemeli
```

### MINOR (New Features)
```yaml
When: Yeni analiz eklendi, eski özellikler çalı�?ıyor
Example:
  v1.3.0 �?? Added SQL injection detection
  v1.4.0 �?? Added N+1 query detection
  
Action Required: None (backward compatible)
```

### PATCH (Bug Fixes)
```yaml
When: Hata düzeltmesi, hiçbir �?ey de�?i�?medi
Example:
  v1.4.1 �?? Fixed false positive in SQL detection
  v1.4.2 �?? Improved regex pattern
  
Action Required: None
```

---

## �??� Current Module Versions (v3.3)

### P0 Modules
```yaml
file_structure_analysis: "1.0.0"
performance_analysis: "1.0.0"
ui_ux_analysis: "1.0.0"
```

### P1 Modules
```yaml
security_analysis: "1.0.0"
database_analysis: "1.0.0"
api_design_analysis: "1.0.0"
developer_experience: "1.0.0"
hidden_gems_deep_scan: "1.0.0"
```

### P2 Modules
```yaml
accessibility_analysis: "1.0.0"
testing_strategy: "1.0.0"
internationalization_analysis: "1.0.0"
state_management_analysis: "1.0.0"
monitoring_observability: "1.0.0"
browser_compatibility: "1.0.0"
code_quality_patterns: "1.0.0"
```

### P3 Modules
```yaml
seo_analysis: "1.0.0"
analytics_analysis: "1.0.0"
mobile_responsive_analysis: "1.0.0"
infrastructure_analysis: "1.0.0"
```

### Specialized Modules
```yaml
ai_assisted_dev_analysis: "1.0.0"
turkish_market_specifics: "1.0.0"
dotnet_core_analysis: "1.0.0"
react_typescript_analysis: "1.0.0"
```

### System Modules (v3.3 NEW)
```yaml
self_test_suite: "1.0.0"
ai_validation_layer: "1.0.0"
```

---

## �??? Version Compatibility Matrix

### ORCHESTRATOR Compatibility

| ORCHESTRATOR | Min Module Version | Max Module Version | Notes |
|--------------|-------------------|-------------------|-------|
| v3.3 | 1.0.0 | 2.x.x | Supports v1 and v2 modules |
| v3.2 | 1.0.0 | 1.x.x | Only v1 modules |
| v3.1 | 1.0.0 | 1.x.x | Only v1 modules |

### Module Compatibility

```yaml
security_analysis:
  v1.0.0: Compatible with ORCHESTRATOR v3.2+
  v1.1.0: Added OWASP Top 10 2023 (compatible)
  v2.0.0: JSON output format (requires ORCHESTRATOR v3.3+)
```

---

## �??� CHANGELOG Template

Her modül bir CHANGELOG.md dosyasına sahip olmalı:

```markdown
# Changelog - security_analysis.md

All notable changes to this module will be documented here.

Format: [Keep a Changelog](https://keepachangelog.com/)
Versioning: [Semantic Versioning](https://semver.org/)

---

## [Unreleased]
### Added
- CSRF token validation check

### Changed
- N/A

### Deprecated
- N/A

### Removed
- N/A

### Fixed
- N/A

---

## [1.1.0] - 2024-12-20
### Added
- OWASP Top 10 2023 support
- XXE (XML External Entity) detection
- SSRF (Server-Side Request Forgery) check

### Changed
- Improved SQL injection pattern matching
- Updated confidence scoring

### Fixed
- False positive in XSS detection for sanitized inputs

---

## [1.0.0] - 2024-11-15
### Added
- Initial release
- SQL injection detection
- XSS vulnerability scan
- Authentication bypass checks
- Sensitive data exposure detection

---

[Unreleased]: https://github.com/user/repo/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/user/repo/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/user/repo/releases/tag/v1.0.0
```

---

## �?�️ Deprecation Policy

### Deprecation Timeline

```yaml
Step 1: Announce (MINOR version bump)
  Example: v1.5.0
  Message: "Feature X is deprecated, use Y instead"
  Action: Add deprecation warning to module
  
Step 2: Keep for 2 versions
  v1.5.0: Deprecated (warning)
  v1.6.0: Still works (warning)
  v1.7.0: Still works (warning)
  
Step 3: Remove (MAJOR version bump)
  v2.0.0: Feature X removed
  Action: Breaking change, users must migrate
```

### Deprecation Warning Format

```markdown
�?�️ DEPRECATION WARNING

Feature: "Old confidence scoring method"
Deprecated in: v1.5.0
Will be removed in: v2.0.0
Migration guide: See MIGRATION_1.5_to_2.0.md

Use instead: "New confidence scoring with uncertainty levels"

Example:
OLD: confidence_score: 0.85
NEW: confidence: { score: 0.85, level: "high", uncertainty: "medium" }
```

---

## �??? Migration Guides

### Format: MIGRATION_X.Y_to_Z.W.md

```markdown
# Migration Guide: v1.5 �?? v2.0
**Module**: security_analysis.md  
**Date**: 2025-01-15  
**Breaking Changes**: Yes

---

## Overview

v2.0 changes the output format from Markdown to JSON.

**Impact**: HIGH (all users affected)
**Migration Effort**: 2-4 hours
**Backward Compatibility**: No

---

## Breaking Changes

### 1. Output Format

**Before (v1.x)**:
```markdown
# Security Issues

## SQL Injection
**Severity**: High
**Location**: OrderService.cs:45
```

**After (v2.0)**:
```json
{
  "security_issues": [
    {
      "type": "sql_injection",
      "severity": "high",
      "location": "OrderService.cs:45"
    }
  ]
}
```

### 2. Confidence Scoring

**Before (v1.x)**:
```
confidence_score: 0.85
```

**After (v2.0)**:
```json
{
  "confidence": {
    "score": 0.85,
    "level": "high",
    "uncertainty": "medium"
  }
}
```

---

## Migration Steps

### Step 1: Update MANIFEST.yaml
```yaml
modules:
  security_analysis:
    version: "2.0.0"  # Update this
```

### Step 2: Update Parser Code
```diff
- report = parse_markdown(output)
+ report = JSON.parse(output)
```

### Step 3: Test
```bash
npm test -- security-analysis
```

### Step 4: Deploy
- Stage: Deploy v2.0
- Production: After 1 week testing

---

## Rollback Plan

If issues arise:

```yaml
# Revert MANIFEST.yaml
modules:
  security_analysis:
    version: "1.7.0"  # Back to v1

# Clear cache
rm -rf /tmp/module-cache/security_analysis
```

---

## Support

- **v1.x support ends**: 2025-06-01 (6 months from v2.0 release)
- **Questions**: support@example.com
- **Community**: Discord #migrations
```

---

## �??� Version Lock

### Lock File: .ai-module-versions.lock

```yaml
# Auto-generated - DO NOT EDIT MANUALLY
# Last updated: 2024-12-20

locked_versions:
  security_analysis: "1.5.0"
  performance_analysis: "1.2.0"
  ui_ux_analysis: "1.0.0"
  
lock_reason: "Production stability - tested combination"
  
update_policy:
  auto_update: false  # Manual updates only
  allow_patch: true   # 1.5.0 �?? 1.5.1 OK
  allow_minor: false  # 1.5.0 �?? 1.6.0 NOT OK (requires approval)
  allow_major: false  # 1.5.0 �?? 2.0.0 NOT OK (requires migration)
```

### Lock Update Process

```bash
# Check for updates
ai-modules check-updates

Output:
�??� security_analysis: 1.5.0 �?? 1.6.0 (minor update available)
�??� performance_analysis: 1.2.0 �?? 1.2.1 (patch available)

# Update patch (safe)
ai-modules update --patch
Updated: performance_analysis 1.2.0 �?? 1.2.1 �??

# Update minor (requires approval)
ai-modules update --minor security_analysis
�?�️ This is a minor version update. Review CHANGELOG:
- Added: New OWASP checks
- Changed: Improved confidence scoring

Approve? [y/N]: y
Updated: security_analysis 1.5.0 �?? 1.6.0 �??
```

---

## �?�� Version Testing

### Test Matrix

| Module Version | ORCHESTRATOR v3.2 | ORCHESTRATOR v3.3 | ORCHESTRATOR v3.4 |
|----------------|------------------|------------------|------------------|
| security v1.0 | �?? Pass | �?? Pass | �?? Pass |
| security v1.5 | �?? Pass | �?? Pass | �?? Pass |
| security v2.0 | �? Fail | �?? Pass | �?? Pass |

### Test Scenario

```bash
# Run compatibility test
npm run test:compatibility

Test Suite: Module Version Compatibility
�?? security_analysis v1.5.0 + ORCHESTRATOR v3.3
�?? performance_analysis v1.2.0 + ORCHESTRATOR v3.3
�?? ui_ux_analysis v1.0.0 + ORCHESTRATOR v3.3

All tests passed (12/12)
```

---

## �??? Version Dashboard

```markdown
# Module Version Status

Last check: 2024-12-20 14:30 UTC

| Module | Current | Latest | Status | Action |
|--------|---------|--------|--------|--------|
| security_analysis | 1.5.0 | 1.6.0 | �??� Update available | Review changelog |
| performance_analysis | 1.2.1 | 1.2.1 | �??� Up to date | None |
| ui_ux_analysis | 1.0.0 | 2.0.0 | �??� Major update | Migration required |
| database_analysis | 1.1.0 | 1.1.2 | �??� Patch available | Safe to update |

Legend:
�??� Up to date
�??� Update available (safe)
�??� Breaking changes (manual review)
```

---

## �??� Best Practices

### DO �??

1. **Always use version numbers in MANIFEST**
```yaml
modules:
  security_analysis:
    version: "1.5.0"  # Specific version
```

2. **Read CHANGELOG before updating**
```bash
cat modules/security_analysis/CHANGELOG.md
```

3. **Test in staging first**
```bash
# Stage environment
ai-modules update --env=staging
ai-modules test --env=staging
# If OK, then production
```

4. **Lock versions in production**
```yaml
update_policy:
  auto_update: false  # Manual only
```

### DON'T �?

1. **Don't use wildcards in production**
```yaml
# BAD
modules:
  security_analysis:
    version: "1.*"  # Unpredictable

# GOOD
modules:
  security_analysis:
    version: "1.5.0"  # Locked
```

2. **Don't skip MINOR versions**
```bash
# BAD: 1.3.0 �?? 1.5.0 (skipped 1.4.0)
# GOOD: 1.3.0 �?? 1.4.0 �?? 1.5.0
```

3. **Don't ignore deprecation warnings**
```markdown
�?�️ DEPRECATION: Feature X will be removed in v2.0
Action: Plan migration NOW, don't wait
```

---

## �??? Related Documents

- `CHANGELOG_TEMPLATE.md` - How to write changelogs
- `MIGRATION_GUIDES/` - Folder for all migration guides
- `DEPRECATION_WARNINGS.md` - Active deprecations
- `MANIFEST_V2.yaml` - Module registry with versions

---

**�?zet**: Her modül versiyonlu, de�?i�?iklikler takip ediliyor, upgrade planlanabilir. �???

---

**Version**: 1.0  
**Next Update**: When first module hits v1.1.0  
**Feedback**: Versiyonlama stratejisi yeterli mi?
