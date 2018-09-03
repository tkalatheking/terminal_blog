import pymongo

class Database(object):
    uri = "mongodb://127.0.1:27017"
    DATABASE = None # client['fullstack']

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)


    @staticmethod
    def insert(collection, query):
        Database.DATABASE[collection].find(query)


    @staticmethod
    def insert(collection, query):
        Database.DATABASE[collection].find_one(query)