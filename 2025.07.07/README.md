# 💻 2025.07.07 - 학습 노트

---

## ✏️ 학습 내용

OpenCV를 사용한 기본적인 이미지 처리 및 객체 검출 방법과 YOLOv3 모델을 활용한 실시간 객체 탐지에 대해 학습했습니다. OpenCV를 통해 이미지와 비디오를 다루는 방법을 익히고, YOLOv3 모델을 로드하여 이미지 내의 다양한 객체를 식별하고 바운딩 박스로 표시하는 실습을 진행했습니다.

---

## 📁 파일 목록

- `opencv_20250707.ipynb`: OpenCV를 사용하여 이미지를 읽고, 화면에 표시하며, 기본적인 이미지 처리 기술을 다루는 Jupyter Notebook 파일입니다.
- `yolo3_20250707.ipynb`: YOLOv3 모델을 사용하여 이미지에서 객체를 탐지하는 과정을 다루는 Jupyter Notebook 파일입니다.
- `yolo/`: YOLO 모델 관련 파일(가중치, 설정 파일 등)이 저장된 디렉터리입니다.

---

## 📌 주요 코드

### 1. OpenCV를 이용한 이미지 처리 (`opencv_20250707.ipynb`)
*OpenCV를 사용하여 이미지를 읽고, 그레이스케일로 변환하며, 화면에 표시하는 기본적인 코드입니다.*
```python
import cv2

# 이미지 읽기
image = cv2.imread('image.jpg')

# 그레이스케일 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 이미지 표시
cv2.imshow('Original Image', image)
cv2.imshow('Gray Image', gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
```

### 2. YOLOv3를 이용한 객체 탐지 (`yolo3_20250707.ipynb`)
*YOLOv3 모델을 로드하고, 이미지에서 객체를 탐지하여 바운딩 박스와 클래스 이름을 표시하는 코드입니다.*
```python
import cv2
import numpy as np

# YOLOv3 모델 로드
net = cv2.dnn.readNet("yolo/yolov3.weights", "yolo/yolov3.cfg")
classes = []
with open("yolo/coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# 이미지 로드 및 전처리
img = cv2.imread("image.jpg")
height, width, channels = img.shape
blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

# 객체 탐지
net.setInput(blob)
outs = net.forward(output_layers)

# 결과 처리
for out in outs:
    for detection in out:
        # ... (바운딩 박스 및 클래스 정보 추출 및 표시)
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ubinn0210@gmail.com)

---
