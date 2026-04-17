#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Beyan v2.0 — Unit Tests
Run: pytest tests/ -v --cov=cli --cov-report=term-missing
"""
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock
import pytest  # type: ignore

# Add project root to sys.path for IDE resolution
sys.path.insert(0, str(Path(__file__).parent.parent))

# Direct imports from the root (all core files are now in the same folder as pyproject.toml)
from discovery import auto_discover, EXCLUDED_DIRS  # type: ignore
from compiler import calculate_tokens, select_modules, compile_prompt, check_token_budget  # type: ignore
from orchestrator import run_interactive_loop  # type: ignore


# ─────────────────────────────────────────────
# Tests: discovery.py
# ─────────────────────────────────────────────

class TestAutoDiscover:
    def test_detects_python_project(self, tmp_path):
        (tmp_path / "requirements.txt").write_text("flask")
        tags = auto_discover(tmp_path)
        assert "python" in tags
        assert "ai" in tags  # Python projects often involve AI in our framework context

    def test_detects_node_project(self, tmp_path):
        # We need dependencies/devDependencies in package.json now for content-aware detection
        (tmp_path / "package.json").write_text('{"dependencies": {}}')
        tags = auto_discover(tmp_path)
        assert "node" in tags
        assert "frontend" in tags

    def test_detects_docker_project(self, tmp_path):
        (tmp_path / "Dockerfile").write_text("FROM python")
        tags = auto_discover(tmp_path)
        assert "docker" in tags

    def test_detects_dotnet_project(self, tmp_path):
        (tmp_path / "App.csproj").write_text("<Project/>")
        tags = auto_discover(tmp_path)
        assert "dotnet" in tags
        assert "backend" in tags

    def test_excludes_node_modules(self, tmp_path):
        # node_modules should be in excluded set
        assert "node_modules" in EXCLUDED_DIRS

    def test_empty_dir_returns_empty_tags(self, tmp_path):
        tags = auto_discover(tmp_path)
        assert isinstance(tags, list)

    def test_blockchain_detection(self, tmp_path):
        (tmp_path / "hardhat.config.js").write_text("module.exports = {}")
        tags = auto_discover(tmp_path)
        assert "blockchain" in tags
        assert "web3" in tags


# ─────────────────────────────────────────────
# Tests: compiler.py — calculate_tokens
# ─────────────────────────────────────────────

class TestCalculateTokens:
    def test_empty_string(self):
        assert calculate_tokens("") == 0

    def test_known_length_heuristic(self):
        # Use realistic prose text, not repeated chars (tokenizers merge long runs of 'a')
        text = "The quick brown fox jumps over the lazy dog. " * 20  # ~900 chars
        tokens = calculate_tokens(text)
        # Both tiktoken and heuristic should land in 150-300 range for this text
        assert 150 <= tokens <= 300

    def test_returns_int(self):
        result = calculate_tokens("hello world")
        assert isinstance(result, int)
        assert result > 0

    def test_longer_text_has_more_tokens(self):
        short = calculate_tokens("hello")
        long = calculate_tokens("hello " * 100)
        assert long > short


# ─────────────────────────────────────────────
# Tests: compiler.py — select_modules
# ─────────────────────────────────────────────

class TestSelectModules:
    def _make_manifest(self, modules: dict) -> dict:
        return {"modules": modules, "max_total_tokens": 35000}

    def test_p0_always_loaded(self):
        manifest = self._make_manifest({
            "always_on": {"priority": "P0", "auto_load_if": []},
            "optional": {"priority": "P3", "auto_load_if": ["node"]},
        })
        result = select_modules(manifest, [], "tr")
        assert "always_on" in result

    def test_tag_match_loads_module(self):
        manifest = self._make_manifest({
            "node_module": {"priority": "P2", "auto_load_if": ["node", "package.json"]},
        })
        result = select_modules(manifest, ["node"], "tr")
        assert "node_module" in result

    def test_no_match_loads_web_mobile_fallback(self):
        manifest = self._make_manifest({
            "web_mobile": {"priority": "P2", "auto_load_if": ["package.json"]},
        })
        result = select_modules(manifest, [], "tr")
        assert "web_mobile" in result

    def test_unmatched_tags_skipped(self):
        manifest = self._make_manifest({
            "blockchain": {"priority": "P2", "auto_load_if": ["solidity", "web3"]},
        })
        result = select_modules(manifest, ["python"], "tr")
        assert "blockchain" not in result

    def test_auto_load_true_always_loads(self):
        manifest = self._make_manifest({
            "special": {"priority": "P2", "auto_load": True, "auto_load_if": []},
        })
        result = select_modules(manifest, [], "tr")
        assert "special" in result


# ─────────────────────────────────────────────
# Tests: compiler.py — compile_prompt
# ─────────────────────────────────────────────

class TestCompilePrompt:
    def _make_manifest(self, modules=None):
        return {
            "base_prompt": "core_prompts/{lang}/BASE_PROMPT.md",
            "orchestrator_prompt": "core_prompts/{lang}/ORCHESTRATOR_PROMPT.md",
            "modules": modules or {},
            "max_total_tokens": 35000,
        }

    def test_mode_in_header(self, tmp_path):
        manifest = self._make_manifest()
        # Create minimal core prompt files
        core_tr = tmp_path / "core_prompts" / "tr"
        core_tr.mkdir(parents=True)
        (core_tr / "BASE_PROMPT.md").write_text("base")
        (core_tr / "ORCHESTRATOR_PROMPT.md").write_text("orch")
        result = compile_prompt(tmp_path, manifest, [], 2, "tr")
        assert "Mode 2" in result
        assert "TR" in result

    def test_mode1_suffix_injected(self, tmp_path):
        manifest = self._make_manifest()
        core_tr = tmp_path / "core_prompts" / "tr"
        core_tr.mkdir(parents=True)
        (core_tr / "BASE_PROMPT.md").write_text("base")
        (core_tr / "ORCHESTRATOR_PROMPT.md").write_text("orch")
        result = compile_prompt(tmp_path, manifest, [], 1, "tr")
        assert "Mode 1" in result
        assert "Analiz Raporu" in result

    def test_mode2_plan_instructions_present(self, tmp_path):
        manifest = self._make_manifest()
        core_tr = tmp_path / "core_prompts" / "tr"
        core_tr.mkdir(parents=True)
        (core_tr / "BASE_PROMPT.md").write_text("base")
        (core_tr / "ORCHESTRATOR_PROMPT.md").write_text("orch")
        result = compile_prompt(tmp_path, manifest, [], 2, "tr")
        assert "implementation_plan.md" in result
        assert "Sprint 1" in result

    def test_mode3_checkpoint_instructions_present(self, tmp_path):
        manifest = self._make_manifest()
        core_tr = tmp_path / "core_prompts" / "tr"
        core_tr.mkdir(parents=True)
        (core_tr / "BASE_PROMPT.md").write_text("base")
        (core_tr / "ORCHESTRATOR_PROMPT.md").write_text("orch")
        result = compile_prompt(tmp_path, manifest, [], 3, "tr")
        assert "CHECKPOINT" in result
        assert "GÜVENLİK KURALLARI" in result


# ─────────────────────────────────────────────
# Tests: compiler.py — check_token_budget
# ─────────────────────────────────────────────

class TestCheckTokenBudget:
    def test_within_budget_returns_count(self):
        manifest = {"max_total_tokens": 35000}
        count, is_exceeded = check_token_budget("a" * 100, manifest, "en")
        assert isinstance(count, int)
        assert count > 0
        assert is_exceeded is False

    def test_exceeds_budget_flag(self):
        manifest = {"max_total_tokens": 10}
        count, is_exceeded = check_token_budget("a" * 1000, manifest, "en")
        assert is_exceeded is True


# ─────────────────────────────────────────────
# Tests: orchestrator.py
# ─────────────────────────────────────────────

class TestOrchestrator:
    @patch("orchestrator.call_openai")
    @patch("orchestrator.load_session", return_value=[])
    @patch("orchestrator.save_session")
    @patch("builtins.input", side_effect=["q"])
    def test_loop_terminates_immediately_on_q(self, mock_input, mock_save, mock_load, mock_api, tmp_path):
        mock_api.return_value = "CHECKPOINT: Do something"
        
        manifest = {"max_agentic_turns": 5}
        run_interactive_loop("openai", "start", manifest, tmp_path, "en", "test_session_1")
        
        # Should have called API once and then stopped because of 'q'
        assert mock_api.call_count == 1

    @patch("orchestrator.call_anthropic")
    @patch("orchestrator.load_session", return_value=[])
    @patch("orchestrator.save_session")
    @patch("builtins.input", side_effect=["yes", "q"])
    def test_loop_continues_on_yes_then_terminates(self, mock_input, mock_save, mock_load, mock_api, tmp_path):
        mock_api.return_value = "CHECKPOINT: Step 1"
        
        manifest = {"max_agentic_turns": 5}
        run_interactive_loop("anthropic", "start", manifest, tmp_path, "en", "test_session_2")
        
        # 1st call: "start" -> response "CHECKPOINT" -> user "yes"
        # 2nd call: user "yes" -> response "CHECKPOINT" -> user "q"
        assert mock_api.call_count == 2

    @patch("orchestrator.call_openai")
    @patch("orchestrator.load_session", return_value=[])
    @patch("orchestrator.save_session")
    @patch("builtins.input", side_effect=[""])  # User just presses enter
    def test_no_checkpoint_ask_followup(self, mock_input, mock_save, mock_load, mock_api, tmp_path):
        mock_api.return_value = "Final report. No checkpoints."
        
        manifest = {"max_agentic_turns": 5}
        run_interactive_loop("openai", "start", manifest, tmp_path, "en", "test_session_3")
        
        # Should stop because enter (empty string) means "no" in the follow-up prompt
        assert mock_api.call_count == 1
