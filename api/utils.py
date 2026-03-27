import os
import joblib
import pandas as pd


MODEL_PATH = os.path.join("models", "random_forest_model.joblib")

FEATURES = [
    "year",
    "month",
    "quarter",
    "month_sin",
    "month_cos",
    "lag_1",
    "lag_3",
    "lag_6",
    "lag_12",
    "rolling_mean_3",
    "rolling_mean_6",
    "rolling_std_3",
    "total_over_4hrs",
    "total_emergency_admissions",
    "total_booked_attendances",
    "total_dta_waits",
]


def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}")
    return joblib.load(MODEL_PATH)


def prepare_input(data: dict) -> pd.DataFrame:
    df = pd.DataFrame([data])
    return df[FEATURES]
