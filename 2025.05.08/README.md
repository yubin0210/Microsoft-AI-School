# 💻 2025.05.08 - 학습 노트

---

## ✏️ 학습 내용

`OpenCV` 라이브러리를 활용한 다양한 이미지 처리 및 컴퓨터 비전 기술을 심층적으로 학습했습니다. 기본적인 이미지 로드 및 표시부터 시작하여, 이미지의 색상 채널 분리, 히스토그램 분석, 이진화, 형태학적 연산 등 이미지 전처리 기법을 다루었습니다. 또한, 감마 보정, 히스토그램 평활화, 블러링, 엠보싱 필터 적용과 같은 이미지 개선 및 필터링 기법을 익혔습니다. 더 나아가 엣지 검출, 윤곽선 찾기, 원 검출, 슈퍼픽셀 분할, 그리고 GrabCut을 이용한 객체 분할 등 고급 컴퓨터 비전 기술을 실습하며 이미지 분석 및 조작 능력을 향상시켰습니다.

---

## 📁 파일 목록

- `ch2/`: OpenCV 기본 이미지 처리 및 GUI 상호작용 실습 파일
  - `2-1.py`: `numpy`를 이용한 배열 정렬 예제.
  - `2-2.py` ~ `2-9.py`: 이미지 로드, 표시, 크기 조절, 그레이스케일 변환, 웹캠 캡처, 이미지에 도형 및 텍스트 그리기, 마우스 이벤트를 이용한 그림 그리기 등.
- `ch3/`: OpenCV 심화 이미지 처리 및 필터링 실습 파일
  - `3-1.py` ~ `3-9.py`: 이미지 채널 추출, 히스토그램, 이진화, 형태학적 연산, 감마 보정, 히스토그램 평활화, 블러링, 엠보싱 필터, 이미지 변환 (이동, 회전), 보간법 비교 등.
- `ch4/`: OpenCV 고급 이미지 처리 및 컴퓨터 비전 기술 실습 파일
  - `4-1.py` ~ `4-8.py`: 엣지 검출 (Sobel, Canny), 윤곽선 찾기, 원 검출 (HoughCircles), 슈퍼픽셀 분할 (SLIC), GrabCut을 이용한 객체 분할 등.
- `links.txt`: 관련 링크 또는 참고 자료가 포함될 수 있는 텍스트 파일입니다.

---

## 📌 주요 코드

### 1. 이미지 이진화 (OTSU 알고리즘)
*이미지의 히스토그램을 분석하여 최적의 임계값을 자동으로 찾아 이진화하는 코드입니다.*
```python
import cv2 as cv

image = cv.imread("2025.05.08/ch3/soccer.jpg")
t, binary_image = cv.threshold(image[:, :, 2], 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)
print(f"OTSU Algorithm이 찾은 최적의 임계값: {t}")
```

### 2. 이미지 형태학적 연산 (팽창, 침식)
*이미지의 객체를 확장하거나 축소하는 형태학적 연산을 수행하는 코드입니다.*
```python
import cv2 as cv
import numpy as np

se = np.uint8([ [0,0,1,0,0], [0,1,1,1,0], [1,1,1,1,1], [0,1,1,1,0], [0,0,1,0,0] ])
b_dilation = cv.dilate(binary_image, se, iterations=1)
b_erosion = cv.erode(binary_image, se, iterations=1)
```

### 3. Canny 엣지 검출
*이미지에서 엣지(가장자리)를 효과적으로 검출하는 Canny 알고리즘을 적용하는 코드입니다.*
```python
import cv2 as cv

image = cv.imread("2025.05.08/ch4/soccer.jpg")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 100, 200)
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
