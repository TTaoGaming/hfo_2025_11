# Gen25 — Gem Gene Seed Regeneration (Vision)

BLUF
- Plain-language Gene Seed MD (with visuals) feeds an Adapter that formats for MBSE; the Adapter drives everything else. No vendor lock-in.

Overview (parser-safe)
```mermaid
graph LR
  G[Gene Seed MD] --> A[Adapter]
  A --> E[Everything Else]
```

Notes
- Gene Seed is the single source of truth; Adapter handles MBSE/SysML export and other targets as needed.
- Keep labels simple ASCII; one arrow per line; no edge labels for compatibility.
