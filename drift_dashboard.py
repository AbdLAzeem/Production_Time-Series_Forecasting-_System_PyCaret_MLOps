'''
src/monitoring/drift_dashboard.py
Drift dashboards (forecast error monitoring)

This uses Evidently (industry standard).
✔ Visual drift detection
✔ Stakeholder-friendly
✔ Production-grade monitoring

This dashboard answers:
Are errors increasing?
Is bias creeping in?
Is retraining required?

********************** Output ***********************
run bash:
outputs/monitoring/drift_report.html
'''

import pandas as pd
from evidently.report import Report
from evidently.metric_preset import RegressionPreset

def generate_drift_report(actual_path, forecast_path):
    actual = pd.read_csv(actual_path)
    forecast = pd.read_csv(forecast_path)

    report = Report(metrics=[RegressionPreset()])
    report.run(
        reference_data=actual,
        current_data=forecast
    )

    report.save_html("outputs/monitoring/drift_report.html")
