import os
import shutil
import yaml
from pathlib import Path

v3 = Path(r'C:\TRAE\beyan-v1.0.0\project-analysis-system-v3.3.1')
v2 = Path(r'C:\TRAE\beyan-v1.0.0\beyan-v2.0-agentic')

# Directories to create
dirs = [
    v2 / 'modules/core/tr',
    v2 / 'modules/specialized/tr',
    v2 / 'modules/guides/tr',
    v2 / 'modules/testing/tr'
]
for d in dirs:
    d.mkdir(parents=True, exist_ok=True)

# 1. Copy files
src_core = v3 / 'modules/core'
for f in src_core.glob('*.md'):
    shutil.copy(f, v2 / 'modules/core/tr' / f.name)

src_spec = v3 / 'modules/specialized'
for f in src_spec.glob('*.md'):
    if f.name != 'umt-architecture.md': # we removed this
        shutil.copy(f, v2 / 'modules/specialized/tr' / f.name)

src_guides = v3 / 'implementation-guides'
for f in src_guides.glob('*.md'):
    shutil.copy(f, v2 / 'modules/guides/tr' / f.name)

src_testing = v3 / 'modules/testing'
for f in src_testing.glob('*.md'):
    shutil.copy(f, v2 / 'modules/testing/tr' / f.name)

print('Files copied successfully.')

# 2. Merge MANIFEST.yaml
with open(v3 / 'MANIFEST.yaml', 'r', encoding='utf-8') as f:
    old_manifest = yaml.safe_load(f)

with open(v2 / 'MANIFEST.yaml', 'r', encoding='utf-8') as f:
    new_manifest = yaml.safe_load(f)

old_modules = old_manifest.get('modules', {})
for k, v in old_modules.items():
    if k == 'umt_architecture_analysis':
        continue
    
    # Rewrite path to include {lang} and fix guides folder
    old_path = v['path']
    if old_path.startswith('modules/core/'):
        new_path = old_path.replace('modules/core/', 'modules/core/{lang}/')
    elif old_path.startswith('modules/specialized/'):
        new_path = old_path.replace('modules/specialized/', 'modules/specialized/{lang}/')
    elif old_path.startswith('implementation-guides/'):
        new_path = old_path.replace('implementation-guides/', 'modules/guides/{lang}/')
    elif old_path.startswith('modules/testing/'):
        new_path = old_path.replace('modules/testing/', 'modules/testing/{lang}/')
    else:
        new_path = old_path
        
    v['path'] = new_path
    new_manifest['modules'][k] = v

new_manifest['total_modules'] = len(new_manifest['modules'])

# Save new manifest preserving yaml structure
with open(v2 / 'MANIFEST.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(new_manifest, f, allow_unicode=True, default_flow_style=False, sort_keys=False)

print(f"Manifest merged successfully. Total modules: {new_manifest['total_modules']}")
