#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Beyan v2.0 — API Clients Module
Handles communication with OpenAI and Anthropic APIs.
"""

import os
import sys
from pathlib import Path

# Optional dependencies
try:
    from openai import OpenAI  # type: ignore
    HAS_OPENAI = True
except (ImportError, ModuleNotFoundError):
    OpenAI = None
    HAS_OPENAI = False

try:
    import anthropic  # type: ignore
    HAS_ANTHROPIC = True
except (ImportError, ModuleNotFoundError):
    anthropic = None
    HAS_ANTHROPIC = False


def call_openai(messages: list, manifest: dict, lang: str) -> str:
    """Sends a list of messages to OpenAI and returns the text response."""
    if not HAS_OPENAI:
        raise ImportError("[ERROR] OpenAI package not installed." if lang == "en" else "[HATA] OpenAI kurulu degil.")

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("[ERROR] API Key missing." if lang == "en" else "[HATA] API Key eksik.")

    model = manifest.get("default_model", {}).get("openai", "gpt-4o")
    temperature = manifest.get("default_temperature", 0.2)
    client = OpenAI(api_key=api_key)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        raise RuntimeError(f"[ERROR] OpenAI API error: {e}" if lang == "en" else f"[HATA] OpenAI hatasi: {e}")


def call_anthropic(messages: list, manifest: dict, lang: str) -> str:
    """Sends a list of messages to Anthropic and returns the text response."""
    if not HAS_ANTHROPIC:
        raise ImportError("[ERROR] Anthropic package not installed." if lang == "en" else "[HATA] Anthropic kurulu degil.")

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise ValueError("[ERROR] API Key missing." if lang == "en" else "[HATA] API Key eksik.")

    model = manifest.get("default_model", {}).get("anthropic", "claude-sonnet-4-6")
    system_prompt = (
        "You are the Master Controller of the Beyan Agentic Framework. "
        "Analyze the provided project prompt and return a structured report."
    ) if lang == "en" else (
        "Beyan Agentic Framework'ün Ana Kontrolcüsüsün. "
        "Analiz yap ve yapılandırılmış rapor üret."
    )

    client = anthropic.Anthropic(api_key=api_key)
    try:
        # Filter out system messages for Anthropic messages array
        anthropic_msgs = [m for m in messages if m["role"] != "system"]
        
        message = client.messages.create(
            model=model,
            max_tokens=8192,
            system=system_prompt,
            messages=anthropic_msgs
        )
        return message.content[0].text
    except Exception as e:
        raise RuntimeError(f"[ERROR] Anthropic API error: {e}" if lang == "en" else f"[HATA] Anthropic hatasi: {e}")


def handle_api_request(engine: str, prompt: str, manifest: dict, target_path: Path, lang: str) -> None:
    """Entry point for single-turn API requests (Mode 1 & 2)."""
    messages = [{"role": "user", "content": prompt}]
    
    try:
        if engine == "openai":
            print(f"[*] OpenAI API'ye istek gonderiliyor...")
            result = call_openai(messages, manifest, lang)
        elif engine == "anthropic":
            print(f"[*] Anthropic API'ye istek gonderiliyor...")
            result = call_anthropic(messages, manifest, lang)
        else:
            return

        _save_result(result, target_path, lang)
    except Exception as e:
        print(f"\n[!] API Hatası: {e}")
        sys.exit(1)


def _save_result(result: str, target_path: Path, lang: str) -> None:
    """Saves the API response to beyan_analysis_result.md."""
    res_file = target_path / "beyan_analysis_result.md"
    with open(res_file, "w", encoding="utf-8") as f:
        f.write(result)
    msg = (f"[SUCCESS] Analysis complete, saved to: {res_file.absolute()}"
           if lang == "en" else
           f"[BASARILI] Analiz tamamlandi ve kaydedildi: {res_file.absolute()}")
    print(msg)
