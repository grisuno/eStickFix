# Symbols

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `TestApp` | class | `app_unit_test.py:7` | `class TestApp(TestCase)` |
| `test_create_config` | method | `app_unit_test.py:23` | `def test_create_config(self, mock_db, mock_User, mock_UserController, mock_url_for, mock_redirect)` |
| `test_etl_status` | method | `app_unit_test.py:52` | `def test_etl_status(self, mock_current_user, mock_ProcessController, mock_render_template)` |
| `test_index` | method | `app_unit_test.py:9` | `def test_index(self, mock_render_template)` |
| `test_start_etl` | method | `app_unit_test.py:40` | `def test_start_etl(self, mock_data_navigator, mock_ETLProcessor, mock_DataQualityChecker, mock_Transformer...` |
| `TestSourceLoader` | class | `data_loader_unit_test.py:5` | `class TestSourceLoader(TestCase)` |
| `setUp` | method | `data_loader_unit_test.py:6` | `def setUp(self)` |
| `test_load_ftp` | method | `data_loader_unit_test.py:33` | `def test_load_ftp(self, mock_print)` |
| `test_load_mysql` | method | `data_loader_unit_test.py:38` | `def test_load_mysql(self)` |
| `DataNavigator` | class | `data_navigation.py:3` | `class DataNavigator` |
| `__init__` | method | `data_navigation.py:4` | `def __init__(self, db_name, collection_name)` |
| `find_by_dataset_tablename_date` | method | `data_navigation.py:9` | `def find_by_dataset_tablename_date(self, dataset, tablename, date)` |
| `find_by_query` | method | `data_navigation.py:13` | `def find_by_query(self, query)` |
| `Config` | class | `etl.py:11` | `class Config` |
| `DataQualityChecker` | class | `etl.py:31` | `class DataQualityChecker` |
| `ETLHandler` | class | `etl.py:39` | `class ETLHandler(FileSystemEventHandler)` |
| `ETLProcessor` | class | `etl.py:65` | `class ETLProcessor` |
| `ETLTests` | class | `etl.py:92` | `class ETLTests(TestCase)` |
| `Transformer` | class | `etl.py:22` | `class Transformer` |
| `__init__` | method | `etl.py:12` | `def __init__(self, config_path)` |
| `__init__` | method | `etl.py:23` | `def __init__(self, transformation_script)` |
| `__init__` | method | `etl.py:32` | `def __init__(self, qa_script)` |
| `__init__` | method | `etl.py:40` | `def __init__(self, config, transformer, quality_checker, collection, data_navigator)` |
| `__init__` | method | `etl.py:66` | `def __init__(self, config, transformer, quality_checker, data_navigator)` |
| `apply` | method | `etl.py:26` | `def apply(self, df)` |
| `check` | method | `etl.py:35` | `def check(self, df)` |
| `get` | method | `etl.py:19` | `def get(self, key)` |
| `load` | method | `etl.py:15` | `def load(self, config_path)` |
| `on_created` | method | `etl.py:47` | `def on_created(self, event)` |
| `process` | method | `etl.py:72` | `def process(self)` |
| `test_etl` | method | `etl.py:93` | `def test_etl(self)` |
| `TestETL` | class | `etl_unit_test.py:4` | `class TestETL(TestCase)` |
| `TestETLProcessor` | class | `etl_unit_test.py:27` | `class TestETLProcessor(TestCase)` |
| `setUp` | method | `etl_unit_test.py:5` | `def setUp(self)` |
| `setUp` | method | `etl_unit_test.py:28` | `def setUp(self)` |
| `test_etl_process` | method | `etl_unit_test.py:35` | `def test_etl_process(self)` |
| `test_quality_check` | method | `etl_unit_test.py:18` | `def test_quality_check(self)` |
| `test_transformation` | method | `etl_unit_test.py:11` | `def test_transformation(self)` |
| `main` | function | `orquestador.py:13` | `def main()` |
| `TestScript` | class | `orquestador_unit_test.py:5` | `class TestScript(TestCase)` |
| `test_main` | method | `orquestador_unit_test.py:8` | `def test_main(self, mock_open, mock_print)` |
