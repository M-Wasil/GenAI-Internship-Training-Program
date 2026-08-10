from __future__ import annotations

import json
import os
from pathlib import Path

from dotenv import load_dotenv
from pymongo import ASCENDING, DESCENDING, MongoClient, UpdateOne

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DATABASE = os.getenv("MONGO_DATABASE", "module5_shop")
COLLECTION = os.getenv("MONGO_COLLECTION", "products")

def get_collection():
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    return client[DATABASE][COLLECTION]

def upsert_products(collection, products: list[dict]) -> None:
    operations = []
    for product in products:
        if product.get("product_url"):
            operations.append(
                UpdateOne({"product_url": product["product_url"]},
                          {"$set": product}, upsert=True)
            )
    if operations:
        result = collection.bulk_write(operations, ordered=False)
        print(f"Matched: {result.matched_count}, upserted: {len(result.upserted_ids)}")

def create_indexes(collection):
    collection.create_index([("product_url", ASCENDING)], unique=True)
    collection.create_index([("price_gbp", DESCENDING)])
    collection.create_index([("category", ASCENDING)])

def crud_examples(collection):
    collection.update_one(
        {"product_url": "https://example.com/demo"},
        {"$set": {"title": "Demo Product", "price_gbp": 10.0, "category": "Demo"}},
        upsert=True
    )
    for doc in collection.find({"price_gbp": {"$gte": 20}}).limit(5):
        print(doc)
    collection.update_one(
        {"product_url": "https://example.com/demo"},
        {"$set": {"category": "Updated"}}
    )
    collection.delete_one({"product_url": "https://example.com/demo"})

def aggregation_example(collection):
    pipeline = [
        {"$match": {"price_gbp": {"$type": "number"}}},
        {"$group": {
            "_id": "$category",
            "product_count": {"$sum": 1},
            "average_price": {"$avg": "$price_gbp"},
            "maximum_price": {"$max": "$price_gbp"}
        }},
        {"$sort": {"average_price": DESCENDING}}
    ]
    return list(collection.aggregate(pipeline))

if __name__ == "__main__":
    collection = get_collection()
    create_indexes(collection)

    source = Path("../Module 4/staging/scraped_books.json")
    if source.exists():
        upsert_products(collection, json.loads(source.read_text(encoding="utf-8")))

    crud_examples(collection)

    print("\nAggregation:")
    for result in aggregation_example(collection):
        print(result)
