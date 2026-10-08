# Architecture

## Internal Dependencies

- `app_unit_test.py` -> `app.py`
- `data_loader_unit_test.py` -> `data_loader.py`
- `etl.py` -> `data_navigation.py`
- `orquestador.py` -> `data_loader.py`
- `orquestador.py` -> `data_navigation.py`
- `orquestador.py` -> `etl.py`
- `orquestador_unit_test.py` -> `orquestador.py`

## External Imports

- `app_unit_test.py` -> `app`
- `app_unit_test.py` -> `flask`
- `app_unit_test.py` -> `flask_login`
- `app_unit_test.py` -> `unittest`
- `app_unit_test.py` -> `unittest.mock`
- `data_loader_unit_test.py` -> `data_loader`
- `data_loader_unit_test.py` -> `unittest`
- `data_loader_unit_test.py` -> `unittest.mock`
- `data_navigation.py` -> `pymongo`
- `etl.py` -> `data_navigation`
- `etl.py` -> `datetime`
- `etl.py` -> `logging`
- `etl.py` -> `os`
- `etl.py` -> `pandas`
- `etl.py` -> `pymongo`
- `etl.py` -> `watchdog.events`
- `etl.py` -> `watchdog.observers`
- `etl.py` -> `yaml`
- `etl_unit_test.py` -> `unittest`
- `etl_unit_test.py` -> `your_etl_script`
- `orquestador.py` -> `data_loader`
- `orquestador.py` -> `data_navigation`
- `orquestador.py` -> `datetime`
- `orquestador.py` -> `etl`
- `orquestador.py` -> `ftplib`
- `orquestador.py` -> `logging`
- `orquestador.py` -> `os`
- `orquestador.py` -> `pandas`
- `orquestador.py` -> `paramiko`
- `orquestador.py` -> `pymysql`
- `orquestador.py` -> `yaml`
- `orquestador_unit_test.py` -> `orquestador`
- `orquestador_unit_test.py` -> `unittest`
- `orquestador_unit_test.py` -> `unittest.mock`
