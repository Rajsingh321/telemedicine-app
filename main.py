import streamlit as st
import streamlit.components.v1 as components
import random


st.set_page_config(page_title="eSwasthya", page_icon=":hospital:", layout="wide")

col1, col2, col3 = st.columns(3)

with col2:
    st.markdown("<h1 style='text-align: center;font-size: 60px;'>eSwasthya</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;font-size: 20px;'>Your Health, Our Priority</h1>", unsafe_allow_html=True)
    st.sidebar.title("👤 User Profile")
    st.sidebar.write("Name = Ramsingh")
    st.sidebar.write("Mobile no. = +918085134393")

    with st.expander("👨‍⚕️ Connect to Doctor", expanded=False):
    
            if st.button("📹 Video Call"):
                patient_number = "+919876543210"
                doctors = {
                "Dr. Singh (101)": "101",
                "Dr. Sharma (102)": "102",
                "Dr. Kumari (103)": "103",
                 }

                doctor_selection = "Dr. Singh"
                room_name = f"eSwasthya_{patient_number}_{doctor_selection}_{random.randint(1000,9999)}"
                jitsi_url = f"https://meet.jit.si/{room_name}"
        
                st.success(f"Connecting to {doctor_selection}...")
                components.iframe(jitsi_url, height=600, width=800)
        
            if st.button("📞 Voice Call"):
                doctor_number = "+917415505769"
                call_button = f"""
    <a href="tel:{doctor_number}">
        <button style="
            background-color:#4CAF50;
            color:white;
            padding:15px 32px;
            font-size:16px;
            border:none;
            border-radius:8px;
            cursor:pointer;
        ">
        Call to Doctor
        </button>
    </a>
                """
                st.markdown(call_button, unsafe_allow_html=True)

            
    st.write("fever prescription")
    st.video("drvideo3.mp4")
    st.write("headache prescription")
    st.video("drvideo1.mp4")
    st.markdown(
    """
    <style>
    .mic-container {
        position: fixed;
        bottom: 30px;
        left: 50%;
        transform: translateX(-50%);
        text-align: center;
    }
    .mic-button {
        font-size: 20px;
        padding: 15px 20px;
        border-radius: 20%;
        background-color: #4CAF50;
        color: white;
        border: 2px solid #4CAF50;
        cursor: pointer;
     }
     </style>

     <div class="mic-container">
        <button class="mic-button">🎙</button>
     </div>
     """,
     unsafe_allow_html=True
    )

    











