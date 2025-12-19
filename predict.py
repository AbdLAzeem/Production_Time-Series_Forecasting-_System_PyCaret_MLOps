# src/predict.py

import pandas as pd
from pycaret.time_series import load_model, predict_model
from utils.validation import validate_timeseries

MODEL_PATH = "artifacts/model/forecast_model"
DATA_PATH = "data/processed/timeseries.csv"
OUTPUT_PATH = "outputs/forecasts/forecast.csv"

def predict():
    df = pd.read_csv(DATA_PATH, parse_dates=["date"], index_col="date")
    validate_timeseries(df)

    model = load_model(MODEL_PATH)
    forecast = predict_model(model, fh=12)

    forecast.to_csv(OUTPUT_PATH)

if __name__ == "__main__":
    predict()
