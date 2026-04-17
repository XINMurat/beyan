#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pytest
import sys
from pathlib import Path

# Add project root to sys.path for IDE resolution
sys.path.insert(0, str(Path(__file__).parent.parent))

from discovery import auto_discover  # type: ignore

def test_detects_flutter_by_content(tmp_path):
    # Create a pubspec.yaml with flutter sdk
    pubspec = tmp_path / "pubspec.yaml"
    pubspec.write_text("name: my_app\ndependencies:\n  flutter:\n    sdk: flutter")
    
    tags = auto_discover(tmp_path)
    assert "flutter" in tags
    assert "mobile" in tags

def test_detects_laravel_by_content(tmp_path):
    # Create composer.json with laravel
    composer = tmp_path / "composer.json"
    composer.write_text('{"require": {"laravel/framework": "^10.0"}}')
    
    tags = auto_discover(tmp_path)
    assert "php-laravel" in tags
    assert "backend" in tags

def test_detects_go_and_rust(tmp_path):
    (tmp_path / "go.mod").write_text("module example.com/test")
    (tmp_path / "Cargo.toml").write_text("[package]\nname = 'test'")
    
    tags = auto_discover(tmp_path)
    assert "go" in tags
    assert "rust" in tags

def test_detects_prisma(tmp_path):
    (tmp_path / "schema.prisma").write_text("datasource db {\n  provider = 'postgresql'\n}")
    
    tags = auto_discover(tmp_path)
    assert "database" in tags
    assert "sql" in tags # Inferred from database tech

def test_detects_kubernetes_by_content(tmp_path):
    k8s_file = tmp_path / "deployment.yaml"
    k8s_file.write_text("apiVersion: apps/v1\nkind: Deployment\nmetadata:\n  name: my-app")
    
    tags = auto_discover(tmp_path)
    assert "infrastructure" in tags
    assert "devops" in tags

def test_security_risks(tmp_path):
    (tmp_path / ".env").write_text("API_KEY=secret")
    
    tags = auto_discover(tmp_path)
    assert "security" in tags
