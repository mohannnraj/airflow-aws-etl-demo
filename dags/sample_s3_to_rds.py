from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import boto3

def upload_to_s3():
    s3 = boto3.client('s3')
    s3.put_object(Bucket='airflow-demo-mohan', Key='test.txt', Body='Hello from Airflow')

def dummy_rds_task():
    print("Pretend we're inserting into RDS...")

with DAG("s3_to_rds_demo",
         start_date=datetime(2025, 1, 1),
         schedule_interval=None,
         catchup=False) as dag:

    upload = PythonOperator(task_id="upload_to_s3", python_callable=upload_to_s3)
    insert = PythonOperator(task_id="insert_to_rds", python_callable=dummy_rds_task)

    upload >> insert
