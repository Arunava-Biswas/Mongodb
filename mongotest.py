# to import the MongoDB
import pymongo
import pprint

# to set up connection with the database
client = pymongo.MongoClient("mongodb+srv://ineuron:Project1@cluster0.rp4qzrr.mongodb.net/?retryWrites=true&w=majority")

# creating a database
db = client.ineuron_FSDS

# the data to be entered in dictionary format (BSON - Binary Javascript Object Notation)
student = {
     'Course': "Python",
     'Details': {
        'Duration': "3 months",
        'Trainer': "Sudhanshu Kumar"
     },
     'Batch': [{'Size': "Small", 'qty': 15}, {'Size': "Medium", 'qty': 25}],
     'Category': "Programming language"
   }

# creating the variable
var1 = client['Bootcamp']

# creating collection
students = var1['test']

# inserting the data
students.insert_one(student)

# to see the result
pprint.pprint(students.find_one())