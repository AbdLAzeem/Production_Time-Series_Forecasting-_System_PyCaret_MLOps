from fastapi import FastAPI
import pandas as pd
from pycaret.time_series import load_model, predict_model

MODEL_PATH = "artifacts/model/forecast_model"

app = FastAPI(
    title="Time Series Forecasting API",
    description="Production-ready forecasting service",
    version="1.0"
)

model = load_model(MODEL_PATH)

@app.post("/forecast")
def forecast(horizon: int = 12):
    """
    Generate forecasts for the next `horizon` periods
    """
    preds = predict_model(model, fh=horizon)
    preds = preds.reset_index().to_dict(orient="records")
    return {"forecast": preds}
