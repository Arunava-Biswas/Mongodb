# to import the MongoDB
import pymongo

# to set up connection with the database
client = pymongo.MongoClient("mongodb+srv://ineuron:Project1@cluster0.rp4qzrr.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# to test the connection
print(db)

# Now let's create a dictionary
d = {
    "name": "Arunava",
    "surname": "Biswas",
    "email": "arunava_biswas@email.com"
}

# Now we will insert the data inside the database
db1 = client['mongotest']       # create a variable
coll = db1['test']              # creating a collection
coll.insert_one(d)             # calling insert_one() on the collection
