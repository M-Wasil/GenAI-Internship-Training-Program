from datetime import datetime, timedelta
from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

PROJECT = "/opt/airflow/module_4_data_engineering_etl"

with DAG(
    dag_id="module_4_etl_pipeline",
    start_date=datetime(2026, 6, 30),
    schedule="@daily",
    catchup=False,
    default_args={"owner":"intern", "retries":2, "retry_delay":timedelta(minutes=5)},
    tags=["etl","module4"],
) as dag:
    scrape = BashOperator(
        task_id="extract_web_data",
        bash_command=f"cd {PROJECT} && python scraper.py"
    )
    api = BashOperator(
        task_id="extract_api_data",
        bash_command=f"cd {PROJECT} && python api_ingest.py"
    )
    etl = BashOperator(
        task_id="transform_and_load",
        bash_command=f"cd {PROJECT} && python etl_pipeline.py"
    )
    [scrape, api] >> etl
