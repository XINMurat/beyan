#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Beyan v2.0 — Orchestrator Module
Manages the interactive Agentic Loop (Mode 3) with Session Persistence and Git Safety.
"""

import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from api_clients import call_openai, call_anthropic  # type: ignore

SESSIONS_DIR = Path(__file__).parent / "sessions"


def save_session(session_id: str, messages: list):
    """Saves the current message history to a JSON file."""
    SESSIONS_DIR.mkdir(exist_ok=True)
    session_path = SESSIONS_DIR / f"{session_id}.json"
    with open(session_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=2, ensure_ascii=False)


def load_session(session_id: str) -> list:
    """Loads message history from a JSON file if it exists."""
    session_path = SESSIONS_DIR / f"{session_id}.json"
    if session_path.exists():
        with open(session_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def ensure_git_safety(target_path: Path, lang: str):
    """Checks for Git and creates a safety branch before analysis."""
    try:
        # Check if it's a git repo
        is_git = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            cwd=target_path, capture_output=True, text=True
        ).returncode == 0
        
        if is_git:
            branch_name = f"beyan-fix-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
            subprocess.run(["git", "checkout", "-b", branch_name], cwd=target_path, capture_output=True)
            
            msg = (
                f"\n[GIT SAFETY] Created safety branch: {branch_name}"
                if lang == "en" else
                f"\n[GIT GÜVENLİĞİ] Güvenlik dalı oluşturuldu: {branch_name}"
            )
            print(msg)
    except Exception as e:
        # If git is not installed or other error, just skip
        pass


def run_interactive_loop(engine: str, prompt: str, manifest: dict, target_path: Path, lang: str, session_id: str):
    """
    Main loop for Mode 3.
    Supports session resume and automatic Git branching.
    """
    # 1. Git Safety First
    ensure_git_safety(target_path, lang)

    # 2. Session Management
    existing_messages = load_session(session_id)
    if existing_messages:
        print(f"[*] Resuming session: {session_id} ({len(existing_messages)} messages)")
        messages = existing_messages
        # Determine turn count from history (approximate)
        turn = (len(messages) // 2) + 1
    else:
        messages = [
            {"role": "system", "content": "Beyan Agentic Loop. Follow checkpoint protocol."},
            {"role": "user", "content": prompt}
        ]
        turn = 1
        save_session(session_id, messages)
    
    max_turns = manifest.get("max_agentic_turns", 10)
    
    print(f"\n{'='*50}")
    print(f" Beyan v2.0 - Agentic Loop (Mode 3) - Turn {turn}")
    print(f" Session ID: {session_id}")
    print(f"{'='*50}\n")

    while turn <= max_turns:
        # 1. Get Response
        if engine == "openai":
            response = call_openai(messages, manifest, lang)
        elif engine == "anthropic":
            response = call_anthropic(messages, manifest, lang)
        else:
            print("[ERROR] Unknown engine")
            break

        # 2. Display Response
        print(f"\n--- [AGENT RESPONSE] ---\n")
        print(response)
        print(f"\n--- [END RESPONSE] ---\n")

        # 3. Add to History and Save
        messages.append({"role": "assistant", "content": response})
        save_session(session_id, messages)

        # 4. Check for Checkpoints or Termination
        if "CHECKPOINT" in response:
            user_input = _get_user_approval(lang)
            if user_input.lower() in ["exit", "q", "iptal"]:
                print("\n[*] Loop terminated by user.")
                break
            
            messages.append({"role": "user", "content": user_input})
            save_session(session_id, messages)
            turn += 1
            print(f"\n--- Starting Turn {turn} ---\n")
        else:
            print("\n[*] No checkpoint detected. Is there anything else?")
            user_input = input(">> ")
            if user_input.lower() in ["exit", "q", "no", "hayir", ""]:
                print("[*] Loop finished.")
                break
            messages.append({"role": "user", "content": user_input})
            save_session(session_id, messages)
            turn += 1

    if turn > max_turns:
        print(f"\n[!] Reached maximum agentic turns ({max_turns}).")


def _get_user_approval(lang: str) -> str:
    """Prompt the user for input during a checkpoint."""
    prompt_msg = (
        "\n[CHECKPOINT DETECTED] Please provide your instruction or 'yes' to proceed (or 'q' to quit): "
        if lang == "en" else
        "\n[CHECKPOINT TESPİT EDİLDİ] Talimatınızı girin veya devam etmek için 'evet' yazın (çıkmak için 'q'): "
    )
    user_input = input(prompt_msg).strip()
    
    if not user_input:
        return "yes" if lang == "en" else "evet"
    return user_input
