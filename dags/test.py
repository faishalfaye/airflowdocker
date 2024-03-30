from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 3, 30),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate the DAG object
dag = DAG(
    'a_test_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval='@daily',
)

# Define tasks
start_task = DummyOperator(task_id='start_task', dag=dag)

def first_python_function():
    print("Executing the first Python function")

def second_python_function():
    print("Executing the second Python function")

# Define PythonOperator tasks
first_python_task = PythonOperator(
    task_id='first_python_task',
    python_callable=first_python_function,
    dag=dag,
)

second_python_task = PythonOperator(
    task_id='second_python_task',
    python_callable=second_python_function,
    dag=dag,
)

end_task = DummyOperator(task_id='end_task', dag=dag)

# Define task dependencies
start_task >> first_python_task >> second_python_task >> end_task

