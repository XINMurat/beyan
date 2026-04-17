#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from pathlib import Path

# Common corrupted sequences and their correct Turkish/Emoji equivalents
replacements = {
    "?": "Ö",
    "örne?i": "örneği",
    "düzenlenmi?": "düzenlenmiş",
    "de?i?iklik": "değişiklik",
    "de?erlendirmesi": "değerlendirmesi",
    "sa?lık": "sağlık",
    "çalı?tır": "çalıştır",
    "Eri?ilebilirlik": "Erişilebilirlik",
    "??": "💡",
    "???": "🔍",
    "ba?vuru": "başvuru",
    "?": "Ş",
    "?": "Ç",
    "?": "Ğ",
    "?": "Ü",
    "?": "Ö",
    "?": "İ",
    "?": "ş",
    "?": "ç",
    "?": "ğ",
    "?": "ü",
    "?": "ö",
    "?": "ı",
    "": "i",
    "??": "ğ",
    "??": "ş",
    "??": "ı",
    "??": "ü",
    "??": "ö",
    "??": "ç",
}

# Add general character fallbacks based on context
context_replacements = [
    ("kar??la??trmas", "karşılaştırması"),
    ("??zellik", "özellik"),
    ("olu??turur", "oluşturur"),
    ("al??trlabilir", "çalıştırılabilir"),
    ("retir", "üretir"),
    ("do??ru", "doğru"),
    ("al??p", "çalışıp"),
    ("davran??", "davranışı"),
    ("karma??k", "karmaşık"),
    ("kullanc", "kullanıcı"),
    ("??deme", "Ödeme"),
    ("i??lemi", "işlemi"),
    ("yanl??", "yanlış"),
    ("kt", "Çıktı"),
    ("ne kar", "öne çıkar"),
    ("gster", "göster"),
    ("al??tr", "çalıştır"),
    ("zlen", "Çözülen"),
    ("akan", "Çakışan"),
    ("deiiklikler", "değişiklikler"),
    ("koptuunda", "koptuğunda"),
    ("Dier", "Diğer"),
    ("grnyor", "görünüyor"),
    ("doru", "doğru"),
    ("m?", "mı?"),
    ("Trk", "Türk"),
    ("piyasas", "piyasası"),
    ("baarl", "başarılı"),
    ("sektr", "sektörü"),
    ("karlatr", "karşılaştır"),
    ("ayr", "ayrı"),
    ("zellikleri", "özellikleri"),
    ("ncelikle", "öncelikle"),
    ("gerekti??ini", "gerektiğini"),
    ("??ekilde", "şekilde"),
    ("yardmc", "yardımcı"),
]

root_dir = Path(r"c:\TRAE\beyan-v1.0.0\project-analysis-system-v3.3.1")

for md_file in root_dir.rglob("*.md"):
    try:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        orig_content = content
        
        for old, new in context_replacements:
            content = content.replace(old, new)
            
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        # Clean up isolated question marks inside Turkish words
        import re
        content = re.sub(r'([a-z])\?([a-z])', r'\1ğ\2', content) # heuristic
        
        if content != orig_content:
            with open(md_file, "w", encoding="utf-8", newline='\n') as f:
                f.write(content)
            print(f"Cleaned {md_file.name}")
            
    except Exception as e:
        pass

print("Cleanup complete.")
