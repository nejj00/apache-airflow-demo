from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    'owner': 'coder2j',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_catchup_backfill_v02',
    default_args=default_args,
    start_date=datetime(2023, 12, 24),
    schedule_interval='@daily',
    catchup=False
) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo This is a simple bash command!'
    )


# 1. Get docker images - docker ps
# 2. Get into terminal for the airflow scheduler - docker exec -it 3e20085533dd bash (change the image ID)
# 3. Execute backfill command with start and end date: (didn't really work in my case) 
#   airflow dags backfill -s 2023-11-01 -e 2023-11-08 dag_with_catchup_backfill_v02