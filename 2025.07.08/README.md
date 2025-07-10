# 💻 2025.07.08 - 학습 노트

---

## ✏️ 학습 내용

YOLO(You Only Look Once) 모델의 발전 과정을 이해하고, YOLOv3와 최신 버전인 YOLOv8을 비교하며 객체 탐지 성능을 실습했습니다. 사전 학습된(pre-trained) YOLO 모델 가중치 파일을 사용하여 이미지 내의 다양한 객체를 빠르고 정확하게 탐지하는 방법을 익혔습니다. 특히 YOLOv8의 간결한 코드와 향상된 성능을 직접 확인했습니다.

---

## 📁 파일 목록

- `yolo3_20250708.ipynb`: YOLOv3 모델을 사용하여 이미지에서 객체를 탐지하는 과정을 다루는 Jupyter Notebook 파일입니다.
- `yolo8_20250708.ipynb`: YOLOv8 모델을 사용하여 이미지에서 객체를 탐지하는 과정을 다루는 Jupyter Notebook 파일입니다.
- `yolov8n.pt`, `yolov8s.pt`, `yolov8x.pt`: YOLOv8의 다양한 크기(nano, small, extra-large)의 사전 학습된 모델 가중치 파일입니다.
- `house-3097664_960_720.jpg`: 객체 탐지 실습에 사용된 샘플 이미지입니다.
- `yolo/`: YOLOv3 모델 관련 파일(가중치, 설정 파일 등)이 저장된 디렉터리입니다.

---

## 📌 주요 코드

### 1. YOLOv3를 이용한 객체 탐지 (`yolo3_20250708.ipynb`)
*OpenCV의 `dnn` 모듈을 사용하여 YOLOv3 모델을 로드하고 객체 탐지를 수행하는 코드입니다.*
```python
import cv2
import numpy as np

# YOLOv3 모델 로드
net = cv2.dnn.readNet("yolo/yolov3.weights", "yolo/yolov3.cfg")
classes = []
with open("yolo/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# 이미지 로드 및 객체 탐지
img = cv2.imread("house-3097664_960_720.jpg")
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(net.getUnconnectedOutLayersNames())

# 결과 시각화
# ... (탐지된 객체에 대한 바운딩 박스 및 레이블 표시)
```

### 2. YOLOv8를 이용한 객체 탐지 (`yolo8_20250708.ipynb`)
*Ultralytics의 `ultralytics` 라이브러리를 사용하여 YOLOv8 모델을 간편하게 로드하고 객체 탐지를 수행하는 코드입니다.*
```python
from ultralytics import YOLO
import cv2

# YOLOv8 모델 로드
model = YOLO('yolov8n.pt')  # nano 버전 모델

# 이미지 로드
img_path = 'house-3097664_960_720.jpg'

# 객체 탐지 수행
results = model(img_path)

# 결과 시각화
for r in results:
    im_array = r.plot()  # plot a BGR numpy array of predictions
    cv2.imshow('YOLOv8 Detection', im_array)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ubinn0210@gmail.com)

---
