import streamlit as st
import tempfile
import pandas as pd
from PIL import Image

from detector import WeaponDetector
from utils import (
    draw_detections,
    generate_explanation,
    classify_risk,
    security_recommendation
)

detector = WeaponDetector()

st.set_page_config(
    page_title="Concealed Weapon Detection",
    layout="wide"
)

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

h1 {
    text-align:center
}

</style>
""", unsafe_allow_html=True) 

st.title(
    "AI-Powered Security Screening Platform"
)

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    st.image(
        uploaded_file,
        caption="Uploaded Image",
        use_container_width=True    
    )

    if st.button("Run Detection"):

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".png"
        ) as temp_file:

            temp_file.write(
                uploaded_file.read()
            )

            image_path = temp_file.name

        results = detector.detect(
            image_path
        )

        output_image, detections = (
            draw_detections(
                image_path,
                results
            )
        )

        if detections:

            highest_conf = max(
                d["confidence"]
                for d in detections
            )

            risk = classify_risk(
                highest_conf
            )

            metric1, metric2, metric3 = st.columns(3)

            metric1.metric(
                "Objects Detected",
                len(detections)
            )

            metric2.metric(
                "Highest Confidence",
                f"{highest_conf:1%}"
            )

            metric3.metric(
                "Risk level",
                risk
            )

            st.subheader(
                "Detection Confidence"
            )

            st.progress(highest_conf)

            st.write(
                f"{highest_conf:1%}"
            )



        st.subheader(
            "Detection Results"
        )

        st.image(
            output_image,
            use_container_width=True
        )

        original_image = Image.open(image_path)

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

        if detections:

            st.dataframe(
                pd.DataFrame(detections)
            )

        explanation = (
            generate_explanation(
                detections
            )
        )

        st.subheader(
            "AI Assessment"
        )

        st.info(
            generate_explanation(
                detections
            )
        )

        st.subheader(
            "Recommended Action"
        )

        st.warning(
            security_recommendation(
                highest_conf
            )
        )