import pymongo

uri = "mongodb://127.0.1:27017"
client = pymongo.MongoClient(uri)
databse = client['fullstack']
collections = databse['students']

students = collections.find({})

for student in students:
    print(student)