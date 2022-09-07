import pymongo
client = pymongo.MongoClient("mongodb+srv://Saranya:advik12345@cluster.ncmrhwz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name": "Sara",
    "email id": "sara@gmail.com",
    "surname":"nathan "
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)