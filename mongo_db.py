import pymongo

# make the connection - below string is default port and host
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")

# client["Employee"] will either create a new db or use the same if one doesnt exists
mydb = client["Employee"]

# employee information is the table which activates everything - without table the db is not created
information = mydb.employeeinformation

# record / records to be added
records = [{
    
    "first_name": "Ankit",
    "second_name": "Aggarwal",
    "Age": 25,
    "Status": "Single",
    "Department": "Python"
    
},
{
    
    "first_name": "Rahul",
    "second_name": "Aggarwal",
    "Age": 28,
    "Status": "Single",
    "Department": "CII"
    
},
{
    
    "first_name": "Umesh",
    "second_name": "Aggarwal",
    "Age": 54,
    "Status": "Married",
    "Department": "havells"
    
}]

# for single record insertion
information.insert_one(records)

# for inserting many records make sure records is a list of json
information.insert_many(records)

# find the first record
information.find_one()

# find all the records - returns the cursor # Type 1
for record in information.find():
    print(record)


# find all the records - returns the cursor # Type 2
for record in information.find({}):
    print(record)

# find all the records with where condition - returns cursor
for record in information.find({"first_name": "Ankit"}):
    print(record)


# find all the records with IN condition
for record in information.find({"Department": {"$in":["havells", "Python"]}}):
    print(record)


# find all the records with LESS ($lt) and Greater ($gt) condition and AND condition
for record in information.find({"Department": "Python", "Age": {"$lt": 50}}):
    print(record)


# find all the records with OR condition
for record in information.find({"$or": [{"Department": "Python"}, {"Age": {"$lt": 50}}]}):
    print(record)