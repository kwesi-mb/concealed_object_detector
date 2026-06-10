import cv2

def draw_detections(image_path, results):

    image = cv2.imread(image_path)

    detections = []

    for result in results:

        for box in result.boxes:

            x1, y1, x2, y2 = map(
                
                int,
                box.xyxy[0]
            )

            conf = float(box.conf[0])

            cls = int(box.cls[0])

            label = result.names[cls]

            detections.append({
                "label": label,
                "confidence": round(conf, 3)
            })

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                image,
                f"(label) {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    return image, detections

def classify_risk(confidence):

    if confidence >= 0.9:
        return "HIGH"

    elif confidence >= 0.7:
        return "MEDIUM"

    return "LOW"

def generate_explanation(detections):

    if len(detections) == 0:

        return (
            "No concealed weapon was detected."
        )

    confidence = detections[0]["confidence"]

    if confidence > 0.9:

        return (
            f"A concealed weapon was detected "
            f"with high confidence ({confidence:.1%}). "
            f"Immediate action is recommended."
        )
    
    elif confidence > 0.7:

        return (
            f"A potential concealed weapon was detected "
            f"with moderate confidence ({confidence:.1%}). "
            f"Additional inspection is advised."
        )

    return (
        "Low confidence detection identified. "
        "Manual verification is recommended."
    )

def security_recommendation(confidence):

    if confidence > 0.9:

        return (
            "Immediate security intervention recommended."
        )

    elif confidence > 0.7:

        return (
            "Secondary screening recommended."
        )

    return (
        "Manual review advised."
    )