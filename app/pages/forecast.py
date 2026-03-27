import os
import pandas as pd
import streamlit as st
import requests

processed_folder = os.path.join("..", "data", "processed")
input_file = os.path.join(processed_folder, "nhs_ae_model_ready_with_features.csv")

df = pd.read_csv(input_file)
df["period"] = pd.to_datetime(df["period"])

st.title("Forecast")

orgs = sorted(df["org_name"].dropna().unique())
selected_org = st.selectbox("Select organisation", orgs)

org_df = df[df["org_name"] == selected_org].sort_values("period").copy()

latest = org_df.iloc[-1]

payload = {
    "year": int(latest["year"]),
    "month": int(latest["month"]),
    "quarter": int(latest["quarter"]),
    "month_sin": float(latest["month_sin"]),
    "month_cos": float(latest["month_cos"]),
    "lag_1": float(latest["lag_1"]),
    "lag_3": float(latest["lag_3"]),
    "lag_6": float(latest["lag_6"]),
    "lag_12": float(latest["lag_12"]),
    "rolling_mean_3": float(latest["rolling_mean_3"]),
    "rolling_mean_6": float(latest["rolling_mean_6"]),
    "rolling_std_3": float(latest["rolling_std_3"]),
    "total_over_4hrs": float(latest["total_over_4hrs"]),
    "total_emergency_admissions": float(latest["total_emergency_admissions"]),
    "total_booked_attendances": float(latest["total_booked_attendances"]),
    "total_dta_waits": float(latest["total_dta_waits"]),
}

if st.button("Generate Forecast"):
    response = requests.post("http://127.0.0.1:8000/predict", json=payload, timeout=30)
    if response.status_code == 200:
        result = response.json()
        st.metric("Predicted Attendance", f"{result['predicted_attendance']:,.0f}")
    else:
        st.error("Failed to get prediction from API.")
