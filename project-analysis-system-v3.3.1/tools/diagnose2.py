#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# BASE_PROMPT.md bozuk byte kalibini incele
with open('BASE_PROMPT.md', 'rb') as f:
    raw = f.read()

print(f"Dosya boyutu: {len(raw)} byte")

# Bozuk byte kaliplarini bul
found = 0
i = 0
print("\nBozuk byte kalibi ornekleri (ilk 10):")
while i < len(raw) - 3 and found < 10:
    # C3 83 E2 80 = multi-encode pattern
    if raw[i] == 0xC3 and raw[i+1] == 0x83:
        snippet = raw[i:i+10].hex()
        print(f"  pos={i}: {snippet}")
        found += 1
    # EF BF BD = replacement character
    elif raw[i] == 0xEF and raw[i+1] == 0xBF and raw[i+2] == 0xBD:
        snippet = raw[i:i+6].hex()
        print(f"  pos={i}: REPLACEMENT {snippet}")
        found += 1
    i += 1

# Kac replacement char var
repl_count = raw.count(bytes([0xEF, 0xBF, 0xBD]))
print(f"\nReplacement char (U+FFFD) sayisi: {repl_count}")

# ftfy deneyelim
print("\nftfy dene:")
try:
    import ftfy
    decoded = raw.decode('utf-8', errors='replace')
    fixed = ftfy.fix_text(decoded)
    has_tr = any(c in fixed for c in 'gusioçGUSIOC')
    print(f"ftfy sonucu: has_turkish={has_tr}")
    print(f"Snippet: {fixed[100:300]}")
except ImportError:
    print("ftfy kurulu degil -- pip install ftfy")

# Manuel deneme: uc kez encode zinciri
print("\nManuel zincir denemeleri:")
chains = [
    ("utf8->latin1->utf8->latin1->utf8",
     lambda b: b.decode('utf-8', errors='replace').encode('latin-1', errors='replace').decode('utf-8', errors='replace').encode('latin-1', errors='replace').decode('utf-8', errors='replace')),
    ("raw as cp1252->utf8",
     lambda b: b.decode('cp1252', errors='replace')),
]
for name, fn in chains:
    try:
        result = fn(raw)
        has_tr = any(c in result for c in 'gusioçGUSIOC\u011f\u015f\u00fc\u00f6')
        has_moji = 'Ã' in result
        print(f"  [{name}] turkce={has_tr} moji={has_moji} | snippet: {result[100:200]}")
    except Exception as e:
        print(f"  [{name}] HATA: {e}")
