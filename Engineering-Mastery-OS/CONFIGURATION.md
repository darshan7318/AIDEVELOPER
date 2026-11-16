# System Configuration Guide

This document details the environment specifications, configuration files, runtime parameters, and customization options for the **Engineering Mastery OS**.

---

## 1. Verified Host Environment

An audit was performed directly on this machine:

| Component | Status | Audited Version / Location |
|---|---|---|
| **Operating System** | Available | Windows 11 Home (AMD64, 10.0.19045) |
| **.NET SDKs** | Available | 8.0.319 (Baseline), 9.0.314 (Active Host), 6.0.428 (`C:\Program Files\dotnet\sdk`) |
| **.NET Runtimes** | Available | Microsoft.AspNetCore.App 8.0.22/27, 9.0.16; Microsoft.NETCore.App 8.0/9.0 |
| **Python** | Available | Python 3.14.6 (`MSC v.1944 64 bit`) |
| **Node.js** | Available | v22.19.0 |
| **Git** | Available | 2.43.0.windows.1 |
| **Ollama** | Available with Config | Client 0.40.13 installed; daemon starts via `ollama serve` |
| **Primary Workspace** | Configured | `C:\AI-Developer\Engineering-Mastery-OS` |
| **Original Assets** | Preserved | `F:\personal\PR\engineering_mastery_agent_prompts` |

---

## 2. Configuration File Reference

All global system parameters reside in `C:\AI-Developer\Engineering-Mastery-OS\CONFIG/`:

### `CONFIG/settings.json`
Controls active frameworks, paths, session durations, and safety boundaries:
```json
{
  "system_name": "Engineering Mastery OS",
  "training_configuration": {
    "target_level": "Senior / Staff Software Engineer & FDE (8-10 years)",
    "default_session_minutes": 120,
    "session_distribution": {
      "retrieval_and_revision_minutes": 15,
      "dsa_challenge_minutes": 30,
      "deep_technical_lesson_minutes": 30,
      "hands_on_implementation_and_tests_minutes": 30,
      "rotating_simulation_minutes": 10,
      "review_and_progress_minutes": 5
    }
  },
  "safety_boundaries": {
    "destructive_operations_require_approval": true,
    "unrestricted_shell_execution": false,
    "untrusted_data_defense": true,
    "external_purchases_allowed": false
  }
}
```

### `CONFIG/agents.json`
Defines the authoritative registry of the Master Orchestrator and all 13 Specialist Agents, mapping agent codes to prompt paths and allowed tools.

### `CONFIG/curriculum.json`
Specifies all 13 phases (Phase 00 through Phase 12), their objectives, prerequisites, and mandatory gate criteria.

### `CONFIG/evaluation-rubric.json`
Specifies the 100-point scoring rubric across the 7 evaluation dimensions and outlines the 6 criteria required before awarding mastery.

---

## 3. Customizing Your Daily Training Session

### Changing Session Duration
The default session budget is **120 minutes**. To adjust the duration for a shorter day (e.g. 60 minutes):

1. **Via CLI**:
   ```powershell
   python C:\AI-Developer\Engineering-Mastery-OS\TOOLS\orchestrator_cli.py --command /start --time 60
   ```
2. **Via Chat**:
   Simply tell the orchestrator:
   > "I only have 60 minutes today. Please adjust today's training split."

The orchestrator dynamically scales the time distribution:
- 10 min: Retrieval & revision
- 20 min: DSA problem
- 20 min: Deep technical lesson & implementation
- 5 min: System design or debugging scenario
- 5 min: Progress review

---

## 4. Enabling Local Ollama Inference (Optional)

Ollama is installed on your machine (`v0.40.13`). If you want to run local inference for Agentic AI labs or offline agent execution:

1. Open PowerShell and start the Ollama daemon:
   ```powershell
   ollama serve
   ```
2. In a separate terminal, pull a local model:
   ```powershell
   ollama pull llama3.2:3b
   # or for coding:
   ollama pull qwen2.5-coder:7b
   ```
3. Test connectivity:
   ```powershell
   Invoke-RestMethod -Uri "http://127.0.0.1:11434/api/tags"
   ```
4. Update `CONFIG/settings.json` under `"ollama"` to set `"active_model": "qwen2.5-coder:7b"`.
