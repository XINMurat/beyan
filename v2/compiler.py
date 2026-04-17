#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Beyan v2.0 — Compiler Module
Loads MANIFEST, selects modules, and compiles the final prompt.
"""

import sys
from pathlib import Path


# Optional dependencies
try:
    import tiktoken  # type: ignore
    _ENCODER = tiktoken.get_encoding("cl100k_base")
    HAS_TIKTOKEN = True
except (ImportError, ModuleNotFoundError):
    _ENCODER = None
    HAS_TIKTOKEN = False


def calculate_tokens(text: str) -> int:
    """
    Accurate token calculation using tiktoken (cl100k_base).
    Falls back to heuristic (len/4) if tiktoken is not installed.
    """
    if HAS_TIKTOKEN and _ENCODER:
        return len(_ENCODER.encode(text))
    return len(text) // 4


# Mode-specific prompt suffixes injected at the end of every compiled prompt
_MODE_SUFFIX = {
    "tr": {
        1: """
---
## 3. Görev: Mode 1 — Analiz Raporu

Yukarıdaki modüllerin yönergelerini izleyerek hedef projeyi analiz et.
Çıktını aşağıdaki yapıda üret:

1. **🧠 Project Intelligence** — Proje tipi, olgunluk, drift
2. **🔒 Güvenlik** — OWASP bulgular, P0/P1/P2 öncelikli
3. **⚡ Performans** — Darboğazlar, ölçüm tablosu
4. **📁 Dosya Yapısı** — Mimari uyum / ihlaller
5. **📊 Sağlık Skoru** — Ağırlıklı nihai skor (0-10)
6. **🎯 Aksiyon Planı** — P0 → P1 → P2 → P3 sıralı görev listesi
""",
        2: """
---
## 3. Görev: Mode 2 — Analiz + Uygulama Planı

**Adım A:** Mode 1 analizini tam olarak çalıştır.
**Adım B:** Bulgulara dayanarak aşağıdaki yapıda bir `implementation_plan.md` üret:

```markdown
# Uygulama Planı — [Proje Adı]
**Oluşturulma:** [Tarih]
**Kaynak:** Beyan v2.0 Mode 2 Analizi

---

## Sprint 1 — Kritik Düzeltmeler (P0)
| # | Görev | Dosya:Satır | Süre | Risk |
|---|-------|-------------|------|------|
| 1 | [P0 bulgu] | [konum] | [X saat] | [Düşük/Orta/Yüksek] |

## Sprint 2 — Önemli İyileştirmeler (P1)
...

## Sprint 3 — Kalite İyileştirmeleri (P2)
...

## Başarı Kriterleri
- [ ] Sağlık skoru >= 8.5
- [ ] Sıfır P0 bulgu
- [ ] Test kapsamı >= %70
```

Kullanıcı onayı olmadan kod değiştirme.
""",
        3: """
---
## 3. Görev: Mode 3 — Yarı-Otonom Düzeltme Akışı

**CHECKPOINT SİSTEMİ AKTİF** — Her kritik noktada kullanıcı onayı gerekiyor.

**Akış:**

### 🔍 CHECKPOINT #1: Analiz Tamamlandı
Mode 1 analizini çalıştır, ardından kullanıcıya sor:
```
📊 Analiz Tamamlandı
─────────────────────────────
P0 (Kritik): X sorun
P1 (Yüksek): Y sorun
Tahmini toplam süre: Z saat

Otomatik düzeltilecek P0 sorunları:
1. [Sorun] — [Dosya:Satır] — [Süre]

Devam edilsin mi?
[EVET — Düzelt] [HAYIR — Sadece rapor ver] [PLAN GÖSTER]
```

### 🔍 CHECKPOINT #2: Kod Değişiklikleri
Her otomatik düzeltmeden önce:
```
🔧 Düzeltme: [Sorun başlığı]
Dosya: [yol:satır]

❌ Mevcut:
[eski kod]

✅ Önerilen:
[yeni kod]

Bu değişikliği uygulayayım mı?
[EVET] [HAYIR] [TÜM P0 EVET] [İPTAL]
```

### 🔍 CHECKPOINT #3: Commit Onayı
```
✅ X dosya değiştirildi, Y test eklendi.
Git commit edilsin mi?
Branch: fix/beyan-p0-[tarih]
[COMMIT] [SADECE KAYDET] [GERI AL]
```

**GÜVENLİK KURALLARI:**
- Veritabanı migrasyon dosyalarına dokunma
- Production config dosyalarını değiştirme
- Bir seferde max 20 dosya
""",
    },
    "en": {
        1: """
---
## 3. Task: Mode 1 — Analysis Report

Follow the module guidelines above to analyze the target project.
Produce your output in this structure:

1. **🧠 Project Intelligence** — Type, maturity, drift
2. **🔒 Security** — OWASP findings, P0/P1/P2 prioritized
3. **⚡ Performance** — Bottlenecks, measurement table
4. **📁 File Structure** — Architecture compliance / violations
5. **📊 Health Score** — Weighted final score (0-10)
6. **🎯 Action Plan** — P0 → P1 → P2 → P3 ordered task list
""",
        2: """
---
## 3. Task: Mode 2 — Analysis + Implementation Plan

**Step A:** Run the full Mode 1 analysis.
**Step B:** Based on findings, generate an `implementation_plan.md` with this structure:

```markdown
# Implementation Plan — [Project Name]
**Generated:** [Date]
**Source:** Beyan v2.0 Mode 2 Analysis

---

## Sprint 1 — Critical Fixes (P0)
| # | Task | File:Line | Effort | Risk |
|---|------|-----------|--------|------|
| 1 | [P0 finding] | [location] | [X hrs] | [Low/Med/High] |

## Sprint 2 — High Priority (P1)
...

## Sprint 3 — Quality Improvements (P2)
...

## Success Criteria
- [ ] Health score >= 8.5
- [ ] Zero P0 findings
- [ ] Test coverage >= 70%
```

Do NOT change any code without user approval.
""",
        3: """
---
## 3. Task: Mode 3 — Semi-Autonomous Fix Flow

**CHECKPOINT SYSTEM ACTIVE** — User approval required at every critical step.

**Flow:**

### 🔍 CHECKPOINT #1: Analysis Complete
Run Mode 1 analysis, then prompt the user:
```
📊 Analysis Complete
─────────────────────────────
P0 (Critical): X issues
P1 (High): Y issues
Estimated total time: Z hours

P0 issues eligible for auto-fix:
1. [Issue] — [File:Line] — [Time]

Proceed?
[YES — Fix] [NO — Report only] [SHOW PLAN]
```

### 🔍 CHECKPOINT #2: Code Changes
Before each automated fix:
```
🔧 Fix: [Issue title]
File: [path:line]

❌ Current:
[old code]

✅ Proposed:
[new code]

Apply this change?
[YES] [NO] [YES TO ALL P0] [CANCEL]
```

### 🔍 CHECKPOINT #3: Commit Approval
```
✅ X files changed, Y tests added.
Commit to Git?
Branch: fix/beyan-p0-[date]
[COMMIT] [SAVE ONLY] [ROLLBACK]
```

**SAFETY RULES:**
- Never touch database migration files
- Never modify production config files
- Max 20 files per run
""",
    }
}


def load_manifest(manifest_path: Path) -> dict:
    """Loads and parses MANIFEST.yaml."""
    try:
        import yaml
    except ImportError:
        print("PyYAML bulunamadi. Lutfen yukleyin: pip install pyyaml")
        sys.exit(1)
    with open(manifest_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def select_modules(manifest: dict, discovered_tags: list, lang: str) -> list:
    """
    Selects which modules to load based on discovered technology tags.
    P0 modules are always loaded. Resolves dependencies recursively.
    """
    modules_to_load = set()
    all_modules = manifest.get("modules", {})

    # Initial selection based on tags and priority
    for mod_key, mod_info in all_modules.items():
        priority = mod_info.get("priority", "P3")
        auto_load_if = mod_info.get("auto_load_if", [])

        if priority == "P0" or mod_info.get("auto_load") is True:
            modules_to_load.add(mod_key)
            continue

        if any(tag in discovered_tags for tag in auto_load_if):
            modules_to_load.add(mod_key)

    if not modules_to_load:
        fallback_msg = (
            "[*] No exact match found, 'web_mobile' loading as default domain."
            if lang == "en" else
            "[*] Kesin eslesme bulunamadi, 'web_mobile' varsayilan domain olarak yukleniyor."
        )
        print(fallback_msg)
        modules_to_load.add("web_mobile")

    # Recursive dependency resolution
    def resolve_deps(mod_key):
        deps = all_modules.get(mod_key, {}).get("dependencies", [])
        for dep in deps:
            if dep in all_modules and dep not in modules_to_load:
                modules_to_load.add(dep)
                resolve_deps(dep)

    # Use a copy of the set to iterate while modifying (or just convert to list)
    initial_selection = list(modules_to_load)
    for mod_key in initial_selection:
        resolve_deps(mod_key)

    return sorted(list(modules_to_load))


def compile_prompt(system_root: Path, manifest: dict, modules_to_load: list,
                   mode: int, lang: str) -> str:
    """
    Assembles the final prompt from BASE_PROMPT, ORCHESTRATOR_PROMPT, selected modules,
    and a mode-specific task suffix.
    Returns the compiled prompt string.
    """
    compiled_text = f"# Beyan v2.0 - Mode {mode} Run ({lang.upper()})\n\n"
    compiled_text += "## 1. Core Engine Rules\n\n"

    try:
        base_path = manifest.get("base_prompt", "core_prompts/{lang}/BASE_PROMPT.md").replace("{lang}", lang)
        orc_path = manifest.get("orchestrator_prompt", "core_prompts/{lang}/ORCHESTRATOR_PROMPT.md").replace("{lang}", lang)
        with open(system_root / base_path, "r", encoding="utf-8") as f:
            compiled_text += f.read() + "\n\n"
        with open(system_root / orc_path, "r", encoding="utf-8") as f:
            compiled_text += f.read() + "\n\n"
    except Exception as e:
        err = f"[ERROR] Failed to read core files: {e}" if lang == "en" else f"[HATA] Core dosyalar okunamadi: {e}"
        print(err)

    compiled_text += "## 2. Domain & Focus Modules\n\n"

    for mod_key in modules_to_load:
        mod_path_str = manifest["modules"][mod_key]["path"].replace("{lang}", lang)
        mod_path = system_root / mod_path_str
        if mod_path.exists():
            with open(mod_path, "r", encoding="utf-8") as f:
                compiled_text += f"### Module: {mod_key}\n"
                compiled_text += f.read() + "\n\n"
        else:
            warn = (f"[WARNING] Module file not found: {mod_path}"
                    if lang == "en" else f"[UYARI] Modul dosyasi bulunamadi: {mod_path}")
            print(warn)

    # Inject mode-specific task instructions
    lang_suffixes = _MODE_SUFFIX.get(lang, _MODE_SUFFIX["en"])
    compiled_text += lang_suffixes.get(mode, lang_suffixes[1])

    return compiled_text


def check_token_budget(compiled_text: str, manifest: dict, lang: str) -> tuple[int, bool]:
    """
    Checks token budget against MANIFEST limit.
    Returns (total_tokens, is_exceeded).
    """
    max_tokens = manifest.get("max_total_tokens", 35000)
    total_tokens = calculate_tokens(compiled_text)
    is_exceeded = total_tokens > max_tokens

    if lang == "en":
        print(f"[*] Estimated Token Cost: {total_tokens} (Limit: {max_tokens})")
        if is_exceeded:
            print(f"[WARNING] Token limit exceeded ({total_tokens} > {max_tokens}).")
    else:
        print(f"[*] Tahmini Token Maliyeti: {total_tokens} (Limit: {max_tokens})")
        if is_exceeded:
            print(f"[UYARI] Token limiti asildi ({total_tokens} > {max_tokens}).")

    return total_tokens, is_exceeded


def prune_modules_by_priority(manifest: dict, modules_to_load: list, lang: str) -> list:
    """
    Removes modules starting from P3, then P2 to fit the token budget.
    P0 and P1 modules are preserved.
    """
    all_modules = manifest.get("modules", {})
    
    # Priority groups
    p3_mods = [m for m in modules_to_load if all_modules.get(m, {}).get("priority") == "P3"]
    p2_mods = [m for m in modules_to_load if all_modules.get(m, {}).get("priority") == "P2"]
    
    pruned_list = list(modules_to_load)
    
    if p3_mods:
        target = p3_mods[0]
        pruned_list.remove(target)
        msg = (f"[*] Budget exceeded. Pruning P3 module: {target}" if lang == "en" 
               else f"[*] Butce asildi. P3 modulu cikartiliyor: {target}")
        print(msg)
        return pruned_list
        
    if p2_mods:
        target = p2_mods[0]
        pruned_list.remove(target)
        msg = (f"[*] Budget exceeded. Pruning P2 module: {target}" if lang == "en" 
               else f"[*] Butce asildi. P2 modulu cikartiliyor: {target}")
        print(msg)
        return pruned_list
        
    return None # Cannot prune further


def save_prompt(compiled_text: str, output_path: Path, lang: str) -> None:
    """Saves the compiled prompt to disk."""
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(compiled_text)

    msg = (f"[SUCCESS] Prompt compiled and saved: {output_path.absolute()}"
           if lang == "en" else
           f"[BASARILI] Prompt derlendi ve kaydedildi: {output_path.absolute()}")
    print(msg)
