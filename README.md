# Production Time Series Forecasting System (PyCaret + MLOps)

Designed and implemented a production-ready time series forecasting pipeline covering the full ML lifecycle — from experimentation to deployment readiness.

# Contributions:

1- Built an end-to-end forecasting workflow using PyCaret with fair model benchmarking (ARIMA, ETS, Theta, baselines)

2- Converted research notebook into production pipelines (train.py, predict.py)

3- Implemented strict data validation checks to prevent silent failures

4- Added forecast error monitoring and drift detection logic

5- Integrated MLflow-ready experiment tracking and model versioning

6- Designed CI pipelines (GitHub Actions) to enforce data and code quality

7- Structured the repository following industry MLOps best practices

# Technologies:
Python, PyCaret, MLflow, Pandas, GitHub Actions, Time Series Forecasting

# Outcome:
A reproducible, auditable, and deployable forecasting baseline suitable for batch or API-based production systems.

# production structure:
.
├── notebooks/
│   └── PyCaret_timeseries.ipynb
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── evaluation.py
│   └── utils/
│       └── validation.py
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   ├── forecasts/
│   └── plots/
├── artifacts/
│   └── model/
├── .github/workflows/ci.yml
├── requirements.txt
└── README.md

# Project Files:
1- train.py — production training pipeline
2- predict.py — batch forecasting
3- validation.py - Data validation checks (critical)
4- evaluation.py - Forecast error monitoring (drift detection)
5- ci.yml - Forecasting CI: CI checks (GitHub Actions)
6- app.py - FastAPI inference service (online forecasting)
7- forecast_pipeline.py - Airflow DAG (scheduled retraining + forecasting)
8- drift_dashboard.py - Drift dashboards (forecast error monitoring) 
9- Dockerfile - Dockerization (full system)

# Final enterprise-grade architecture
        ┌──────────────┐
        │   Raw Data   │
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │ Airflow DAG  │
        │  (Retrain)   │
        └──────┬───────┘
               │
        ┌──────▼───────┐
        │   MLflow     │
        │ Model Store  │
        └──────┬───────┘
               │
     ┌─────────▼─────────┐
     │ FastAPI Inference │
     └─────────┬─────────┘
               │
     ┌─────────▼─────────┐
     │ Drift Dashboard   │
     │   (Evidently)     │
     └───────────────────┘
