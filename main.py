import streamlit as st

st.set_page_config(page_title="eSwasthya", page_icon=":hospital:", layout="wide")

col1, col2, col3 = st.columns(3)

with col2:
    st.markdown("Welcome to eSwasthya")
    st.write("Your Health, Our Priority")

st.write("it's working")


