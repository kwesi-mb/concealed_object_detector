#  SecureVision AI

### Concealed Weapon Detection & Security Screening Platform

SecureVision AI is an AI-powered concealed weapon detection system developed using YOLOv8 and Streamlit. The solution analyzes thermal images and automatically detects potential concealed weapons, providing confidence scores, risk assessments, and actionable security recommendations.

The project was developed as part of the Temsconsu Software/AI Engineer assessment and demonstrates the application of computer vision techniques to modern security screening challenges.

---

## Features

* Concealed weapon detection using YOLOv8
* Thermal image analysis
* Confidence score visualization
* Risk level classification
* AI-generated assessment
* Security action recommendations
* Interactive Streamlit dashboard
* Temsconsu-branded user interface

---

## Project Structure

```text
concealed_object_detector
│
├── app/
│   ├── detector.py
│   ├── utils.py
│   └── ui.py
│
├── model/
│   └── best.pt
│
├── assets/
│   └── temsconsu_logo.png
│
├── test_images/
│   ├── sample_1.jpg
│   ├── sample_2.jpg
│   └── sample_3.jpg
│
├── requirements.txt
└── README.md
```

---

## Model Performance

| Metric    | Score |
| --------- | ----- |
| Precision | 94.5% |
| Recall    | 99.4% |
| mAP@50    | 98.6% |
| mAP@50-95 | 62.9% |

These results demonstrate strong weapon detection performance while maintaining a low rate of missed detections.

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>

cd concealed_object_detector
```

### 2. Create a Virtual Environment

Windows:

```bash
python -m venv venv

venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Model

Ensure the trained model file is located at:

```text
model/best.pt
```

The application automatically loads the model during startup.

---

## Launching the Interactive Interface

Run:

```bash
streamlit run app/ui.py
```

After startup, Streamlit will provide a local URL:

```text
http://localhost:8501
```

Open the URL in your browser to access the SecureVision AI dashboard.

---

## How to Use

### Step 1

Launch the Streamlit application.

### Step 2

Upload a thermal image using the file uploader.

### Step 3

Click:

```text
Run Detection
```

### Step 4

Review:

* Detection Result
* Confidence Score
* Risk Classification
* AI Assessment
* Recommended Action

---

## Example Test Images

The repository includes sample thermal images in:

```text
test_images/
```

Example scenarios include:

* Concealed weapon present
* No weapon present
* Partial weapon visibility
* Multiple subject screening

To test the model:

1. Open the application.
2. Upload an image from the test_images folder.
3. Run inference.
4. Review the generated results.

---

## Technology Stack

### AI & Machine Learning

* YOLOv8
* PyTorch
* Ultralytics

### Backend

* Python

### Frontend

* Streamlit

### Computer Vision

* OpenCV
* Pillow

---

## Future Enhancements

Potential improvements include:

* Real-time video stream detection
* Multi-class weapon classification
* Incident report generation
* LLM-powered security assistant
* Security operations dashboard
* Edge deployment support
* Multi-camera monitoring

---

## Author

Malachy Kwesike Madu

Software Engineer | Machine Learning Engineer

---

## Acknowledgements

Temsconsu Software Services Company

This project was developed as part of the Software/AI Engineer technical assessment and demonstrates the use of modern computer vision techniques for intelligent security screening.
