import streamlit as st
import tempfile
import pandas as pd

from detector import WeaponDetector
from utils import (
    draw_detections,
    generate_explanation
)

detector = WeaponDetector()

st.title(
    "Concealed Weapon Detection System"
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

        st.subheader(
            "Detection Results"
        )

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
            "AI Explanation"
        )

        st.info(explanation)