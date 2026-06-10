import cv2

def draw_detections(image_path, results):
    """
    Draw bounding boxes on image and extract detections.
    """

    image = cv2.imread(image_path)

    detections = []

    for result in results:

        for box in result.boxes:

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            confidence = float(box.conf[0])

            class_id = int(box.cls[0])

            label = result.names[class_id]

            detections.append(
                {
                    "label": label,
                    "confidence": round(confidence, 3)
                }
            )

            # Draw bounding box
            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            # Draw label
            cv2.putText(
                image,
                f"{label} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 255, 0),
                2
            )

    # Convert BGR to RGB for Streamlit
    image = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2RGB
    )

    return image, detections

def classify_risk(confidence):
    """
    Classify risk level based on confidence score.
    """

    if confidence >= 0.90:
        return "HIGH" 
    
    elif confidence >= 0.70:
        return "MEDIUM"

    return "LOW"

def generate_explanation(detections):
    """
    Generate a human-readable explanation.
    """

    if len(detections) == 0:

        return (
            "No concealed weapon was detected in the uploaded image. "
            "The scanned individual appears clear based on the model's analysis."
        )

    highest_confidence = max(
        detection["confidence"]
        for detection in detections
    )

    risk_level = classify_risk(
        highest_confidence
    )

    if risk_level == "HIGH":

        return (
            f"The system detected a concealed weapon with a high confidence score "
            f"of {highest_confidence:.1%}. "
            f"This is classified as HIGH risk and warrants immediate attention."
        )

    elif risk_level == "MEDIUM":

        return (
            f"The system detected a potential concealed weapon with a confidence "
            f"score of {highest_confidence:.1%}. " 
            f"This is classified as MEDIUM risk and should be reviewed by security personnel."
        )

    return (
        f"A low-confidence detection was identified "
        f"({highest_confidence:.1%}). "
        f"Manual verification is recommended before taking action."
    )

def security_recommendation(confidence):
    """
    Generate recommended security action.
    """

    risk_level = classify_risk(confidence)

    if risk_level == "HIGH":

        return (
            "Immediate security intervention recommended. "
            "Conduct secondary screening and notify security personnel."
        )

    elif risk_level == "MEDIUM":

        return (
            "Secondary screening recommended. "
            "Review the highlighted region and verify the detection."
        )

    return (
        "Manual review advised. "
        "Detection confidence is low and requires verification."
    )