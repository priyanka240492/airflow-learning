from airflow import DAG
from datetime import datetime, timedelta

from airflow.operators.python import PythonOperator

default_args = {
    'owner' : 'klp',
    'retries' : 5,
    'retry_delay': timedelta(minutes=2)
}

def greet():
    print("Hello Priya! Welcome to your first DAG PythonOperator task")

with DAG(
    dag_id='my-python-op-dag',
    default_args = default_args,
    description='This DAG contains PythoOperator task',
    start_date=datetime(2025,5,28,2),
    schedule=None #For daily schedule, use @daily
) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet
    )

    task1

