#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from pathlib import Path
import re

# Context-aware replacements for corrupted Turkish text
replacements = {
    "örne?i": "örneği",
    "düzenlenmi?": "düzenlenmiş",
    "de?i?iklik": "değişiklik",
    "de?erlendirmesi": "değerlendirmesi",
    "sa?lık": "sağlık",
    "çalı?tır": "çalıştır",
    "Eri?ilebilirlik": "Erişilebilirlik",
    "TǬrke": "Türkçe",
    "rne?i": "örneği",
    "farkl": "farklı",
    "kullanm": "kullanım",
    "gre": "göre",
    "dǬzenlenmi?": "düzenlenmiş",
    "?rnekleri": "Örnekleri",
    "-zellik": "Özellik",
    "iin": "için",
    "dǬzelt": "düzelt",
    "baYlat": "başlat",
    "saYlk": "sağlık",
    "deYiYikliYinde": "değişikliğinde",
    "deYiYmeli": "değişmeli",
    "karlatrmas": "karşılaştırması",
    "zellik": "özellik",
    "al??tr": "çalıştır",
    "zellikleri": "özellikleri",
    "nerileri": "önerileri",
    "ncelik": "öncelik",
    "gster": "göster",
    "al??p": "çalışıp",
    "al??yor": "çalışıyor",
    "do??ru": "doğru",
    "al??myor": "çalışmıyor",
    "i??lemi": "işlemi",
    "olu??turur": "oluşturur",
    "olu??tur": "oluştur",
    "kar??la??trmas": "karşılaştırması",
    "??zellik": "özellik",
    "kullanc": "kullanıcı",
    "yanl??": "yanlış",
    "kt": "Çıktı",
    "ne kar": "öne çıkar",
    "Trk": "Türk",
    "piyasas": "piyasası",
    "baarl": "başarılı",
    "sektr": "sektör",
    "Sresi": "Süresi",
    "al??lacak": "çalışılacak",
    "? Mevcut": "- Mevcut",
    "? Eksik": "- Eksik",
    "?? Feature": "- Feature",
    "?? Rakip": "- Rakip",
    "? Quick wins": "- Quick wins",
    "?? Sprint": "- Sprint",
    "?? Uzun": "- Uzun",
    "?Y?f": "🚀",
    "?Y\"": "📊",
    "?YZ": "🧹",
    "?Y\"'": "🔒",
    "s": "⚡",
    "?Y\"S": "📈",
    "?Y": "✨",
    "?Ys?": "🚢",
    "?YZs?": "🧠",
    "?Y'": "💡",
    "o": "✅",
    "?O": "❌",
    "?Y\"\"": "🔄",
    "??": "🎯",
}

root_dir = Path(r"c:\TRAE\beyan-v1.0.0\project-analysis-system-v3.3.1")

for md_file in root_dir.rglob("*.md"):
    try:
        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        orig_content = content
        
        for old, new in replacements.items():
            content = content.replace(old, new)
            
        if content != orig_content:
            with open(md_file, "w", encoding="utf-8", newline='\n') as f:
                f.write(content)
            print(f"Cleaned {md_file.name}")
            
    except Exception as e:
        pass

print("Safe cleanup complete.")
