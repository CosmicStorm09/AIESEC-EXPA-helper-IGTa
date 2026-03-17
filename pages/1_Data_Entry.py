import streamlit as st
import pandas as pd

st.title("Data Entry Tool")

uploaded_file = st.file_uploader(
    "Upload Internship Master CSV",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip().str.lower()

    sheet_row = st.number_input(
        "Enter Sheet Row Number",
        min_value=2,
        step=1
    )

    if st.button("Load Opportunity"):

        df_index = sheet_row - 2

        if df_index < 0 or df_index >= len(df):
            st.error("Invalid row number")

        else:
            row = df.iloc[df_index]

            title = row.get("opportunity title", "N/A")
            duration = row.get("duration of internship", "N/A")

            st.subheader("Preview")

            st.write(f"**Opportunity Title:** {title}")
            st.write(f"**Duration:** {duration}")
