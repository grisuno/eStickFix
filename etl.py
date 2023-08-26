import os
import yaml
import pandas as pd
import pymongo
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
from data_navigation import DataNavigator

class Config:
    def __init__(self, config_path):
        self.load(config_path)

    def load(self, config_path):
        with open(config_path, "r") as config_file:
            self.data = yaml.safe_load(config_file)
    
    def get(self, key):
        return self.data.get(key)

class Transformer:
    def __init__(self, transformation_script):
        self.transformation_script = transformation_script
    
    def apply(self, df):
        if os.path.exists(self.transformation_script):
            exec(open(self.transformation_script).read())
        return df

class DataQualityChecker:
    def __init__(self, qa_script):
        self.qa_script = qa_script
    
    def check(self, df):
        if os.path.exists(self.qa_script):
            exec(open(self.qa_script).read())

class ETLHandler(FileSystemEventHandler):
    def __init__(self, config, transformer, quality_checker, collection, data_navigator):
        self.config = config
        self.transformer = transformer
        self.quality_checker = quality_checker
        self.collection = collection
        self.data_navigator = data_navigator
    
    def on_created(self, event):
        if event.src_path.endswith(".parquet"):
            df = pd.read_parquet(event.src_path)
            transformed_df = self.transformer.apply(df)
            self.quality_checker.check(transformed_df)
            
            self.collection.insert_many(transformed_df.to_dict(orient="records"))
            logging.info(f"Data loaded for dataset: {self.config.get('dataset')} - table: {self.config.get('tablename')} - date: {self.config.get('date_now')}")
            
            log_data = {
                "dataset": self.config.get("dataset"),
                "tablename": self.config.get("tablename"),
                "date": self.config.get("date_now"),
                "status": "success",
                "timestamp": datetime.now()
            }
            self.data_navigator.collection.insert_one(log_data)

class ETLProcessor:
    def __init__(self, config, transformer, quality_checker, data_navigator):
        self.config = config
        self.transformer = transformer
        self.quality_checker = quality_checker
        self.data_navigator = data_navigator
    
    def process(self):
        dataset = self.config.get("dataset")
        tablename = self.config.get("tablename")
        date_now = self.config.get("date_now")
        etl_directory = f"etl/{dataset}/{tablename}/{dataset}_{tablename}_{date_now}"
        
        collection = self.data_navigator.db[tablename]
        event_handler = ETLHandler(self.config, self.transformer, self.quality_checker, collection, self.data_navigator)
        observer = Observer()
        observer.schedule(event_handler, path=etl_directory, recursive=False)
        observer.start()
        
        try:
            while True:
                pass
        except KeyboardInterrupt:
            observer.stop()
        
        observer.join()

class ETLTests(unittest.TestCase):
    def test_etl(self):
        # Your test logic here
        
        # Use assertions to verify the ETL process
        
        pass

if __name__ == "__main__":
    logging.basicConfig(filename="log/etl_log.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    
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
    
    unittest.main()
