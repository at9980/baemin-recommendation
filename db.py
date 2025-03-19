import os
import urllib.parse
import certifi
from pymongo import MongoClient
from pymongo.server_api import ServerApi

def fetch_restaurant_info():
    username = urllib.parse.quote_plus(os.environ['MONGODB_USERNAME'])
    password = urllib.parse.quote_plus(os.environ['MONGODB_PASSWORD'])
    uri = f"mongodb+srv://{username}:{password}@cluster0.61sar.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
    db = client.restaurant_db
    collection = db.restaurant_info

    # 필요한 필드만 조회 (예시로 _id 제외)
    restaurants_info = list(collection.find({}, {'_id': False}))
    return restaurants_info

def insert_to_mongo(query, recommendations, text):
    username = urllib.parse.quote_plus(os.environ['MONGODB_USERNAME'])
    password = urllib.parse.quote_plus(os.environ['MONGODB_PASSWORD'])
    uri = f"mongodb+srv://{username}:{password}@cluster0.61sar.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri, server_api=ServerApi('1'), tlsCAFile=certifi.where())
    db = client.recommendations_db
    collection = db.recommendations

    insertion = {
        "recommend_text": "",
        "recommend_reason": text,
        "recommendations": [
            {"restaurant": key, "menus": value} for key, value in recommendations.items()
        ]
    }
    result = collection.update_one({"_id": query}, {"$set": insertion}, upsert=True)
    return result
