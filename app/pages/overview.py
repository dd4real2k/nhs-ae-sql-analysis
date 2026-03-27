import os
import pandas as pd
import streamlit as st
import plotly.express as px

processed_folder = os.path.join("..", "data", "processed")
input_file = os.path.join(processed_folder, "nhs_ae_model_ready_with_features.csv")

df = pd.read_csv(input_file)
df["period"] = pd.to_datetime(df["period"])

monthly = (
    df.groupby("period", as_index=False)["total_attendances"]
    .sum()
)

st.title("Overview")

fig = px.line(
    monthly,
    x="period",
    y="total_attendances",
    title="Monthly NHS A&E Attendances"
)
st.plotly_chart(fig, use_container_width=True)
