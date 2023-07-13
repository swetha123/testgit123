from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb+srv://swethahavalkod123:newmongodb%402023@cluster0.0oyzytt.mongodb.net/?retryWrites=true&w=majority")
# Send a ping to confirm a successful connection
db = client.test
print(db)
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

d1 = {
    "name" : "swetha",
    "email" : "xyzineuron.com",
    "surname" : "havalkod"
}

db1 = client['mongotest']
collecton1 = db1["test"]
collecton1.insert_one(d1)













