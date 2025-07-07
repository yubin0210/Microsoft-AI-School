# 💻 2025.05.28 - 학습 노트

---

## ✏️ 학습 내용

`Gradio` 라이브러리를 활용하여 머신러닝 모델을 위한 웹 인터페이스를 구축하는 방법을 학습했습니다. 사용자가 이미지를 업로드하면 `Azure Custom Vision` 서비스를 통해 이미지 분류 또는 객체 탐지 모델이 예측을 수행하고, 그 결과를 웹 인터페이스에 표시하는 과정을 실습했습니다. 특히, `Gradio`의 다양한 컴포넌트와 레이아웃 기능을 사용하여 사용자 친화적인 인터페이스를 설계하는 방법을 익혔습니다. 이를 통해 클라우드 기반의 AI 모델을 웹 애플리케이션 형태로 배포하고 활용하는 능력을 향상시켰습니다.

---

## 📁 파일 목록

- `GradioTest.ipynb`: `Gradio`를 이용한 Custom Vision 이미지 분류 모델 웹 인터페이스 구축 기본 실습.
- `GradioTest2.ipynb`: `Gradio`를 이용한 Custom Vision 이미지 분류 모델 웹 인터페이스 (상위 2개 예측 표시) 실습.
- `GradioTest3.ipynb`: `Gradio.Blocks()`를 이용한 Custom Vision 이미지 분류 모델 웹 인터페이스 레이아웃 구성 실습.
- `moonrock_identification_master.ipynb`: `Azure Custom Vision` 서비스를 이용한 월석 이미지 분류 및 예측 실습.
- `object_detection_master.ipynb`: `Azure Custom Vision` 서비스를 이용한 이미지 객체 탐지 및 시각화 실습.
- `data/`: 실습에 사용되는 이미지 데이터가 포함된 폴더.

---

## 📌 주요 코드

### 1. `Gradio`를 이용한 Custom Vision 모델 웹 인터페이스
*`Gradio`를 사용하여 `Azure Custom Vision` 모델의 예측 결과를 웹 인터페이스로 제공하는 코드입니다.*
```python
import requests
from PIL import Image
import gradio as gr
import io

# Custom Vision Prediction 키와 URL (실제 키와 URL로 대체 필요)
PREDICTION_KEY = "YOUR_PREDICTION_KEY"
ENDPOINT_URL = "YOUR_ENDPOINT_URL"
headers = {"Prediction-Key": PREDICTION_KEY, "Content-Type": "application/octet-stream"}

def predict_with_api(image: Image.Image):
    buf = io.BytesIO()
    image.save(buf, format="JPEG")
    byte_data = buf.getvalue()

    response = requests.post(ENDPOINT_URL, headers=headers, data=byte_data)
    predictions = response.json()["predictions"]

    top_prediction = max(predictions, key=lambda x: x["probability"])
    label = top_prediction["tagName"]
    probability = top_prediction["probability"]

    return f"{label} ({probability*100:.2f}%)"

interface = gr.Interface(
    fn=predict_with_api,
    inputs=gr.Image(type="pil"),
    outputs=gr.Text(),
    title="Custom Vision Image Classifier",
    description="Upload an image to see the prediction from your Custom Vision model.",
)

interface.launch()
```

### 2. `Azure Custom Vision`을 이용한 객체 탐지 및 시각화
*`Azure Custom Vision` 서비스를 호출하여 이미지 내 객체를 탐지하고, 탐지된 객체에 바운딩 박스를 그려 시각화하는 코드입니다.*
```python
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from PIL import Image, ImageDraw
import numpy as np

# Custom Vision Prediction 설정 (실제 값으로 대체 필요)
prediction_endpoint = "YOUR_PREDICTION_ENDPOINT"
prediction_key = "YOUR_PREDICTION_KEY"
project_id = "YOUR_PROJECT_ID"
model_name = "YOUR_MODEL_NAME"

credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(endpoint=prediction_endpoint, credentials=credentials)

image_file = "data/test-1.png" # 테스트 이미지 파일 경로
image = Image.open(image_file)
h, w, ch = np.array(image).shape

with open(image_file, mode="rb") as image_data:
    results = predictor.detect_image(project_id, model_name, image_data)

draw = ImageDraw.Draw(image)
lineWidth = int(w / 100)
color = 'magenta'

for prediction in results.predictions:
    if (prediction.probability * 100) > 50:
        left = prediction.bounding_box.left * w
        top = prediction.bounding_box.top * h
        width = prediction.bounding_box.width * w
        height = prediction.bounding_box.height * h

        points = ((left, top), (left + width, top), (left + width, top + height), (left, top + height), (left, top))
        draw.line(points, fill=color, width=lineWidth)
        # 텍스트 추가 (폰트 설정 필요)
        # plt.annotate(prediction.tag_name + ' {0:.2f}%'.format(prediction.probability * 100), (left, top), color=color)

# image.save("output.jpg") # 결과 이미지 저장
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
