# src/utils/validation.py

import pandas as pd

def validate_timeseries(df: pd.DataFrame):
    if not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("Index must be a DatetimeIndex")

    if df.isnull().sum().sum() > 0:
        raise ValueError("Missing values detected in time series")

    if df.index.is_monotonic_increasing is False:
        raise ValueError("Datetime index must be sorted")

    if df.shape[0] < 30:
        raise ValueError("Insufficient data points for forecasting")
