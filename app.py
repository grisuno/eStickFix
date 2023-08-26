import os
import yaml
import pandas as pd
import paramiko
import pymysql
import logging
from ftplib import FTP
from datetime import datetime
from data_navigation import DataNavigator
from etl import Config, Transformer, DataQualityChecker, ETLProcessor
from data_loader import SourceLoader

def main():
    with open("sources.yaml", "r") as sources_file:
        sources_config = yaml.safe_load(sources_file)['sources']
    
    loader = SourceLoader(sources_config)
    loader.load_sources()
    
    logging.basicConfig(filename="log/orchestration_log.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
    config_files = ["config/config1.yaml", "config/config2.yaml", "config/config3.yaml"]
    
    for config_file in config_files:
        config = Config(config_file)
        transformation_script = f"transformation/{config.get('dataset')}/{config.get('tablename')}/{config.get('date_now')}/script.py"
        qa_script = f"qa/{config.get('dataset')}/{config.get('tablename')}/{config.get('date_now')}/qa_script.py"
        
        transformer = Transformer(transformation_script)
        quality_checker = DataQualityChecker(qa_script)
        
        data_navigator = DataNavigator("mydatabase", "etl_log")
        
        etl_processor = ETLProcessor(config, transformer, quality_checker, data_navigator)
        etl_processor.process()
    
    data_nav = DataNavigator("mydatabase", "etl_log")
    dataset = "dataset1"
    table_name = "table1"
    
    data = data_nav.find_by_dataset_tablename_date(dataset, table_name, datetime.now().strftime('%Y%m%d'))
    print("Data:")
    print(data)
    
    query = {"dataset": dataset, "tablename": table_name}
    result = data_nav.find_by_query(query)
    print("Result:")
    for item in result:
        print(item)
    
    df = pd.DataFrame(result)
    print("Statistics:")
    print(df.describe())
    print("Correlation:")
    print(df.corr())

if __name__ == "__main__":
    main()
