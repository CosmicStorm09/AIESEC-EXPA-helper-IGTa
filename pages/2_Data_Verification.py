import streamlit as st
import pandas as pd

st.title("Data Verification Tool")

uploaded_file = st.file_uploader(
    "Upload Verification Dataset",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")

    st.dataframe(df)

    st.write("Add verification checks here")
