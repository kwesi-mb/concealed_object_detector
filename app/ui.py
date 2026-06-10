import streamlit as st
import tempfile
import pandas as pd
from PIL import Image

from detector import WeaponDetector
from utils import (
    draw_detections,
    classify_risk,
    generate_explanation,
    security_recommendation
)

# Page configuration

st.set_page_config(
    page_title="Concealed Weapon Detection",
    page_icon="🔍",
    layout="wide"
)

# CUSTOM CSS

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# LOAD MODEL

detector = WeaponDetector()

# HEADER

st.title(" Concealed Weapon Detection System")

st.markdown(
    "### AI-Powered Security Screening Platform"
)

st.divider()

# FILE UPLOAD

uploaded_file = st.file_uploader(
    "Upload a thermal image",
    type=["jpg", "jpeg", "png"]
)

# DETECTION WORKFLOW

if uploaded_file:

    if st.button("Run Detection"):

        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        ) as temp_file:

            temp_file.write(
                uploaded_file.read()
            )

            image_path = temp_file.name

        # Original image
        original_image = Image.open(image_path)

        #Run inference
        results = detector.detect(image_path)

        # Draw detection
        output_image, detections = draw_detections(
            image_path,
            results
        )

        # IMAGE DISPLAY

        col1, col2 = st.columns(2)

        with col1:
            
            st.subheader("Original Image")

            st.image(
                original_image,
                use_container_width=True
            )

        with col2:

            st.subheader("Detection Result")

            st.image(
                output_image,
                use_container_width=True
            )

        st.divider()

        # IF DETECTION EXISTS

        if detections:
            
            highest_conf = max(
                d["confidence"]
                for d in detections
            )

            risk_level = classify_risk(
                highest_conf
            )

            # METRICS

            metric1, metric2, metric3 = st.columns(3)

            metric1.metric(
                "Objects Detected",
                len(detections)
            )

            metric2.metric(
                "Highest Confidence",
                f"{highest_conf:.1%}"
            )

            metric3.metric(
                "Risk Level",
                risk_level
            )

            st.divider()

            # CONFIDENCE BAR

            st.subheader(
                "Detection  Confidence"
            )

            st.progress(
                float(highest_conf)
            )

            st.write(
                f"{highest_conf:.1%}"
            )

            st.divider()

            # DETECTION TABLE

            st.subheader(
                "Detection Results"
            )

            st.dataframe(
                pd.DataFrame(detections),
                use_container_width=True
            )

            st.divider()

            # AI EXPLANATION

            st.subheader(
                "AI Assessment"
            )

            st.info(
                generate_explanation(
                    detections
                )
            )

            # RECOMMENDATION

            st.subheader(
                "Recommended Action"
            )

            st.warning(
                security_recommendation(
                    highest_conf
                )
            )

        else:

            st.success(
                "No concealed weapon detected."
            )