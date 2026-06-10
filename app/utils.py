import cv2

def draw_detections(image_path, results):
    
    image = cv2.imread(image_path)

    detections = []

    for result in results:

        boxes = result.boxes

        for box in boxes:

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            conf = float(box.conf[0])

            cls = int(box.cls[0])

            label = result.names[cls]

            detections.append(
                {
                    "label": label,
                    "confidence": round(conf, 3)
                }
            )

            cv2.rectangle(
                image,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                image,
                f"{label} {conf:.2f}",
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    return image, detections

def generate_explanation(detections):

    if len(detections) == 0:

        return (
            "No concealed weapon was detected "
            "within the uploaded image."
        )

    return (
        f"The system detected "
        f"{len(detections)} potential weapon(s). "
        f"Review the highlighted region(s) in the image for more details."
    )
