from ultralytics import YOLO

class WeaponDetector:
    def __init__(self, model_path):
        """
        Initialize the detector with a YOLO model.
        """

        self.model = YOLO(model_path)

    def detect(self, image_path):
        """
        Run inference on an image.
        """

        results = self.model(image_path)

        return results