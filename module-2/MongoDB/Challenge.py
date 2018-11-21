from pymongo import MongoClient 
client = MongoClient("localhost",27017)
db = client.test_database
print(list(db.docus.find({"founded_year":{"$gte":2010}})))
