# Concepts

Second-brain semantic layer: nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

| Concept | Files | Mentions | Top Files |
|---------|-------|----------|-----------|
| `data` | 4 | 8 | `data_loader.py`, `data_loader_unit_test.py`, `data_navigation.py`, `etl.py` |
| `unit` | 4 | 8 | `app_unit_test.py`, `data_loader_unit_test.py`, `etl_unit_test.py`, `orquestador_unit_test.py` |
| `etl` | 3 | 9 | `app_unit_test.py`, `etl.py`, `etl_unit_test.py` |
| `app` | 2 | 5 | `app.py`, `app_unit_test.py` |
| `loader` | 2 | 5 | `data_loader.py`, `data_loader_unit_test.py` |
| `orquestador` | 2 | 4 | `orquestador.py`, `orquestador_unit_test.py` |
| `load` | 2 | 3 | `data_loader_unit_test.py`, `etl.py` |
| `set` | 2 | 3 | `data_loader_unit_test.py`, `etl_unit_test.py` |
| `check` | 2 | 2 | `etl.py`, `etl_unit_test.py` |
| `config` | 2 | 2 | `app_unit_test.py`, `etl.py` |
| `etlprocessor` | 2 | 2 | `etl.py`, `etl_unit_test.py` |
| `process` | 2 | 2 | `etl.py`, `etl_unit_test.py` |
| `quality` | 2 | 2 | `etl.py`, `etl_unit_test.py` |

## Verb Edges

| Source | Verb | Target | Strength |
|--------|------|--------|----------|
| `orquestador` | `depends_on` | `data` | 1.00 |
| `load` | `depends_on` | `data` | 0.67 |
| `check` | `depends_on` | `data` | 0.33 |
| `config` | `depends_on` | `app` | 0.33 |
| `config` | `depends_on` | `data` | 0.33 |
| `data` | `depends_on` | `loader` | 0.33 |
| `etl` | `depends_on` | `app` | 0.33 |
| `etl` | `depends_on` | `data` | 0.33 |
| `etlprocessor` | `depends_on` | `data` | 0.33 |
| `load` | `depends_on` | `loader` | 0.33 |
| `loader` | `depends_on` | `data` | 0.33 |
| `orquestador` | `depends_on` | `check` | 0.33 |
| `orquestador` | `depends_on` | `config` | 0.33 |
| `orquestador` | `depends_on` | `etl` | 0.33 |
| `orquestador` | `depends_on` | `etlprocessor` | 0.33 |
| `orquestador` | `depends_on` | `load` | 0.33 |
| `orquestador` | `depends_on` | `loader` | 0.33 |
| `orquestador` | `depends_on` | `process` | 0.33 |
| `orquestador` | `depends_on` | `quality` | 0.33 |
| `process` | `depends_on` | `data` | 0.33 |
| `quality` | `depends_on` | `data` | 0.33 |
| `set` | `depends_on` | `data` | 0.33 |
| `set` | `depends_on` | `loader` | 0.33 |
| `unit` | `depends_on` | `app` | 0.33 |
| `unit` | `depends_on` | `data` | 0.33 |
| `unit` | `depends_on` | `loader` | 0.33 |
| `unit` | `depends_on` | `orquestador` | 0.33 |

## Dialectic Prompts

- Thesis: `check` centralizes 2 files; Antithesis: `etl` pulls 3 files with 2 shared (Jaccard 0.67); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `check` centralizes 2 files; Antithesis: `etlprocessor` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `check` centralizes 2 files; Antithesis: `process` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `check` centralizes 2 files; Antithesis: `quality` pulls 2 files with 2 shared (Jaccard 1.00); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `config` centralizes 2 files; Antithesis: `etl` pulls 3 files with 2 shared (Jaccard 0.67); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `data` centralizes 4 files; Antithesis: `load` pulls 2 files with 2 shared (Jaccard 0.50); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `data` centralizes 4 files; Antithesis: `loader` pulls 2 files with 2 shared (Jaccard 0.50); Synthesis: should they merge, split by layer, or keep `depends_on` explicit?
- Thesis: `etl` centralizes 3 files; Antithesis: `etlprocessor` pulls 2 files with 2 shared (Jaccard 0.67); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `etl` centralizes 3 files; Antithesis: `process` pulls 2 files with 2 shared (Jaccard 0.67); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `etl` centralizes 3 files; Antithesis: `quality` pulls 2 files with 2 shared (Jaccard 0.67); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
