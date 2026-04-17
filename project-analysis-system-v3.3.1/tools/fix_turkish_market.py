#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
import re
from pathlib import Path

# Fix turkish-market.md encoding artifacts that multi_replace couldn't match due to mojibake
target_file = Path(r"C:\TRAE\beyan-v1.0.0\project-analysis-system-v3.3.1\modules\specialized\turkish-market.md")
with open(target_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix header
content = content.replace("Turkish Character Handling (İ, ?, ?, ?, ?, ?)", "Turkish Character Handling (İ, Ş, Ğ, Ü, Ö, Ç)")
# Fix code comments
content = content.replace("i ?? I (wrong), should be i ?? İ", "i -> I (wrong), should be i -> İ")
content = content.replace("Turkish alphabetical order: A B C ? D E F G ? H I İ J K L M N O ? P R S ? T U ? V Y Z", "Turkish alphabetical order: A B C Ç D E F G Ğ H I İ J K L M N O Ö P R S Ş T U Ü V Y Z")
content = content.replace("Türkçe ?? turkce", "Türkçe -> turkce")
content = content.replace("// ? Wrong", "// ❌ Wrong")
content = content.replace("// ?? Correct", "// ✅ Correct")
content = content.replace("Database has \"İSTANBUL\" ?? No match!", "Database has \"İSTANBUL\" -> No match!")
content = content.replace("?anakkale", "Çanakkale")
content = content.replace("Ki?isel", "Kişisel")
content = content.replace("Açık Rıza Metni", "Açık Rıza Metni")
content = content.replace("?irketimiz", "Şirketimiz")
content = content.replace("i?lemektedir", "işlemektedir")
content = content.replace("i?lenmesine", "işlenmesine")
content = content.replace("iste?e ba?lı", "isteğe bağlı")
content = content.replace("? Ticari", "✓ Ticari")
content = content.replace("?erez Politikası", "Çerez Politikası")
content = content.replace("İ? Bankası", "İş Bankası")
content = content.replace("Tek ?ekim", "Tek Çekim")
content = content.replace("Giri?", "Giriş")
content = content.replace("?", "₺")
content = content.replace("?ankaya", "Çankaya")
content = content.replace("??", "🟡")
content = content.replace("??", "✅")
content = content.replace("İ, ?, ?", "İ, Ş, Ğ")

# Apply M1 fixes that failed before
# KVKK basics penalties
content = re.sub(
    r'penalties: "Up to 2% of annual revenue"',
    'penalties:\n    system: "Kategorik sabit ceza (GDPR gibi yüzde bazlı DEĞİL)"\n    administrative_2024: "1.813 TL - 3.625.732 TL (yeniden değerleme ile)"\n    criminal: "Madde 17 kapsamında hapis cezası riski"\n    note: "GDPR\'dan farklıdır — AB yüzde bazlı cezalarla karıştırılmamalı"',
    content
)

# Implementation checklist (VERBİS and Article 9)
content = re.sub(
    r'- \[ \] Data encryption \(AES-256 at rest, TLS 1\.3 in transit\)',
    '- [ ] Data encryption (AES-256 at rest, TLS 1.3 in transit)\n  - [ ] VERBİS kaydı (yıllık ciro > 10M TL veya çalışan > 50 ise zorunlu)\n  - [ ] Yurt dışı veri aktarımı için KVKK Madde 9 uyumluluğu',
    content
)

# BKM Express -> Tosla
content = content.replace(
    "- BKM Express (Bank Association mobile wallet)",
    "- Tosla (BKM'nin güncel mobil cüzdanı — BKM Express'in halefi)"
)

# Add verbis and international data transfer sections if not there
if "verbis_registry" not in content:
    content = content.replace(
        "    - DPO (Data Protection Officer) if needed",
        "    - DPO (Data Protection Officer) if needed\n\n  verbis_registry:\n    required_if: \"Yıllık ciro > 10M TL VEYA çalışan sayısı > 50\"\n    registration_url: \"https://verbis.kvkk.gov.tr\"\n    deadline: \"Yeni veri sorumluları için faaliyet başlangıcında\"\n    penalty: \"KVKK Madde 18 — kayıt yaptırmama idari para cezası\"\n\n  international_data_transfer:\n    law: \"KVKK Madde 9\"\n    requirement: \"Yurt dışına veri aktarımı için KVKK Kurulu onayı VEYA açık rıza zorunlu\"\n    common_services_affected:\n      - \"Google Analytics (ABD) — IP adresi kişisel veri sayılır\"\n      - \"AWS, Azure, GCP (ABD/AB sunucu) — veri depolama\"\n      - \"SendGrid / Mailchimp (ABD) — e-posta adresi aktarımı\"\n    solutions:\n      - \"Türkiye'deki sunuculara taşı (veri yerelleştirme)\"\n      - \"GA4 IP anonimleştirme + consent mode aktif et\"\n      - \"Standart Sözleşme Maddeleri (SCCs) + açık rıza\"\n    kurul_kararlar: \"https://www.kvkk.gov.tr/Icerik/6908\""
    )

with open(target_file, 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
print("turkish-market.md duzeltildi.")
