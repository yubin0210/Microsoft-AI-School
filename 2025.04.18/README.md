# 💻 2025.04.18 - 학습 노트

---

## ✏️ 학습 내용

서울시 공공자전거 '따릉이' 데이터를 활용하여 데이터 분석 및 시각화 프로젝트를 진행했습니다. 여러 CSV 파일로 나뉜 대여 이력 데이터를 `pandas`를 이용해 하나로 병합하고, `datetime` 객체를 다루어 '일자', '시간대', '요일', '주말구분' 등 의미 있는 파생 변수를 생성했습니다. 또한, 별도의 대여소 정보 파일을 불러와 기존 데이터와 병합하여 '대여구', '위도', '경도' 등 공간 정보를 추가했습니다. 마지막으로 `seaborn`과 `folium` 라이브러리를 사용하여 다양한 조건에 따른 이용 현황을 시각화하고, 지도 위에 대여소 위치를 표시하는 등 다각적인 분석을 수행했습니다.

---

## 📁 파일 목록

- `3_따릉이_미션.ipynb`: 서울시 공공자전거 '따릉이' 데이터를 분석하고 시각화하는 과정을 담은 Jupyter Notebook 파일입니다.
- `data/`: 분석에 사용된 원본 CSV 파일들이 들어있는 폴더입니다.
  - `bike_rent_1.csv` ~ `bike_rent_6.csv`: 2019년 6월 따릉이 대여 이력 데이터
  - `bike_shop.csv`: 따릉이 대여소 정보
  - `seoul.json`: 서울시 행정구역 경계 GeoJSON 데이터

---

## 📌 주요 코드

### 1. 여러 CSV 파일 병합
*여러 파일로 나뉘어 있는 데이터를 `for`문과 `pd.concat`을 이용해 하나의 DataFrame으로 합치는 코드입니다.*
```python
import pandas as pd

bikes_temp = {}
for i in range(6):
    bikes_temp[i] = pd.read_csv(f"./data/bike_rent_{i + 1}.csv")

bikes = pd.concat(bikes_temp, ignore_index=True)
```

### 2. `datetime` 객체를 이용한 파생 변수 생성
*`dt` 접근자를 사용하여 '대여일시' 컬럼에서 '일자', '시간대', '요일' 등 다양한 시간 관련 정보를 추출하는 코드입니다.*
```python
bikes["일자"] = bikes["대여일시"].dt.day
bikes["대여시간대"] = bikes["대여일시"].dt.hour

days = ["월", "화", "수", "목", "금", "토", "일"]
bikes["요일"] = bikes["대여일시"].dt.dayofweek.apply(lambda day: days[day])
```

### 3. `folium`을 이용한 지도 시각화
*대여소의 위도, 경도 정보를 활용하여 `folium`으로 지도 위에 위치를 표시하고, 이용 건수에 따라 원의 크기를 다르게 표현하는 코드입니다.*
```python
import folium

# 대여소별 이용 건수 계산
bike_shop_count = bikes.groupby("대여 대여소명")["자전거번호"].count().to_frame()

# 대여소 정보와 병합
bike_shop_map_data = pd.merge(bike_shop, bike_shop_count, left_on="대여소명", right_index=True)

# 지도 생성
seoul_map = folium.Map(location=[37.55, 126.99], zoom_start=11)

# 지도에 원 추가
for name, lat, lng, count in zip(bike_shop_map_data["대여소명"], bike_shop_map_data["위도"], bike_shop_map_data["경도"], bike_shop_map_data["자전거번호"]):
    folium.CircleMarker(
        [lat, lng],
        radius=count * 0.005, # 이용 건수에 비례하는 반지름
        popup=f"{name}: {count}",
        color="#3186cc",
        fill=True,
        fill_color="#3186cc",
    ).add_to(seoul_map)
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
