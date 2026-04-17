#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Beyan v2.0 — Enhanced Discovery Module
Scans the target directory with content-aware fingerprinting to identify technologies.
"""

import re
from pathlib import Path

EXCLUDED_DIRS = {'.git', 'node_modules', 'dist', '__pycache__', '.venv', 'venv', '.idea', 'build', 'out', 'vendor'}

# Deep Fingerprints: Mapping file patterns and content regex to tags
FINGERPRINTS = {
    "python": {
        "files": ["requirements.txt", "pyproject.toml", "setup.py"],
        "extensions": [".py", ".ipynb"],
        "content": {}
    },
    "node": {
        "files": ["package.json", "yarn.lock", "pnpm-lock.yaml"],
        "extensions": [".js", ".ts", ".jsx", ".tsx"],
        "content": {"package.json": r'"dependencies":| "devDependencies":'}
    },
    "flutter": {
        "files": ["pubspec.yaml"],
        "content": {"pubspec.yaml": r"sdk:\s*flutter"}
    },
    "react-native": {
        "files": ["app.json", "package.json"],
        "content": {"package.json": r'"react-native":'}
    },
    "go": {
        "files": ["go.mod", "go.sum"],
        "extensions": [".go"],
        "content": {}
    },
    "rust": {
        "files": ["Cargo.toml", "Cargo.lock"],
        "extensions": [".rs"],
        "content": {}
    },
    "php-laravel": {
        "files": ["artisan", "composer.json"],
        "content": {"composer.json": r'"laravel/framework":'}
    },
    "dotnet": {
        "files": [],
        "extensions": [".csproj", ".sln", ".fsproj"],
        "content": {}
    },
    "java": {
        "files": ["pom.xml", "build.gradle", "settings.gradle"],
        "extensions": [".java", ".kt"],
        "content": {}
    },
    "blockchain": {
        "files": ["hardhat.config.js", "anchor.toml", "truffle-config.js"],
        "extensions": [".sol"],
        "content": {".sol": r"pragma solidity"}
    },
    "docker": {
        "files": ["dockerfile", "docker-compose.yml", "docker-compose.yaml"],
        "content": {}
    },
    "infrastructure": {
        "files": ["main.tf", "terragrunt.hcl", "kustomization.yaml", "kustomization.yml"],
        "extensions": [".tf", ".tfvars", ".yaml", ".yml"],
        "content": {".yaml": r"apiVersion:|kind:\s*Deployment|helm\.sh", ".yml": r"apiVersion:|kind:\s*Deployment|helm\.sh", ".tf": r"resource\s+|variable\s+"}
    },
    "database": {
        "files": ["schema.prisma", "drizzle.config.ts"],
        "extensions": [".sql"],
        "content": {"schema.prisma": r"datasource\s+db", ".sql": r"CREATE TABLE|INSERT INTO"}
    },
    "security": {
        "files": [".env", "secrets.json", "credentials.json"],
        "content": {}
    }
}


def _check_content(file_path: Path, pattern: str) -> bool:
    """Helper to check if a file contains a specific regex pattern."""
    if not file_path.is_file():
        return False
    try:
        # Read only first 4KB for performance
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read(4096)
            return bool(re.search(pattern, content, re.IGNORECASE))
    except Exception:
        return False


def auto_discover(target_dir: Path) -> list:
    """
    Scans the target directory and returns discovered environment tags.
    Uses multi-stage detection: File names -> Extensions -> Content Regex.
    """
    tags = set()
    target_dir = Path(target_dir)

    # Performance optimization: collect file info first
    # We only scan 2 levels deep for tech detection to avoid deep-dive performance hits
    # but we search for specific files.
    for item in target_dir.rglob("*"):
        # Skip excluded dirs
        if any(excluded in item.parts for excluded in EXCLUDED_DIRS):
            continue
            
        if not item.is_file():
            continue

        name = item.name.lower()
        ext = item.suffix.lower()

        for tech, rules in FINGERPRINTS.items():
            found = False
            
            # 1. Match by specific filenames
            if name in [f.lower() for f in rules.get("files", [])]:
                found = True
            
            # 2. Match by extensions
            if not found and ext in rules.get("extensions", []):
                found = True
                
            # 3. Match by content if filename/extension matches a content rule
            if found and rules.get("content"):
                # Check if this specific file or extension has a regex rule
                for pattern_key, regex in rules["content"].items():
                    if name == pattern_key.lower() or ext == pattern_key.lower():
                        if not _check_content(item, regex):
                            found = False # Reset found if content check fails
                        break
            
            if found:
                tags.add(tech)
                # Add inferred tags
                if tech == "python": tags.update(["ai", "model"])
                if tech == "node": tags.update(["frontend", "web", "react"])
                if tech in ["go", "rust", "php-laravel", "java", "dotnet"]: tags.add("backend")
                if tech == "infrastructure": tags.update(["devops", "cloud", "kubernetes"])
                if tech == "database": tags.update(["data", "sql"])
                if tech == "blockchain": tags.update(["web3", "smart-contract"])
                if tech == "flutter" or tech == "react-native": tags.update(["mobile", "ios", "android"])

    return sorted(list(tags))
