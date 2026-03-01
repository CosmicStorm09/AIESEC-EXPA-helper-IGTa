import streamlit as st
import pandas as pd

st.title("AIESEC EXPA Helper – IGTa")

uploaded_file = st.file_uploader("Upload Internship Master CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = df.columns.str.strip().str.lower()

    st.success("CSV uploaded successfully ✅")

    row_number = st.number_input(
        "Enter Sheet Row Number",
        min_value=2,
        step=1
    )

    if st.button("Load Opportunity"):
        df_index = int(row_number) - 2

        if df_index < 0 or df_index >= len(df):
            st.error("Invalid row number ❌")
        else:
            row = df.iloc[df_index]

            st.subheader("Preview")
            st.write("**Opportunity Title:**", row.get("opportunity title", "N/A"))
            st.write("**Duration:**", row.get("duration of internship", "N/A"))
            st.write("**Preferred Background:**", row.get("preferred academic background", "N/A"))
