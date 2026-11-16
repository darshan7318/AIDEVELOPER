"""
Agent Loader & Prompt Registry for Engineering Mastery OS
Loads specialist agent system prompts, verifies prompt contracts, and prepares subagent definitions.
"""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional

OS_ROOT = Path(r"C:\AI-Developer\Engineering-Mastery-OS")
CONFIG_DIR = OS_ROOT / "CONFIG"
PROMPTS_DIR = OS_ROOT / "PROMPTS"

def load_agents_config() -> Dict[str, Any]:
    with open(CONFIG_DIR / "agents.json", "r", encoding="utf-8") as f:
        return json.load(f)

def get_orchestrator_prompt() -> str:
    path = PROMPTS_DIR / "master" / "orchestrator.md"
    return path.read_text(encoding="utf-8")

def get_agent_prompt(code: str) -> Optional[str]:
    cfg = load_agents_config()
    for sp in cfg["specialists"]:
        if sp["code"] == code or sp["id"] == code:
            path = OS_ROOT / sp["prompt_path"]
            if path.exists():
                return path.read_text(encoding="utf-8")
    return None

def list_specialists() -> List[Dict[str, Any]]:
    cfg = load_agents_config()
    return cfg["specialists"]

def validate_all_prompts() -> Dict[str, bool]:
    results = {}
    cfg = load_agents_config()
    
    # Check orchestrator
    orch_path = OS_ROOT / cfg["orchestrator"]["prompt_path"]
    results["orchestrator"] = orch_path.exists() and len(orch_path.read_text(encoding="utf-8")) > 100
    
    # Check each specialist
    for sp in cfg["specialists"]:
        sp_path = OS_ROOT / sp["prompt_path"]
        results[sp["code"]] = sp_path.exists() and len(sp_path.read_text(encoding="utf-8")) > 100
        
    return results

def get_subagent_specs_for_platform() -> List[Dict[str, Any]]:
    """Returns specialist configurations formatted for native subagent declaration."""
    cfg = load_agents_config()
    specs = []
    for sp in cfg["specialists"]:
        prompt = get_agent_prompt(sp["code"])
        specs.append({
            "name": f"specialist_{sp['code'].replace('-', '_')}",
            "role": sp["name"],
            "description": f"Domain: {sp['domain']}",
            "system_prompt": prompt,
            "enable_write_tools": True,
            "enable_subagent_tools": False,
            "enable_mcp_tools": False
        })
    return specs
