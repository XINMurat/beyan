#!/usr/bin/env python3
"""
Beyan v1 -> v2 Module Migration Tool

Usage:
    python merge_modules.py --v3 /path/to/beyan-v1 --v2 /path/to/beyan-v2
    python merge_modules.py --v3 ../project-analysis-system-v3.3.1 --v2 .
"""
import argparse
import os
import shutil
import yaml
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Beyan v1 -> v2 module migration tool")
    parser.add_argument("--v3", required=True, help="Kaynak v3 dizini (project-analysis-system-v3.x)")
    parser.add_argument("--v2", required=True, help="Hedef v2 dizini (beyan-v2.0-agentic)")
    parser.add_argument("--dry-run", action="store_true", help="Değişiklik yapmadan önizle")
    args = parser.parse_args()

    v3 = Path(args.v3).resolve()
    v2 = Path(args.v2).resolve()

    if not v3.exists():
        print(f"[HATA] v3 dizini bulunamadı: {v3}")
        return 1
    if not v2.exists():
        print(f"[HATA] v2 dizini bulunamadı: {v2}")
        return 1

    print(f"[*] Kaynak (v3): {v3}")
    print(f"[*] Hedef  (v2): {v2}")
    if args.dry_run:
        print("[*] DRY-RUN modu — hiçbir dosya kopyalanmayacak\n")

    # Directories to create
    dirs = [
        v2 / 'modules/core/tr',
        v2 / 'modules/specialized/tr',
        v2 / 'modules/guides/tr',
        v2 / 'modules/testing/tr'
    ]
    if not args.dry_run:
        for d in dirs:
            d.mkdir(parents=True, exist_ok=True)

    # 1. Copy files
    copy_map = [
        (v3 / 'modules/core', v2 / 'modules/core/tr', lambda f: True),
        (v3 / 'modules/specialized', v2 / 'modules/specialized/tr', lambda f: f.name != 'umt-architecture.md'),
        (v3 / 'implementation-guides', v2 / 'modules/guides/tr', lambda f: True),
        (v3 / 'modules/testing', v2 / 'modules/testing/tr', lambda f: True)
    ]

    for src_dir, dst_dir, filter_func in copy_map:
        for f in src_dir.glob('*.md'):
            if filter_func(f):
                target = dst_dir / f.name
                if not args.dry_run:
                    shutil.copy2(f, target)
                    print(f"[OK] Kopyalandı: {f.name} -> {target.relative_to(v2)}")
                else:
                    print(f"[DRY-RUN] Kopyalanacak: {f.name} -> {target.relative_to(v2)}")

    # 2. Merge MANIFEST.yaml
    with open(v3 / 'MANIFEST.yaml', 'r', encoding='utf-8') as f:
        old_manifest = yaml.safe_load(f)

    with open(v2 / 'MANIFEST.yaml', 'r', encoding='utf-8') as f:
        new_manifest = yaml.safe_load(f)

    old_modules = old_manifest.get('modules', {})
    for k, v in old_modules.items():
        if k == 'umt_architecture_analysis':
            continue
        
        old_path = v['path']
        if old_path.startswith('modules/core/'):
            new_path = old_path.replace('modules/core/', 'modules/core/tr/')
        elif old_path.startswith('modules/specialized/'):
            new_path = old_path.replace('modules/specialized/', 'modules/specialized/tr/')
        elif old_path.startswith('implementation-guides/'):
            new_path = old_path.replace('implementation-guides/', 'modules/guides/tr/')
        elif old_path.startswith('modules/testing/'):
            new_path = old_path.replace('modules/testing/', 'modules/testing/tr/')
        else:
            new_path = old_path
            
        v['path'] = new_path
        new_manifest['modules'][k] = v

    new_manifest['total_modules'] = len(new_manifest['modules'])

    if not args.dry_run:
        with open(v2 / 'MANIFEST.yaml', 'w', encoding='utf-8') as f:
            yaml.dump(new_manifest, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        print(f"\n[BASARILI] Manifest güncellendi. Toplam modül: {new_manifest['total_modules']}")
    else:
        print(f"\n[DRY-RUN] Manifest güncellenecekti. Yeni toplam modül: {new_manifest['total_modules']}")

if __name__ == "__main__":
    main()
