from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time

def do_something():
    time.sleep(5)

with DAG(
    "test_metrics_dag",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@once",
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id="task_1",
        python_callable=do_something
    )

    t2 = PythonOperator(
        task_id="task_2",
        python_callable=do_something
    )

    t1 >> t2
