# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis.

**Total Files Parsed:** 10 | **Total Symbols Extracted:** 41 | **Total Imports:** 34

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray: 5 5,color:#aaa;
    orquestador_py["orquestador.py (py)"]
    class orquestador_py mod;
    orquestador_py_main["main"]
    class orquestador_py_main fn;
    orquestador_py --> orquestador_py_main
    etl_py["etl.py (py)"]
    class etl_py mod;
    etl_py_Config["Config"]
    class etl_py_Config cls;
    etl_py --> etl_py_Config
    etl_py_Transformer["Transformer"]
    class etl_py_Transformer cls;
    etl_py --> etl_py_Transformer
    etl_py_DataQualityChecker["DataQualityChecker"]
    class etl_py_DataQualityChecker cls;
    etl_py --> etl_py_DataQualityChecker
    etl_py_ETLHandler["ETLHandler"]
    class etl_py_ETLHandler cls;
    etl_py --> etl_py_ETLHandler
    etl_py_ETLProcessor["ETLProcessor"]
    class etl_py_ETLProcessor cls;
    etl_py --> etl_py_ETLProcessor
    app_unit_test_py["app_unit_test.py (py)"]
    class app_unit_test_py mod;
    app_unit_test_py_TestApp["TestApp"]
    class app_unit_test_py_TestApp cls;
    app_unit_test_py --> app_unit_test_py_TestApp
    app_unit_test_py_test_index["test_index"]
    class app_unit_test_py_test_index fn;
    app_unit_test_py --> app_unit_test_py_test_index
    app_unit_test_py_test_create_config["test_create_config"]
    class app_unit_test_py_test_create_config fn;
    app_unit_test_py --> app_unit_test_py_test_create_config
    app_unit_test_py_test_start_etl["test_start_etl"]
    class app_unit_test_py_test_start_etl fn;
    app_unit_test_py --> app_unit_test_py_test_start_etl
    app_unit_test_py_test_etl_status["test_etl_status"]
    class app_unit_test_py_test_etl_status fn;
    app_unit_test_py --> app_unit_test_py_test_etl_status
    data_loader_unit_test_py["data_loader_unit_test.py (py)"]
    class data_loader_unit_test_py mod;
    data_loader_unit_test_py_TestSourceLoader["TestSourceLoader"]
    class data_loader_unit_test_py_TestSourceLoader cls;
    data_loader_unit_test_py --> data_loader_unit_test_py_TestSourceLoader
    data_loader_unit_test_py_setUp["setUp"]
    class data_loader_unit_test_py_setUp fn;
    data_loader_unit_test_py --> data_loader_unit_test_py_setUp
    data_loader_unit_test_py_test_load_ftp["test_load_ftp"]
    class data_loader_unit_test_py_test_load_ftp fn;
    data_loader_unit_test_py --> data_loader_unit_test_py_test_load_ftp
    data_loader_unit_test_py_test_load_mysql["test_load_mysql"]
    class data_loader_unit_test_py_test_load_mysql fn;
    data_loader_unit_test_py --> data_loader_unit_test_py_test_load_mysql
    orquestador_unit_test_py["orquestador_unit_test.py (py)"]
    class orquestador_unit_test_py mod;
    orquestador_unit_test_py_TestScript["TestScript"]
    class orquestador_unit_test_py_TestScript cls;
    orquestador_unit_test_py --> orquestador_unit_test_py_TestScript
    orquestador_unit_test_py_test_main["test_main"]
    class orquestador_unit_test_py_test_main fn;
    orquestador_unit_test_py --> orquestador_unit_test_py_test_main
    etl_unit_test_py["etl_unit_test.py (py)"]
    class etl_unit_test_py mod;
    etl_unit_test_py_TestETL["TestETL"]
    class etl_unit_test_py_TestETL cls;
    etl_unit_test_py --> etl_unit_test_py_TestETL
    etl_unit_test_py_TestETLProcessor["TestETLProcessor"]
    class etl_unit_test_py_TestETLProcessor cls;
    etl_unit_test_py --> etl_unit_test_py_TestETLProcessor
    etl_unit_test_py_setUp["setUp"]
    class etl_unit_test_py_setUp fn;
    etl_unit_test_py --> etl_unit_test_py_setUp
    etl_unit_test_py_test_transformation["test_transformation"]
    class etl_unit_test_py_test_transformation fn;
    etl_unit_test_py --> etl_unit_test_py_test_transformation
    etl_unit_test_py_test_quality_check["test_quality_check"]
    class etl_unit_test_py_test_quality_check fn;
    etl_unit_test_py --> etl_unit_test_py_test_quality_check
    data_navigation_py["data_navigation.py (py)"]
    class data_navigation_py mod;
    data_navigation_py_DataNavigator["DataNavigator"]
    class data_navigation_py_DataNavigator cls;
    data_navigation_py --> data_navigation_py_DataNavigator
    data_navigation_py___init__["__init__"]
    class data_navigation_py___init__ fn;
    data_navigation_py --> data_navigation_py___init__
    data_navigation_py_find_by_dataset_tablename_date["find_by_dataset_tablename_date"]
    class data_navigation_py_find_by_dataset_tablename_date fn;
    data_navigation_py --> data_navigation_py_find_by_dataset_tablename_date
    data_navigation_py_find_by_query["find_by_query"]
    class data_navigation_py_find_by_query fn;
    data_navigation_py --> data_navigation_py_find_by_query
    app_py["app.py (py)"]
    class app_py mod;
    data_loader_py["data_loader.py (py)"]
    class data_loader_py mod;
    install_sh["install.sh (sh)"]
    class install_sh mod;
    ext_unittest["unittest"]
    class ext_unittest ext;
    app_unit_test_py -.->|imports| ext_unittest
    ext_unittest_mock["unittest.mock"]
    class ext_unittest_mock ext;
    app_unit_test_py -.->|imports| ext_unittest_mock
    ext_flask["flask"]
    class ext_flask ext;
    app_unit_test_py -.->|imports| ext_flask
    ext_flask_login["flask_login"]
    class ext_flask_login ext;
    app_unit_test_py -.->|imports| ext_flask_login
    ext_app["app"]
    class ext_app ext;
    app_unit_test_py -.->|imports| ext_app
    data_loader_unit_test_py -.->|imports| ext_unittest
    data_loader_unit_test_py -.->|imports| ext_unittest_mock
    ext_data_loader["data_loader"]
    class ext_data_loader ext;
    data_loader_unit_test_py -.->|imports| ext_data_loader
    ext_pymongo["pymongo"]
    class ext_pymongo ext;
    data_navigation_py -.->|imports| ext_pymongo
    ext_os["os"]
    class ext_os ext;
    etl_py -.->|imports| ext_os
    ext_yaml["yaml"]
    class ext_yaml ext;
    etl_py -.->|imports| ext_yaml
    ext_pandas["pandas"]
    class ext_pandas ext;
    etl_py -.->|imports| ext_pandas
    etl_py -.->|imports| ext_pymongo
    ext_logging["logging"]
    class ext_logging ext;
    etl_py -.->|imports| ext_logging
    ext_watchdog_observers["watchdog.observers"]
    class ext_watchdog_observers ext;
    etl_py -.->|imports| ext_watchdog_observers
    ext_watchdog_events["watchdog.events"]
    class ext_watchdog_events ext;
    etl_py -.->|imports| ext_watchdog_events
    ext_datetime["datetime"]
    class ext_datetime ext;
    etl_py -.->|imports| ext_datetime
    ext_data_navigation["data_navigation"]
    class ext_data_navigation ext;
    etl_py -.->|imports| ext_data_navigation
    etl_unit_test_py -.->|imports| ext_unittest
    ext_your_etl_script["your_etl_script"]
    class ext_your_etl_script ext;
    etl_unit_test_py -.->|imports| ext_your_etl_script
    orquestador_py -.->|imports| ext_os
    orquestador_py -.->|imports| ext_yaml
    orquestador_py -.->|imports| ext_pandas
    ext_paramiko["paramiko"]
    class ext_paramiko ext;
    orquestador_py -.->|imports| ext_paramiko
    ext_pymysql["pymysql"]
    class ext_pymysql ext;
    orquestador_py -.->|imports| ext_pymysql
    orquestador_py -.->|imports| ext_logging
    ext_ftplib["ftplib"]
    class ext_ftplib ext;
    orquestador_py -.->|imports| ext_ftplib
    orquestador_py -.->|imports| ext_datetime
    orquestador_py -.->|imports| ext_data_navigation
    ext_etl["etl"]
    class ext_etl ext;
    orquestador_py -.->|imports| ext_etl
    orquestador_py -.->|imports| ext_data_loader
    orquestador_unit_test_py -.->|imports| ext_unittest
    orquestador_unit_test_py -.->|imports| ext_unittest_mock
    ext_orquestador["orquestador"]
    class ext_orquestador ext;
    orquestador_unit_test_py -.->|imports| ext_orquestador
```

---

## Architecture Reference

### PY (9 files)

#### `app.py`
**Path:** `app.py`

*No symbols extracted*

#### `app_unit_test.py`
**Path:** `app_unit_test.py`

**Classs:**
- `TestApp` (line 7)

**Functions:**
- `test_index` (line 9)
- `test_create_config` (line 23)
- `test_start_etl` (line 40)
- `test_etl_status` (line 52)

#### `data_loader.py`
**Path:** `data_loader.py`

*No symbols extracted*

#### `data_loader_unit_test.py`
**Path:** `data_loader_unit_test.py`

**Classs:**
- `TestSourceLoader` (line 5)

**Functions:**
- `setUp` (line 6)
- `test_load_ftp` (line 33)
- `test_load_mysql` (line 38)

#### `data_navigation.py`
**Path:** `data_navigation.py`

**Classs:**
- `DataNavigator` (line 3)

**Functions:**
- `__init__` (line 4)
- `find_by_dataset_tablename_date` (line 9)
- `find_by_query` (line 13)

#### `etl.py`
**Path:** `etl.py`

**Classs:**
- `Config` (line 11)
- `Transformer` (line 22)
- `DataQualityChecker` (line 31)
- `ETLHandler` (line 39)
- `ETLProcessor` (line 65)
- `ETLTests` (line 92)

**Functions:**
- `__init__` (line 12)
- `load` (line 15)
- `get` (line 19)
- `__init__` (line 23)
- `apply` (line 26)
- `__init__` (line 32)
- `check` (line 35)
- `__init__` (line 40)
- `on_created` (line 47)
- `__init__` (line 66)
- `process` (line 72)
- `test_etl` (line 93)

#### `etl_unit_test.py`
**Path:** `etl_unit_test.py`

**Classs:**
- `TestETL` (line 4)
- `TestETLProcessor` (line 27)

**Functions:**
- `setUp` (line 5)
- `test_transformation` (line 11)
- `test_quality_check` (line 18)
- `setUp` (line 28)
- `test_etl_process` (line 35)

#### `orquestador.py`
**Path:** `orquestador.py`

**Functions:**
- `main` (line 13)

#### `orquestador_unit_test.py`
**Path:** `orquestador_unit_test.py`

**Classs:**
- `TestScript` (line 5)

**Functions:**
- `test_main` (line 8)

### SH (1 files)

#### `install.sh`
**Path:** `install.sh`

*No symbols extracted*
