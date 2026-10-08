# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `orquestador.py` (score: 8.10, imported by 1 files)
- `etl.py` (score: 5.80, imported by 1 files)
- `data_navigation.py` (score: 4.40, imported by 2 files)
- `data_loader.py` (score: 4.00, imported by 2 files)
- `app.py` (score: 2.00, imported by 1 files)
- `install.sh` (score: 0.00)

## Blast Radius (change impact)

Editing these files can break the listed number of dependents. Run their tests after any change.

- `data_loader.py` -- 2 direct, 3 total dependents
- `data_navigation.py` -- 2 direct, 3 total dependents
- `etl.py` -- 1 direct, 2 total dependents
- `app.py` -- 1 direct, 1 total dependents
- `orquestador.py` -- 1 direct, 1 total dependents

## Hotspots (complexity + centrality)

- `etl.py` -- complexity: 1.0, centrality: 0.7, combined: 0.8
- `orquestador.py` -- complexity: 0.1, centrality: 1.0, combined: 0.6
- `data_navigation.py` -- complexity: 0.2, centrality: 0.2, combined: 0.2
- `data_loader.py` -- complexity: 0.0, centrality: 0.1, combined: 0.1
- `app.py` -- complexity: 0.0, centrality: 0.1, combined: 0.0
- `install.sh` -- complexity: 0.0, centrality: 0.0, combined: 0.0
