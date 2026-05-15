# Production Time Series Forecasting System (PyCaret + MLOps)

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/ML%20Framework-PyCaret-red.svg)](https://pycaret.org/)
[![MLOps](https://img.shields.io/badge/MLops-MLflow-blueviolet.svg)](https://mlflow.org/)
[![API](https://img.shields.io/badge/Inference-FastAPI-009688.svg)](https://fastapi.tiangolo.com/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF.svg)](https://github.com/features/actions)

A production-ready, end-to-end time series forecasting pipeline covering the entire machine learning lifecycle—from automated model experimentation to orchestration, deployment, and live monitoring. 

This system bridges the gap between research notebooks and enterprise-grade deployment, providing a reproducible, auditable, and robust baseline suitable for batch or API-based production systems.

---

## 🚀 Key Features & Contributions

*   **Automated & Fair Benchmarking:** Built an end-to-end forecasting workflow leveraging **PyCaret** to systematically evaluate classical and statistical baselines (**ARIMA, ETS, Theta**) alongside machine learning models.
*   **Productionization:** Converted experimental research notebooks into modular, clean, and maintainable production scripts (`train.py`, `predict.py`).
*   **Defensive Engineering:** Implemented strict data validation checks within the ingestion layer to intercept schema anomalies and prevent silent pipeline failures.
*   **Drift & Error Monitoring:** Integrated continuous forecast error tracking and data drift detection logic to flag performance degradation over time.
*   **Experiment & Model Lineage:** Integrated **MLflow** for unified experiment tracking, parameter logging, and strict model version control.
*   **Continuous Integration:** Designed **GitHub Actions** CI pipelines to programmatically enforce data quality, code styling, and unit test compliance.
*   **Standardized MLOps Architecture:** Structured the repository following industry-best layout design practices for clear separation of concerns.

---

## 📐 Enterprise Architecture

The data pipeline flows seamlessly from automated retraining to live inference serving and data validation monitoring:

```text
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
