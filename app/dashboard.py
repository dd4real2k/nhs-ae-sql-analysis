import streamlit as st

st.set_page_config(
    page_title="NHS A&E Forecast Dashboard",
    page_icon="🏥",
    layout="wide"
)

st.title("NHS A&E Performance Analysis and Demand Forecasting")
st.markdown(
    """
    This app explores NHS A&E demand trends, waiting-time pressure,
    forecasting outputs, and model comparison results.
    """
)
