.
├── .github/workflows/
│   └── ci.yml               # GitHub Actions continuous integration pipeline
├── notebooks/
│   └── PyCaret_timeseries.ipynb # Experimental research & exploration notebook
├── src/
│   ├── train.py             # Production model training pipeline
│   ├── predict.py           # Batch forecasting engine
│   ├── evaluation.py        # Error tracking & drift detection logic
│   ├── app.py               # FastAPI online inference service
│   ├── drift_dashboard.py   # Evidently-powered dashboard module
│   └── utils/
│       └── validation.py    # Critical incoming data validation checks
├── dags/
│   └── forecast_pipeline.py # Airflow DAG for orchestration & scheduling
├── data/
│   ├── raw/                 # Immutable source data files
│   └── processed/           # Cleaned and engineered features
├── outputs/
│   ├── forecasts/           # Generated batch inference outputs
│   └── plots/               # Evaluation & tracking visuals
├── artifacts/
│   └── model/               # Locally serialized model binaries
├── Dockerfile               # System containerization configurations
├── requirements.txt         # Project dependencies
└── README.md
