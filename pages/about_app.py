import streamlit as st

st.set_page_config(
    page_title="🌱 AI Crop Disease Detection",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>

[data-testid="stSidebar"] {display:none;}
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp{
    background: linear-gradient(135deg,#e8f5e9,#f8fafc);
}

h1, h2, h3, h4, h5, h6 {
    color: #14532d !important;
}

[data-testid="stMarkdownContainer"] h3 {
    color: #14532d !important;
}

p {
    color: #374151 !important;
    font-size: 17px;
}

li {
    color: #374151 !important;
}

.stButton>button{
    background: linear-gradient(135deg,#166534,#22c55e);
    color: white;
    border-radius: 12px;
    height: 48px;
    font-weight: 600;
    border: none;
    transition: 0.25s;
}

.stButton>button:hover{
    transform: translateY(-2px);
    box-shadow:0 6px 20px rgba(0,0,0,0.15);
}

.card{
    background:white;
    padding:30px;
    border-radius:16px;
    box-shadow:0 8px 25px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)



st.markdown(
"""
<h1 style='text-align:center; color:#14532d;'>
🌱 About App
</h1>
""",
unsafe_allow_html=True
)


c1,c2,c3,c4,c5 = st.columns([2,1.5,2,1.5,2])

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



st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
### 🌱 Project Overview

**AI Crop Disease Detection System** is a deep learning–based application
designed to identify plant diseases using leaf images.

The system helps in:

• Early disease detection  
• Reducing crop loss  
• Supporting farmers with actionable insights  

The application is built using **PyTorch** and deployed with **Streamlit**.
""")

st.markdown("</div>", unsafe_allow_html=True)



st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
### 🧠 Machine Learning Model

The disease detection model is a **Custom Convolutional Neural Network (CNN)**.

**Model Highlights**

• Multiple convolutional layers for feature extraction  
• Batch normalization for stable training  
• Dropout layers to prevent overfitting  
• Fully connected classifier for final prediction  

The model was trained on labeled plant leaf images and saved using
PyTorch’s `state_dict()` for efficient loading.
""")

st.markdown("</div>", unsafe_allow_html=True)



st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
### 📊 Dataset Information

• Leaf images of healthy and diseased crops  
• Multiple disease categories per crop  
• Images resized to **224 × 224** for consistency  
• Dataset split into training and validation sets  

The dataset includes diseases such as:

• Apple Scab  
• Tomato Late Blight  
• Corn Rust  
• Potato Early Blight  
• And many more
""")

st.markdown("</div>", unsafe_allow_html=True)



st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
### 🛠 Technology Stack

• **Python**  
• **PyTorch** – model training & inference  
• **Torchvision** – image preprocessing  
• **Streamlit** – web interface  
• **PIL** – image handling  

This stack enables fast inference and a user-friendly interface.
""")

st.markdown("</div>", unsafe_allow_html=True)



st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
### ⚠ Limitations

• Predictions depend on image quality  
• Not a replacement for professional agricultural advice  
• Limited to diseases present in the training dataset  

Use this system as a **decision-support tool**, not a final diagnosis.
""")

st.markdown("</div>", unsafe_allow_html=True)



st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
### 🚀 Future Enhancements

🔥 Grad-CAM visual explanations  
📱 Mobile-friendly UI  
🌍 Multi-language support  
📈 Disease severity estimation  
☁ Cloud deployment for real-time access
""")

st.markdown("</div>", unsafe_allow_html=True)


st.info("🌾 This project is developed for educational and research purposes.")
