from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)

db = client.location_voitures

users = db.users

user_id = users.insert_one({'name': 'John', 'email': 'John123@gmail.com', 'password': '123', 'role': 'admin'}).inserted_id
users.insert_one({'name': 'Jane', 'email': 'Jane123@gmail.com', 'password': '123', 'role': 'manager'})

print('Users added successfully')

for user in users.find():
    print(user)

print([user for user in users.find({"_id": ObjectId(user_id)})])
#print(user for user in users.find({"age": {"$gt": 20}}))

print(users.count_documents({"name": "Jane"}))

users.update_one({"_id": user_id}, {"$set": {"password": "111"}})

users.delete_many({"name": "John"})

