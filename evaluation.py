
# ✔ Can be triggered daily
# ✔ Integrates with alerts (Slack, email)
# ✔ Retraining hook ready

# src/evaluation.py

import pandas as pd
from sklearn.metrics import mean_absolute_error

ERROR_THRESHOLD = 1.5  # business-defined

def monitor(actual: pd.Series, forecast: pd.Series):
    mae = mean_absolute_error(actual, forecast)

    if mae > ERROR_THRESHOLD:
        raise RuntimeError(
            f"Forecast drift detected! MAE={mae:.2f} exceeds threshold."
        )

    return mae
