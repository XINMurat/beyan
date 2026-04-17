#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Beyan v2.0 Agentic Framework - CLI Analyzer
Usage: python cli/analyzer.py --target <path> --mode <1|2|3> --lang <tr|en> [--api openai]
"""

import argparse
import os
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML bulunamadi. Lutfen once yukleyin: pip install pyyaml")
    sys.exit(1)

try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False

SYSTEM_ROOT = Path(__file__).parent.parent.absolute()
MANIFEST_PATH = SYSTEM_ROOT / "MANIFEST.yaml"

def calculate_tokens(text: str) -> int:
    """Heuristic token calculation: 1 token = ~4 characters"""
    return len(text) // 4

def auto_discover(target_dir: Path) -> list:
    """Scans the target directory and returns discovered environment tags."""
    tags = set()
    
    for item in target_dir.rglob("*"):
        name = item.name.lower()
        if name == "package.json":
            tags.update(["package.json", "node", "frontend", "react", "web"])
        elif name == "pom.xml" or name == "build.gradle":
            tags.update(["java", "backend"])
        elif name.endswith(".sol") or name == "hardhat.config.js":
            tags.update(["sol", "blockchain", "web3", "smart-contract"])
        elif name.endswith(".c") or name.endswith(".cpp") or name == "cmakelists.txt":
            tags.update(["c", "cpp", "firmware", "os", "system"])
        elif name.endswith(".ipynb") or name == "requirements.txt":
            tags.update(["ipynb", "ai", "model", "python"])
        elif name == "dockerfile" or name == "docker-compose.yml":
            tags.update(["dockerfile", "docker", "devops", "infrastructure"])
        elif name.endswith(".sql") or name == "dbt_project.yml":
            tags.update(["data", "pipeline", "etl", "sql"])
        elif name == "manifest.yaml" or name.endswith(".py"):
            tags.update(["yaml", "manifest.yaml", "python", "cli"])
            
    return list(tags)

def load_manifest():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def compile_prompt(target_dir: str, mode: int, lang: str, api_choice: str):
    target_path = Path(target_dir)
    if not target_path.exists():
        print(f"[ERROR] Hedef dizin bulunamadi / Target directory not found -> {target_path}" if lang == "en" else f"[HATA] Hedef dizin bulunamadi -> {target_path}")
        sys.exit(1)
        
    manifest = load_manifest()
    
    if lang not in manifest.get("languages", ["tr", "en"]):
        print(f"[ERROR] Unsupported language / Desteklenmeyen dil: {lang}")
        sys.exit(1)
        
    max_tokens = manifest.get("max_total_tokens", 35000)
    
    if lang == "en":
        print(f"[*] Scanning target directory: {target_path.absolute()}")
        discovered_tags = auto_discover(target_path)
        print(f"[*] Detected technologies: {', '.join(discovered_tags) if discovered_tags else 'Not found (Default modules will be loaded)'}")
    else:
        print(f"[*] Hedef dizin taranıyor: {target_path.absolute()}")
        discovered_tags = auto_discover(target_path)
        print(f"[*] Algılanan teknolojiler: {', '.join(discovered_tags) if discovered_tags else 'Bulunamadi (Varsayilan moduller yuklenecek)'}")
    
    modules_to_load = []
    
    for mod_key, mod_info in manifest.get("modules", {}).items():
        priority = mod_info.get("priority", "P3")
        auto_load_if = mod_info.get("auto_load_if", [])
        
        # Load P0 modules always
        if priority == "P0" or mod_info.get("auto_load") == True:
            modules_to_load.append(mod_key)
            continue
            
        # Load if discovered tags match auto_load_if
        if any(tag in discovered_tags for tag in auto_load_if):
            modules_to_load.append(mod_key)
            
    if not modules_to_load:
        if lang == "en":
            print("[*] No exact match found, 'web_mobile' is loading as the default domain.")
        else:
            print("[*] Kesin eslesme bulunamadi, 'web_mobile' varsayilan domain olarak yukleniyor.")
        modules_to_load.append("web_mobile")
            
    if lang == "en":
        print(f"[*] Selected Modules ({len(modules_to_load)} count): {', '.join(modules_to_load)}")
    else:
        print(f"[*] Secilen Modüller ({len(modules_to_load)} adet): {', '.join(modules_to_load)}")
    
    compiled_text = f"# Beyan v2.0 - Mode {mode} Run ({lang.upper()})\n\n"
    compiled_text += "## 1. Core Engine Rules\n\n"
    
    try:
        base_path = manifest.get("base_prompt", "core_prompts/{lang}/BASE_PROMPT.md").replace("{lang}", lang)
        orc_path = manifest.get("orchestrator_prompt", "core_prompts/{lang}/ORCHESTRATOR_PROMPT.md").replace("{lang}", lang)
        
        with open(SYSTEM_ROOT / base_path, "r", encoding="utf-8") as f:
            compiled_text += f.read() + "\n\n"
        with open(SYSTEM_ROOT / orc_path, "r", encoding="utf-8") as f:
            compiled_text += f.read() + "\n\n"
    except Exception as e:
        if lang == "en":
            print(f"[ERROR] Failed to read core files: {e}")
        else:
            print(f"[HATA] Core dosyalar okunamadi: {e}")
        
    compiled_text += "## 2. Domain & Focus Modules\n\n"
    
    for mod_key in modules_to_load:
        mod_path_str = manifest["modules"][mod_key]["path"].replace("{lang}", lang)
        mod_path = SYSTEM_ROOT / mod_path_str
        if mod_path.exists():
            with open(mod_path, "r", encoding="utf-8") as f:
                compiled_text += f"### Module: {mod_key}\n"
                compiled_text += f.read() + "\n\n"
        else:
            if lang == "en":
                print(f"[WARNING] Module file not found: {mod_path}")
            else:
                print(f"[UYARI] Modul dosyasi bulunamadi: {mod_path}")
                
    total_tokens = calculate_tokens(compiled_text)
    if lang == "en":
        print(f"[*] Estimated Token Cost: {total_tokens} (Limit: {max_tokens})")
        if total_tokens > max_tokens:
            print("WARNING: Total token limit exceeded! LLM API request might be rejected.")
    else:
        print(f"[*] Tahmini Token Maliyeti: {total_tokens} (Limit: {max_tokens})")
        if total_tokens > max_tokens:
            print("UYARI: Toplam token limiti asildi! LLM API istegi reddedilebilir.")
        
    output_file = target_path / "beyan_compiled_prompt.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(compiled_text)
        
    if lang == "en":
        print(f"[SUCCESS] Prompt compiled and saved: {output_file.absolute()}")
    else:
        print(f"[BASARILI] Prompt derlendi ve kaydedildi: {output_file.absolute()}")
    
    if api_choice == "openai":
        if not HAS_OPENAI:
            print("[ERROR] OpenAI missing." if lang == "en" else "[HATA] OpenAI kutuphanesi kurulu degil.")
            return
            
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            print("[HATA] OPENAI_API_KEY cevre degiskeni bulunamadi.")
            return
            
        print("[*] OpenAI API'sine istek gonderiliyor (GPT-4o)...")
        client = OpenAI(api_key=api_key)
        
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are the Master Controller of the Beyan Agentic Framework."},
                    {"role": "user", "content": compiled_text[:100000]} # Safe cutoff
                ],
                temperature=0.2
            )
            result = response.choices[0].message.content
            
            res_file = target_path / "beyan_analysis_result.md"
            with open(res_file, "w", encoding="utf-8") as f:
                f.write(result)
            if lang == "en":
                print(f"[SUCCESS] Analysis complete, saved to: {res_file.absolute()}")
            else:
                print(f"[BASARILI] Analiz tamamlandi ve kaydedildi: {res_file.absolute()}")
        except Exception as e:
            print(f"[ERROR] API Error: {e}" if lang == "en" else f"[HATA] API Hatasi: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Beyan v2.0 CLI Analyzer")
    parser.add_argument("--target", type=str, default=".", help="Hedef proje dizini")
    parser.add_argument("--mode", type=int, choices=[1, 2, 3], default=1, help="Calisma Modu (1: Analiz, 2: Plan, 3: Fix)")
    parser.add_argument("--lang", type=str, choices=["tr", "en"], default="tr", help="Modul Dili")
    parser.add_argument("--api", type=str, choices=["none", "openai", "anthropic"], default="none", help="LLM API kullanimi")
    
    args = parser.parse_args()
    
    compile_prompt(args.target, args.mode, args.lang, args.api)
