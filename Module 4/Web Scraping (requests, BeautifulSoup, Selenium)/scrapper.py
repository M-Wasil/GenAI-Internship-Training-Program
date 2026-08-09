from __future__ import annotations
import csv, json, logging, time
from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/"
OUT = Path("staging")
HEADERS = {"User-Agent": "Module4-ETL-LearningBot/1.0 (educational use)"}
DELAY = 1.0
TIMEOUT = 15

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger(__name__)

def fetch(session, url):
    try:
        response = session.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except requests.RequestException as exc:
        logger.error("Request failed: %s", exc)
        return None

def parse_books(html, page_url):
    soup = BeautifulSoup(html, "html.parser")
    records = []

    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 a")
        price_tag = article.select_one(".price_color")
        availability = article.select_one(".availability")

        if not title_tag or not price_tag:
            continue

        url = urljoin(page_url, title_tag.get("href"))

        price_text = price_tag.get_text(strip=True)
        price_text = price_text.replace("Â£", "").replace("£", "").strip()
        price = float(price_text)

        records.append({
            "title": title_tag.get("title") or title_tag.get_text(strip=True),
            "price_gbp": price,
            "availability": availability.get_text(" ", strip=True)
                if availability else "",
            "product_url": url
        })

    return records

def scrape(max_pages=5):
    records, next_url = [], BASE_URL
    with requests.Session() as session:
        for page in range(1, max_pages + 1):
            logger.info("Scraping page %d", page)
            html = fetch(session, next_url)
            if html is None:
                break
            records.extend(parse_books(html, next_url))
            soup = BeautifulSoup(html, "html.parser")
            link = soup.select_one("li.next a")
            if not link:
                break
            next_url = urljoin(next_url, link.get("href"))
            time.sleep(DELAY)
    return list({r["product_url"]: r for r in records}.values())

def save(records):
    OUT.mkdir(exist_ok=True)
    with (OUT / "scraped_books.json").open("w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    with (OUT / "scraped_books.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["title","price_gbp","availability","product_url"])
        writer.writeheader()
        writer.writerows(records)
    logger.info("Saved %d records", len(records))

if __name__ == "__main__":
    data = scrape()
    if not data:
        raise RuntimeError("No books were scraped.")
    save(data)
