# mongodb

import pymongo
from bson.objectid import ObjectId

client = pymongo.MongoClient(host='localhost', port=27017)

db = client.test
# db = client['test']

collection = db.students
# collection = db['students']

# student = {
#     'id': '20170101',
#     'name': 'Jordan',
#     'age': 20,
#     'gender': 'male'
# }

# result = collection.insert_one(student)
# print(result)
# print(result.inserted_id)

# student1 = {
#     'id': '20170103',
#     'name': 'Amy',
#     'age': 22,
#     'gender': 'female'
# }

# student2 = {
#     'id': '20170102',
#     'name': 'Mike',
#     'age': 21,
#     'gender': 'male'
# }

# student3 = {
#     'id': '20170104',
#     'name': 'Kevin',
#     'age': 20,
#     'gender': 'male'
# }

# result = collection.insert_one(student3)
# print(result)
# print(result.inserted_id)

# result = collection.insert_many([student1, student2])
# print(result)
# print(result.inserted_ids)

# result = collection.find_one({'name': 'Mike'})
# print(type(result))
# print(result)

# result = collection.find_one({'_id': ObjectId('637d97976f8847a6211e010f')})
# print(result)
results = collection.find()
# results = collection.find({'age' : 20})
# results = collection.find({'age': {'$gt': 20}})
# results = collection.find({'name': {'$regex': '^M.*'}})
# print(results)
for result in results:
    print(result)

# count = collection.count_documents({'age': {'$gt': 20}})
# print(count)

# results = collection.find().sort('name', pymongo.ASCENDING)
# print([result['name'] for result in results])

# results = collection.find().sort('name', pymongo.ASCENDING).skip(2)
# print([result['name'] for result in results])

# results = collection.find().sort('name', pymongo.ASCENDING).skip(2).limit(1)
# print([result['name'] for result in results])

# condition = {'name': 'Kevin'}
# student = collection.find_one(condition)
# student['age'] = 26
# result = collection.update_one(condition, {"$set": student})
# print(result)
# print(result.matched_count, result.modified_count)

# condition = {'age': {'$gt': 20}}
# result = collection.update_one(condition, {'$inc': {'age': 1}})
# print(result)
# print(result.matched_count, result.modified_count)

# condition = {'age': {'$gt': 20}}
# result = collection.update_many(condition, {'$inc': {'age': 1}})
# print(result)
# print(result.matched_count, result.modified_count)

# result = collection.delete_one({'name': 'Kevin'})
# print(result)
# print(result.deleted_count)
# result = collection.delete_many({'age': {'$lt': 25}})
# print(result.deleted_count)
