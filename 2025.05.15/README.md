# 💻 2025.05.15 - 학습 노트

---

## ✏️ 학습 내용

회귀 분석 모델링에 대한 심층적인 학습을 진행했습니다. 광고 플랫폼별 판매량 예측과 공공자전거 수요 예측이라는 두 가지 주요 주제를 다루며, 데이터 탐색(EDA), 다양한 회귀 모델(단순 선형 회귀, 다중 회귀, 다항 회귀 및 규제)의 적용, 데이터 전처리, 그리고 효율적인 머신러닝 워크플로우를 위한 파이프라인 구성 방법을 실습했습니다. 이를 통해 실제 데이터를 기반으로 예측 모델을 구축하고 평가하는 능력을 향상시켰습니다.

---

## 📁 파일 목록

- `notebooks/`: 회귀 분석 실습을 위한 Jupyter Notebook 파일들이 포함된 폴더입니다.
  - `01_회귀_광고플랫폼에따른판매량예측*.ipynb`: 광고 플랫폼에 따른 판매량 예측에 대한 단순 선형 회귀, 다중 회귀, 다항 회귀 및 규제, 파이프라인 구성 실습.
  - `02_회귀_공공자전거 수요 예측*.ipynb`: 공공자전거 수요 예측에 대한 EDA, 모델링, 전처리 및 모델링, 파이프라인 구성 실습.
- `data/`: 분석에 사용된 원본 CSV 파일들이 들어있는 폴더입니다.
  - `advertising.csv`: 광고 플랫폼별 판매량 데이터.
  - `bike_sharing_demand.csv`: 공공자전거 수요 데이터.
- `models/`: 학습된 모델 파일들이 저장되는 폴더입니다.

---

## 📌 주요 코드

### 1. 데이터 로드 및 탐색 (EDA)
*광고 판매량 데이터를 불러와 기본적인 정보를 확인하고 시각화하는 코드입니다.*
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
advertising_df = pd.read_csv('data/advertising.csv')

# 데이터 정보 확인
advertising_df.info()

# 산점도 시각화
sns.pairplot(advertising_df, x_vars=['TV', 'Radio', 'Newspaper'], y_vars='Sales', height=4, aspect=1, kind='scatter')
plt.show()
```

### 2. 선형 회귀 모델 학습 및 예측
*`scikit-learn`을 사용하여 단순 선형 회귀 모델을 학습하고 예측하는 코드입니다.*
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = advertising_df[['TV']]
Y = advertising_df['Sales']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)
```

### 3. 머신러닝 파이프라인 구성
*데이터 전처리(스케일링)와 모델 학습을 하나의 파이프라인으로 묶어 효율적인 워크플로우를 구축하는 코드입니다.*
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# 파이프라인 정의
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# 파이프라인 학습
pipeline.fit(X_train, Y_train)

# 예측
Y_pred_pipeline = pipeline.predict(X_test)
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
