# System Troubleshooting & Diagnostic Guide

This guide details diagnostics, common recovery procedures, and operational fixes for the **Engineering Mastery OS**.

---

## 1. Automated System Health Check

Whenever you suspect a configuration drift, missing file, or broken agent prompt, run the automated validation suite:

```powershell
python C:\AI-Developer\Engineering-Mastery-OS\TOOLS\system_validator.py
```

### Expected Output
```text
================================================================================
RUNNING ENGINEERING MASTERY OS VALIDATION SUITE
================================================================================
Test 1: Orchestrator curriculum loading... PASS (13 curriculum phases verified)
Test 2: Selection of DSA Agent... PASS (DSA Coach prompt verified with progressive hints and C#)
Test 3: Selection of .NET Runtime Agent... PASS (.NET Runtime Specialist prompt verified with CLR/GC/Span)
Test 4: Quality Reviewer sample defect evaluation... PASS (Reviewer dimensions and defect classification verified)
Test 5: Progress persistence write and read-back... PASS (Atomic state update and read-back confirmed)
Test 6: Session continuity and resumption after restart... PASS (Session checkpoint read and resume verified)
Test 7: Research workflow and primary source verification... PASS (Source-backed research note verified with .NET 8 citations)
Test 8: Command interface router (23 commands)... PASS (All 23 commands routed successfully)
Test 9: Agent prompt and contract integrity... PASS (13 specialist prompts + orchestrator + contract verified)
Test 10: Safety boundaries and destructive action safeguards... PASS (Safety boundaries, approval checks, and least-privilege active)
================================================================================
VALIDATION SUMMARY: 10/10 TESTS PASSED (100% SUCCESS)
================================================================================
```

---

## 2. Common Issues & Resolutions

### Issue 1: .NET SDK Version Mismatch (.NET 8 Baseline vs .NET 9 Active)
* **Symptom**: `dotnet new console` targets .NET 9.0 by default, while the curriculum baseline targets .NET 8 LTS.
* **Explanation**: The host machine has both .NET SDK 8.0.319 and .NET SDK 9.0.314 installed. .NET CLI defaults to the latest installed SDK unless pinned.
* **Resolution**: When creating projects targeting the .NET 8 compatibility baseline, pass `--framework net8.0` or create a `global.json` file in the lab directory:
  ```json
  {
    "sdk": {
      "version": "8.0.319",
      "rollForward": "latestPatch"
    }
  }
  ```

### Issue 2: Ollama Connection Refused (`http://127.0.0.1:11434`)
* **Symptom**: `Warning: could not connect to a running Ollama instance`.
* **Explanation**: Ollama is installed as a client application but is not configured as an automatic Windows service.
* **Resolution**: Start the Ollama background daemon manually:
  ```powershell
  Start-Process -FilePath "ollama" -ArgumentList "serve" -NoNewWindow
  ```
  Verify with:
  ```powershell
  curl http://127.0.0.1:11434/api/tags
  ```

### Issue 3: Session State Interruption or Crash Recovery
* **Symptom**: A training session was interrupted before completion.
* **Explanation**: The state files are atomically maintained so data cannot be corrupted, but the active step pointer may need resumption.
* **Resolution**:
  1. Inspect `STATE/CURRENT-SESSION.md` to see the last recorded checkpoint data.
  2. Run the resume command:
     ```powershell
     python C:\AI-Developer\Engineering-Mastery-OS\TOOLS\orchestrator_cli.py --command /continue
     ```
     Or type `/continue` in chat. The system will resume directly from the unfinished step without resetting the session.

### Issue 4: PowerShell Script Quoting and Dollar-Sign Traps
* **Symptom**: Errors such as `Missing variable name after foreach` or parameter binding failures when running PowerShell commands from external runners.
* **Explanation**: PowerShell evaluates `$` as a variable substitution inside double quotes (`"..."`).
* **Resolution**: Always escape `$var` as `` `$var `` in inline strings, or write a dedicated `.py` or `.ps1` script file and execute it cleanly.

### Issue 5: Antigravity Subagent Timeout
* **Symptom**: A deep code review or research subagent takes longer than normal.
* **Explanation**: Subagents run asynchronously in the background. Antigravity notifies you automatically upon completion.
* **Resolution**: You do not need to poll. If you wish to check status, invoke `manage_subagents` with `Action: "list"`.

---

## 3. Emergency State Rollback

All state updates write through `state_manager.py` using atomic temporary files. In the unlikely event that a state file requires manual reset:
1. Backups of pristine template state files exist in `C:\AI-Developer\Engineering-Mastery-OS\TEMPLATES/`.
2. To re-initialize `CURRENT-SESSION.md`, copy `TEMPLATES/SESSION-TEMPLATE.md` to `STATE/CURRENT-SESSION.md`.
