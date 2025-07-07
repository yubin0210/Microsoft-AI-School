# 💻 2025.05.16 - 학습 노트

---

## ✏️ 학습 내용

분류(Classification) 모델링에 대한 심층적인 학습을 진행했습니다. 붓꽃 품종 예측과 로켓 발사 성공 여부 예측이라는 두 가지 주요 주제를 다루며, `DecisionTreeClassifier`와 `RandomForestClassifier`와 같은 분류 모델의 적용, 교차 검증, `GridSearchCV`를 이용한 하이퍼파라미터 튜닝, 그리고 데이터 전처리 파이프라인 구성 방법을 실습했습니다. 이를 통해 실제 데이터를 기반으로 분류 모델을 구축하고 평가하며, 모델의 성능을 최적화하는 능력을 향상시켰습니다.

---

## 📁 파일 목록

- `notebooks/`: 분류 모델링 실습을 위한 Jupyter Notebook 파일들이 포함된 폴더입니다.
  - `03_붓꽃품종예측*.ipynb`: 붓꽃 품종 예측에 대한 의사결정 트리 모델 학습, 교차 검증, GridSearchCV 실습.
  - `04_로켓발사 성공여부 예측*.ipynb`: 로켓 발사 성공 여부 예측에 대한 랜덤 포레스트 모델 학습, 전처리 파이프라인 구성, 특성 중요도 분석 실습.
- `data/`: 분석에 사용된 원본 CSV 파일들이 들어있는 폴더입니다.
  - `RocketLaunchDataCompleted.csv`: 로켓 발사 데이터.
- `models/`: 학습된 모델 파일들이 저장되는 폴더입니다.

---

## 📌 주요 코드

### 1. 붓꽃 품종 예측 (Decision Tree)
*`scikit-learn`의 `DecisionTreeClassifier`를 사용하여 붓꽃 품종을 분류하고, 모델의 정확도와 특성 중요도를 확인하는 코드입니다.*
```python
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target)

model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print(f"예측 정확도: {accuracy_score(y_test, pred):.2f}")
print(classification_report(y_test, pred))
```

### 2. 로켓 발사 성공 여부 예측 (Random Forest with Pipeline)
*데이터 전처리(`OneHotEncoder`, `StandardScaler`)와 `RandomForestClassifier`를 파이프라인으로 구성하여 로켓 발사 성공 여부를 예측하는 코드입니다.*
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/RocketLaunchDataCompleted.csv", encoding="cp949")
# ... (데이터 전처리 코드 생략)

X = df.drop("Launched?", axis=1)
y = df["Launched?"]

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

categorical_features = X_train.select_dtypes(include="object").columns
numerical_features = X_train.select_dtypes(include="number").columns

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", StandardScaler(), numerical_features),
    ],
    remainder="passthrough",
)

pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("rf", RandomForestClassifier())
    ]
)

pipeline.fit(X_train, y_train)
print(f"모델 정확도: {pipeline.score(X_test, y_test):.2f}")
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
