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

            title = row.get("opportunity title", "N/A")
duration = row.get("duration of internship", "N/A")
background = row.get("preferred academic background", "N/A")

st.subheader("Opportunity Details")
st.write(f"**Title:** {title}")
st.write(f"**Duration Type:** {duration}")
st.write("**Host LC:** M.A.H.E.")

st.subheader("Eligibility")
st.write(f"**Preferred Background:** {background}")
st.write("**Minimum Study Level:** Bachelor")

st.subheader("Logistics")

if duration.lower() == "mid term":
    stipend = 6500
else:
    stipend = 0

st.write(f"**Gross Salary:** INR {stipend} / month")

jd_text = f"""
# {title}

## Organization
M.A.H.E., Manipal, Karnataka, India

## Role Details
Duration Type: {duration}

## Eligibility
Preferred Background: {background}
Minimum Study Level: Bachelor

## Logistics
Stipend: INR {stipend} / month
"""

st.download_button(
    label="Download JD",
    data=jd_text,
    file_name="Job_Description.txt",
    mime="text/plain"
)
