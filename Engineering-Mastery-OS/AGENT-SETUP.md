# Agent Configuration & Setup Guide

This document details the configuration, runtime models, permissions, and handoff protocols for the **Master Engineering Orchestrator** and all **13 Specialist Agents** within the Engineering Mastery OS.

---

## 1. Multi-Agent Execution Architecture

The system supports a **hybrid execution model** matching the capabilities audited in this environment:

```
                                  +-------------------------------+
                                  |  Master Engineering           |
                                  |  Orchestrator                 |
                                  +---------------+---------------+
                                                  |
         +----------------------------------------+----------------------------------------+
         |                                        |                                        |
         v                                        v                                        v
+------------------+                    +------------------+                    +------------------+
| Specialist Agent |                    | Quality Reviewer |                    | State & Progress |
| (e.g. .NET / DSA)|                    | (Challenges Code)|                    | (Atomic Storage) |
+--------+---------+                    +--------+---------+                    +--------+---------+
         |                                       |                                       |
         +---------------------------------------+---------------------------------------+
                                                 |
                                                 v
                               +-----------------------------------+
                               | Verified Knowledge & Skill Mastered|
                               +-----------------------------------+
```

### Supported Runtime Modes
1. **Antigravity Native Subagents (Primary Interactive Mode)**:
   - Defined via `define_subagent` with isolated system prompts, unique conversation IDs, and granular tool configurations.
   - Invoked via `invoke_subagent` with options for workspace sharing (`inherit`, `share`, `branch`).
   - Run asynchronously with automatic reactive notifications.
2. **Dynamic Agent Workflows (`run_workflow`)**:
   - Python-driven multi-agent pipelines (`agent()`, `parallel()`, `pipeline()`) for multi-file code reviews, benchmark runs, and test fan-outs.
3. **Native Swarm (`swarm`)**:
   - Multi-agent message board collaboration for cross-agent debates (e.g. Architect proposing vs Reviewer challenging vs Security reviewing).
4. **Standalone Python CLI (`TOOLS/orchestrator_cli.py`)**:
   - Local command-line execution outside the agent chat interface, supporting batch evaluation, state checking, and continuous learning tracking.

---

## 2. Agent Roster & Domain Specifications

### Agent 00: Master Engineering Orchestrator
- **Code**: `orchestrator`
- **System Prompt**: `PROMPTS/master/orchestrator.md`
- **Role**: Chief Engineering Orchestrator
- **Scope**: Curriculum ownership, phase gate enforcement, daily session generation, specialist task delegation, conflict resolution with primary documentation, progress persistence.
- **Authority**: Makes final curricular decisions. Reconciles disagreements between specialists and reviewers using executable test evidence and official documentation.

### Agent 01: CS Fundamentals Researcher
- **Code**: `cs-fundamentals`
- **System Prompt**: `PROMPTS/agents/cs-fundamentals.md`
- **Scope**: CPU registers/caches, virtual memory, paging, process scheduling, threads, synchronization primitives, system calls, network stack (Ethernet, IP, TCP, UDP, TLS, HTTP/2/3), compilers, ASTs, IL, JIT.
- **Teaching Standard**: First-principles mental models, diagrams, memory layouts, runnable proof programs.

### Agent 02: DSA and LeetCode Coach
- **Code**: `dsa`
- **System Prompt**: `PROMPTS/agents/dsa.md`
- **Scope**: 26 algorithmic patterns, complexity proofs (Big-O time and space), canonical LeetCode problem tracking, invariant identification.
- **Language**: Primary solutions in C#.
- **Strict Rule**: Progressive hints only. Never reveal complete solutions before independent learner attempts.

### Agent 03: C# and .NET Runtime Specialist
- **Code**: `dotnet-runtime`
- **System Prompt**: `PROMPTS/agents/dotnet-runtime.md`
- **Scope**: C# 12/13, CLR, JIT tiered compilation, GC generations (Gen 0/1/2, LOH, POH, DATAS), Span<T>, Memory<T>, ref structs, async state machines, thread pool work-stealing, memory profiling.
- **Baseline**: .NET 8 LTS compatibility baseline with .NET 9 feature distinction.

### Agent 04: ASP.NET Core Backend Architect
- **Code**: `backend`
- **System Prompt**: `PROMPTS/agents/backend.md`
- **Scope**: Kestrel, middleware pipeline order, dependency injection lifetimes (Transient, Scoped, Singleton, captive dependencies), Minimal APIs, Problem Details, OAuth/OIDC, JWT, rate limiting, resilience.
- **Deliverables**: API contracts, validation, integration tests, error models, cancellation tokens.

### Agent 05: EF Core and Database Engineer
- **Code**: `database`
- **System Prompt**: `PROMPTS/agents/database.md`
- **Scope**: Relational schema design, indexes (clustered, non-clustered, covering, filtered), query execution plans, ACID transaction isolation levels, deadlock resolution, EF Core change tracking, migrations, raw SQL.
- **Rule**: Predict SQL and execution plan before running or viewing generated queries.

### Agent 06: Angular and React Specialist
- **Code**: `frontend`
- **System Prompt**: `PROMPTS/agents/frontend.md`
- **Scope**: Browser rendering, JavaScript event loop (microtasks vs macrotasks), TypeScript type system, Angular (Signals, RxJS, DI), React (Hooks, reconciliation, context, error boundaries), web accessibility (WCAG), performance.

### Agent 07: System Design Specialist
- **Code**: `system-design`
- **System Prompt**: `PROMPTS/agents/system-design.md`
- **Scope**: Low-level design (SOLID, GoF patterns, domain modeling), high-level distributed systems (capacity estimations, load balancing, sharding, replication, eventual consistency, CAP theorem, distributed transactions).
- **Rule**: Challenge unnecessary microservices and CQRS; require capacity calculations and failure mode defenses.

### Agent 08: Forward Deployed Engineer Coach
- **Code**: `fde`
- **System Prompt**: `PROMPTS/agents/fde.md`
- **Scope**: Ambiguous customer discovery, stakeholder requirements, legacy system integration, mTLS/firewall navigation, enterprise identity federation, rapid working prototypes, customer handovers, runbooks.

### Agent 09: DevOps, Cloud and SRE Specialist
- **Code**: `devops-sre`
- **System Prompt**: `PROMPTS/agents/devops-sre.md`
- **Scope**: Git branching strategies, CI/CD pipelines, Docker containerization, Windows/Linux hosting, OpenTelemetry distributed tracing, Prometheus metrics, SLI/SLO/SLA error budgets, blue/green rollbacks.

### Agent 10: Application Security Engineer
- **Code**: `security`
- **System Prompt**: `PROMPTS/agents/security.md`
- **Scope**: Threat modeling (STRIDE), OWASP Top 10, cryptographic primitives (AES-GCM, PBKDF2, Argon2), SQL injection prevention, broken object-level authorization (BOLA), secrets management, least privilege.
- **Constraint**: Defensive engineering and authorized synthetic labs only.

### Agent 11: Principal Engineering Quality Reviewer
- **Code**: `code-reviewer`
- **System Prompt**: `PROMPTS/agents/code-reviewer.md`
- **Scope**: Candid, evidence-driven code reviews across 15 dimensions.
- **Defect Classification**:
  - `Critical`: Causes crashes, data corruption, security exploits, or deadlocks (e.g. `async void`, unhandled DbContext concurrency).
  - `High`: Performance bottlenecks, memory leaks, missing cancellation, captive DI.
  - `Medium`: Code duplication, missing unit tests, weak error messages.
  - `Low`: Minor style or naming inconsistencies.
  - `Informational`: Educational observations or future architectural suggestions.

### Agent 12: Senior/Staff Technical Interviewer
- **Code**: `interviewer`
- **System Prompt**: `PROMPTS/agents/interviewer.md`
- **Scope**: Realistic, high-bar technical interviews across coding, runtime internals, system design, production outages, and technical leadership.
- **Protocol**: One question at a time. Follows up on candidate assumptions. Evaluates depth over memorization.

### Agent 13: Agentic AI Systems Engineer
- **Code**: `agentic-ai`
- **System Prompt**: `PROMPTS/agents/agentic-ai.md`
- **Scope**: LLM fundamentals, structured tool calling, typed planner/executor loops, memory graphs, prompt injection defenses, multi-agent evaluation metrics, cost/latency optimization.
- **Tooling**: Python 3.14, Ollama local inference, Semantic Kernel, LangGraph.

---

## 3. Tool Permissions & Safety Boundaries

All agents operate under strict safety boundaries defined in `CONFIG/settings.json`:

```json
"safety_boundaries": {
  "destructive_operations_require_approval": true,
  "unrestricted_shell_execution": false,
  "untrusted_data_defense": true,
  "external_purchases_allowed": false
}
```

1. **Destructive Operations**: File deletions or git branch resets require explicit user confirmation.
2. **Untrusted Data Protection**: All user code inputs, retrieved web documents, and external API responses are treated as untrusted data, never as executable system prompts.
3. **No Unsanctioned Networks**: Agents do not send external credentials or access unauthorized third-party hosts.

---

## 4. How to Register a New Specialist Agent

To extend the system with an additional specialist (e.g. `embedded-systems` or `quantum-computing`):

1. **Create the Prompt File**: Add `PROMPTS/agents/<new-agent>.md` with clear role boundaries, scope, and deliverable format.
2. **Update `CONFIG/agents.json`**: Add an entry under `"specialists"` specifying `id`, `code`, `name`, `prompt_path`, `domain`, and `tools`.
3. **Update `TOOLS/orchestrator_cli.py`**: Add the relevant command mapping into `COMMAND_AGENT_MAP`.
4. **Register Native Subagent**: Run `define_subagent` within Antigravity or execute `python TOOLS/system_validator.py` to verify full system integration.
