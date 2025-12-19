# Airflow DAG (scheduled retraining + forecasting)
# airflow/dags/forecast_pipeline.py
"""
✔ Weekly retraining
✔ Clear dependency chain
✔ Easy to extend (monitoring, alerts)
"""
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "mlops",
    "start_date": datetime(2024, 1, 1),
    "retries": 1
}

with DAG(
    dag_id="timeseries_forecasting_pipeline",
    schedule_interval="@weekly",
    default_args=default_args,
    catchup=False
) as dag:

    train = BashOperator(
        task_id="train_model",
        bash_command="python src/train.py"
    )

    predict = BashOperator(
        task_id="batch_forecast",
        bash_command="python src/predict.py"
    )

    train >> predict
