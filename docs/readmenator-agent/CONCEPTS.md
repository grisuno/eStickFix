# Concepts

Nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

- `data` | files=4 | mentions=8 | `data_loader.py`, `data_loader_unit_test.py`, `data_navigation.py`, `etl.py`
- `unit` | files=4 | mentions=8 | `app_unit_test.py`, `data_loader_unit_test.py`, `etl_unit_test.py`, `orquestador_unit_test.py`
- `etl` | files=3 | mentions=9 | `app_unit_test.py`, `etl.py`, `etl_unit_test.py`
- `app` | files=2 | mentions=5 | `app.py`, `app_unit_test.py`
- `loader` | files=2 | mentions=5 | `data_loader.py`, `data_loader_unit_test.py`
- `orquestador` | files=2 | mentions=4 | `orquestador.py`, `orquestador_unit_test.py`
- `load` | files=2 | mentions=3 | `data_loader_unit_test.py`, `etl.py`
- `set` | files=2 | mentions=3 | `data_loader_unit_test.py`, `etl_unit_test.py`
- `check` | files=2 | mentions=2 | `etl.py`, `etl_unit_test.py`
- `config` | files=2 | mentions=2 | `app_unit_test.py`, `etl.py`
- `etlprocessor` | files=2 | mentions=2 | `etl.py`, `etl_unit_test.py`
- `process` | files=2 | mentions=2 | `etl.py`, `etl_unit_test.py`
- `quality` | files=2 | mentions=2 | `etl.py`, `etl_unit_test.py`

## Verb Edges

- `orquestador` --depends_on--> `data` (strength 1.00)
- `load` --depends_on--> `data` (strength 0.67)
- `check` --depends_on--> `data` (strength 0.33)
- `config` --depends_on--> `app` (strength 0.33)
- `config` --depends_on--> `data` (strength 0.33)
- `data` --depends_on--> `loader` (strength 0.33)
- `etl` --depends_on--> `app` (strength 0.33)
- `etl` --depends_on--> `data` (strength 0.33)
- `etlprocessor` --depends_on--> `data` (strength 0.33)
- `load` --depends_on--> `loader` (strength 0.33)
- `loader` --depends_on--> `data` (strength 0.33)
- `orquestador` --depends_on--> `check` (strength 0.33)
- `orquestador` --depends_on--> `config` (strength 0.33)
- `orquestador` --depends_on--> `etl` (strength 0.33)
- `orquestador` --depends_on--> `etlprocessor` (strength 0.33)
- `orquestador` --depends_on--> `load` (strength 0.33)
- `orquestador` --depends_on--> `loader` (strength 0.33)
- `orquestador` --depends_on--> `process` (strength 0.33)
- `orquestador` --depends_on--> `quality` (strength 0.33)
- `process` --depends_on--> `data` (strength 0.33)
- `quality` --depends_on--> `data` (strength 0.33)
- `set` --depends_on--> `data` (strength 0.33)
- `set` --depends_on--> `loader` (strength 0.33)
- `unit` --depends_on--> `app` (strength 0.33)
- `unit` --depends_on--> `data` (strength 0.33)
- `unit` --depends_on--> `loader` (strength 0.33)
- `unit` --depends_on--> `orquestador` (strength 0.33)

## Dialectic

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
