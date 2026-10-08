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

- `app_unit_test.py` -> flask, flask_login, unittest, unittest.mock
- `data_loader_unit_test.py` -> unittest, unittest.mock
- `data_navigation.py` -> pymongo
- `etl.py` -> datetime, logging, os, pandas, pymongo, watchdog.events, watchdog.observers, yaml
- `etl_unit_test.py` -> unittest, your_etl_script
- `orquestador.py` -> datetime, ftplib, logging, os, pandas, paramiko, pymysql, yaml
- `orquestador_unit_test.py` -> unittest, unittest.mock
