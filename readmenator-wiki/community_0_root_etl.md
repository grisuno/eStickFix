# root: etl

*Community 0 | 6 files | cohesion 1.00*

## Definition

This community groups 6 file(s) rooted at `root` with dominant language py (cohesion 1.00). Central symbols: `Config`, `DataNavigator`, `DataQualityChecker`, `ETLHandler`, `ETLProcessor`, `ETLTests`, `TestScript`, `TestSourceLoader`. Core file: `etl.py` (18 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `data_loader.py` | py | data_access | 0 | no |
| `data_loader_unit_test.py` | py | testing | 4 | no |
| `data_navigation.py` | py | data_access | 4 | no |
| `etl.py` | py | utility | 18 | no |
| `orquestador.py` | py | utility | 1 | no |
| `orquestador_unit_test.py` | py | testing | 2 | no |

## Key Symbols

- `TestSourceLoader` (class, `data_loader_unit_test.py:5`) `class TestSourceLoader(TestCase)`
- `setUp` (method, `data_loader_unit_test.py:6`) `def setUp(self)`
- `test_load_ftp` (method, `data_loader_unit_test.py:33`) `def test_load_ftp(self, mock_print)`
- `test_load_mysql` (method, `data_loader_unit_test.py:38`) `def test_load_mysql(self)`
- `DataNavigator` (class, `data_navigation.py:3`) `class DataNavigator`
- `__init__` (method, `data_navigation.py:4`) `def __init__(self, db_name, collection_name)`
- `find_by_dataset_tablename_date` (method, `data_navigation.py:9`) `def find_by_dataset_tablename_date(self, dataset, tablename, date)`
- `find_by_query` (method, `data_navigation.py:13`) `def find_by_query(self, query)`
- `Config` (class, `etl.py:11`) `class Config`
- `__init__` (method, `etl.py:12`) `def __init__(self, config_path)`
- `load` (method, `etl.py:15`) `def load(self, config_path)`
- `get` (method, `etl.py:19`) `def get(self, key)`
- `Transformer` (class, `etl.py:22`) `class Transformer`
- `__init__` (method, `etl.py:23`) `def __init__(self, transformation_script)`
- `apply` (method, `etl.py:26`) `def apply(self, df)`
- `DataQualityChecker` (class, `etl.py:31`) `class DataQualityChecker`
- `__init__` (method, `etl.py:32`) `def __init__(self, qa_script)`
- `check` (method, `etl.py:35`) `def check(self, df)`
- `ETLHandler` (class, `etl.py:39`) `class ETLHandler(FileSystemEventHandler)`
- `__init__` (method, `etl.py:40`) `def __init__(self, config, transformer, quality_checker, collection, data_naviga`
- `on_created` (method, `etl.py:47`) `def on_created(self, event)`
- `ETLProcessor` (class, `etl.py:65`) `class ETLProcessor`
- `__init__` (method, `etl.py:66`) `def __init__(self, config, transformer, quality_checker, data_navigator)`
- `process` (method, `etl.py:72`) `def process(self)`
- `ETLTests` (class, `etl.py:92`) `class ETLTests(TestCase)`
- `test_etl` (method, `etl.py:93`) `def test_etl(self)`
- `main` (function, `orquestador.py:13`) `def main()`
- `TestScript` (class, `orquestador_unit_test.py:5`) `class TestScript(TestCase)`
- `test_main` (method, `orquestador_unit_test.py:8`) `def test_main(self, mock_open, mock_print)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 6
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 1 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (root: etl) and community 1 (root: app).
- [INFERRED] shares_context community 0 <-> 2 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (root: etl) and community 2 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 6 file(s) lack file-level docs (e.g. `data_loader.py`)? What purpose do they serve?
- What would break if the most connected file in root: etl changed?
- Should root: etl be split, given cohesion 1.00?

## Sources

- `data_loader.py`
- `data_loader_unit_test.py`
- `data_navigation.py`
- `etl.py`
- `orquestador.py`
- `orquestador_unit_test.py`
