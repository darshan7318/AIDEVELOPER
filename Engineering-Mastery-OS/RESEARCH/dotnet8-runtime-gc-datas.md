# Research Note: .NET 8 Garbage Collection & DATAS

- **Topic**: .NET 8 Runtime GC Dynamic Adaptation to Application Sizes (DATAS)
- **Date**: 2026-11-16
- **Framework Version**: .NET 8 LTS (Baseline) & .NET 9 Comparison
- **Primary Sources**:
  - Microsoft Learn: [What's new in the .NET 8 runtime](https://learn.microsoft.com/en-us/dotnet/core/whats-new/dotnet-8/runtime)
  - Microsoft DevBlogs: [Dynamic Adaptation to Application Sizes (DATAS)](https://devblogs.microsoft.com/dotnet/dynamic-adaptation-to-application-sizes-datas/)
  - GitHub: [dotnet/runtime issue #78995](https://github.com/dotnet/runtime)

## Summary
In .NET 8, Microsoft introduced a new Garbage Collector capability called **Dynamic Adaptation to Application Sizes (DATAS)**.
Historically, Server GC scaled heap memory aggressively to prioritize throughput across all available CPU cores, which often resulted in high memory consumption for containerized or bursty workloads.

DATAS allows the GC to dynamically tune its heap footprint based on the application's actual memory demands:
- In .NET 8, DATAS is **opt-in** via `<GarbageCollectionAdaptationMode>1</GarbageCollectionAdaptationMode>` or `DOTNET_GCDynamicAdaptationMode=1`.
- In .NET 9, DATAS became the **default** mode for Server GC in many environments.
- .NET 8 also introduced dynamic adjustment of hard memory limits on the fly (`GC.RefreshMemoryLimit()`), critical for Kubernetes horizontal/vertical pod autoscalers.

## Practical Implications
1. **Containerized ASP.NET Core**: Microservices running in small memory footprints (e.g. 512MB-1GB) benefit significantly from DATAS to avoid container OOM kills.
2. **High-Throughput Services**: If pure raw throughput is required and memory is abundant, benchmark traditional Server GC against DATAS before switching.

## Unresolved Questions / Verification Items
- Test memory compaction overhead under rapid heap size fluctuation in benchmark tests.
