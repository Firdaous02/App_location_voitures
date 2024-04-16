from pymongo import MongoClient
from bson.objectid import ObjectId

client = MongoClient('localhost', 27017)#make sure had ra9m correct mlli tfta7 compass

db = client.location_voitures

users = db.users

users.insert_one({'name': 'John', 'email': 'John123@gmail.com', 'password': '123', 'role': 'admin'})
users.insert_one({'name': 'Jane', 'email': 'Jane123@gmail.com', 'password': '123', 'role': 'manager'})

print('Users added successfully')
