import streamlit as st
import pandas as pd

# Load the data
df = pd.read_csv("Minapur.csv")

st.title("🔍 Minapur Worker Search")

# Search options
search_col = st.selectbox("Search by:", df.columns)
search_val = st.text_input("Enter value to search:")

if search_val:
    results = df[df[search_col].astype(str).str.contains(search_val, case=False, na=False)]
    st.write(f"Found {len(results)} result(s):")
    st.dataframe(results)
else:
    st.dataframe(df)
