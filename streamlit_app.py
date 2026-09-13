import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Minapur Worker Search",
    page_icon="🔍",
    layout="wide"
)

# Load Minapur.csv from the same folder as this Streamlit app
csv_path = Path(__file__).parent / "Minapur.csv"

try:
    df = pd.read_csv(csv_path)
except FileNotFoundError:
    st.error(f"Minapur.csv not found at: {csv_path}")
    st.stop()

st.title("🔍 Minapur Worker Search")
st.caption(f"Total workers: {len(df):,}")

search_col = st.selectbox("Search by:", df.columns)
search_val = st.text_input("Enter value to search:")

if search_val.strip():
    results = df[
        df[search_col].astype(str).str.contains(
            search_val.strip(), case=False, na=False
        )
    ]

    st.write(f"Found **{len(results):,}** result(s):")
    st.dataframe(results, use_container_width=True, hide_index=True)
else:
    st.dataframe(df, use_container_width=True, hide_index=True)
