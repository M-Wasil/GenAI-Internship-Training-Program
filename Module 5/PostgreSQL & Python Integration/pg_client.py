from __future__ import annotations

import logging
import os
from pathlib import Path

import pandas as pd
import psycopg2
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

DB_CONFIG = {
    "host": os.getenv("PG_HOST", "localhost"),
    "port": int(os.getenv("PG_PORT", "5432")),
    "dbname": os.getenv("PG_DATABASE", "module5_shop"),
    "user": os.getenv("PG_USER", "postgres"),
    "password": os.getenv("PG_PASSWORD", ""),
}

QUERY = '''
SELECT p.product_id, p.title, c.name AS category, pp.price_gbp
FROM products p
JOIN categories c ON c.category_id = p.category_id
JOIN product_prices pp ON pp.product_id = p.product_id
WHERE pp.price_gbp >= %s
ORDER BY pp.price_gbp DESC;
'''

def fetch_products(min_price: float = 0.0) -> pd.DataFrame:
    if min_price < 0:
        raise ValueError("min_price must be non-negative")
    with psycopg2.connect(**DB_CONFIG) as connection:
        return pd.read_sql_query(QUERY, connection, params=(min_price,))

def save_report(df: pd.DataFrame) -> Path:
    output = Path("postgres_product_report.csv")
    df.to_csv(output, index=False)
    logger.info("Saved %d rows to %s", len(df), output)
    return output

if __name__ == "__main__":
    df = fetch_products(min_price=20.0)
    print(df)
    save_report(df)
