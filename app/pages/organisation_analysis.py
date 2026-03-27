import os
import pandas as pd
import streamlit as st
import plotly.express as px

processed_folder = os.path.join("..", "data", "processed")
input_file = os.path.join(processed_folder, "nhs_ae_model_ready_with_features.csv")

df = pd.read_csv(input_file)
df["period"] = pd.to_datetime(df["period"])

st.title("Organisation Analysis")

orgs = sorted(df["org_name"].dropna().unique())
selected_org = st.selectbox("Select organisation", orgs)

org_df = df[df["org_name"] == selected_org].copy()

fig = px.line(
    org_df,
    x="period",
    y="total_attendances",
    title=f"Total Attendances - {selected_org}"
)
st.plotly_chart(fig, use_container_width=True)

fig2 = px.line(
    org_df,
    x="period",
    y="total_over_4hrs",
    title=f"Over 4-Hour Waits - {selected_org}"
)
st.plotly_chart(fig2, use_container_width=True)
