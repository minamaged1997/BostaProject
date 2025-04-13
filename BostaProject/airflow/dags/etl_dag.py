from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
# from airflow.providers.smtp.hooks.smtp import send_email


def send_failure_email(context):
    subject = f"Airflow Task Failed: {context['task_instance'].task_id}"
    body = f"Task failed for DAG {context['dag'].dag_id} at {context['ts']}. Error: {context['exception']}"
    send_email(
        to='your-email@example.com',
        subject=subject,
        html_content=body
    )

with DAG("json_to_pg_etl",
        default_args={
            'email_on_failure': True,
            'on_failure_callback': send_failure_email },
        start_date=datetime(2024, 1, 1),
        schedule_interval='00 9 * * *',  # Run daily at 9:30 AM
        catchup=False) as dag:
    run_etl = BashOperator(
        task_id="run_etl_script",
        bash_command="docker exec python_etl_container python /app/etl.py"
    )
