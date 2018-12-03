import os
from pymongo import MongoClient
import json

def main():
    print(os.environ['APPDATA'])
    client = MongoClient('mongodb://admin:password1@ds117334.mlab.com:17334/item')
    db = client.item
    collection = db.items
    print(collection)
    item = {
        "name": "Samsung S9",
        "price": "800€",
        "comment": {
            "note": 5,
            "text": "Good"
        },
        "description": {
            "color": "black",
            "model": "64GB"
        }
    }
    rec = collection.insert_one(item)
    print("Done", rec)

def co_db_item(self):
    print(os.environ['MONGO_URL'])

def co_db_user(self):
    print(os.environ['DATABASE_URL'])

if __name__ == "__main__":
    main()

