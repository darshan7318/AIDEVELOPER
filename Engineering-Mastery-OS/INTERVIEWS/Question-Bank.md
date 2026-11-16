# Staff Engineering Question Bank

## Track 1: .NET Runtime & Language Internals
1. **Explain the memory layout of an object on the 64-bit CLR heap.** What are the Object Header and MethodTable pointer used for?
2. **How does the .NET ThreadPool's work-stealing algorithm operate?** Why does each worker thread have a local queue in addition to the global queue?
3. **Contrast `Task` vs `ValueTask`.** When does `ValueTask` allocate, and what are the restrictions on awaiting a `ValueTask` multiple times?
4. **Explain how `Span<T>` guarantees memory safety while avoiding bounds-check overhead.** Why can `Span<T>` only live on the stack?
5. **How does .NET 8's DATAS (Dynamic Adaptation to Application Sizes) GC differ from the traditional Server GC?**

## Track 2: ASP.NET Core & Backend Architecture
1. **Trace an HTTP request through the ASP.NET Core pipeline from Kestrel socket receipt to Controller/Minimal API action execution.**
2. **Explain the captive dependency problem in .NET Dependency Injection.** How can it be detected and prevented?
3. **Design an idempotent payment processing endpoint.** How do you handle network retries, race conditions, and duplicate requests?

## Track 3: Database & EF Core
1. **Explain the difference between a B-Tree clustered index and a non-clustered index with included columns.**
2. **How does EF Core's change tracker detect modifications?** Compare snapshot tracking with notification tracking.
3. **Diagnose and resolve an unexpected deadlocking scenario in SQL Server under high concurrency.**

## Track 4: System Design & Distributed Systems
1. **Design a globally distributed rate limiter that handles 100,000 requests/sec with sub-millisecond local latency.**
2. **Compare 2-Phase Commit (2PC) with the Saga pattern for managing distributed transactions across microservices.**
3. **Design an event-driven notification dispatch system with guaranteed at-least-once delivery and deduplication.**

## Track 5: Forward Deployed Engineering
1. **A prospective client requires integration with an on-premises legacy SOAP service with no documentation.** Walk through your discovery, testing, and adapter architecture.
2. **A customer's IT security team refuses cloud API credentials.** How do you design a hybrid deployment architecture that satisfies their governance while delivering functionality?
