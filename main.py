import streamlit as st

st.set_page_config(page_title="eSwasthya", page_icon=":hospital:", layout="wide")

col1, col2, col3 = st.columns(3)

with col2:
    st.title("Welcome to eSwasthya")
    st.header("Your Health, Our Priority")
