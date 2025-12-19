# src/train.py

import os
import pandas as pd
import mlflow
import mlflow.sklearn
from pycaret.time_series import setup, compare_models, save_model, pull
from utils.validation import validate_timeseries

DATA_PATH = "data/processed/timeseries.csv"
MODEL_DIR = "artifacts/model"
os.makedirs(MODEL_DIR, exist_ok=True)

def train():
    df = pd.read_csv(DATA_PATH, parse_dates=["date"], index_col="date")
    validate_timeseries(df)

    setup(
        data=df,
        target=df.columns[0],
        session_id=42,
        fold=3,
        fh=12,
        numeric_imputation_target="interpolate",
        verbose=False
    )

    best_model = compare_models()

    metrics = pull().iloc[0]

    with mlflow.start_run(run_name="timeseries_training"):
        mlflow.log_metrics({
            "RMSE": metrics["RMSE"],
            "MAE": metrics["MAE"],
            "MAPE": metrics.get("MAPE", None)
        })

        mlflow.log_param("model_type", type(best_model).__name__)
        save_model(best_model, f"{MODEL_DIR}/forecast_model")
        mlflow.sklearn.log_model(best_model, artifact_path="model")

if __name__ == "__main__":
    train()
