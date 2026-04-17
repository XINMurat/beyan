import pytest
from pathlib import Path
from compiler import calculate_tokens, select_modules, prune_modules_by_priority

def test_calculate_tokens():
    text = "Hello world"
    tokens = calculate_tokens(text)
    assert tokens > 0
    
    long_text = "A" * 100
    long_tokens = calculate_tokens(long_text)
    assert long_tokens > 0
    assert long_tokens < 100 # Should be compressed

def test_select_modules_basic():
    manifest = {
        "modules": {
            "m1": {"priority": "P0", "auto_load": True},
            "m2": {"priority": "P1", "auto_load_if": ["tag1"]},
            "m3": {"priority": "P3", "auto_load_if": ["tag2"]}
        }
    }
    # P0 should always load
    mods = select_modules(manifest, [], "en")
    assert "m1" in mods
    assert len(mods) == 1
    
    # Tag1 should load m2
    mods = select_modules(manifest, ["tag1"], "en")
    assert "m1" in mods
    assert "m2" in mods
    assert len(mods) == 2

def test_select_modules_dependencies():
    manifest = {
        "modules": {
            "m1": {"priority": "P1", "auto_load_if": ["tag1"], "dependencies": ["dep1"]},
            "dep1": {"priority": "P2", "dependencies": ["dep2"]},
            "dep2": {"priority": "P3"}
        }
    }
    mods = select_modules(manifest, ["tag1"], "en")
    assert "m1" in mods
    assert "dep1" in mods
    assert "dep2" in mods
    assert len(mods) == 3

def test_prune_modules():
    manifest = {
        "modules": {
            "p0_mod": {"priority": "P0"},
            "p2_mod": {"priority": "P2"},
            "p3_mod": {"priority": "P3"}
        }
    }
    mods = ["p0_mod", "p2_mod", "p3_mod"]
    
    # Prune should remove P3 first
    pruned = prune_modules_by_priority(manifest, mods, "en")
    assert "p3_mod" not in pruned
    assert "p2_mod" in pruned
    assert "p0_mod" in pruned
    
    # Next prune should remove P2
    pruned2 = prune_modules_by_priority(manifest, pruned, "en")
    assert "p2_mod" not in pruned2
    assert "p0_mod" in pruned2
    
    # Cannot prune P0
    pruned3 = prune_modules_by_priority(manifest, pruned2, "en")
    assert pruned3 is None
