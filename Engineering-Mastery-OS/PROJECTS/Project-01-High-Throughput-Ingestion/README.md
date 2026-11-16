# Project 01: High-Throughput Ingestion & Analytics Pipeline

## Architectural Overview
A resilient, backpressure-managed telemetry ingestion service built in .NET 8.

```
[HTTP Clients] ---> [Minimal API Endpoint]
                           |
                           v
                [System.Threading.Channels (Bounded)]
                           |
                           v
               [Background Processing Worker]
                           |
            +--------------+--------------+
            |                             |
            v                             v
[Zero-Allocation Parser]       [Batch Database Writer]
    (ReadOnlySpan<byte>)             (EF Core / SQLite)
```

## Acceptance Criteria
- Process 5,000 requests/sec with p99 latency < 15ms.
- Zero Gen 2 GC collections under steady-state load.
- Graceful degradation using bounded channels and drop/spillover policies.
- Full OpenTelemetry trace propagation.
