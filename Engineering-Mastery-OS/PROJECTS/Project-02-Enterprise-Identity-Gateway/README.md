# Project 02: Enterprise Identity & Reverse-Proxy Gateway

## Scenario (FDE Simulation)
A Fortune 500 enterprise client needs to route internal API traffic through an intelligent reverse proxy that validates custom claims, terminates mTLS, enforces strict tenant isolation, and throttles noisy neighbors without downtime.

## Key Deliverables
- ASP.NET Core proxy pipeline with custom middleware.
- JWT and API-key authentication with claims transformation.
- Sliding-window rate limiter per tenant.
- Comprehensive customer runbook and deployment guide.
