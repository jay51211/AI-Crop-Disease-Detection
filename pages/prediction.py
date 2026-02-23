import streamlit as st
import torch
from PIL import Image
from torchvision import transforms
import torch.nn.functional as F
from pages.disease import generate_disease_report, DISEASE_INFO
from pages.model import SimpleCNN

st.set_page_config(page_title="Disease Prediction", layout="centered")

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

CLASS_NAMES = list(DISEASE_INFO.keys())

@st.cache_resource
def load_model():
    model = SimpleCNN(len(CLASS_NAMES))

    state_dict = torch.load(
        "models/plant_disease.pth",
        map_location="cpu"
    )

    model.load_state_dict(state_dict)
    model.eval()
    return model

model = load_model()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    )
])

uploaded_file = st.file_uploader(
    "📤 Upload a leaf image",
    type=["jpg", "jpeg", "png"]
)
if uploaded_file:
    image = Image.open(uploaded_file).convert('RGB')
    input_tensor = transform(image).unsqueeze(0)
    st.subheader("📷 Uploaded Leaf Image")
    st.image(image, use_container_width=False, width=250)
    st.markdown("""
    <style>
    img {
        border-radius: 10px;
        border: 2px solid #e0e0e0;
    }
    </style>
    """, unsafe_allow_html=True)

    with torch.no_grad():
        outputs = model(input_tensor)
        probs = F.softmax(outputs, dim=1)
        confidence, predicted_idx = torch.max(probs, 1)

    predicted_class = CLASS_NAMES[predicted_idx.item()]
    confidence = confidence.item() * 100
    predict = st.button("Predict")

    if predict:
        st.markdown("---")
        st.subheader("🧠 Prediction Result")

        st.success(f"**Disease:** {predicted_class}")
        st.info(f"**Confidence:** {confidence:.2f}%")

        report = generate_disease_report(predicted_class)

        if report:
            st.markdown("### 📋 Disease Information")
            st.write(f"**Summary:** {report['summary']}")
            st.write(f"**Causes:** {report['causes']}")
            st.write(f"**Treatment:** {report['treatment']}")
            st.write(f"**Prevention:** {report['prevention']}")
        else:
            st.warning("No detailed information available for this disease.")