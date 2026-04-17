#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project Analysis System v3.3.1 encoding duzeltme araci.
Uc farkli bozulma tipini tespir edip duzeltir:
  Tip A (2x encode): utf-8 -> latin-1 -> utf-8  (1 gecis yeterli)
  Tip B (3x encode): utf-8 -> latin-1 -> utf-8 x2 (2 gecis gerekli)
  Tip C: Replacement char (U+FFFD) iceren — kurtarilamaz, orijinal birakilir
"""
import io, sys, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
from pathlib import Path

ROOT   = Path(r"C:\TRAE\beyan-v1.0.0\project-analysis-system-v3.3.1")
BACKUP = Path(r"C:\TRAE\beyan-v1.0.0\_encoding_backup_20260417_094010\project-analysis-system-v3.3.1")

TR_CHARS = set('ğüşıöçĞÜŞİÖÇ')
MOJI = 'Ã'

def has_turkish(text):
    return any(c in text for c in TR_CHARS)

def has_mojibake(text):
    return MOJI in text

def try_fix(raw_bytes):
    """En uygun encoding zinciirini dener, temiz Türkçe metin döndürür."""
    # Tip A: 2x encode  (utf-8 -> latin-1 -> utf-8 = 1 gecis)
    try:
        step1 = raw_bytes.decode('utf-8', errors='strict')
        step2 = step1.encode('latin-1', errors='strict').decode('utf-8', errors='strict')
        if has_turkish(step2) and not has_mojibake(step2):
            return step2, 'TipA(2x)'
    except Exception:
        pass

    # Tip B: 3x encode (2 gecis)
    try:
        step1 = raw_bytes.decode('utf-8', errors='replace')
        step2 = step1.encode('latin-1', errors='replace').decode('utf-8', errors='replace')
        step3 = step2.encode('latin-1', errors='replace').decode('utf-8', errors='replace')
        if has_turkish(step3) and not has_mojibake(step3):
            return step3, 'TipB(3x)'
    except Exception:
        pass

    # Tip A gevşek (errors=replace ile)
    try:
        step1 = raw_bytes.decode('utf-8', errors='replace')
        step2 = step1.encode('latin-1', errors='replace').decode('utf-8', errors='replace')
        if has_turkish(step2) and not has_mojibake(step2):
            return step2, 'TipA-relaxed'
    except Exception:
        pass

    return None, None


backup_files = sorted(BACKUP.rglob("*.md"))
print(f"Yedekte {len(backup_files)} .md dosyasi bulundu\n")

counts = {'fixed_A': 0, 'fixed_B': 0, 'fixed_relaxed': 0, 'skipped': 0, 'error': 0}
skip_list = []

for backup_file in backup_files:
    rel = backup_file.relative_to(BACKUP)
    target = ROOT / rel

    # Hedef dosya yoksa oluştur
    target.parent.mkdir(parents=True, exist_ok=True)

    try:
        with open(backup_file, 'rb') as f:
            raw = f.read()

        fixed_text, method = try_fix(raw)

        if fixed_text:
            with open(target, 'w', encoding='utf-8', newline='\n') as f:
                f.write(fixed_text)
            print(f"[{method:16s}] {rel.name}")
            key = 'fixed_A' if 'A' in method else ('fixed_B' if 'B' in method else 'fixed_relaxed')
            counts[key] += 1
        else:
            # Duzeltilemeyen: orijinal bytes koru
            with open(target, 'wb') as f:
                f.write(raw)
            print(f"[SKIP             ] {rel.name}")
            counts['skipped'] += 1
            skip_list.append(str(rel))

    except Exception as e:
        print(f"[ERR              ] {rel.name} - {e}")
        counts['error'] += 1

print(f"\n{'='*55}")
print(f"TipA (2x) duzeltilen  : {counts['fixed_A']}")
print(f"TipB (3x) duzeltilen  : {counts['fixed_B']}")
print(f"Relaxed duzeltilen    : {counts['fixed_relaxed']}")
print(f"Atlanan (SKIP)        : {counts['skipped']}")
print(f"Hata                  : {counts['error']}")
print(f"TOPLAM                : {sum(counts.values())}")

if skip_list:
    print(f"\nAtlanan dosyalar (manuel inceleme gerekebilir):")
    for f in skip_list:
        print(f"  - {f}")
