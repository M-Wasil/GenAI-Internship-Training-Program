from __future__ import annotations
import json, logging, sqlite3
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

BASE = Path(__file__).resolve().parent
STAGING, OUTPUT, LOGS = BASE/"staging", BASE/"output", BASE/"logs"
API_INPUT, BOOK_INPUT = STAGING/"raw_api_posts.json", STAGING/"scraped_books.json"
DB, CSV = OUTPUT/"etl_output.db", OUTPUT/"etl_output.csv"

OUTPUT.mkdir(exist_ok=True); LOGS.mkdir(exist_ok=True)
logging.basicConfig(filename=LOGS/"etl_pipeline.log", level=logging.INFO,
                    format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

def extract_api():
    with API_INPUT.open(encoding="utf-8") as f:
        data = json.load(f)["data"]
    return pd.DataFrame(data).rename(columns={"id":"record_id","userId":"source_user_id",
                                               "title":"name","body":"description"})[
        ["record_id","name","description"]]

def extract_books():
    with BOOK_INPUT.open(encoding="utf-8") as f:
        data = json.load(f)
    return pd.DataFrame(data).rename(columns={"title":"name","price_gbp":"price"})

def transform(api, books):
    a = api.copy()
    a["source"], a["category"], a["price"], a["url"] = "api", "post", pd.NA, pd.NA
    a = a[["record_id","name","description","price","source","category","url"]]

    b = books.copy()
    b["record_id"] = "book:" + b["product_url"].astype(str)
    b["description"], b["source"], b["category"], b["url"] = b["availability"], "web", "book", b["product_url"]
    b = b[["record_id","name","description","price","source","category","url"]]

    df = pd.concat([a,b], ignore_index=True)
    for col in ["name","description"]:
        df[col] = df[col].astype("string").str.strip().str.replace(r"\s+", " ", regex=True)
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["processed_at"] = datetime.now(timezone.utc).isoformat()
    return df.drop_duplicates("record_id", keep="last")

def validate(df):
    required = {"record_id","name","description","price","source","category","url","processed_at"}
    missing = required - set(df.columns)
    if missing: raise ValueError(f"Missing columns: {sorted(missing)}")
    if df.empty: raise ValueError("Empty dataset")
    if df.record_id.isna().any(): raise ValueError("Null record_id")
    if df.record_id.duplicated().any(): raise ValueError("Duplicate record_id")
    if (df.price.dropna() < 0).any(): raise ValueError("Negative price")
    logger.info("Validation passed: %d records", len(df))

def load(df):
    df.to_csv(CSV, index=False)
    with sqlite3.connect(DB) as con:
        df.to_sql("etl_records", con, if_exists="replace", index=False)

if __name__ == "__main__":
    logger.info("Pipeline started")
    transformed = transform(extract_api(), extract_books())
    validate(transformed)
    load(transformed)
    logger.info("Pipeline completed successfully")
