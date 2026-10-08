# Subsystem: root

## app.py
- Layer: utility
- Language: py
- Imported by: `app_unit_test.py`

## app_unit_test.py
- Layer: testing
- Language: py
- Symbols:
  - `TestApp` (class, line 7) `class TestApp(TestCase)`
  - `test_index` (method, line 9) `def test_index(self, mock_render_template)`
  - `test_create_config` (method, line 23) `def test_create_config(self, mock_db, mock_User, mock_UserController, mock_url_for, mock_redirect)`
  - `test_start_etl` (method, line 40) `def test_start_etl(self, mock_data_navigator, mock_ETLProcessor, mock_DataQualityChecker, mock_Transformer...`
  - `test_etl_status` (method, line 52) `def test_etl_status(self, mock_current_user, mock_ProcessController, mock_render_template)`
- Depends on: `app.py`

## data_loader.py
- Layer: data_access
- Language: py
- Imported by: `data_loader_unit_test.py`, `orquestador.py`

## data_loader_unit_test.py
- Layer: testing
- Language: py
- Symbols:
  - `TestSourceLoader` (class, line 5) `class TestSourceLoader(TestCase)`
  - `setUp` (method, line 6) `def setUp(self)`
  - `test_load_ftp` (method, line 33) `def test_load_ftp(self, mock_print)`
  - `test_load_mysql` (method, line 38) `def test_load_mysql(self)`
- Depends on: `data_loader.py`

## data_navigation.py
- Layer: data_access
- Language: py
- Symbols:
  - `DataNavigator` (class, line 3) `class DataNavigator`
  - `__init__` (method, line 4) `def __init__(self, db_name, collection_name)`
  - `find_by_dataset_tablename_date` (method, line 9) `def find_by_dataset_tablename_date(self, dataset, tablename, date)`
  - `find_by_query` (method, line 13) `def find_by_query(self, query)`
- Imported by: `etl.py`, `orquestador.py`

## etl.py
- Layer: utility
- Language: py
- Symbols:
  - `Config` (class, line 11) `class Config`
  - `Transformer` (class, line 22) `class Transformer`
  - `DataQualityChecker` (class, line 31) `class DataQualityChecker`
  - `ETLHandler` (class, line 39) `class ETLHandler(FileSystemEventHandler)`
  - `ETLProcessor` (class, line 65) `class ETLProcessor`
  - `ETLTests` (class, line 92) `class ETLTests(TestCase)`
  - `__init__` (method, line 12) `def __init__(self, config_path)`
  - `load` (method, line 15) `def load(self, config_path)`
  - `get` (method, line 19) `def get(self, key)`
  - `__init__` (method, line 23) `def __init__(self, transformation_script)`
  - `apply` (method, line 26) `def apply(self, df)`
  - `__init__` (method, line 32) `def __init__(self, qa_script)`
  - `check` (method, line 35) `def check(self, df)`
  - `__init__` (method, line 40) `def __init__(self, config, transformer, quality_checker, collection, data_navigator)`
  - `on_created` (method, line 47) `def on_created(self, event)`
  - `__init__` (method, line 66) `def __init__(self, config, transformer, quality_checker, data_navigator)`
  - `process` (method, line 72) `def process(self)`
  - `test_etl` (method, line 93) `def test_etl(self)`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

## etl_unit_test.py
- Layer: testing
- Language: py
- Symbols:
  - `TestETL` (class, line 4) `class TestETL(TestCase)`
  - `TestETLProcessor` (class, line 27) `class TestETLProcessor(TestCase)`
  - `setUp` (method, line 5) `def setUp(self)`
  - `test_transformation` (method, line 11) `def test_transformation(self)`
  - `test_quality_check` (method, line 18) `def test_quality_check(self)`
  - `setUp` (method, line 28) `def setUp(self)`
  - `test_etl_process` (method, line 35) `def test_etl_process(self)`

## install.sh
- Layer: utility
- Language: sh

## orquestador.py
- Layer: utility
- Language: py
- Symbols:
  - `main` (function, line 13) `def main()`
- Depends on: `data_loader.py`, `data_navigation.py`, `etl.py`
- Imported by: `orquestador_unit_test.py`

## orquestador_unit_test.py
- Layer: testing
- Language: py
- Symbols:
  - `TestScript` (class, line 5) `class TestScript(TestCase)`
  - `test_main` (method, line 8) `def test_main(self, mock_open, mock_print)`
- Depends on: `orquestador.py`
