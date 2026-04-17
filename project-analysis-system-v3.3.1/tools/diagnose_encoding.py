#!/usr/bin/env python3
"""
Encoding bozulma teşhis aracı.
Farklı encoding zincirlerini deneyerek doğru dönüşümü bulur.
"""
import sys

file_path = r"C:\TRAE\beyan-v1.0.0\project-analysis-system-v3.3.1\ORCHESTRATOR_PROMPT.md"

with open(file_path, "rb") as f:
    raw_bytes = f.read()

print(f"Dosya boyutu: {len(raw_bytes)} byte")
print(f"İlk 3 byte (BOM kontrolü): {raw_bytes[:3].hex()}")
print()

# Örnek bozuk bölge bul
sample_start = 200
sample = raw_bytes[sample_start:sample_start+100]
print(f"Örnek bytes (hex): {sample.hex()}")
print()

# Farklı encoding zincirleri dene
chains = [
    ("utf-8 direkt", lambda b: b.decode("utf-8", errors="replace")),
    ("latin-1 direkt", lambda b: b.decode("latin-1")),
    ("cp1252 direkt", lambda b: b.decode("cp1252")),
    ("utf-8 -> latin-1 re-encode -> utf-8", lambda b: b.decode("utf-8", errors="replace").encode("latin-1", errors="replace").decode("utf-8", errors="replace")),
    ("latin-1 -> utf-8", lambda b: b.decode("latin-1").encode("utf-8").decode("utf-8")),
    ("cp1252 -> utf-8", lambda b: b.decode("cp1252").encode("utf-8").decode("utf-8")),
]

print("=== Encoding Zinciri Denemeleri ===")
for name, func in chains:
    try:
        result = func(raw_bytes)
        # Türkçe karakter kontrolü
        has_turkish = any(c in result for c in "ğüşıöçĞÜŞİÖÇ")
        has_mojibake = "Ã" in result or "Å" in result
        snippet = result[150:350].replace("\n", " ")
        print(f"\n[{name}]")
        print(f"  Türkçe karakter: {'✅ VAR' if has_turkish else '❌ YOK'}")
        print(f"  Mojibake:        {'❌ VAR' if has_mojibake else '✅ YOK'}")
        print(f"  Snippet: {snippet[:100]}")
    except Exception as e:
        print(f"\n[{name}] HATA: {e}")
