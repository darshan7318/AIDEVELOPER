# Engineering Mastery Capstone Projects

These production-grade projects are designed to demonstrate end-to-end engineering excellence at the senior/staff level.

## Project Portfolio

1. **Project 01: High-Throughput Ingestion & Analytics Pipeline**
   - **Stack**: .NET 8, ASP.NET Core Minimal APIs, System.Threading.Channels, SQLite/SQL Server, OpenTelemetry.
   - **Focus**: High throughput (10k+ req/sec), zero-allocation buffer management (`Memory<byte>`, `Span<byte>`), backpressure, and structured logging.
   - **Path**: `PROJECTS/Project-01-High-Throughput-Ingestion/`

2. **Project 02: Enterprise Identity & Reverse-Proxy Gateway**
   - **Stack**: ASP.NET Core, YARP (Yet Another Reverse Proxy), OAuth/OIDC, JWT validation, Redis distributed cache, Rate limiting.
   - **Focus**: FDE integration, multi-tenant token validation, policy enforcement, distributed rate-limiting, and circuit breaking.
   - **Path**: `PROJECTS/Project-02-Enterprise-Identity-Gateway/`

3. **Project 03: Autonomous Agentic AI Code Evaluator**
   - **Stack**: Python 3.14, Ollama / Local LLM, Typed Tool Calling, AST Analysis, Docker / Process isolation.
   - **Focus**: Safe code sandbox execution, multi-agent evaluation pipeline, prompt injection defense, and automated test synthesis.
   - **Path**: `PROJECTS/Project-03-Agentic-Code-Evaluator/`
