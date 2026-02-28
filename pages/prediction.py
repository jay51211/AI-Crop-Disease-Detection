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
    [data-testid="stSidebar"] {display: none;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
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



CLASS_NAMES = ['Tomato___Spider_mites Two-spotted_spider_mite', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
               'Cherry_(including_sour)___Powdery_mildew', 'Apple___Black_rot', 'Apple___healthy',
               'Grape___Esca_(Black_Measles)', 'Strawberry___Leaf_scorch', 'Corn_(maize)___Common_rust_',
               'Apple___Apple_scab', 'Grape___healthy', 'Tomato___Leaf_Mold', 'Apple___Cedar_apple_rust',
               'Peach___Bacterial_spot', 'Blueberry___healthy', 'Corn_(maize)___healthy',
               'Tomato___Tomato_mosaic_virus', 'Strawberry___healthy', 'Orange___Haunglongbing_(Citrus_greening)',
               'Peach___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Raspberry___healthy',
               'Tomato___Late_blight', 'Potato___Early_blight', 'Pepper,_bell___Bacterial_spot', 'Grape___Black_rot',
               'Corn_(maize)___Northern_Leaf_Blight', 'Squash___Powdery_mildew', 'Potato___Late_blight',
               'Tomato___Target_Spot', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Soybean___healthy',
               'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Cherry_(including_sour)___healthy', 'Pepper,_bell___healthy',
               'Tomato___Septoria_leaf_spot', 'Potato___healthy', 'Tomato___healthy'
               ]



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
    transforms.Resize((256, 256)),   # Important: match notebook size
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
