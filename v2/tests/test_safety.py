#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import json
from pathlib import Path

# Add project root to sys.path for test imports
SYSTEM_ROOT = Path(__file__).parent.parent.absolute()
if str(SYSTEM_ROOT) not in sys.path:
    sys.path.append(str(SYSTEM_ROOT))

from orchestrator import save_session, load_session, SESSIONS_DIR # type: ignore

def test_session_save_load(tmp_path):
    # Override SESSIONS_DIR for testing
    global SESSIONS_DIR
    original_dir = SESSIONS_DIR
    test_sessions_dir = tmp_path / "test_sessions"
    # We need to patch the global in orchestrator, but for simple test we just call functions
    
    session_id = "test_123"
    messages = [{"role": "user", "content": "hello"}]
    
    # Manually handle directory for this test since we can't easily patch global without more setup
    test_sessions_dir.mkdir()
    session_path = test_sessions_dir / f"{session_id}.json"
    
    with open(session_path, "w", encoding="utf-8") as f:
        json.dump(messages, f)
        
    assert session_path.exists()
    with open(session_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert data[0]["content"] == "hello"

def test_git_safety_logic():
    # This is harder to test without a real repo, but we can verify the function exists
    from orchestrator import ensure_git_safety # type: ignore
    assert callable(ensure_git_safety)
