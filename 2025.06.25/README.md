# 💻 2025.06.25 - 학습 노트

---

## ✏️ 학습 내용

`Azure Document Intelligence` 서비스를 활용하여 문서 분석을 수행하는 방법을 학습했습니다. 이미지 파일이나 URL을 통해 문서를 서비스에 전송하고, OCR(광학 문자 인식), 폰트 스타일 감지, 수식 인식, 바코드 감지, 언어 감지 등 다양한 기능을 활용하여 문서에서 정보를 추출하는 과정을 실습했습니다. 비동기 분석 작업의 상태를 모니터링하고 최종 결과를 검색하는 방법을 익혀, 문서 처리 자동화 및 데이터 추출 솔루션 개발에 필요한 기초를 다졌습니다.

---

## 📁 파일 목록

- `document_intelligence.py`: `Azure Document Intelligence` 서비스를 사용하여 문서를 분석하는 Python 스크립트.
- `document_intelligence.http`: `document_intelligence.py`에서 사용되는 HTTP 요청 예제 파일.

---

## 📌 주요 코드

### 1. `Azure Document Intelligence`를 이용한 문서 분석
*이미지 파일이나 URL을 통해 문서를 `Azure Document Intelligence` 서비스에 전송하고 분석 결과를 비동기적으로 가져오는 코드입니다.*
```python
import os
import requests
import time

from dotenv import load_dotenv

load_dotenv()

DOCUEMNT_INTELLIGENCE_ENDPOINT_URL = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT_URL")
DOCUMENT_INTELLIGENCE_API_KEY = os.getenv("AZURE_DOCUMENT_INTELLIGENCE_API_KEY")

HEADERS = {"Ocp-Apim-Subscription-Key": DOCUMENT_INTELLIGENCE_API_KEY}

def analyze_document(
    data: str | bytes,
    service: str,
    model: str,
    api_version: str,
    content_type: str = "application/json",
) -> str | None:
    HEADERS["Content-Type"] = content_type

    params = {
        "api-version": api_version,
        "stringIndexType": "utf16CodeUnit",
        "features": "ocrHighResolution,styleFont,formulas,barcodes,languages",
    }

    post_kwargs = {
        "params": params,
        "headers": HEADERS,
    }

    if content_type == "application/json":
        post_kwargs["json"] = {"urlSource": data}
    elif content_type == "image/png":
        post_kwargs["data"] = data
    else:
        raise ValueError(f"Unsupported content_type: '{content_type}'")

    response = requests.post(
        f"{DOCUEMNT_INTELLIGENCE_ENDPOINT_URL}/{service}/documentModels/{model}:analyze",
        **post_kwargs,
    )

    return response.headers.get("operation-location")

def get_analyze_result(operation_location: str):
    def request_result():
        return requests.get(operation_location, headers=HEADERS).json()

    response_json = request_result()

    while response_json.get("status") == "running":
        time.sleep(1)
        response_json = request_result()

    return response_json

if __name__ == "__main__":
    result_url = analyze_document(
        data="https://raw.githubusercontent.com/Azure-Samples/cognitive-services-REST-api-samples/master/curl/form-recognizer/rest-api/read.png",
        service="documentintelligence",
        model="prebuilt-read",
        api_version="2024-11-30",
    )

    result = get_analyze_result(result_url)
    print(result)
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
