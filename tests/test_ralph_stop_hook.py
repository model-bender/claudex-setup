"""Regression cases for scripts/ralph-stop-hook.sh, the Stop hook behind /ralph-loop.

The same script serves Claude Code (which sends a transcript path) and Codex (which
sends last_assistant_message). Each case sets up a loop with the real setup script in
a temporary directory, feeds the hook a payload shaped like that tool's Stop event,
and checks what the tool would do next. Codex rejects plain text on stdout from a Stop
hook, so every case also checks stdout is empty or one JSON object.

Run: uv run --with pytest pytest -q tests/
"""

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SETUP = REPO / "scripts" / "setup-ralph-loop.sh"
HOOK = REPO / "scripts" / "ralph-stop-hook.sh"
STATE = Path(".claude") / "ralph-loop.local.md"

pytestmark = pytest.mark.skipif(shutil.which("bash") is None, reason="needs bash")


def start_loop(tmp_path, *args):
    subprocess.run(["bash", str(SETUP), *args], cwd=tmp_path, check=True, capture_output=True, text=True)
    return tmp_path / STATE


def run_hook(tmp_path, payload, env=None):
    result = subprocess.run(["bash", str(HOOK)], cwd=tmp_path, input=json.dumps(payload),
                            capture_output=True, text=True, env=env)
    out = result.stdout.strip()
    data = json.loads(out) if out else None
    if out:
        assert isinstance(data, dict), f"stdout is not one JSON object: {out!r}"
    return result.returncode, data


def codex_stop(message, active=False):
    return {"session_id": "s", "transcript_path": None, "cwd": "/w", "hook_event_name": "Stop",
            "model": "gpt-6.1-sol", "turn_id": "t", "permission_mode": "default",
            "stop_hook_active": active, "last_assistant_message": message}


def test_no_active_loop_lets_the_session_stop(tmp_path):
    code, data = run_hook(tmp_path, codex_stop("anything"))
    assert (code, data) == (0, None)


def test_codex_without_the_promise_continues_with_the_same_prompt(tmp_path):
    state = start_loop(tmp_path, "Fix", "the", "flaky", "test", "--max-iterations", "5",
                       "--completion-promise", "DONE")
    code, data = run_hook(tmp_path, codex_stop("Still working on it.", active=True))
    assert code == 0
    assert data["decision"] == "block"
    assert data["reason"].strip() == "Fix the flaky test"
    assert "iteration: 2" in state.read_text()


def test_codex_with_the_promise_ends_the_loop(tmp_path):
    state = start_loop(tmp_path, "Fix it", "--completion-promise", "DONE")
    code, data = run_hook(tmp_path, codex_stop("All green now. <promise>DONE</promise>"))
    assert code == 0
    assert "decision" not in data
    assert "Complete" in data["systemMessage"]
    assert not state.exists()


def test_max_iterations_ends_the_loop_with_a_json_status(tmp_path):
    state = start_loop(tmp_path, "Fix it", "--max-iterations", "1")
    code, data = run_hook(tmp_path, codex_stop("Did one pass."))
    assert code == 0
    assert "Max iterations (1)" in data["systemMessage"]
    assert not state.exists()


def claude_stop(tmp_path, text):
    transcript = tmp_path / "transcript.jsonl"
    line = {"type": "assistant", "message": {"role": "assistant", "content": [{"type": "text", "text": text}]}}
    transcript.write_text(json.dumps(line, separators=(",", ":")) + "\n")
    return {"session_id": "s", "transcript_path": str(transcript), "hook_event_name": "Stop",
            "stop_hook_active": False}


def test_claude_code_transcript_still_drives_the_loop(tmp_path):
    start_loop(tmp_path, "Fix it", "--completion-promise", "DONE")
    code, data = run_hook(tmp_path, claude_stop(tmp_path, "Not done yet."))
    assert code == 0
    assert data["decision"] == "block"
    assert data["reason"].strip() == "Fix it"


def test_runs_where_only_python3_exists(tmp_path):
    # WSL has python3 and no python. A failing `python` first on PATH stands in for
    # that here, since the test runner itself may supply one. The hook used to call
    # python unconditionally, so on WSL it ended every loop after one pass.
    shims = tmp_path / "shims"
    shims.mkdir()
    (shims / "python").write_text("#!/bin/sh\nexit 127\n")
    (shims / "python").chmod(0o755)
    env = dict(os.environ, PATH=f"{shims}{os.pathsep}{os.environ['PATH']}")
    start_loop(tmp_path, "Fix it", "--completion-promise", "DONE")
    code, data = run_hook(tmp_path, claude_stop(tmp_path, "Not done yet."), env=env)
    assert code == 0
    assert data and data["decision"] == "block"
