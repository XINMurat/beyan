#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Project Analysis System - CLI Analyzer (M4)
Usage: python analyzer.py --target <path> --mode <1|2|3> [--api openai|anthropic]
"""

import argparse
import os
import sys
from pathlib import Path

# Try importing pyyaml, provide a friendly error if missing
try:
    import yaml
except ImportError:
    print("PyYAML bulunamadi. Lutfen once yukleyin: pip install pyyaml")
    sys.exit(1)

# Optional API imports
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
    
    # Check for Node.js / Frontend
    if (target_dir / "package.json").exists():
        tags.update(["node", "frontend", "package.json"])
        
    # Check for Java
    if (target_dir / "pom.xml").exists() or (target_dir / "build.gradle").exists():
        tags.update(["java", "backend"])
        
    # Check for Python
    if (target_dir / "requirements.txt").exists() or (target_dir / "setup.py").exists():
        tags.update(["python", "backend", "requirements.txt"])
        
    # Check for Docker / Infra
    if (target_dir / "Dockerfile").exists() or (target_dir / "docker-compose.yml").exists():
        tags.update(["docker", "infrastructure", "cloud"])
        
    return list(tags)

def load_manifest():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def compile_prompt(target_dir: str, mode: int, api_choice: str):
    target_path = Path(target_dir)
    if not target_path.exists():
        print(f"Hata: Hedef dizin bulunamadi -> {target_path}")
        sys.exit(1)
        
    manifest = load_manifest()
    max_tokens = manifest.get("max_total_tokens", 30000)
    
    print(f"[*] Hedef dizin taranıyor: {target_path}")
    discovered_tags = auto_discover(target_path)
    print(f"[*] Algılanan teknolojiler: {', '.join(discovered_tags) if discovered_tags else 'Bulunamadi'}")
    
    # Determine which modules to load
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
            
    print(f"[*] Secilen Modüller ({len(modules_to_load)} adet): {', '.join(modules_to_load)}")
    
    # Compile text
    compiled_text = f"# Project Analysis - Mode {mode} Run\n\n"
    compiled_text += "## 1. Core System Prompts\n\n"
    
    # Read Base and Orchestrator
    try:
        with open(SYSTEM_ROOT / "BASE_PROMPT.md", "r", encoding="utf-8") as f:
            compiled_text += f.read() + "\n\n"
        with open(SYSTEM_ROOT / "ORCHESTRATOR_PROMPT.md", "r", encoding="utf-8") as f:
            compiled_text += f.read() + "\n\n"
    except Exception as e:
        print(f"Sistem dosyalari okunamadi: {e}")
        
    compiled_text += "## 2. Selected Modules\n\n"
    
    # Read modules
    for mod_key in modules_to_load:
        mod_path = SYSTEM_ROOT / manifest["modules"][mod_key]["path"]
        if mod_path.exists():
            with open(mod_path, "r", encoding="utf-8") as f:
                compiled_text += f"### Module: {mod_key}\n"
                compiled_text += f.read() + "\n\n"
                
    total_tokens = calculate_tokens(compiled_text)
    print(f"[*] Tahmini Token Maliyeti: {total_tokens} (Limit: {max_tokens})")
    
    if total_tokens > max_tokens:
        print("UYARI: Toplam token limiti asildi! LLM API istegi reddedilebilir.")
        
    # Save output
    output_file = target_path / "compiled_prompt.md"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(compiled_text)
        
    print(f"[*] Basariyla kaydedildi: {output_file.absolute()}")
    
    # API Integration
    if api_choice == "openai":
        if not HAS_OPENAI:
            print("[HATA] OpenAI kutuphanesi kurulu degil. 'pip install openai' calistirin.")
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
                    {"role": "system", "content": "You are the Master Controller of the Project Analysis System."},
                    {"role": "user", "content": compiled_text[:100000]} # Safe cutoff
                ],
                temperature=0.2
            )
            result = response.choices[0].message.content
            
            res_file = target_path / "analysis_result.md"
            with open(res_file, "w", encoding="utf-8") as f:
                f.write(result)
            print(f"[BASARILI] Analiz tamamlandi ve kaydedildi: {res_file.absolute()}")
        except Exception as e:
            print(f"[HATA] API Hatasi: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Project Analysis System CLI")
    parser.add_argument("--target", type=str, default=".", help="Hedef proje dizini")
    parser.add_argument("--mode", type=int, choices=[1, 2, 3], default=1, help="Calisma Modu (1: Analiz, 2: Plan, 3: Fix)")
    parser.add_argument("--api", type=str, choices=["none", "openai", "anthropic"], default="none", help="Dogrudan LLM API'sine gonder (Opsiyonel)")
    
    args = parser.parse_args()
    
    compile_prompt(args.target, args.mode, args.api)
