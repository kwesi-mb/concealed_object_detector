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

logo = Image.open("assets/temsconsu_logo.png")

st.set_page_config(
    page_title="Concealed Weapon Detection",
    page_icon=logo,
    layout="wide"
)

# CUSTOM CSS

st.markdown("""
<style>

/* Main app background*/
[data-testid="stAppViewContainer"] {
    background-color: white;
}

/* Main content area */
.main {
    background-color: white;
}

/* Remove horizontal padding from the main container */




/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #f7f9fc;
}

/* Headers */
h1, h2,  h3, h4, h5, h6 {
    color: #000000;
    font-weight: 700;
}

[data-testid="stMarkdownContainer"] h1,
[data-testid="stMarkdownContainer"] h2,
[data-testid="stMarkdownContainer"] h3,
[data-testid="stMarkdownContainer"] h4 {
    color: #000000;
    font-weight: 700;
}

/* Metric card container */
[data-testid="stMetric"] {
    background-color: #f7f9fc;
    border-radius: 10px;
    padding: 15px
    border-left: 5px solid #0B4EA2;
}

/* Metric label */
[data-testid="stMetricLabel"] {
    color: #000000;
    font-weight: 700;
}

/* Metric value */
[data-testid="stMetricValue"] {
    color: #000000;
    font-weight: 700;
}

/* Metric delta (if any) */
[data-testid="stMetricDelta"] {
    color: #000000;
}

/* Upload box */
[data-testid="stFileUploader"] {
    border: 2px solid #0B4EA2;
    border-radius: 10px;
    padding: 10px;
}

/* Buttons */
.stButton > button {
    background-color: #0B4EA2;
    color: white;
    border-radius: 8px;
    border: none;
    font-weight: bold;
}

.stButton > button:hover {
    background-color: #083a79
}

/* Warning text */
[data-testid="stAlert"] {
    color: #000000;
}

[data-testid="stAlert] * {
    color: #000000;
    opacity:1;
}

/* Reduce top spacing */
.block-container {
    padding-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

# LOAD MODEL

detector = WeaponDetector()

# HEADER
st.markdown('<div class="main-content">', unsafe_allow_html=True)
from PIL import Image


logo = Image.open("assets/temsconsu_logo.png")

logo_col, title_col = st.columns([1, 5])

with logo_col:
    st.image(
        logo,
        width=120
    )

with title_col:
    st.markdown(
        """
        <h1 style='margin-bottom:0; color:#0B4EA2;'>
        Temsconsu SecureVision AI
        </h1>

        <h4 style='color:#F26722;'>
        Concealed Weapon Detection & Security Screening Platform
        </h4>
        """,
        unsafe_allow_html=True
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

            
            st.markdown(
                f"""
                <h3 style="
                    color:#000000;
                    font-weight:bold;
                    text-align:center;
                ">
                    {highest_conf:.1%}
                </h3>
                """,
                unsafe_allow_html=True
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

            
            st.markdown(
                f"""
                <div style="
                    background-color:#FFF4E5;
                    padding:15px;
                    border-radius:10px;
                    border-left:5px solid #F26722;
                    color:#000000;
                    font-weight:500;
                ">
                    {security_recommendation(highest_conf)}
                </div>
                """,
                unsafe_allow_html=True
            )

        else:

            st.success(
                "No concealed weapon detected."
            )

#st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# Footer section
st.markdown(
    """
    <div style="
        background-color:#0B4EA2;
        padding:20px;
        border-radius:10px;
        text-align:center;
        margin-top:30px;
        border-top:5px solid #F26722;
    ">
        <p style="color:white; margin-top:8px;">
            SecureVision AI
        </p>
        <p style="color:#F26722; margin-top:8px;">
            Powered by Temsconsu Software Services Company
        </p>
    </div>
    """,
    unsafe_allow_html=True
)