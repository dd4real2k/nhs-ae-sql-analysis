import os
import pandas as pd
import streamlit as st
import plotly.express as px

processed_folder = os.path.join("..", "data", "processed")
comparison_file = os.path.join(processed_folder, "model_comparison.csv")

df = pd.read_csv(comparison_file)

st.title("Model Comparison")
st.dataframe(df, use_container_width=True)

fig = px.bar(df, x="model", y="RMSE", title="Model Comparison by RMSE")
st.plotly_chart(fig, use_container_width=True)

fig2 = px.bar(df, x="model", y="MAE", title="Model Comparison by MAE")
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.bar(df, x="model", y="R2", title="Model Comparison by R²")
st.plotly_chart(fig3, use_container_width=True)
