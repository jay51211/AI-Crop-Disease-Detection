import streamlit as st

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

st.title("📘 About This Project")

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
## 🌱 Project Overview

**AI Crop Disease Detection System** is a deep learning–based application
designed to identify plant diseases using leaf images.

The system helps in:
- Early disease detection  
- Reducing crop loss  
- Supporting farmers with actionable insights  

The application is built using **PyTorch** and deployed with **Streamlit**.
""")

st.markdown("""
---
## 🧠 Machine Learning Model

The disease detection model is a **Custom Convolutional Neural Network (SimpleCNN)**.

### Model Highlights:
- Multiple convolutional layers for feature extraction  
- Batch normalization for stable training  
- Dropout layers to prevent overfitting  
- Fully connected classifier for final prediction  

The model was trained on labeled plant leaf images and saved using
PyTorch’s `state_dict()` for efficient loading.
""")

st.markdown("""
---
## 📊 Dataset Information

- Leaf images of healthy and diseased crops  
- Multiple disease categories per crop  
- Images resized to **224 × 224** for consistency  
- Dataset split into training and validation sets  

The dataset includes diseases such as:
- Apple Scab  
- Tomato Late Blight  
- Corn Rust  
- Potato Early Blight  
- And many more
""")

st.markdown("""
---
## 🛠️ Technology Stack

- **Python**
- **PyTorch** – model training & inference  
- **Torchvision** – image preprocessing  
- **Streamlit** – web application interface  
- **PIL** – image handling  

This combination allows fast inference and an easy-to-use UI.
""")

st.markdown("""
---
## ⚠️ Limitations

- Predictions depend on image quality  
- Not a replacement for professional agricultural advice  
- Limited to diseases present in the training dataset  

Users should use this tool as a **decision-support system**, not a final diagnosis.
""")

st.markdown("""
---
## 🚀 Future Enhancements

- 🔥 Grad-CAM visual explanations  
- 📱 Mobile-friendly UI  
- 🌍 Multi-language support  
- 📈 Disease severity estimation  
- ☁️ Cloud deployment for real-time access  
""")

st.info("This project is developed for educational and research purposes 🌾")
