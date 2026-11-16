"""
State Manager for Engineering Mastery OS
Provides safe, atomic reads and writes of learning state files.
"""

import os
import json
import tempfile
from pathlib import Path
from typing import Dict, Any, Optional

OS_ROOT = Path(r"C:\AI-Developer\Engineering-Mastery-OS")
STATE_DIR = OS_ROOT / "STATE"
CONFIG_DIR = OS_ROOT / "CONFIG"

def _atomic_write_text(filepath: Path, content: str) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    temp_dir = filepath.parent
    with tempfile.NamedTemporaryFile("w", dir=temp_dir, delete=False, encoding="utf-8") as tf:
        tf.write(content)
        temp_path = Path(tf.name)
    temp_path.replace(filepath)

def load_settings() -> Dict[str, Any]:
    with open(CONFIG_DIR / "settings.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_curriculum() -> Dict[str, Any]:
    with open(CONFIG_DIR / "curriculum.json", "r", encoding="utf-8") as f:
        return json.load(f)

def load_current_session() -> str:
    path = STATE_DIR / "CURRENT-SESSION.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""

def save_current_session(content: str) -> None:
    _atomic_write_text(STATE_DIR / "CURRENT-SESSION.md", content)

def load_progress() -> str:
    path = STATE_DIR / "PROGRESS.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""

def save_progress(content: str) -> None:
    _atomic_write_text(STATE_DIR / "PROGRESS.md", content)

def load_competency_matrix() -> str:
    path = STATE_DIR / "COMPETENCY-MATRIX.md"
    if path.exists():
        return path.read_text(encoding="utf-8")
    return ""

def update_competency(domain: str, rating: str, evidence: str, weakness: str, next_assessment: str) -> None:
    path = STATE_DIR / "COMPETENCY-MATRIX.md"
    content = path.read_text(encoding="utf-8")
    lines = content.splitlines()
    new_lines = []
    updated = False
    
    for line in lines:
        if line.startswith(f"| {domain} "):
            new_lines.append(f"| {domain} | {rating} | {evidence} | {weakness} | {next_assessment} |")
            updated = True
        else:
            new_lines.append(line)
            
    if not updated:
        # Append before note if possible
        new_lines.append(f"| {domain} | {rating} | {evidence} | {weakness} | {next_assessment} |")
        
    _atomic_write_text(path, "\n".join(new_lines))

def add_weakness(weakness_id: str, topic: str, severity: str, root_cause: str, remediation: str, reassessment_date: str) -> None:
    path = STATE_DIR / "WEAKNESS-REGISTER.md"
    content = path.read_text(encoding="utf-8")
    new_entry = f"| {weakness_id} | {topic} | {severity} | 2026-11-16 | {root_cause} | {remediation} | {reassessment_date} | Open |"
    updated_content = content.strip() + "\n" + new_entry + "\n"
    _atomic_write_text(path, updated_content)

def add_revision_item(topic: str, pattern: str, interval_days: int) -> None:
    path = STATE_DIR / "REVISION-QUEUE.md"
    content = path.read_text(encoding="utf-8")
    new_entry = f"| {topic} | {pattern} | 2026-11-16 | Due in {interval_days}d | {interval_days} | In Queue | Active |"
    updated_content = content.strip() + "\n" + new_entry + "\n"
    _atomic_write_text(path, updated_content)

def append_session_history(session_num: int, summary: str, score: Optional[int] = None) -> None:
    path = STATE_DIR / "SESSION-HISTORY.md"
    content = path.read_text(encoding="utf-8")
    entry = f"""
## Session {session_num:03d} — {summary} (2026-11-16)
- **Score**: {score if score is not None else 'N/A'}
- **Summary**: {summary}
"""
    _atomic_write_text(path, content.strip() + "\n" + entry)
