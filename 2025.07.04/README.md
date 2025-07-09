# 💻 2025.07.04 - 학습 노트 (김유빈)

---

## ✏️ 학습 내용

`Azure Custom Vision` 서비스를 사용하여 객체 탐지 모델을 구축하는 전반적인 과정을 학습했습니다. 새로운 Custom Vision 프로젝트를 생성하고, 탐지할 객체(예: '포크', '가위')에 대한 태그를 정의했습니다. 학습에 필요한 이미지들을 업로드하고, 각 이미지 내의 객체 위치를 바운딩 박스로 지정하는 라벨링 작업을 수행했습니다. 라벨링된 데이터를 기반으로 객체 탐지 모델을 학습시키고, 학습이 완료된 모델을 예측 엔드포인트에 배포했습니다. 마지막으로, 배포된 모델을 사용하여 새로운 이미지에 대한 객체 탐지 예측을 수행하고, 탐지된 객체들을 원본 이미지 위에 바운딩 박스와 함께 시각화하여 모델의 성능을 확인했습니다.

---

## 📁 파일 목록

- `customvision_20250704.ipynb`: `Azure Custom Vision` 서비스를 이용한 객체 탐지 모델 학습, 배포, 예측 및 시각화 실습.
- `fork/`: '포크' 객체 탐지 학습에 사용되는 이미지 파일들이 포함된 폴더.
- `scissors/`: '가위' 객체 탐지 학습에 사용되는 이미지 파일들이 포함된 폴더.

---

## 📌 주요 코드

### 1. `Azure Custom Vision` 프로젝트 및 태그 생성
*`Azure Custom Vision` 트레이닝 클라이언트를 사용하여 새로운 프로젝트를 생성하고, 객체 탐지를 위한 태그를 정의하는 코드입니다.*
```python
from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from msrest.authentication import ApiKeyCredentials

TRAINING_ENDPOINT = "YOUR_TRAINING_ENDPOINT"
TRAINING_API_KEY = "YOUR_TRAINING_API_KEY"

training_credentials = ApiKeyCredentials(in_headers={"Training-key": TRAINING_API_KEY})
trainer = CustomVisionTrainingClient(endpoint=TRAINING_ENDPOINT, credentials=training_credentials)

project_name = "7ai010-kitchen"
project_description = "음식을 감지하는 모델"

# 기존 프로젝트 확인 또는 생성
project = None
for p in trainer.get_projects():
    if p.name == project_name: project = p; break

if project is None:
    # ObjectDetection 도메인 ID 찾기
    domain_id = None
    for domain in trainer.get_domains():
        if domain.type == "ObjectDetection" and domain.name == "General (compact) [S1]":
            domain_id = domain.id; break
    project = trainer.create_project(project_name, project_description, domain_id)

# 태그 생성 또는 가져오기
FORK_TAG_NAME = "포크"
SCISSORS_TAG_NAME = "가위"
fork_tag = trainer.create_tag(project.id, FORK_TAG_NAME)
scissors_tag = trainer.create_tag(project.id, SCISSORS_TAG_NAME)
```

### 2. 이미지 업로드 및 라벨링
*이미지 파일을 읽어와 `Azure Custom Vision` 프로젝트에 업로드하고, 이미지 내 객체의 바운딩 박스 정보를 포함하여 라벨링하는 코드입니다.*
```python
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region

image_list = []
# 예시: '포크' 이미지 업로드 및 라벨링
file_name = "fork_1"
file_path = "./fork/{}.jpg".format(file_name)
# 바운딩 박스 좌표 (left, top, width, height) - 0.0 ~ 1.0 사이의 비율
left, top, width, height = 0.145833328, 0.3509314, 0.5894608, 0.238562092

regions = [Region(tag_id=fork_tag.id, left=left, top=top, width=width, height=height)]
with open(file_path, "rb") as image_data: contents = image_data.read()
entry = ImageFileCreateEntry(name=file_name, contents=contents, regions=regions)
image_list.append(entry)

# 이미지 일괄 업로드
batch = ImageFileCreateBatch(images=image_list)
result = trainer.create_images_from_files(project_id=project.id, batch=batch)
```

### 3. 모델 학습 및 배포
*라벨링된 데이터를 기반으로 모델을 학습시키고, 학습이 완료되면 예측 엔드포인트에 배포하는 코드입니다.*
```python
import time

# 모델 학습
iteration = trainer.train_project(project_id=project.id)
while iteration.status == "Training":
    time.sleep(3)
    iteration = trainer.get_iteration(project_id=project.id, iteration_id=iteration.id)

# 모델 배포
publish_name = "7ai010-kitchen-v1"
PREDICTION_RESOURCE_ID = "YOUR_PREDICTION_RESOURCE_ID" # Azure Custom Vision 예측 리소스 ID
trainer.publish_iteration(project_id=project.id, iteration_id=iteration.id, publish_name=publish_name, prediction_id=PREDICTION_RESOURCE_ID)
```

### 4. 예측 수행 및 시각화
*배포된 모델을 사용하여 새로운 이미지에 대한 객체 탐지 예측을 수행하고, 결과를 이미지 위에 시각화하는 코드입니다.*
```python
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests

PREDICTION_ENDPOINT = "YOUR_PREDICTION_ENDPOINT"
PREDICTION_API_KEY = "YOUR_PREDICTION_API_KEY"
publish_name = "7ai010-kitchen-v1"

predictor_credentials = ApiKeyCredentials(in_headers={"Prediction-key": PREDICTION_API_KEY})
predictor = CustomVisionPredictionClient(endpoint=PREDICTION_ENDPOINT, credentials=predictor_credentials)

IMAGE_URL = "https://cdn.pixabay.com/photo/2017/04/04/17/16/scissors-2202215_1280.jpg"
image_response = requests.get(IMAGE_URL)
image_data = image_response.content
image = Image.open(BytesIO(image_data))

response = predictor.detect_image(project_id=project.id, published_name=publish_name, image_data=image_data)

draw = ImageDraw.Draw(image, 'RGBA')
font = ImageFont.truetype("폰트_경로", size=20) # 폰트 경로 설정 필요

for prediction in response.predictions:
    if prediction.probability > 0.5:
        left = prediction.bounding_box.left * image.width
        top = prediction.bounding_box.top * image.height
        width = prediction.bounding_box.width * image.width
        height = prediction.bounding_box.height * image.height

        draw.rectangle([(left, top), (left + width, top + height)], outline="red", width=2)
        draw.text((left + 10, top), "{}({:.2f}%) ".format(prediction.tag_name, prediction.probability * 100), font=font, fill="red")

# image.save("output_prediction.jpg") # 결과 이미지 저장
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
