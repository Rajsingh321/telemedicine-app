import streamlit as st
from PIL import Image
import pandas as pd
#import plotly.express as px
import warnings
warnings.filterwarnings("ignore")

# --- Header ---
st.set_page_config(page_title="Punjab Health Dashboard", layout="wide")
st.image("logo.png", width=200)  # अपना लोगो यहाँ डालें
st.title("Punjab Health Department Dashboard")
st.markdown("सार्वजनिक स्वास्थ्य की रिपोर्ट और अलर्ट्स का विज़ुअलाइजेशन")

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Alerts", "Reports"])

# --- Sample Data ---
# सैंपल डेटा के लिए
data = {
    'District': ['Amritsar', 'Ludhiana', 'Patiala', 'Jalandhar', 'Bathinda'],
    'Cases': [120, 90, 150, 80, 60],
    'Medicine Shortage': [5, 2, 8, 3, 1]
}
df = pd.DataFrame(data)

# --- Dashboard Page ---
if page == "Dashboard":
    st.image("dash1.png")
    #st.subheader("Disease Cases by District")
    #fig_cases = px.bar(df, x='District', y='Cases', color='Cases', title="Cases Distribution")
    #st.plotly_chart(fig_cases, use_container_width=True)
    
    #st.subheader("Medicine Shortage by District")
    #fig_meds = px.bar(df, x='District', y='Medicine Shortage', color='Medicine Shortage',
                      #title="Medicine Shortage")
    #st.plotly_chart(fig_meds, use_container_width=True)
    st.image("dash2.png")
    # Sample Map
    st.subheader("Affected Areas Map (Sample)")
    map_data = pd.DataFrame({
        'lat': [31.6340, 30.9010, 30.3398, 31.3260, 30.2110],
        'lon': [74.8723, 75.8573, 76.3869, 75.5762, 74.9450],
        'Cases': [120, 90, 150, 80, 60]
    })
    st.map(map_data)

# --- Alerts Page ---
elif page == "Alerts":
    st.subheader("Current Alerts")
    st.warning("Amritsar: Medicine X running low")
    st.warning("Patiala: High number of fever cases reported")
    st.info("Bathinda: Normal status")

# --- Reports Page ---
elif page == "Reports":
    st.subheader("Sample Reports")
    st.markdown("यहां आप जनरल रिपोर्ट और चार्ट्स देख सकते हैं")
    
    # सैंपल रिपोर्ट images
    st.image("dashboard_sample1.png")
    st.image("dashboard_sample2.png")

st.sidebar.markdown("---")
st.sidebar.write("© 2025 Punjab Health Department")




