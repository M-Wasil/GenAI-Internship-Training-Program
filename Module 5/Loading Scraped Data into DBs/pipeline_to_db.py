from __future__ import annotations

import json
import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from pymongo import MongoClient, UpdateOne

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

INPUT = Path(os.getenv(
    "SCRAPED_PRODUCTS_FILE",
    r"C:\Wasil\TMC\Assignment ETL\Data\clean_products.json"
))
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DATABASE = os.getenv("MONGO_DATABASE", "module5_shop")
COLLECTION = os.getenv("MONGO_COLLECTION", "products")

def load_products():
    if not INPUT.exists():
        raise FileNotFoundError(f"Input not found: {INPUT}. Run Module 4 scraper.py first.")

    products = json.loads(INPUT.read_text(encoding="utf-8"))
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    client.admin.command("ping")
    collection = client[DATABASE][COLLECTION]

    collection.create_index("product_url", unique=True)
    collection.create_index("price_gbp")

    operations = [
        UpdateOne({"product_url": p["product_url"]}, {"$set": p}, upsert=True)
        for p in products if p.get("product_url")
    ]

    if operations:
        result = collection.bulk_write(operations, ordered=False)
        logger.info(
            "MongoDB load complete: matched=%d modified=%d upserted=%d",
            result.matched_count, result.modified_count, len(result.upserted_ids)
        )
    client.close()

if __name__ == "__main__":
    load_products()
