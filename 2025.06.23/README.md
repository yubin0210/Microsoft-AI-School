# 💻 2025.06.23 - 학습 노트 

---

## ✏️ 학습 내용

`OpenAI` API의 다양한 기능을 활용하는 방법을 학습했습니다. 텍스트 기반 질의응답, 이미지 분석을 통한 코드 설명 등 기본적인 `OpenAI` 모델 활용법을 익혔습니다. 특히, 외부 문서를 참조하여 답변을 생성하는 `RAG` (Retrieval-Augmented Generation) 패턴을 구현하는 방법을 심층적으로 다루었습니다. 또한, 텍스트를 음성으로 변환하는 `TTS` (Text-to-Speech) 기능과 음성 파일을 텍스트로 변환하는 `Whisper` (Speech-to-Text) 기능을 실습하여 `OpenAI`의 멀티모달 기능을 활용하는 능력을 향상시켰습니다.

---

## 📁 파일 목록

- `openai.ipynb`: `OpenAI` API의 기본적인 텍스트 및 이미지 분석 기능을 활용하는 실습.
- `openai_add.ipynb`: `OpenAI` API에 추가적인 기능을 활용하는 실습.
- `openai_rag.ipynb`: `RAG` (Retrieval-Augmented Generation) 패턴을 구현하는 실습.
- `openai_references.ipynb`: `RAG` 패턴에서 참조 문서를 활용하는 방법을 보여주는 실습.
- `openai_tts.ipynb`: `OpenAI`의 텍스트-음성 변환 (TTS) 기능을 활용하는 실습.
- `openai_whisper.ipynb`: `OpenAI`의 음성-텍스트 변환 (Whisper) 기능을 활용하는 실습.
- `data/`: 실습에 사용되는 데이터 파일들이 포함된 폴더.

---

## 📌 주요 코드

### 1. `OpenAI` API를 이용한 텍스트 질의응답
*`requests` 라이브러리를 사용하여 `OpenAI` API에 텍스트 메시지를 보내고 응답을 받는 코드입니다.*
```python
import requests

endpoint = "YOUR_OPENAI_ENDPOINT"
headers = {"Content-Type": "application/json", "api-key": "YOUR_API_KEY"}

payload = {
    "messages": [{"role": "system", "content": "You are a helpful assistant."},
                 {"role": "user", "content": "What is the capital of France?"}],
    "temperature": 0.8,
    "top_p": 0.95,
    "max_tokens": 800,
}

response = requests.post(endpoint, headers=headers, json=payload)
print(response.json()["choices"][0]["message"]["content"])
```

### 2. `OpenAI` API를 이용한 이미지 분석 (코드 설명)
*이미지 파일을 Base64로 인코딩하여 `OpenAI` API에 보내고, 이미지에 대한 설명을 요청하는 코드입니다.*
```python
import os
import base64
from openai import AzureOpenAI

# API 설정 (환경 변수 또는 직접 설정)
endpoint = os.getenv("ENDPOINT_URL", "YOUR_ENDPOINT")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o-mini")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "YOUR_API_KEY")

client = AzureOpenAI(azure_endpoint=endpoint, api_key=subscription_key, api_version="2025-01-01-preview")

image_path = "./backend.png" # 분석할 이미지 파일 경로
image_base64 = base64.b64encode(open(image_path, "rb").read()).decode("ascii")

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": [
        {"type": "text", "text": "다음 이미지를 읽고 일부 코드에 대한 설명을 진행해줘"},
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}}
    ]}
]

completion = client.chat.completions.create(model=deployment, messages=messages, max_tokens=800)
print(completion.choices[0].message.content)
```

### 3. `OpenAI` TTS (Text-to-Speech) 기능 활용
*텍스트를 음성 파일로 변환하는 코드입니다.*
```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

speech_file_path = "./speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input="안녕하세요. OpenAI TTS 기능 테스트입니다."
)
response.stream_to_file(speech_file_path)
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
