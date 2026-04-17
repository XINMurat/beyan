#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ftfy kullanarak encoding bozulmasini duzeltir.
SKIP kalan dosyalar icin ek yontemler dener.
"""
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from pathlib import Path
import ftfy

ROOT   = Path(r"C:\TRAE\beyan-v1.0.0\project-analysis-system-v3.3.1")
BACKUP = Path(r"C:\TRAE\beyan-v1.0.0\_encoding_backup_20260417_094010\project-analysis-system-v3.3.1")

TR_CHARS = set('gusioçGUSIOC\u011f\u015f\u00fc\u00f6\u00e7\u0131\u011e\u015e\u00dc\u00d6\u00c7\u0130')
MOJI_PATTERNS = ['Ã', '\ufffd']

def has_turkish(text):
    return any(c in text for c in TR_CHARS)

def has_mojibake(text):
    return any(p in text for p in MOJI_PATTERNS)

def try_fix_ftfy(raw_bytes):
    """ftfy ile duzeltmeyi dene."""
    for enc in ['utf-8', 'latin-1', 'cp1252']:
        try:
            decoded = raw_bytes.decode(enc, errors='replace')
            fixed = ftfy.fix_text(decoded)
            if has_turkish(fixed) and not has_mojibake(fixed):
                return fixed, f'ftfy+{enc}'
        except Exception:
            continue
    return None, None

def try_manual(raw_bytes):
    """Manuel encoding zincirleri."""
    # Zincir 1: utf8 -> latin-1 -> utf8 (2 kat)
    try:
        s = raw_bytes.decode('utf-8', errors='replace')
        s = s.encode('latin-1', errors='replace').decode('utf-8', errors='replace')
        s = ftfy.fix_text(s)
        if has_turkish(s) and not has_mojibake(s):
            return s, 'manual-2x+ftfy'
    except Exception:
        pass

    # Zincir 2: 3 kat
    try:
        s = raw_bytes.decode('utf-8', errors='replace')
        s = s.encode('latin-1', errors='replace').decode('utf-8', errors='replace')
        s = s.encode('latin-1', errors='replace').decode('utf-8', errors='replace')
        s = ftfy.fix_text(s)
        if has_turkish(s) and not has_mojibake(s):
            return s, 'manual-3x+ftfy'
    except Exception:
        pass

    return None, None

# Sadece SKIP listesindeki dosyalari isle
skip_files = [
    "AGENTIC_WORKFLOW.md", "AI_VALIDATION_LAYER.md", "AUTOMATION_RULES.md",
    "BASE_PROMPT.md", "CHANGELOG-v3.3.1.md", "EXECUTION_LOG_TEMPLATE.md",
    "FEATURE_GAP_UPDATE.md", "FILE_MIGRATION_GUIDE.md", "FILE_SELECTION_GUIDE.md",
    "MODE_TRANSITIONS.md", "ORCHESTRATOR_PROMPT.md", "PROJECT-INTEL-DEMO.md",
    "QUICK_START.md", "REGRESSION_TESTS.md", "ROADMAP_GENERATOR.md",
    "ROLLBACK_PROCEDURES.md", "SAFETY_GATES.md", "SYSTEM_IMPROVEMENT_ACTION_PLAN.md",
    "TASK_BREAKDOWN.md", "TRACKING_TEMPLATE.md", "UNIFIED_PROMPTS.md",
    "USAGE_GUIDE.md", "VALIDATION_RULES.md",
]
skip_paths_sub = [
    "implementation-guides/accessibility-fixes.md",
    "implementation-guides/database-migration.md",
    "modules/core/accessibility-analysis.md",
    "modules/core/analytics-analysis.md",
    "modules/core/api-design-analysis.md",
    "modules/core/browser-compatibility.md",
    "modules/core/code-quality-patterns.md",
    "modules/core/database-analysis.md",
    "modules/core/developer-experience.md",
    "modules/core/file-structure-analysis.md",
    "modules/core/i18n-analysis.md",
    "modules/core/infrastructure.md",
    "modules/core/mobile-responsive.md",
    "modules/core/performance-analysis.md",
    "modules/core/refactoring-guide.md",
    "modules/core/security-analysis.md",
    "modules/core/seo-analysis.md",
    "modules/core/state-management.md",
    "modules/core/testing-strategy.md",
    "modules/core/ui-ux-analysis.md",
    "modules/specialized/ai-assisted-dev-analysis.md",
    "modules/specialized/dotnet-core.md",
    "modules/specialized/hidden-gems-deep-scan.md",
    "modules/specialized/project-intelligence.md",
    "modules/specialized/react-typescript.md",
    "modules/specialized/umt-architecture.md",
    "modules/testing/collaboration-test.md",
    "modules/testing/ui-interaction-test.md",
]

all_targets = [(BACKUP / f, ROOT / f) for f in skip_files]
all_targets += [(BACKUP / f.replace('/', '\\'), ROOT / f.replace('/', '\\')) for f in skip_paths_sub]

fixed = 0
still_skip = 0

print(f"SKIP dosyalar isleniyor: {len(all_targets)}\n")

for backup_file, target_file in all_targets:
    if not backup_file.exists():
        print(f"[NOT FOUND] {backup_file.name}")
        continue

    with open(backup_file, 'rb') as f:
        raw = f.read()

    # Once ftfy dene
    fixed_text, method = try_fix_ftfy(raw)
    if not fixed_text:
        fixed_text, method = try_manual(raw)

    if fixed_text:
        target_file.parent.mkdir(parents=True, exist_ok=True)
        with open(target_file, 'w', encoding='utf-8', newline='\n') as f:
            f.write(fixed_text)
        print(f"[{method:20s}] {backup_file.name}")
        fixed += 1
    else:
        print(f"[STILL SKIP          ] {backup_file.name}")
        still_skip += 1

print(f"\n{'='*55}")
print(f"Bu turda duzeltilen : {fixed}")
print(f"Hala SKIP           : {still_skip}")
