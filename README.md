# 💻 Microsoft AI School 공부 기록 - 김유빈

---

## 💡 소개

이 리포지토리는 Microsoft AI School에서 학습하고 기록한 내용을 담고 있습니다. Python, 데이터 분석, 인공지능 및 머신러닝 / 딥러닝 그리고 Azure AI Serice 등 다양한 개념과 기술을 체계적으로 학습하고, 이를 활용한 애플리케이션 개발 프로젝트까지의 기록을 담고 있습니다.

매일 학습한 내용은 **날짜별 폴더(예: `2025.04.10`)** 내에 커밋되어 있으며, 각 폴더에는 해당 날짜의 학습 노트, 코드 스니펫, 그리고 관련 자료들이 포함되어 있습니다.

## 🎯 학습 목표

- Python 프로그래밍 기초부터 실전까지 체계적으로 학습  
- Pandas, Numpy, Matplotlib 등 주요 데이터 분석 라이브러리를 활용한 실습을 통해 데이터 처리 및 시각화 
- Scikit-learn 기반의 머신러닝 알고리즘을 실습하며 회귀, 분류, 군집화 모델 구현 및 평가 
- 딥러닝 프레임워크를 활용해 신경망과 전이 학습을 적용해보고, 이미지 분류 등의 실습 문제 해결 
- Azure의 다양한 AI 서비스를 활용하여 클라우드 기반 AI 솔루션 개발  

## 🗓️ 학습 로드맵


| 날짜 | 주요 학습 내용 | 핵심 기술/라이브러리 |
| :--- | :--- | :--- |
| Foundational Python | 
| [2025.04.10](./2025.04.10/) | Python 기초 문법: 자료형, 변수, 연산자 | `Python` |
| [2025.04.11](./2025.04.11/) | Python 제어문: 조건문(if), 반복문(for, while) | `Python` |
| [2025.04.14](./2025.04.14/) | Python 자료구조(튜플, 세트, 딕셔너리) 및 코드 모듈화 | `Python` |
| Data Analysis | 
| [2025.04.16](./2025.04.16/) | **[Pandas]** `Pandas`를 활용한 데이터 분석 입문 (달 탐사 미션) | `Pandas`, `Matplotlib` |
| [2025.04.17](./2025.04.17/) | **[Pandas]** 여러 데이터 소스 병합 및 통합 분석 (유성우 미션) | `Pandas` |
| [2025.04.18](./2025.04.18/) | **[Pandas]** 대용량 분할 데이터 처리 및 시각화 (따릉이 미션) | `Pandas`, `Seaborn` |
| [2025.04.30](./2025.04.30/) | 데이터 과학 관련 다양한 학습 자료 모음 (데이터 전처리, Custom Vision 등) | `Pandas`, `Scikit-learn` |
| Machine Learning | 
| [2025.05.08](./2025.05.08/) | **[CV]** `OpenCV`를 활용한 컴퓨터 비전 기초: 이미지 입출력, 도형 그리기 | `OpenCV`, `Numpy` |
| [2025.05.15](./2025.05.15/) | **[ML]** 머신러닝 **회귀**: 선형/다항 회귀, 규제(Ridge, Lasso), 파이프라인 | `Scikit-learn`, `Statsmodels` |
| [2025.05.16](./2025.05.16/) | **[ML]** 머신러닝 **분류**: 교차 검증, GridSearchCV, 랜덤 포레스트 | `Scikit-learn` |
| [2025.05.19](./2025.05.19/) | **[Crawling & ML]** `BeautifulSoup`을 이용한 정적 웹 크롤링 및 K-Means 군집화 | `BeautifulSoup`, `Scikit-learn` |
| [2025.05.20](./2025.05.20/) | **[Crawling & NLP]** `Selenium`을 이용한 동적 웹 크롤링 및 OpenAPI 활용, 기초 자연어 처리 | `Selenium`, `WordCloud` |
| Deep Learning | 
| [2025.05.21](./2025.05.21/) | **[DL]** "밑바닥부터 시작하는 딥러닝" 실습: `NumPy`로 신경망, CNN 구현 | `Numpy`, `Matplotlib` |
| [2025.05.27](./2025.05.27/) | **[DL]** 이미지 분류 프로젝트: `TensorFlow`와 **전이 학습(Transfer Learning)** 활용 | `TensorFlow`, `Keras` |
| [2025.05.28](./2025.05.28/) | **[Deployment]** `Gradio`를 활용한 머신러닝 모델 데모 웹 앱 제작 | `Gradio` |
| Azure Ai Services | 
| [2025.06.18](./2025.06.18/) | **[Azure OpenAI]** `Azure OpenAI Service` 기반 지능형 앱 개발 입문, RAG 개념 소개 | `Azure OpenAI` |
| [2025.06.19](./2025.06.19/) | **[Azure OpenAI]** Azure OpenAI 심화: 프롬프트 엔지니어링, DALL-E, RAG 시스템 구축 | `Azure OpenAI`, `DALL-E` |
| [2025.06.23](./2025.06.23/) | **[Azure OpenAI]** RAG 시스템 직접 구축, Function Calling, 음성 API(Whisper, TTS) 활용 | `Azure OpenAI`, `Whisper`, `TTS` |
| Azure Ai Services Advanced | 
| [2025.06.24](./2025.06.24/) | **[Project]** `Gradio`와 `Azure OpenAI`를 결합한 다기능(채팅, 이미지, RAG) AI 앱 개발 | `Gradio`, `Azure OpenAI` |
| [2025.06.25](./2025.06.25/) | **[Project]** `Azure Document Intelligence` REST API를 활용한 OCR 및 문서 분석 | `Azure AI Services` |
| [2025.06.26](./2025.06.26/) | **[Project]** `Document Intelligence`와 `Gradio`를 결합한 OCR 앱 및 **AI 언어 서비스** 활용 | `Gradio`, `Azure AI Services` |
| [2025.06.27](./2025.06.27/) | **[Project]** `Azure Speech`(STT/TTS) 및 `Custom NER`을 활용한 대화형 AI 개발 | `Gradio`, `Azure AI Services` |
| [2025.06.30](./2025.06.30/) | **[Project]** `Gradio`와 `Azure OpenAI`를 활용한 다중 모드 AI 챗봇 개발 | `Gradio`, `Azure OpenAI`, `STT/TTS` |
| [2025.07.02](./2025.07.02/) | **[Project]** `Azure Vision & Face` API를 활용한 이미지 분석 앱 기반 구축 | `Gradio`, `Azure AI Services` |
| [2025.07.03](./2025.07.02/) | **[Project]** 이미지 분석 앱 UX 고도화: 동적 UI 및 `Pillow` 결과 처리 | `Gradio`, `Pillow` |
| [2025.07.04](./2025.07.04/) | **[Project]** `Azure Custom Vision` SDK를 활용한 객체 탐지 모델 구축 자동화 | `Azure Custom Vision`, `Pillow` |
| [2025.07.07](./2025.07.07/) | **[CV]** `OpenCV` 및 `YOLOv3`를 활용한 객체 탐지 | `OpenCV`, `YOLO` |
| [2025.07.08](./2025.07.08/) | **[CV]** `YOLOv3`와 `YOLOv8` 모델 비교 및 실습 | `YOLO`, `Ultralytics` |
| Web Frontend |
| [2025.07.09](./2025.07.09/) | **[HTML]** `HTML` 기본 및 시맨틱 태그 학습 | `HTML` |
| [2025.07.10](./2025.07.10/) | **[CSS]** `CSS`를 활용한 웹 페이지 스타일링 및 반응형 웹 구현 | `CSS` |
| [2025.07.11](./2025.07.11/) | **[JavaScript]** `JavaScript` 기본 문법 및 핵심 개념 | `JavaScript` |
| [2025.07.14](./2025.07.14/) | **[JavaScript]** `JavaScript` 심화 (함수형 프로그래밍, 비동기 처리, 웹 API) | `JavaScript` |
| [2025.07.15](./2025.07.15/) | **[JavaScript]** `JavaScript ES6+` 고급 문법 및 미니 프로젝트 | `JavaScript`, `ES6+` |
**_참고:_** 위의 표는 학습 진도에 따라 계속 업데이트될 예정입니다. 각 날짜 폴더에서 자세한 학습 내용을 확인하실 수 있습니다.


---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---