# 💻 2025.04.17 - 학습 노트

---

## ✏️ 학습 내용

여러 개의 CSV 데이터 소스를 `pandas`를 사용하여 통합하고 분석하는 방법을 학습했습니다. 유성우, 달의 위상, 별자리, 도시 데이터를 각각 불러와 필요한 형태로 가공했습니다. 문자열로 된 월(month) 정보를 숫자형으로 변환하고, 날짜 관련 컬럼들을 `datetime` 객체로 만들어 시계열 데이터를 다룰 수 있도록 준비했습니다. 또한, 불필요한 컬럼을 제거하고 데이터를 정제하여 분석에 용이한 형태로 만드는 과정을 실습했습니다.

---

## 📁 파일 목록

- `2_유성우_미션.ipynb`: 유성우 관련 데이터를 종합적으로 분석하고 가공하는 과정을 담은 Jupyter Notebook 파일입니다.
- `data/`: 분석에 사용된 원본 CSV 파일들이 들어있는 폴더입니다.
  - `meteorshowers.csv`: 유성우 정보
  - `moonphases.csv`: 월별 위상 정보
  - `constellations.csv`: 별자리 정보
  - `cities.csv`: 도시 위도 정보

---

## 📌 주요 코드

### 1. 여러 데이터 소스 불러오기
*분석에 필요한 여러 CSV 파일들을 `pandas` DataFrame으로 읽어오는 코드입니다.*
```python
import pandas as pd

meteor_showers = pd.read_csv('data/meteorshowers.csv')
moon_phases = pd.read_csv('data/moonphases.csv')
constellations = pd.read_csv('data/constellations.csv')
cities = pd.read_csv('data/cities.csv')
```

### 2. 데이터 타입 변환 (월 -> 숫자, 날짜 -> Datetime)
*문자열로 된 월(Month) 데이터를 숫자로 바꾸고, 날짜 관련 정보를 `datetime` 객체로 변환하는 코드입니다.*
```python
# 월 이름을 숫자로 매핑하는 딕셔너리 생성
months = {'january':1, 'february':2, ... , 'december':12}

# 'bestmonth' 컬럼의 월 이름을 숫자로 변환
meteor_showers['bestmonth'] = meteor_showers['bestmonth'].map(months)

# 날짜 형식의 문자열을 datetime 객체로 변환
meteor_showers['startdate'] = pd.to_datetime('2020-' + meteor_showers['startmonth'].astype(str) + '-' + meteor_showers['startday'].astype(str))
```

### 3. 불필요한 컬럼 제거
*분석에 사용하지 않을 컬럼들을 `drop` 메소드를 사용하여 제거하는 코드입니다.*
```python
# 여러 컬럼을 한 번에 제거
meteor_showers.drop(['startmonth', 'endmonth', 'startday', 'endday', 'hemisphere'], axis=1, inplace=True)
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
