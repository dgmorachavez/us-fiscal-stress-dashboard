import streamlit as st
import pandas as pd
import requests
from io import StringIO

st.set_page_config(
    page_title="US Fiscal Stress Dashboard",
    layout="wide"
)

st.title("US Fiscal Stress Dashboard")
st.markdown("""
The topic of US public debt and rising Treasury yields has increasingly moved to the forefront of economic and financial debate.

US Treasury yields have risen considerably from the exceptionally low levels that characterized much of the post-Global Financial Crisis period. This raises an important question: **what is driving the increase in long-term borrowing costs?**

This dashboard examines several possible explanations, including inflation expectations, real interest rates, the term premium, Treasury supply, fiscal conditions, and monetary policy.
""")
@st.cache_data(ttl=3600)
def load_fred_series(series_id):
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"

    response = requests.get(url, timeout=20)
    response.raise_for_status()

    df = pd.read_csv(StringIO(response.text))
    df.columns = ["date", series_id]

    df["date"] = pd.to_datetime(df["date"])
    df[series_id] = pd.to_numeric(df[series_id], errors="coerce")

    return df.dropna()

dgs30 = load_fred_series("DGS30")

st.subheader("30-Year Treasury Yield")
st.dataframe(dgs30.tail(10))