# 💻 2025.04.16 - 학습 노트

---

## ✏️ 학습 내용

`pandas` 라이브러리를 활용한 데이터 분석 및 전처리 기술을 학습했습니다. CSV 파일을 DataFrame으로 불러와 기본적인 정보를 탐색하고, 결측치를 확인 및 처리하는 방법을 익혔습니다. 또한, 데이터의 단위를 변환하고, `groupby`를 이용해 데이터를 집계하며, 여러 DataFrame을 병합하고 차이를 계산하는 등 실질적인 데이터 가공 및 분석 작업을 수행했습니다.

---

## 📁 파일 목록

- `1_달탐사_미션.ipynb`: `pandas`를 사용하여 월석 샘플 데이터를 분석하는 과정을 담은 Jupyter Notebook 파일입니다.
- `data/rocksamples.csv`: 아폴로 임무에서 수집된 월석 샘플에 대한 원본 데이터 파일입니다.

---

## 📌 주요 코드

### 1. 데이터 불러오기 및 기본 전처리
*CSV 파일을 `pandas` DataFrame으로 읽어오고, 무게 단위를 변환하며 컬럼명을 수정하는 코드입니다.*
```python
import pandas as pd

# 데이터 파일을 읽어오기
rock_samples = pd.read_csv('data/rocksamples.csv')

# 무게 단위를 g에서 kg으로 변환
rock_samples['Weight (kg)'] = rock_samples['Weight (g)'].apply(lambda weight: weight / 1000.0)

# 컬럼명 변경
rock_samples.rename(columns={'Weight (g)': 'Weight (kg)'}, inplace=True)
```

### 2. `groupby`를 이용한 데이터 집계
*임무(Mission)별로 샘플의 총 무게를 계산하는 코드입니다.*
```python
# 'Mission' 컬럼을 기준으로 그룹화하여 'Weight (kg)'의 합계를 계산
sample_total_weight = rock_samples.groupby('Mission')['Weight (kg)'].sum()

# 새로운 DataFrame과 병합
missions = pd.DataFrame()
missions['Mission'] = rock_samples['Mission'].unique()
missions = pd.merge(missions, sample_total_weight, on='Mission')
```

### 3. 파생 변수 추가
*계산된 값을 바탕으로 임무 간 샘플 무게 차이, 달 착륙선 정보 등 새로운 컬럼을 추가하는 코드입니다.*
```python
# 임무간 중량 차이 컬럼 추가
missions['Weight diff'] = missions['Sample Weight (kg)'].diff()

# 달 착륙선 정보 추가
lunar_module = ['Eagle (LM-5)', 'Intrepid (LM-6)', 'Antares (LM-8)', 'Falcon (LM-10)', 'Orion (LM-11)', 'Challenger (LM-12)']
missions['Lunar Module(LM)'] = lunar_module
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
