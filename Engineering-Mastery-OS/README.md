# Engineering Mastery OS

> **A Persistent, Agent-Driven Software Engineering Training Environment targeting Senior/Staff SDE and Forward Deployed Engineer (FDE) capabilities (8–10 years engineering maturity level).**

---

## 1. Executive Overview

**Engineering Mastery OS** transforms standard coding practice into a rigorous, adaptive, multi-agent training operating system. Built upon the Engineering Mastery Agent Prompt Pack, this system coordinates a **Chief Engineering Orchestrator** and **13 Specialist Agents** across genuine execution runtimes (Antigravity native subagents, dynamic Python workflows, and standalone CLI tooling).

The operating system continuously adapts based on your demonstrated knowledge, code quality, edge-case handling, and architectural trade-off defenses—operating as an authoritative training harness rather than a static tutorial or generic chatbot.

### Core Engineering Disciplines Covered
1. **Computer Science & Operating Systems Fundamentals** (Memory hierarchies, CPU caches, virtual memory, OS scheduling, TCP/IP, TLS).
2. **Data Structures & Algorithms (DSA)** (26 core patterns, progressive hint coaching, canonical LeetCode tracking in C#).
3. **Advanced C# & .NET Runtime Internals** (C# 12/13, CLR, JIT tiered compilation, GC generations, DATAS, Span<T>, ValueTask).
4. **ASP.NET Core Backend Architecture** (Request pipelines, middleware, DI lifetimes, Minimal APIs, OAuth/OIDC, resilience).
5. **Entity Framework Core & Database Engineering** (Execution plans, indexing strategies, ACID isolation levels, deadlocks, change tracking).
6. **Modern Frontend Engineering** (Angular Signals, RxJS, React hooks/reconciliation, state management, web accessibility).
7. **Full-Stack Architecture & Delivery** (End-to-end integration, API contracts, CORS/CSRF defense, unified telemetry).
8. **Low-Level Design (LLD) & High-Level System Design (HLD)** (SOLID, design patterns, capacity estimations, service boundaries, sharding).
9. **Distributed Systems, Cloud & Site Reliability (SRE)** (CAP theorem, eventual consistency, OpenTelemetry tracing, SLO/SLI error budgets, chaos testing).
10. **Forward Deployed Engineering (FDE)** (Ambiguous enterprise discovery, legacy integrations, identity federation, rapid prototyping, runbooks).
11. **Agentic AI Systems Engineering** (Tool calling, typed planners, memory graphs, prompt injection defenses, multi-agent evaluation).
12. **Staff/Principal Engineering & Technical Leadership** (Cross-team governance, RFC authoring, post-mortems, executive framing, staff interview simulations).

---

## 2. Directory Architecture

```
C:\AI-Developer\Engineering-Mastery-OS/
├── README.md                      # System overview and entry point
├── AGENT-SETUP.md                 # Agent configuration and runtime instructions
├── SYSTEM-ARCHITECTURE.md         # Multi-agent coordination and data-flow architecture
├── ROADMAP.md                     # Adaptive curriculum progression and phase gates
├── MASTER-ORCHESTRATOR.md         # Central orchestrator prompt specification
├── CONFIGURATION.md               # Environment variables, SDKs, and platform settings
├── TROUBLESHOOTING.md             # Common errors, runtime diagnostics, and recovery
├── DAILY-USAGE.md                 # Daily training routine and command walkthroughs
│
├── CONFIG/                        # System configurations
│   ├── settings.json              # Active environment, stack baseline, safety rules
│   ├── agents.json                # Registry of orchestrator and 13 specialists
│   ├── curriculum.json            # 13-phase curriculum definitions and gate criteria
│   └── evaluation-rubric.json     # 100-point rubric, scoring tiers, mastery rules
│
├── PROMPTS/                       # System prompts
│   ├── master/orchestrator.md     # Chief Orchestrator prompt
│   ├── agents/                    # 13 Specialist prompts (cs-fundamentals, dsa, dotnet, etc.)
│   └── shared/                    # Contracts, templates, commands, research protocol
│
├── STATE/                         # Persistent training memory
│   ├── PROFILE.md                 # Target profile, stack, learning philosophy
│   ├── PROGRESS.md                # Phase completion, hours trained, milestone tallies
│   ├── COMPETENCY-MATRIX.md       # Verifiable ratings across all 16 skill domains
│   ├── WEAKNESS-REGISTER.md       # Captured bugs, root causes, and remediation plans
│   ├── REVISION-QUEUE.md          # Spaced repetition schedule (1d, 3d, 7d, 14d, 30d)
│   ├── CURRENT-SESSION.md         # Active session state and checkpoint resume data
│   └── SESSION-HISTORY.md         # Historical session logs and milestone scores
│
├── CURRICULUM/                    # Phase guides and milestone requirements
│   ├── PHASE-00-DIAGNOSTIC/       # Initial baseline diagnostic
│   ├── PHASE-01-CS-FUNDAMENTALS/  # OS & Computer Science internals
│   ├── PHASE-02-DSA/              # 26 algorithmic patterns in C#
│   ├── PHASE-03-CSHARP-DOTNET/    # CLR, GC, JIT, Span<T>, async state machines
│   ├── PHASE-04-BACKEND/          # ASP.NET Core request pipeline & architecture
│   ├── PHASE-05-DATABASE/         # Query execution plans, indexes, EF Core
│   ├── PHASE-06-FRONTEND/         # Angular signals, React reconciliation, DOM
│   ├── PHASE-07-FULLSTACK/        # End-to-end integration & contract testing
│   ├── PHASE-08-SYSTEM-DESIGN/    # Capacity planning, distributed architectures
│   ├── PHASE-09-DISTRIBUTED-SYS/  # Eventual consistency, SRE, OpenTelemetry
│   ├── PHASE-10-FDE/              # Enterprise discovery, legacy integrations
│   ├── PHASE-11-AGENTIC-AI/       # Typed tool calling, memory graphs, guardrails
│   └── PHASE-12-STAFF-ENGINEERING/# RFC authoring, executive communication
│
├── DSA/                           # Algorithmic practice repository
│   ├── PROBLEMS.md                # Canonical problems, links, and difficulty
│   ├── PATTERNS.md                # 26 patterns and mental models
│   ├── MISTAKES.md                # Captured algorithmic anti-patterns
│   └── SOLUTIONS/                 # Verified C# reference solutions
│
├── PROJECTS/                      # Capstone real-world systems
│   ├── Project-01-High-Throughput-Ingestion/
│   ├── Project-02-Enterprise-Identity-Gateway/
│   └── Project-03-Agentic-Code-Evaluator/
│
├── LABS/                          # Hands-on profiling and debugging drills
├── INTERVIEWS/                    # Staff-level question bank and mock rubrics
├── RESEARCH/                      # Cited research notes from official docs
├── REPORTS/                       # Generated evaluation and session reports
├── TEMPLATES/                     # Session, diagnostic, RFC, and ADR templates
└── TOOLS/                         # Automation & validation utilities
    ├── state_manager.py           # Safe atomic file persistence engine
    ├── agent_loader.py            # Prompt loader and contract validator
    ├── orchestrator_cli.py        # 23-command CLI dispatch engine
    └── system_validator.py        # Automated 10-test validation suite
```

---

## 3. Quick Start

### Starting Your First Diagnostic Session
To establish your verified baseline competency across all 10 engineering domains:

```powershell
python C:\AI-Developer\Engineering-Mastery-OS\TOOLS\orchestrator_cli.py --command /diagnose
```

Or within this Antigravity session, simply type:
```text
/diagnose
```

### Running the Automated System Validation
Verify that all 13 agents, curriculum phases, persistence channels, and security boundaries are fully operational:

```powershell
python C:\AI-Developer\Engineering-Mastery-OS\TOOLS\system_validator.py
```
*(Result: 10/10 tests passing)*

---

## 4. Supported Command Reference

| Command | Action / Dispatch | Lead Specialist |
|---|---|---|
| `/start` | Launch today's 120-minute adaptive training session | Master Orchestrator |
| `/diagnose` | Execute the interactive baseline competency diagnostic | Senior/Staff Interviewer |
| `/dsa` | Algorithmic problem solving with progressive hints | DSA / LeetCode Coach |
| `/dotnet` | Deep dive into C# semantics and .NET runtime internals | .NET Runtime Specialist |
| `/backend` | ASP.NET Core request pipeline & architecture | Backend Architect |
| `/frontend` | Angular (Signals/RxJS) or React (Hooks) deep dive | Frontend Specialist |
| `/sql` | Query plans, indexing strategies, and EF Core tracking | EF Core & Database Engineer |
| `/lld` | Low-level object-oriented design and SOLID patterns | System Design Specialist |
| `/hld` | High-level distributed system design & capacity bounds | System Design Specialist |
| `/fde` | Ambiguous client scenario and integration simulation | Forward Deployed Coach |
| `/debug` | Synthetic production outage and root-cause analysis | Quality Reviewer & Debugger |
| `/project` | Next milestone on capstone enterprise projects | Full-Stack Architect |
| `/agents` | Build and evaluate autonomous agentic AI systems | Agentic AI Systems Engineer |
| `/research [topic]` | Sourced, cited research from Microsoft Learn / official specs | CS Fundamentals Researcher |
| `/interview` | Realistic senior/staff mock technical interview | Senior/Staff Interviewer |
| `/review` | Principal code review against 15 engineering dimensions | Quality Reviewer |
| `/revise` | Spaced repetition drills from the active revision queue | Orchestrator |
| `/progress` | View current phase, completed hours, and competency matrix | Orchestrator |
| `/weakness` | Review registered bugs, root causes, and remediation plans | Orchestrator |
| `/challenge` | Unfamiliar staff-level engineering scenario | Staff Challenge Master |
| `/checkpoint` | Serialized snapshot of learning progress | Orchestrator |
| `/plan` | Review and adapt curriculum roadmap milestones | Orchestrator |
| `/continue` | Resume current active session without restarting | Orchestrator |
