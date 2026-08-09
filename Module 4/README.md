# Module 4 — Data Engineering & ETL

## Deliverables

| Day | Topic | Deliverable |
|---|---|---|
| 15 | Data Engineering Foundations | `etl_architecture.md` |
| 16 | Web Scraping | `scraper.py` |
| 17 | APIs & Data Ingestion | `api_ingest.py` |
| 18 | ETL Pipeline | `etl_pipeline.py` |
| 19 | Automation & Orchestration | `airflow/module4_etl_dag.py` + this runbook |

## Install

```bash
pip install -r requirements.txt
```

## Run

First extract both sources:

```bash
python scraper.py
python api_ingest.py
```

Then run the ETL:

```bash
python etl_pipeline.py
```

Outputs:

- `staging/scraped_books.json`
- `staging/scraped_books.csv`
- `staging/raw_api_posts.json`
- `output/etl_output.csv`
- `output/etl_output.db`
- `logs/etl_pipeline.log`

## Pipeline

```text
Books website ──> scraper.py ──┐
                               ├──> staging ──> etl_pipeline.py ──> CSV + SQLite
REST API ───────> api_ingest.py ┘
```

## Features

- Requests + BeautifulSoup
- Pagination
- Responsible scraping with User-Agent and rate limiting
- REST API ingestion
- Pagination
- Retry + exponential backoff
- Raw staging
- Pandas transformation
- Data-quality validation
- Deduplication
- Idempotent output replacement
- SQLite loading
- Structured logging
- Environment-based configuration
- Airflow DAG
- Scheduled daily execution

## Windows scheduling

For Task Scheduler, create a `.bat` file that runs:

```bat
cd /path/to/module_4_data_engineering_etl
python scraper.py
python api_ingest.py
python etl_pipeline.py
```

Schedule it daily.

## Airflow

Copy `airflow/module4_etl_dag.py` into the Airflow `dags/` directory and adjust
the `PROJECT` path to the location visible inside the Airflow environment.

The DAG runs both extraction tasks in parallel and then starts the ETL task.
Failed tasks receive two retries with a five-minute delay.

## Secrets

Never commit `.env`. Use `.env.example` as the template and store real
credentials in `.env` or an orchestration platform's secret manager.
