#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Beyan v2.0 Agentic Framework — CLI Analyzer (Orchestrator)
Usage: python cli/analyzer.py --target <path> --mode <1|2|3> --lang <tr|en> [--api openai|anthropic]

Module responsibilities:
  analyzer.py   ← Argparse + orchestration (this file)
  discovery.py  ← auto_discover() — technology tag detection
  compiler.py   ← MANIFEST loading, module selection, prompt compilation
  api_clients.py← OpenAI and Anthropic API communication
"""

import argparse
import sys
from datetime import datetime
from pathlib import Path

# Robust detection of the Beyan system root
SYSTEM_ROOT = Path(__file__).parent.parent.absolute()
sys.path.append(str(SYSTEM_ROOT))

# Direct sibling imports (now from parent)
from discovery import auto_discover  # type: ignore
from compiler import load_manifest, select_modules, compile_prompt, check_token_budget, save_prompt  # type: ignore
from api_clients import handle_api_request  # type: ignore

MANIFEST_PATH = SYSTEM_ROOT / "MANIFEST.yaml"


def run_orchestration(target: str, mode: int, lang: str, api_choice: str, session_id: str = None):
    target_path = Path(target).absolute()
    
    print(f"\n[*] Target: {target_path}")
    print(f"[*] Mode: {mode}")
    print(f"[*] Session: {session_id}")
    
    # Phase 1: Discovery
    tags = auto_discover(target_path)
    print(f"[*] Detected technologies: {', '.join(tags) if tags else 'none'}")

    # Phase 2: Load Manifest
    manifest = load_manifest(MANIFEST_PATH)

    # Phase 3: Module Selection
    selected_modules_list = select_modules(manifest, tags, lang)
    print(f"[*] Loaded modules: {', '.join(selected_modules_list)}")

    # Phase 4 & 5: Compilation & Token Budget Check (with Pruning)
    while True:
        compiled_text = compile_prompt(SYSTEM_ROOT, manifest, selected_modules_list, mode, lang)
        token_count, is_exceeded = check_token_budget(compiled_text, manifest, lang)
        
        if is_exceeded:
            from compiler import prune_modules_by_priority
            pruned_list = prune_modules_by_priority(manifest, selected_modules_list, lang)
            if pruned_list:
                selected_modules_list = pruned_list
                continue
            else:
                err = ("[ERROR] Token limit exceeded even after pruning. "
                       "Please target a smaller directory." if lang == "en" else
                       "[HATA] Budamaya ragmen token limiti asildi. "
                       "Lutfen daha kucuk bir dizini hedefleyin.")
                print(err)
                sys.exit(1)
        break

    print(f"[*] Final compiled prompt size: ~{token_count} tokens")

    # Save prompt to file for manual review
    output_filename = "beyan_compiled_prompt.md"
    save_prompt(compiled_text, SYSTEM_ROOT / output_filename, lang)

    # Phase 6: LLM Interaction
    if api_choice != "none":
        if mode == 3:
            from orchestrator import run_interactive_loop  # type: ignore
            run_interactive_loop(api_choice, compiled_text, manifest, target_path, lang, session_id)
        else:
            handle_api_request(api_choice, compiled_text, manifest, target_path, lang)


def run() -> None:
    """Entry point for the 'beyan' console script."""
    parser = argparse.ArgumentParser(
        description="Beyan v2.0 Agentic Framework — CLI Analyzer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  beyan --target . --mode 1 --lang tr
  beyan --target /path/to/project --mode 1 --lang en --api anthropic
        """
    )
    parser.add_argument("--target", type=str, default=".",
                        help="Target directory to analyze (default: .)")
    parser.add_argument("--mode", type=int, choices=[1, 2, 3], default=1,
                        help="Operation mode: 1=Analysis, 2=Plan, 3=Fix (default: 1)")
    parser.add_argument("--lang", type=str, choices=["tr", "en"], default="tr",
                        help="Module language (default: tr)")
    parser.add_argument("--api", choices=["none", "openai", "anthropic"], default="none", help="LLM API choice (default: none — compile prompt only)")
    parser.add_argument("--session", type=str, help="Resume an existing session ID or specify a new one")

    args = parser.parse_args()

    # Session ID management
    session_id = args.session if args.session else f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

    run_orchestration(args.target, args.mode, args.lang, args.api, session_id)


if __name__ == "__main__":
    run()
