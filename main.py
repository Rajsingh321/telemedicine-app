import streamlit as st

st.set_page_config(page_title="eSwasthya", page_icon=":hospital:", layout="wide")

col1, col2, col3 = st.columns(3)

with col2:
    st.title("eSwasthya")
    st.write("Your Health, Our Priority")
    st.video("drvideo1.mp4", format="video/mp4", start_time=0)
    st.video("drvideo2.mp4", format="video/mp4", start_time=0)
    st.video("drvideo3.mp4", format="video/mp4", start_time=0)





