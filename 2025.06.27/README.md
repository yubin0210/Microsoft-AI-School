# 💻 2025.06.27 - 학습 노트

---

## ✏️ 학습 내용

`Azure AI Language` 서비스의 Custom NER(사용자 지정 명명된 개체 인식) 기능과 `Azure Speech Service`의 음성-텍스트 변환(STT) 및 텍스트-음성 변환(TTS) 기능을 학습했습니다. Custom NER을 통해 텍스트에서 특정 엔티티를 추출하는 작업을 제출하고 그 결과를 비동기적으로 가져오는 방법을 익혔습니다. `Gradio`를 활용한 웹 인터페이스를 통해 음성 파일을 텍스트로 변환하거나 텍스트를 음성으로 변환하는 실습을 진행하여, 음성 기반 AI 서비스 개발에 필요한 기술을 습득했습니다.

---

## 📁 파일 목록

- `custom_ner.py`: `Azure AI Language` 서비스의 Custom NER 기능을 사용하여 텍스트에서 사용자 지정 엔티티를 추출하는 Python 스크립트.
- `custom_ner.http`: `custom_ner.py`에서 사용되는 HTTP 요청 예제 파일.
- `speech.py`: `Azure Speech Service`의 음성-텍스트 변환(STT) 및 텍스트-음성 변환(TTS) 기능을 `Gradio` 인터페이스와 함께 구현한 Python 스크립트.
- `speech.http`: `speech.py`에서 사용되는 HTTP 요청 예제 파일.
- `data/`: 실습에 사용되는 데이터 파일들이 포함된 폴더 (예: 음성 파일, 텍스트 파일).

---

## 📌 주요 코드

### 1. `Azure AI Language` Custom NER 작업 제출 및 결과 폴링
*텍스트에서 사용자 지정 엔티티를 추출하는 Custom NER 작업을 제출하고, 작업 상태를 폴링하여 결과를 가져오는 코드입니다.*
```python
import os
import requests
import time
import json
from dotenv import load_dotenv

load_dotenv()

# 환경 변수 로드 (생략)

def submit_ner_job(document_text: str) -> str | None:
    # ... (환경 변수 확인 및 payload 구성 생략)
    job_payload = {
        "displayName": "Extracting entities from loan agreements",
        "analysisInput": {"documents": [{"id": "1", "language": "en-us", "text": document_text}]},
        "tasks": [{
            "kind": "CustomEntityRecognition",
            "taskName": "Entity Recognition",
            "parameters": {"projectName": os.getenv("AZURE_CUSTOM_NER_PROJECT_NAME"), "deploymentName": os.getenv("AZURE_CUSTOM_NER_DEPLOYMENT_NAME")}
        }]
    }
    headers = {"Content-Type": "application/json", "Ocp-Apim-Subscription-Key": os.getenv("AZURE_CUSTOM_NER_API_KEY")}
    url = f"{os.getenv("AZURE_CUSTOM_NER_ENDPOINT_URL")}/language/analyze-text/jobs?api-version={os.getenv("AZURE_CUSTOM_NER_API_VERSION")}"
    response = requests.post(url, headers=headers, json=job_payload)
    if response.status_code == 202: return response.headers.get("operation-location")
    return None

def get_ner_result(job_url: str):
    headers = {"Ocp-Apim-Subscription-Key": os.getenv("AZURE_CUSTOM_NER_API_KEY")}
    while True:
        response = requests.get(job_url, headers=headers)
        if response.status_code == 200:
            result = response.json()
            status = result.get("status")
            if status == "succeeded": return result
            time.sleep(2)
        else: return None

if __name__ == "__main__":
    # ... (파일 읽기 및 함수 호출 생략)
    pass
```

### 2. `Azure Speech Service` 음성-텍스트 변환 (STT)
*오디오 파일을 `Azure Speech Service`에 전송하여 텍스트로 변환하는 코드입니다.*
```python
import os
import requests
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

def transcribe_audio(audio_path: str, language: str = "en-US") -> dict | None:
    speech_key = os.getenv("AZURE_SPEECH_API_KEY")
    speech_region = os.getenv("AZURE_SPEECH_REGION")
    url = f"https://{speech_region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1?language={language}&format=detailed"
    headers = {"Ocp-Apim-Subscription-Key": speech_key, "Content-Type": "audio/wav"}
    try:
        with open(audio_path, "rb") as audio_file: audio_data = audio_file.read()
        response = requests.post(url, headers=headers, data=audio_data, timeout=30)
        response.raise_for_status()
        return response.json()
    except Exception as e: gr.Error(f"API 요청 중 오류가 발생했습니다: {e}"); return None

# ... (Gradio 인터페이스 코드 생략)
```

### 3. `Azure Speech Service` 텍스트-음성 변환 (TTS)
*텍스트를 `Azure Speech Service`에 전송하여 음성 파일로 변환하는 코드입니다.*
```python
import os
import requests
import gradio as gr
import time
from dotenv import load_dotenv

load_dotenv()

def synthesize_speech(text: str, voice_name: str) -> str | None:
    speech_key = os.getenv("AZURE_SPEECH_API_KEY")
    speech_region = os.getenv("AZURE_SPEECH_REGION")
    url = f"https://{speech_region}.tts.speech.microsoft.com/cognitiveservices/v1"
    headers = {
        "Ocp-Apim-Subscription-Key": speech_key,
        "Content-Type": "application/ssml+xml",
        "X-Microsoft-OutputFormat": "audio-16khz-128kbitrate-mono-mp3",
        "User-Agent": "curl",
    }
    language = "-".join(voice_name.split("-")[0:2])
    ssml_body = f"""<speak version='1.0' xml:lang='{language}'><voice xml:lang='{language}' name='{voice_name}'>{text}</voice></speak>"""
    try:
        response = requests.post(url, headers=headers, data=ssml_body.encode("utf-8"), timeout=30)
        response.raise_for_status()
        output_dir = os.path.join(os.path.dirname(__file__), "data", "speech", "output")
        os.makedirs(output_dir, exist_ok=True)
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        output_audio_path = os.path.join(output_dir, f"output_{timestamp}.mp3")
        with open(output_audio_path, "wb") as audio_file: audio_file.write(response.content)
        gr.Info(f"음성 파일이 '{output_audio_path}' 경로에 저장되었습니다.")
        return output_audio_path
    except Exception as e: gr.Error(f"API 요청 중 오류가 발생했습니다: {e}"); return None

# ... (Gradio 인터페이스 코드 생략)
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
