# creating a new collection for multiple queries

import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:Project1@cluster0.rp4qzrr.mongodb.net/?retryWrites=true&w=majority")

database = client["mongodb_queries"]
collection = database["learning"]

# inserting a single data to check
"""
d = {
    "name": "Arunava",
    "email_id": "arunava@email.com",
    "subject": ["Data Science", "Big Data", "Data Analytics"]
}

collection.insert_one(d)
"""
# deleting the data
# collection.delete_many({})

# Now for the tests:
data =  [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

# inserting the data
# collection.insert_many(data)

# now to select all the data
"""
d = collection.find()

for i in d:
    print(i)
"""


# looking for data where status is either 'A'
"""
d = collection.find({"status":"A"})

for i in d:
    print(i)
"""


# looking for data where status is either 'A' or 'P'
# here the '$in' is a keyword in mongoDB
"""
condition = {"status": {'$in': ['A', 'P']}}
records = collection.find(condition)

for i in records:
    print(i)
"""

# where quantity is >= 75
# here the '$gte' is a keyword in mongoDB
"""
condition = {"qty": {'$gte': 75}}
records = collection.find(condition)

for i in records:
    print(i)
"""

# where quantity is =< 75
# here the '$gte' is a keyword in mongoDB
"""
condition = {"qty": {'$lte': 75}}
records = collection.find(condition)

for i in records:
    print(i)
"""

# where quantity is equal to 95 and item is 'sketch pad
# where quantity is greater than or equal to 75 and item is 'sketch pad
"""
condition1 = {"item": "sketch pad", 'qty': 95}
condition2 = {"item": "sketch pad", 'qty': {'$gte': 75}}
records = collection.find(condition2)

for i in records:
    print(i)
"""

# now with the or condition i.e. either based on item or based on the quantity
# for this the keyword is '$or'
"""
condition = {'$or': [{"item": "sketch pad"}, {'qty': 75}]}
records = collection.find(condition)

for i in records:
    print(i)
"""


# now up-date
# up-date the 'canvas' to 'sudhanshu'
"""
present_data = {"item": 'canvas'}
new_data = {'$set':{"item": 'sudhanshu'}}

update1 = collection.update_one(present_data, new_data)

d = collection.find({'item': "sudhanshu"})

for i in d:
    print(i)
"""

