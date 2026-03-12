import streamlit as st

st.set_page_config(
    page_title="🌾 AI Crop Disease Detection",
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
🌱 AI Crop Disease Detection System
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"""
<div class="subtitle" style="
text-align:center;
font-size:20px;
color:#374151;
font-weight:500;
margin-bottom:20px;
">
Detect plant diseases instantly using Artificial Intelligence
</div>
""",
unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)


c1, c2, c3, c4, c5 = st.columns([2,1.5,2,1.5,2])

with c2:
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")

with c3:
    if st.button("🌿 Prediction", use_container_width=True):
        st.switch_page("pages/prediction.py")

with c4:
    if st.button("ℹ️ About", use_container_width=True):
        st.switch_page("pages/about_app.py")


st.markdown("<hr>", unsafe_allow_html=True)


st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
### Welcome 👋

This application uses **Artificial Intelligence and Deep Learning** to help detect  
**crop diseases from leaf images quickly and accurately.**

Farmers, students, and researchers can upload an image of a crop leaf and instantly receive:

- 🧠 **Disease Prediction**
- 📊 **Confidence Score**
- 📋 **Disease Description**
- 💊 **Treatment & Prevention Tips**
""")

st.markdown("</div>", unsafe_allow_html=True)


st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
### 🚀 How to Use

1️⃣ Go to the **Prediction** page  
2️⃣ Upload a **clear crop leaf image**  
3️⃣ Wait a few seconds for **AI analysis**  
4️⃣ View the **disease result and treatment tips**
""")

st.markdown("</div>", unsafe_allow_html=True)


st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
### 🌾 Supported Crops

Apple • Blueberry • Cherry • Corn • Grape  
Orange • Peach • Pepper • Potato • Raspberry  
Soybean • Squash • Strawberry • Tomato
""")

st.markdown("</div>", unsafe_allow_html=True)


st.success("👉 Use the **Prediction** page to start detecting crop diseases.")

st.markdown("""
<div class="footer">
🎯 Goal: Support smart agriculture using AI to detect plant diseases early and reduce crop loss.
</div>
""", unsafe_allow_html=True)
