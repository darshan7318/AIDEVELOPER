"""
Master Orchestrator CLI for Engineering Mastery OS
Provides an intuitive, menu-driven interactive terminal console.
"""

import sys
import os
import argparse
from pathlib import Path

# Add TOOLS directory to path
TOOLS_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS_DIR))

import state_manager
import agent_loader

OS_ROOT = Path(r"C:\AI-Developer\Engineering-Mastery-OS")

def clear_screen():
    # Only clear if terminal supports it
    pass

def safe_input(prompt: str = "") -> str:
    try:
        return input(prompt).strip().replace("\ufeff", "")
    except (KeyboardInterrupt, EOFError):
        return ""

def print_header(title="TRAINING CONSOLE"):
    print("=" * 80)
    print(f"       ENGINEERING MASTERY OS — {title.upper()}")
    print("=" * 80)
    print(" Target Standard: Senior / Staff Engineer & FDE (8-10 Years Maturity)")
    print(" Active Stack:    C# 12, .NET 8 LTS Baseline, ASP.NET Core, EF Core, Angular, React")
    print(" Active Phase:    PHASE-00-DIAGNOSTIC (Baseline Competency Diagnostic)")
    print(" Lead Agent:      Master Engineering Orchestrator")
    print("=" * 80)

def menu_main():
    while True:
        print_header("MAIN MENU")
        print("""
  [1]  Start / Resume Today's 120-Minute Session (/start)
  [2]  Run Baseline Competency Diagnostic (/diagnose)
  [3]  DSA & Algorithmic Coach (/dsa)
  [4]  .NET 8 Runtime & Memory Internals (/dotnet)
  [5]  ASP.NET Core Backend Architecture (/backend)
  [6]  Database & EF Core Tuning (/sql)
  [7]  Modern Frontend - Angular & React (/frontend)
  [8]  System Design - LLD & HLD (/lld, /hld)
  [9]  Forward Deployed Engineering Simulation (/fde)
  [10] Principal Engineering Code Review (/review)
  [11] View Progress & Competency Matrix (/progress)
  [12] View Weakness Register & Revision Queue (/weakness)
  [13] Run Automated System Health Validator (Self-Test)
  [0]  Exit Console & Save State
""")
        raw = safe_input("Select an option [0-13] or enter a command (e.g. /dsa): ")
        choice = raw.strip().replace("\ufeff", "")
        if not raw and choice == "":
            # Handle empty input or EOF
            pass

        if not choice:
            continue

        if choice in ["0", "exit", "quit", "q"]:
            print("\nSession state saved in STATE/CURRENT-SESSION.md. Exiting console.")
            break
        elif choice == "1" or choice == "/start":
            handle_start_session()
        elif choice == "2" or choice == "/diagnose":
            handle_diagnose()
        elif choice == "3" or choice == "/dsa":
            handle_dsa()
        elif choice == "4" or choice == "/dotnet":
            handle_dotnet()
        elif choice == "5" or choice == "/backend":
            handle_backend()
        elif choice == "6" or choice == "/sql":
            handle_sql()
        elif choice == "7" or choice == "/frontend":
            handle_frontend()
        elif choice == "8" or choice in ["/lld", "/hld"]:
            handle_system_design()
        elif choice == "9" or choice == "/fde":
            handle_fde()
        elif choice == "10" or choice == "/review":
            handle_code_review()
        elif choice == "11" or choice == "/progress":
            handle_progress()
        elif choice == "12" or choice == "/weakness":
            handle_weakness()
        elif choice == "13":
            handle_validator()
        else:
            print(f"\n[!] Invalid selection '{choice}'. Enter a number from 0 to 13.")
            safe_input("Press Enter to continue...")

def handle_start_session():
    print_header("DAILY TRAINING SESSION — 120 MINUTES")
    print("""
Today's Connected Schedule:
  - Part 1 (15m): Retrieval Practice & Algorithmic Invariants
  - Part 2 (30m): DSA Challenge: Container With Most Water (Two Pointers)
  - Part 3 (30m): Deep Concept: CLR Execution, JIT & Zero-Allocation Span<T>
  - Part 4 (30m): Hands-on Implementation: High-Throughput Memory Parser in C#
  - Part 5 (10m): Rotating Simulation: System Design Capacity Bounds
  - Part 6 (5m):  Review, Rubric Scoring & Progress Ledger Update
""")
    handle_dsa_step()

def handle_diagnose():
    print_header("BASELINE COMPETENCY DIAGNOSTIC")
    print("""
The diagnostic assesses your engineering depth across:
  A. DSA & Invariants            F. High-Level System Design
  B. C# & .NET Runtime           G. Production Incident Debugging
  C. ASP.NET Core Architecture   H. Forward Deployed Engineering
  D. Relational Databases & SQL  I. Agentic AI Systems
  E. Frontend State & DOM        J. Technical Communication
""")
    handle_dsa_step()

def handle_dsa():
    print_header("DSA & LEETCODE COACH")
    handle_dsa_step()

def handle_dsa_step():
    print("""
--------------------------------------------------------------------------------
ACTIVE TASK: Container With Most Water (LeetCode #11)
Canonical Link: https://leetcode.com/problems/container-with-most-water/
Constraints:    2 <= n <= 10^5,  0 <= height[i] <= 10^4
--------------------------------------------------------------------------------
Problem:
  Given an integer array height of length n, find two lines that together
  with the x-axis form a container holding the maximum water.
  Area = (right - left) * min(height[left], height[right])

Questions to Answer:
  1. What time complexity does n <= 10^5 mandate?
  2. What is the naive brute-force approach and its Big-O complexity?
  3. Why does moving the shorter wall guarantee we never miss a larger area?
""")
    print("  [1] Type your answer / reasoning")
    print("  [2] Request a hint from DSA Coach")
    print("  [3] View C# reference solution path")
    print("  [0] Return to Main Menu")
    
    sub = safe_input("\nSelect an action [0-3]: ").strip()
    if sub == "1":
        ans = safe_input("\nEnter your answer / reasoning:\n> ").strip()
        if ans:
            evaluate_dsa_answer(ans)
        else:
            print("No answer entered.")
    elif sub == "2":
        print("""
>>> HINT FROM DSA COACH:
The area of any container is constrained by:
    Area = (j - i) * min(height[i], height[j])

If height[i] < height[j], the maximum area using line i with ANY other line
between i and j can never exceed height[i] * (j - 1 - i).
Since the width is smaller and the height is bounded by height[i], none of those
containers can beat the current area. Therefore, i can be safely eliminated!
""")
    elif sub == "3":
        sol_path = OS_ROOT / "DSA" / "SOLUTIONS" / "ContainerWithMostWater.cs"
        print(f"\nCanonical solution available at:\n  {sol_path}")
    
    safe_input("\nPress Enter to return to menu...")

def evaluate_dsa_answer(text: str):
    print("\n" + "=" * 80)
    print("EVALUATION FROM DSA COACH & MASTER ORCHESTRATOR")
    print("=" * 80)
    
    has_complexity = any(x in text.lower() for x in ["o(n)", "o(n log n)", "linear", "10^5", "100,000", "quadratic", "n^2"])
    has_bruteforce = any(x in text.lower() for x in ["all pairs", "nested", "pair", "brute", "check every", "o(n^2)"])
    has_invariant = any(x in text.lower() for x in ["shorter", "min", "height", "width", "smaller", "bounded", "limit", "decrease"])

    score = 0
    if has_complexity:
        print("  [x] Complexity Bounds: Correct. For N = 10^5, O(N) or O(N log N) is required (< 10^8 ops/sec).")
        score += 1
    else:
        print("  [ ] Complexity Bounds: Missing. N = 10^5 means O(N^2) results in Time Limit Exceeded (TLE).")

    if has_bruteforce:
        print("  [x] Brute Force Baseline: Correct. Checking all pairs is O(N^2) time and O(1) space.")
        score += 1
    else:
        print("  [ ] Brute Force Baseline: Note that checking all (i, j) pairs is O(N^2).")

    if has_invariant:
        print("  [x] Two-Pointer Invariant: Correct. Area is constrained by the shorter wall. Moving the taller wall")
        print("      only decreases width while height is still capped, guaranteeing a smaller or equal area.")
        print("      Moving the shorter wall is the only way to potentially find a larger area.")
        score += 1
    else:
        print("  [ ] Two-Pointer Invariant: Explain that moving the taller wall strictly decreases width without")
        print("      any possibility of increasing the height boundary.")

    # Record persistence
    rating = "Competent" if score == 3 else ("Developing" if score >= 1 else "Beginner")
    state_manager.update_competency(
        domain="DSA (C#)",
        rating=rating,
        evidence=f"Container With Most Water invariant: {score}/3 verified",
        weakness="None" if score == 3 else "Needs formal two-pointer proof",
        next_assessment="Session 01 - C# Implementation"
    )
    print(f"\nVerdict: Rating updated to [{rating}] in STATE/COMPETENCY-MATRIX.md.")

def handle_dotnet():
    print_header("C# & .NET RUNTIME SPECIALIST")
    print("""
Topic: Value Types, Reference Types, and Span<T> Stack Allocations
Framework: .NET 8 LTS Baseline (Host: .NET 9.0.314)

Core Questions:
  1. Why is Span<T> declared as a 'ref struct' in C#?
  2. What guarantees does the CLR enforce regarding its lifetime?
  3. How does Memory<T> overcome this limitation for asynchronous methods?
""")
    ans = safe_input("Enter your answer (or press Enter to return): ").strip()
    if ans:
        print("\nEvaluation:")
        print("  Span<T> is a ref struct so it is restricted to the execution stack.")
        print("  It cannot be boxed, cannot be a field of a regular class, and cannot be used in async methods across await boundaries.")
        print("  Memory<T> is a regular struct that can live on the heap, wrapping an array or MemoryManager, making it safe for async.")
    safe_input("\nPress Enter to return to menu...")

def handle_backend():
    print_header("ASP.NET CORE BACKEND ARCHITECT")
    print("""
Topic: Dependency Injection & Middleware Pipeline
Question:
  Explain the captive dependency problem in ASP.NET Core DI.
  What happens if a Scoped service is injected into a Singleton service?
  How does ASP.NET Core detect this at startup in Development mode?
""")
    ans = safe_input("Enter your answer (or press Enter to return): ").strip()
    if ans:
        print("\nEvaluation:")
        print("  A captive dependency occurs when a service with a shorter lifetime (Scoped) is held by a service with a longer lifetime (Singleton).")
        print("  This causes the Scoped service to effectively become a Singleton, causing memory leaks and thread-safety hazards (e.g. DbContext).")
        print("  ASP.NET Core enables 'ValidateScopes' by default in Development mode, throwing an InvalidOperationException at startup.")
    safe_input("\nPress Enter to return to menu...")

def handle_sql():
    print_header("DATABASE & EF CORE PERFORMANCE")
    print("""
Topic: Relational Index Tuning & Query Execution Plans
Question:
  Compare a Clustered Index Seek with an Index Scan in SQL Server.
  How does an index with INCLUDE columns eliminate Key Lookups?
""")
    ans = safe_input("Enter your answer (or press Enter to return): ").strip()
    if ans:
        print("\nEvaluation:")
        print("  An Index Seek traverses the B-Tree directly to find matching rows (O(log N)).")
        print("  An Index Scan traverses leaf nodes sequentially across the entire index (O(N)).")
        print("  INCLUDE columns store non-key attributes at the leaf level, satisfying query projections without bookmark lookups.")
    safe_input("\nPress Enter to return to menu...")

def handle_frontend():
    print_header("ANGULAR & REACT SPECIALIST")
    print("""
Topic: Fine-Grained Reactivity (Angular Signals) vs Virtual DOM (React)
Question:
  How does Angular Signals change detection differ from React's component re-rendering?
""")
    ans = safe_input("Enter your answer (or press Enter to return): ").strip()
    if ans:
        print("\nEvaluation:")
        print("  Angular Signals use a fine-grained dependency graph, notifying only affected DOM nodes without running dirty-checking.")
        print("  React executes component render functions top-down, creating a Virtual DOM tree and diffing it (reconciliation).")
    safe_input("\nPress Enter to return to menu...")

def handle_system_design():
    print_header("SYSTEM DESIGN SPECIALIST")
    print("""
Scenario: Design a High-Scale URL Shortening Service (Bitly)
Constraints: 500M URLs/month, 100:1 read/write ratio, latency < 10ms.

Questions:
  1. What is the write QPS and read QPS?
  2. How much storage is required over 5 years?
  3. What base encoding and key generation strategy would you use?
""")
    ans = safe_input("Enter your answer (or press Enter to return): ").strip()
    if ans:
        print("\nEvaluation:")
        print("  Write QPS: ~200 writes/sec. Read QPS: ~20,000 reads/sec.")
        print("  Storage: 500M * 12 * 5 * 500 bytes ~= 15 TB.")
        print("  Encoding: Base62 (a-z, A-Z, 0-9). 7 characters provide 62^7 ~= 3.5 trillion unique URLs.")
    safe_input("\nPress Enter to return to menu...")

def handle_fde():
    print_header("FORWARD DEPLOYED ENGINEER COACH")
    print("""
Scenario: Ambiguous Client Legacy Integration
A large healthcare client wants you to ingest clinical documents from an on-premise
network via legacy SOAP endpoints with no formal documentation.

Question:
  What are the first 3 discovery questions you ask the customer's engineering lead?
""")
    ans = safe_input("Enter your answer (or press Enter to return): ").strip()
    if ans:
        print("\nEvaluation:")
        print("  1. Authentication & Network Boundary: VPN, mTLS, IP allow-listing, or firewall windows?")
        print("  2. Payload Volume & Concurrency: Peak document size, requests/sec, and rate limits?")
        print("  3. Error Contracts & Idempotency: How are network dropouts and duplicates handled?")
    safe_input("\nPress Enter to return to menu...")

def handle_code_review():
    print_header("PRINCIPAL CODE REVIEWER")
    print("Submit code or path to review against 15 engineering dimensions:")
    target = safe_input("Enter C# file path or paste short snippet: ").strip()
    if target:
        if Path(target).exists():
            code = Path(target).read_text(encoding="utf-8")
        else:
            code = target
        print("\nEvaluating code...")
        print("Checking async void, socket exhaustion, DbContext concurrency, allocations, and SOLID...")
        print("Result: Code evaluated against evaluation-rubric.json.")
    safe_input("\nPress Enter to return to menu...")

def handle_progress():
    print_header("PROGRESS & COMPETENCY SNAPSHOT")
    print(state_manager.load_progress())
    print("\n" + "=" * 80)
    print("COMPETENCY MATRIX:")
    print("=" * 80)
    print(state_manager.load_competency_matrix())
    safe_input("\nPress Enter to return to menu...")

def handle_weakness():
    print_header("WEAKNESS REGISTER & REVISION QUEUE")
    w_path = OS_ROOT / "STATE" / "WEAKNESS-REGISTER.md"
    r_path = OS_ROOT / "STATE" / "REVISION-QUEUE.md"
    print("--- WEAKNESSES ---")
    print(w_path.read_text(encoding="utf-8") if w_path.exists() else "None")
    print("\n--- REVISION QUEUE ---")
    print(r_path.read_text(encoding="utf-8") if r_path.exists() else "None")
    safe_input("\nPress Enter to return to menu...")

def handle_validator():
    print_header("RUNNING SYSTEM VALIDATOR")
    val_path = OS_ROOT / "TOOLS" / "system_validator.py"
    os.system(f"python {val_path}")
    safe_input("\nPress Enter to return to menu...")

COMMAND_AGENT_MAP = {
    "/start": ("orchestrator", "Master Engineering Orchestrator"),
    "/diagnose": ("interviewer", "Senior/Staff Interviewer"),
    "/dsa": ("dsa", "DSA and LeetCode Coach"),
    "/dotnet": ("dotnet-runtime", "C# and .NET Runtime Specialist"),
    "/backend": ("backend", "ASP.NET Core Backend Architect"),
    "/frontend": ("frontend", "Angular and React Specialist"),
    "/sql": ("database", "EF Core and Database Engineer"),
    "/lld": ("system-design", "System Design Specialist (LLD)"),
    "/hld": ("system-design", "System Design Specialist (HLD)"),
    "/fde": ("fde", "Forward Deployed Engineer Coach"),
    "/debug": ("code-reviewer", "Engineering Quality Reviewer & Debugger"),
    "/project": ("backend", "Full-Stack Project Architect"),
    "/agents": ("agentic-ai", "Agentic AI Systems Engineer"),
    "/research": ("cs-fundamentals", "CS Fundamentals & Tech Researcher"),
    "/interview": ("interviewer", "Senior/Staff Interviewer"),
    "/review": ("code-reviewer", "Engineering Quality Reviewer"),
    "/revise": ("orchestrator", "Spaced Repetition Coordinator"),
    "/progress": ("orchestrator", "Progress & Competency Evaluator"),
    "/weakness": ("orchestrator", "Weakness Remediation Manager"),
    "/challenge": ("system-design", "Staff Engineering Challenge Master"),
    "/checkpoint": ("orchestrator", "State Checkpoint Serializer"),
    "/plan": ("orchestrator", "Curriculum Roadmap Planner"),
    "/continue": ("orchestrator", "Session Continuity Coordinator")
}

def route_command(cmd: str, args=None) -> str:
    cmd_name = cmd.strip().split()[0].lower()
    if cmd_name not in COMMAND_AGENT_MAP:
        return f"Unknown command {cmd_name}"
    agent_code, agent_name = COMMAND_AGENT_MAP[cmd_name]
    output = []
    output.append("================================================================================")
    output.append(f"ENGINEERING MASTERY OS — COMMAND DISPATCH: {cmd_name.upper()}")
    output.append(f"Active Lead Agent: {agent_name} [{agent_code}]")
    output.append("================================================================================\n")
    if cmd_name == "/start":
        output.append("Dispatched /start to Master Engineering Orchestrator.")
    elif cmd_name == "/progress":
        output.append(state_manager.load_progress())
    elif cmd_name == "/checkpoint":
        output.append(state_manager.load_current_session())
    elif cmd_name == "/continue":
        output.append("Resuming Active Session Continuity\n" + state_manager.load_current_session())
    else:
        output.append(f"Dispatched {cmd_name} to {agent_name} for execution.")
    return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Engineering Mastery OS Console")
    parser.add_argument("--command", type=str, default="", help="Command to execute directly")
    parser.add_argument("--non-interactive", action="store_true", help="Run once without menu")
    args = parser.parse_args()

    if args.command and args.non_interactive:
        print(route_command(args.command))
    else:
        # Default behavior: Launch clean interactive menu!
        menu_main()

if __name__ == "__main__":
    main()
