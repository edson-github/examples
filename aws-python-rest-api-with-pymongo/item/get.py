import json
import os
import pymongo

# Fetch mongo env vars
usr = os.environ['MONGO_DB_USER']
pwd = os.environ['MONGO_DB_PASS']
mongo_db_name = os.environ['MONGO_DB_NAME']
mongo_collection_name = os.environ['MONGO_COLLECTION_NAME']
url = os.environ['MONGO_DB_URL']

# Connection String
client = pymongo.MongoClient(
    f"mongodb+srv://{usr}:{pwd}@{url}/test?retryWrites=true&w=majority"
)
db = client[mongo_db_name]
collection = db[mongo_collection_name]


def get(event, context):
    # get item_id to delete from path parameter
    item_id = event['pathParameters']['id']

    # delete item from the database
    item = collection.find_one({"_id": item_id})

    return {"statusCode": 200, "body": json.dumps(item)}
