from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'neji',
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}


def get_sklearn():
    import sklearn
    print(f"sklearn with version: {sklearn.__version__} ")


def get_matplotlib():
    import matplotlib
    print(f"matplotlib with version: {matplotlib.__version__}")

# After changing the requirements file:
# sudo docker build . --tag extending_airflow:latest
# We rebuild the webserver and scheduler in docker after making changes
# to the dependencies and docker file: 
# docker-compose up -d --no-deps --build airflow-webserver airflow-scheduler
with DAG(
    default_args=default_args,
    dag_id="dag_with_python_dependencies_v02",
    start_date=datetime(2024, 12, 24),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_sklearn
    )
    
    task2 = PythonOperator(
        task_id='get_matplotlib',
        python_callable=get_matplotlib
    )

    task1 >> task2