# API

## app_unit_test.py

### test_index (method) `def test_index(self, mock_render_template)`
- Defined: `app_unit_test.py:9`
- Depends on: `app.py`

### test_create_config (method) `def test_create_config(self, mock_db, mock_User, mock_UserController, mock_url_for, mock_redirect)`
- Defined: `app_unit_test.py:23`
- Depends on: `app.py`

### test_start_etl (method) `def test_start_etl(self, mock_data_navigator, mock_ETLProcessor, mock_DataQualityChecker, mock_Transformer, mock_Config, mock_ETLController, mock_url_for, mock_redirect, mock_flash)`
- Defined: `app_unit_test.py:40`
- Depends on: `app.py`

### test_etl_status (method) `def test_etl_status(self, mock_current_user, mock_ProcessController, mock_render_template)`
- Defined: `app_unit_test.py:52`
- Depends on: `app.py`

## data_loader_unit_test.py

### setUp (method) `def setUp(self)`
- Defined: `data_loader_unit_test.py:6`
- Depends on: `data_loader.py`

### test_load_ftp (method) `def test_load_ftp(self, mock_print)`
- Defined: `data_loader_unit_test.py:33`
- Depends on: `data_loader.py`

### test_load_mysql (method) `def test_load_mysql(self)`
- Defined: `data_loader_unit_test.py:38`
- Depends on: `data_loader.py`

## data_navigation.py

### __init__ (method) `def __init__(self, db_name, collection_name)`
- Defined: `data_navigation.py:4`
- Imported by: `etl.py`, `orquestador.py`

### find_by_dataset_tablename_date (method) `def find_by_dataset_tablename_date(self, dataset, tablename, date)`
- Defined: `data_navigation.py:9`
- Imported by: `etl.py`, `orquestador.py`

### find_by_query (method) `def find_by_query(self, query)`
- Defined: `data_navigation.py:13`
- Imported by: `etl.py`, `orquestador.py`

## etl.py

### __init__ (method) `def __init__(self, config_path)`
- Defined: `etl.py:12`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

### load (method) `def load(self, config_path)`
- Defined: `etl.py:15`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

### get (method) `def get(self, key)`
- Defined: `etl.py:19`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

### __init__ (method) `def __init__(self, transformation_script)`
- Defined: `etl.py:23`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

### apply (method) `def apply(self, df)`
- Defined: `etl.py:26`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

### __init__ (method) `def __init__(self, qa_script)`
- Defined: `etl.py:32`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

### check (method) `def check(self, df)`
- Defined: `etl.py:35`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

### __init__ (method) `def __init__(self, config, transformer, quality_checker, collection, data_navigator)`
- Defined: `etl.py:40`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

### on_created (method) `def on_created(self, event)`
- Defined: `etl.py:47`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

### __init__ (method) `def __init__(self, config, transformer, quality_checker, data_navigator)`
- Defined: `etl.py:66`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

### process (method) `def process(self)`
- Defined: `etl.py:72`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

### test_etl (method) `def test_etl(self)`
- Defined: `etl.py:93`
- Depends on: `data_navigation.py`
- Imported by: `orquestador.py`

## etl_unit_test.py

### setUp (method) `def setUp(self)`
- Defined: `etl_unit_test.py:5`

### test_transformation (method) `def test_transformation(self)`
- Defined: `etl_unit_test.py:11`

### test_quality_check (method) `def test_quality_check(self)`
- Defined: `etl_unit_test.py:18`

### setUp (method) `def setUp(self)`
- Defined: `etl_unit_test.py:28`

### test_etl_process (method) `def test_etl_process(self)`
- Defined: `etl_unit_test.py:35`

## orquestador.py

### main (function) `def main()`
- Defined: `orquestador.py:13`
- Depends on: `data_loader.py`, `data_navigation.py`, `etl.py`
- Imported by: `orquestador_unit_test.py`

## orquestador_unit_test.py

### test_main (method) `def test_main(self, mock_open, mock_print)`
- Defined: `orquestador_unit_test.py:8`
- Depends on: `orquestador.py`
