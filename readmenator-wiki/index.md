# Second Brain

*Last synthesized: 2026-10-07 | 10 files | 3 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `orquestador.py`, `etl.py`, `data_navigation.py`. Architecturally it is 3 layers, dominant utility (4 files) across 3 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between root: etl, root: app, orphans: 0 extracted cross-community imports and 3 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (0% file coverage), 0 security findings, 0 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 10 |
| Symbols | 41 |
| Resolved imports | 7 |
| Languages | py, sh |
| Communities | 3 |
| Doc coverage | 0% (0/10 files) |
| Security findings | 0 |
| Estimated read cost | ~735 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target readmenator_eStickFix_4yfvbfaw
```

## Concept Wiki

- [root: etl (6 files, cohesion 1.00)](./community_0_root_etl.md)
- [root: app (2 files, cohesion 1.00)](./community_1_root_app.md)
- [orphans (2 files, cohesion 0.00)](./community_2_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `orquestador.py` | 8.1 |
| `etl.py` | 5.8 |
| `data_navigation.py` | 4.4 |
| `data_loader.py` | 4.0 |
| `app_unit_test.py` | 2.5 |

## Strongest Connections

- 0 -> 1: shares_context (strength 0.5, INFERRED)
- 0 -> 2: shares_context (strength 0.5, INFERRED)
- 1 -> 2: shares_context (strength 0.5, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
