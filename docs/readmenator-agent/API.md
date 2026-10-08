# API

## data_navigation.py
Imported by: `etl.py`, `orquestador.py`
- `DataNavigator.__init__` (method) `data_navigation.py:4` `def __init__(self, db_name, collection_name)`
- `DataNavigator.find_by_dataset_tablename_date` (method) `data_navigation.py:9` `def find_by_dataset_tablename_date(self, dataset, tablename, date)`
- `DataNavigator.find_by_query` (method) `data_navigation.py:13` `def find_by_query(self, query)`

## etl.py
Depends on: `data_navigation.py`
Imported by: `orquestador.py`
- `Config.__init__` (method) `etl.py:12` `def __init__(self, config_path)`
- `Config.load` (method) `etl.py:15` `def load(self, config_path)`
- `Config.get` (method) `etl.py:19` `def get(self, key)`
- `Transformer.__init__` (method) `etl.py:23` `def __init__(self, transformation_script)`
- `Transformer.apply` (method) `etl.py:26` `def apply(self, df)`
- `DataQualityChecker.__init__` (method) `etl.py:32` `def __init__(self, qa_script)`
- `DataQualityChecker.check` (method) `etl.py:35` `def check(self, df)`
- `ETLHandler.__init__` (method) `etl.py:40` `def __init__(self, config, transformer, quality_checker, collection, data_navigator)`
- `ETLHandler.on_created` (method) `etl.py:47` `def on_created(self, event)`
- `ETLProcessor.__init__` (method) `etl.py:66` `def __init__(self, config, transformer, quality_checker, data_navigator)`
- `ETLProcessor.process` (method) `etl.py:72` `def process(self)`
- `ETLTests.test_etl` (method) `etl.py:93` `def test_etl(self)`

## orquestador.py
Depends on: `data_loader.py`, `data_navigation.py`, `etl.py`
Imported by: `orquestador_unit_test.py`
- `main` (function) `orquestador.py:13` `def main()`
