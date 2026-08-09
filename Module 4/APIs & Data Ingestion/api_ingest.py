from __future__ import annotations
import json, logging, os, time
from pathlib import Path
import requests
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv("API_URL", "https://jsonplaceholder.typicode.com/posts")
PAGE_SIZE = int(os.getenv("PAGE_SIZE", "10"))
MAX_PAGES = int(os.getenv("MAX_PAGES", "3"))
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
BACKOFF = float(os.getenv("BACKOFF_FACTOR", "1.0"))
TIMEOUT = int(os.getenv("API_TIMEOUT", "15"))

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

def get_with_retry(session, params):
    last_error = None
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = session.get(URL, params=params, timeout=TIMEOUT)
            if response.status_code == 429 or response.status_code >= 500:
                raise requests.HTTPError(f"Retryable status {response.status_code}")
            response.raise_for_status()
            return response
        except requests.RequestException as exc:
            last_error = exc
            if attempt < MAX_RETRIES:
                delay = BACKOFF * (2 ** (attempt - 1))
                logger.warning("Attempt %d failed; retrying in %.1fs", attempt, delay)
                time.sleep(delay)
    raise RuntimeError(f"API request failed: {last_error}")

def ingest():
    records = []
    with requests.Session() as session:
        for page in range(1, MAX_PAGES + 1):
            logger.info("Fetching API page %d", page)
            response = get_with_retry(session, {"_page": page, "_limit": PAGE_SIZE})
            data = response.json()
            if not isinstance(data, list):
                raise ValueError("Expected a JSON list")
            records.extend(data)
            if len(data) < PAGE_SIZE:
                break
    return records

if __name__ == "__main__":
    records = ingest()
    if not records:
        raise RuntimeError("API returned no records.")
    Path("staging").mkdir(exist_ok=True)
    with Path("staging/raw_api_posts.json").open("w", encoding="utf-8") as f:
        json.dump({"source": URL, "record_count": len(records), "data": records}, f, indent=2)
    logger.info("Saved %d raw API records", len(records))
