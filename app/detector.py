from ultralytics import YOLO



class WeaponDetector:

    def __init__(self):
        self.model = YOLO("model/best.pt")

    def detect(self, image_path):
        results = self.model(image_path)
        return results