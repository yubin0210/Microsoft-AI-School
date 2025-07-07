# 💻 2025.05.19 - 학습 노트

---

## ✏️ 학습 내용

텍스트 마이닝, 비지도 학습(군집화), 그리고 웹 크롤링에 대한 실습을 진행했습니다. `KoNLPy`를 활용하여 한글 텍스트를 분석하고 워드클라우드를 생성하는 방법을 익혔습니다. K-Means 군집화 알고리즘을 사용하여 데이터를 그룹화하고, 엘보우 방법과 실루엣 분석을 통해 최적의 군집 개수를 찾는 방법을 학습했습니다. 특히, 프로야구 선수 데이터를 활용하여 PCA(주성분 분석) 적용 여부에 따른 군집화 결과를 비교 분석했습니다. 마지막으로 `requests`와 `BeautifulSoup` 라이브러리를 사용하여 웹 페이지에서 데이터를 효율적으로 수집하는 웹 크롤링 기술을 습득했습니다.

---

## 📁 파일 목록

- `03_워드클라우드시각화.ipynb`: `KoNLPy`를 이용한 한글 텍스트 워드클라우드 시각화 실습.
- `05_군집화_k-means*.ipynb`: `make_blobs`로 생성된 가상 데이터를 이용한 K-Means 군집화 실습.
- `06_군집화_프로야구*.ipynb`: 프로야구 선수 데이터를 활용한 K-Means 군집화 및 PCA 적용 비교 실습.
- `silhouette_analysis.py`: 실루엣 분석을 위한 헬퍼 함수를 포함하는 Python 스크립트.
- `Crawling/`: 웹 크롤링 실습 파일들이 포함된 폴더입니다.
  - `01_정적웹페이지 데이터 수집*.ipynb`: 정적 웹페이지에서 데이터 수집하는 기본 실습.
  - `02_네이버뉴스데이터수집*.ipynb`: 네이버 증권 뉴스에서 여러 페이지의 뉴스 데이터 및 본문 내용까지 수집하는 실습.

---

## 📌 주요 코드

### 1. K-Means 군집화 및 실루엣 분석
*데이터를 K-Means로 군집화하고, 실루엣 점수를 계산하여 군집의 품질을 평가하는 코드입니다.*
```python
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import silhouette_analysis as s

k = 3 # 최적의 k 값
km = KMeans(n_clusters=k, random_state=10)
cluster_labels = km.fit_predict(scaled_features) # scaled_features는 스케일링된 데이터

print(f'실루엣 점수: {silhouette_score(scaled_features, cluster_labels):.2f}')
s.silhouette_plot(scaled_features, k) # 실루엣 플롯 시각화
```

### 2. 웹 크롤링 (requests, BeautifulSoup)
*`requests`로 웹 페이지를 요청하고, `BeautifulSoup`으로 HTML을 파싱하여 원하는 데이터를 추출하는 코드입니다.*
```python
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/news/mainnews.naver'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 뉴스 제목 추출
article_titles = [a.text for a in soup.select(".articleSubject > a")]

# 뉴스 링크 추출
article_links = [a.attrs['href'] for a in soup.select(".articleSubject > a")]

print(article_titles[0])
print(article_links[0])
```

### 3. PCA (주성분 분석)
*데이터의 차원을 축소하고, 주성분으로 변환된 데이터를 활용하는 코드입니다.*
```python
from sklearn.decomposition import PCA

pca = PCA(n_components=2) # 2개의 주성분으로 축소
principal_components = pca.fit_transform(X_scaled) # X_scaled는 스케일링된 원본 데이터

# 설명된 분산 비율 확인
print(pca.explained_variance_ratio_)

# 누적 분산 확인
print(pca.explained_variance_ratio_.cumsum())
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
