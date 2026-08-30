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

dgs2 = load_fred_series("DGS2")
dgs10 = load_fred_series("DGS10")
dgs30 = load_fred_series("DGS30")

treasury = (
    dgs2
    .merge(dgs10, on="date", how="outer")
    .merge(dgs30, on="date", how="outer")
    .sort_values("date")
)

st.header("1. US Treasury Yields")

st.markdown("""
Treasury yields represent the market's required return for lending to the US government across different maturities.

Comparing short-, medium-, and long-term yields helps distinguish changes in near-term monetary policy expectations from changes in longer-term inflation, growth, and risk expectations.
""")

chart_data = treasury.set_index("date")[["DGS2", "DGS10", "DGS30"]].rename(
    columns={
        "DGS2": "2-Year",
        "DGS10": "10-Year",
        "DGS30": "30-Year"
    }
)


st.line_chart(
    chart_data,
    y_label="Yield (%)",
    x_label="Date"
)
with st.expander("View underlying data"):
    st.dataframe(
        chart_data.sort_index(ascending=False),
        use_container_width=True
    )
