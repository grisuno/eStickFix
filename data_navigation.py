import pymongo

class DataNavigator:
    def __init__(self, db_name, collection_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]
    
    def find_by_dataset_tablename_date(self, dataset, tablename, date):
        query = {"dataset": dataset, "tablename": tablename, "date": date}
        return self.collection.find_one(query)
    
    def find_by_query(self, query):
        return self.collection.find(query)
