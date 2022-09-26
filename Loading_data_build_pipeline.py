from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta, datetime
import pandas as pd


# For PythonOperator

def convert_date_format():
    retail = pd.read_csv("gs://online_retail_for_study/cleaned_online_retail.csv")
    retail['InvoiceDate'] = pd.to_datetime(retail['InvoiceDate']).dt.date
    retail.to_csv("gs://online_retail_for_study/online_retail.csv", index=False)
    

# Default Args

default_args = {
    'owner': 'Chutdanai',
    'depends_on_past': False,
    'start_date': datetime(2015, 12, 1),
    'email': ['chutdanai.thongsom@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '@once',
}

# Create DAG

dag = DAG(
    'online_retail2',
    default_args=default_args,
    description='Pipeline for ETL online_retail data',
    schedule_interval=None,
)

# Tasks

# change the date format
t1 = PythonOperator(
    task_id='convert_format',
    python_callable=convert_date_format,
    dag=dag,
)

# move cloud storage file to airflow/data
t2 = BashOperator(
    task_id="move_file_to_data_directory",
    bash_command="gsutil cp gs://online_retail_for_study/online_retail.csv \
                  gs://asia-southeast1-onlineretai-8e267622-bucket/data/",
    dag=dag
)

# load date to Bigquert
t3 = BashOperator(
    task_id="move_to_bigquery",
    bash_command="bq load --source_format=CSV --autodetect \
                  --time_partitioning_field=InvoiceTimestamp \
                  online_retail_pipeline.online_retail_data \
                  gs://asia-southeast1-onlineretai-8e267622-bucket/data/online_retail.csv",
    dag=dag
)

# Dependencies

t1 >> t2 >> t3
