# 💻 2025.05.20 - 학습 노트

---

## ✏️ 학습 내용

웹 크롤링 및 데이터 수집의 고급 기술을 심층적으로 학습했습니다. `Selenium`을 활용하여 동적으로 로드되는 웹 페이지의 데이터를 수집하고, 뉴스 댓글과 같이 동적으로 추가되는 콘텐츠를 효과적으로 크롤링하는 방법을 익혔습니다. 특히, `time.sleep`과 `WebDriverWait`을 이용한 대기 전략을 통해 웹 페이지 로딩 문제를 해결하는 방법을 다루었습니다. 또한, 무한 스크롤 페이지 처리, 셀렉트 박스 제어, 그리고 공공 데이터 API를 활용한 데이터 수집 방법을 실습했습니다. 수집된 데이터에 대해서는 Azure Text Analytics API를 이용한 감성 분석과 `KoNLPy` 및 `WordCloud`를 활용한 텍스트 시각화(워드클라우드)를 수행하여 데이터 분석 능력을 향상시켰습니다.

---

## 📁 파일 목록

- `Crawling/`: 웹 크롤링 및 API 활용 실습 파일들이 포함된 폴더입니다.
  - `03_동적웹페이지 데이터수집*.ipynb`: `Selenium`을 이용한 동적 웹페이지 데이터 수집 기본 실습.
  - `04_뉴스댓글 수집*.ipynb`: `Selenium`을 이용한 뉴스 댓글 수집 (암묵적/명시적 대기 포함).
  - `06_무한스크롤.ipynb`: 무한 스크롤 페이지의 데이터 수집 실습.
  - `07_셀렉트박스*.ipynb`: `Selenium`을 이용한 셀렉트 박스 제어 실습.
  - `08_opneAPI_공공데이터_문화축제*.ipynb`: 공공 데이터 API를 활용한 문화 축제 정보 수집.
  - `08_opneAPI_공공데이터_포트홀.ipynb`: 공공 데이터 API를 활용한 포트홀 데이터 수집.
  - `99_뉴스댓글 수집3_감성분석.ipynb`: 수집된 뉴스 댓글에 대한 감성 분석 실습.
  - `99_워드클라우드시각화.ipynb`: 텍스트 데이터 전처리 및 워드클라우드 시각화 실습.

---

## 📌 주요 코드

### 1. `Selenium`을 이용한 동적 웹페이지 제어
*크롬 웹드라이버를 생성하고, 웹 페이지를 이동하며 요소를 클릭하거나 키를 입력하는 기본적인 코드입니다.*
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.naver.com')

search_box = driver.find_element(By.CSS_SELECTOR, "#query")
search_box.send_keys("인공지능")
search_box.send_keys(Keys.ENTER)

driver.quit()
```

### 2. `WebDriverWait`을 이용한 명시적 대기
*특정 요소가 클릭 가능한 상태가 될 때까지 기다리는 명시적 대기 코드입니다. 동적으로 로드되는 콘텐츠에 유용합니다.*
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# #comment_count 요소가 클릭 가능할 때까지 최대 10초 대기
element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#comment_count")))
element.click()
```

### 3. 공공 데이터 API 활용
*공공 데이터 포털에서 발급받은 API 키를 사용하여 데이터를 요청하고 JSON 형식으로 파싱하는 코드입니다.*
```python
import requests
import json

url = 'http://api.data.go.kr/openapi/tn_pubr_public_cltur_fstvl_api'
params ={
    'serviceKey' : 'YOUR_API_KEY',
    'pageNo' : 1,
    'numOfRows' : '100',
    'type' : 'json'
}

response = requests.get(url, params=params)
data = response.json()['response']['body']['items']
print(data[0])
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
