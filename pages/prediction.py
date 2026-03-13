import streamlit as st
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import transforms
from PIL import Image
from pages.disease import generate_disease_report

st.set_page_config(
    page_title="🌱 AI Crop Disease Detection",
    layout="centered",
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
    background: linear-gradient(135deg,#e8f5e9,#ffffff);
}

.block-container{
    max-width:1100px;
    padding-top:2rem;
}

h1{
    color:#14532d !important;
    font-weight:700 !important;
    text-align:center;
}

h2, h3{
    color:#14532d !important;
    font-weight:600 !important;
}

p{
    color:#374151 !important;
    font-size:17px;
    line-height:1.6;
}

li{
    color:#374151 !important;
    font-size:16px;
}

.subtitle{
    text-align:center;
    font-size:20px;
    color:#374151 !important;
    font-weight:500;
    margin-bottom:20px;
}

.stButton>button{
    background: linear-gradient(135deg,#166534,#22c55e);
    color:white;
    border-radius:10px;
    height:48px;
    font-weight:600;
    border:none;
    transition:0.25s;
}

.stButton>button:hover{
    transform:translateY(-2px);
    box-shadow:0 6px 20px rgba(0,0,0,0.15);
}

.card{
    background:white;
    padding:30px;
    border-radius:16px;
    box-shadow:0 8px 25px rgba(0,0,0,0.08);
    margin-top:20px;
}

hr{
    border:none;
    height:1px;
    background:#e5e7eb;
    margin:30px 0;
}

[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3{
    color:#14532d !important;
}

</style>
""", unsafe_allow_html=True)

st.title("🌿 Crop Disease Prediction")
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



CLASS_NAMES = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 
               'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 
               'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot','Corn_(maize)___Common_rust_', 
               'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy','Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 
               'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)','Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 
               'Peach___Bacterial_spot','Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
               'Potato___Early_blight','Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 
               'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
               'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 
               'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus',
               'Tomato___Tomato_mosaic_virus','Tomato___healthy']



def ConvBlock(in_channels, out_channels, pool=False):
    layers = [
        nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1),
        nn.BatchNorm2d(out_channels),
        nn.ReLU(inplace=True)
    ]
    if pool:
        layers.append(nn.MaxPool2d(4))
    return nn.Sequential(*layers)


class CNN_NeuralNet(nn.Module):
    def __init__(self, in_channels, num_diseases):
        super().__init__()

        self.conv1 = ConvBlock(in_channels, 64)
        self.conv2 = ConvBlock(64, 128, pool=True)
        self.res1 = nn.Sequential(
            ConvBlock(128, 128),
            ConvBlock(128, 128)
        )

        self.conv3 = ConvBlock(128, 256, pool=True)
        self.conv4 = ConvBlock(256, 512, pool=True)

        self.res2 = nn.Sequential(
            ConvBlock(512, 512),
            ConvBlock(512, 512)
        )

        self.classifier = nn.Sequential(
            nn.MaxPool2d(4),
            nn.Flatten(),
            nn.Linear(512, num_diseases)
        )

    def forward(self, x):
        out = self.conv1(x)
        out = self.conv2(out)
        out = self.res1(out) + out
        out = self.conv3(out)
        out = self.conv4(out)
        out = self.res2(out) + out
        out = self.classifier(out)
        return out



@st.cache_resource
def load_model():
    model = CNN_NeuralNet(3, len(CLASS_NAMES))
    state_dict = torch.load("models/plant_disease_model.pth", map_location="cpu")
    model.load_state_dict(state_dict)
    model.eval()
    return model

model = load_model()



transform = transforms.Compose([
    transforms.Resize((256, 256)),  
    transforms.ToTensor()
])



uploaded_file = st.file_uploader("📤 Upload a leaf image", type=["jpg", "jpeg", "png"])
predict = st.button("🔍 Predict")

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")
    st.subheader("📷 Uploaded Image")
    st.image(image, width=280)

    if predict:

        img_tensor = transform(image).unsqueeze(0)

        with torch.no_grad():
            outputs = model(img_tensor)
            probs = F.softmax(outputs, dim=1)
            confidence, predicted_idx = torch.max(probs, 1)

        predicted_class = CLASS_NAMES[predicted_idx.item()]

        crop, disease = predicted_class.split("___")
        crop = crop.replace("_", " ")
        disease = disease.replace("_", " ")

        st.markdown("---")

        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.subheader("🧠 Prediction Result")

        if "healthy" in disease.lower():
            st.markdown(f"""
            ### ✅ {crop} is Healthy

            No visible disease symptoms detected.
            Continue regular crop monitoring.
            """)
        else:
            st.markdown(f"""
            ### Crop Name: {crop}
            ### 🦠 Possible Disease: {disease}

            This is an AI-generated prediction.
            Please consult an agricultural expert for confirmation.
            """)

        st.markdown("</div>", unsafe_allow_html=True)

        report = generate_disease_report(predicted_class)

        if report and "healthy" not in disease.lower():
            st.markdown("### 📋 Disease Information")
            st.write(f"**Summary:** {report['summary']}")
            st.write(f"**Causes:** {report['causes']}")
            st.write(f"**Treatment:** {report['treatment']}")
            st.write(f"**Prevention:** {report['prevention']}")
        elif not report:
            st.warning("No detailed information available.")
            st.warning("No detailed information available.")
