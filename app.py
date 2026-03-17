import streamlit as st

st.set_page_config(page_title="AIESEC EXPA Helper", layout="centered")

st.title("AIESEC EXPA Helper – IGTa")

st.markdown("### Select Operation")

col1, col2 = st.columns(2)

with col1:
    if st.button("Data Entry"):
        st.switch_page("pages/1_Data_Entry.py")

with col2:
    if st.button("Data Verification"):
        st.switch_page("pages/2_Data_Verification.py")
