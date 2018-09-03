import pymongo

uri = "mongodb://127.0.1:27017"
client = pymongo.MongoClient(uri)
databse = client['fullstack']
collections = databse['students']

students = [student for student in collections.find({})]

print(students)

