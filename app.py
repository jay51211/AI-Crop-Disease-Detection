import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="🌱  AI Crop Disease Detection",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    [data-testid="stSidebar"] {
        display: none;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>

html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background: linear-gradient(135deg, #e8f5e9, #ffffff);
}

.stButton>button {
    background-color: #1f2937;
    color: white;
    font-weight: 600;
    border-radius: 8px;
    height: 45px;
}

.stButton>button:hover {
    background-color: #1b5e20;
    color: white;
}

</style>
""", unsafe_allow_html=True)

st.title("🌱 AI Crop Disease Detection System")
st.write("""
Welcome to the AI-based crop disease detection app.

""")

st.markdown("---")

c1, c2, c3, c4, c5 = st.columns([2, 1.5, 2, 1.5, 2])

with c2:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

with c3:
    if st.button("🌿 Prediction", use_container_width=True):
        st.switch_page("pages/prediction.py")

with c4:
    if st.button("ℹ️ About", use_container_width=True):
        st.switch_page("pages/about_app.py")

st.markdown("---")

st.markdown("""
### Welcome 👋  

This application uses **Artificial Intelligence and Deep Learning** to help detect  
**crop diseases from leaf images** quickly and accurately.

Farmers, students, and researchers can upload an image of a crop leaf and instantly
get:
- 🧠 Disease prediction  
- 📊 Confidence score  
- 📋 Disease description  
- 💊 Treatment and prevention tips  

---
""")

st.markdown("""
### 🚀 How to Use the App
1. Go to the **Prediction** page  
2. Upload a clear image of a crop leaf  
3. Wait a few seconds for AI analysis  
4. View disease details and recommendations  

---
""")

st.markdown("""
### 🌾 Supported Crops
- Apple
- Blueberry
- Cherry
- Corn
- Grape
- Orange
- Peach
- Pepper
- Potato
- Raspberry
- Soybean
- Squash
- Strawberry
- Tomato

---
""")

st.success("👉 Use the **Prediction** page from the navigation menu to get started!")

st.markdown("""
### 🎯 Project Goal
To support **smart agriculture** by providing an easy-to-use AI tool
that helps identify plant diseases early and reduce crop losses.
""")