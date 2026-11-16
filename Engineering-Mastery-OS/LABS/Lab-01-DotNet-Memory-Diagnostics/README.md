# Lab 01: .NET Memory Diagnostics & Zero-Allocation Optimization

## Problem Statement
The provided string parsing logic generates excessive garbage collection pressure due to string allocations inside a high-frequency loop.

## Objectives
1. Profile allocations before refactoring.
2. Refactor parsing using `ReadOnlySpan<char>` and `MemoryExtensions`.
3. Eliminate heap allocations in hot paths.
4. Verify correctness with unit tests.
