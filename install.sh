#!/bin/bash

mkdir -p project/{config,etl,transformation,qa,log}

# Create sample config files
touch project/config/config1.yaml
touch project/config/config2.yaml
touch project/config/config3.yaml

# Create sample subdirectories and files for etl, transformation, and qa
datasets=("dataset1" "dataset2")
tables=("table1" "table2")

for dataset in "${datasets[@]}"; do
    for table in "${tables[@]}"; do
        mkdir -p project/etl/$dataset/$table
        mkdir -p project/transformation/$dataset/$table
        mkdir -p project/qa/$dataset/$table
        touch project/etl/$dataset/$table/${dataset}_${table}_date_now.parquet
        touch project/transformation/$dataset/$table/${dataset}_${table}_date_now/script.py
        touch project/qa/$dataset/$table/${dataset}_${table}_date_now/qa_script.py
    done
done

# Create data_navigation.py and etl.py
touch project/data_navigation.py
touch project/etl.py

echo "Project structure created successfully!"

pip install pyyaml
pip install watchdog
pip install pandas
pip install pymongo
