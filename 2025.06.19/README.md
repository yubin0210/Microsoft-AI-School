# 💻 2025.06.19 - 학습 노트

---

## ✏️ 학습 내용

`Azure OpenAI` API의 기본적인 사용법을 학습했습니다. 환경 변수 설정을 통해 API 키와 엔드포인트를 관리하고, `AzureOpenAI` 클라이언트를 초기화하는 방법을 익혔습니다. 사용자의 입력을 받아 `OpenAI` 모델에 전송하고, 모델의 응답을 받아 출력하는 간단한 챗봇 애플리케이션을 구현했습니다. 이를 통해 `Azure OpenAI` 서비스를 활용하여 대화형 AI 기능을 개발하는 기초를 다졌습니다.

---

## 📁 파일 목록

- `Labfiles/`: 랩 실습 파일들이 포함된 폴더입니다.
  - `02-azure-openai-api/`: `Azure OpenAI` API의 기본적인 사용법을 다루는 랩 파일입니다.
    - `main.py`: `Azure OpenAI` API를 사용하여 간단한 챗봇 기능을 구현하는 메인 스크립트.
    - `Python/test-openai-model.py`: `Azure OpenAI` 모델 테스트를 위한 예제 스크립트.
    - `text-files/`: 텍스트 파일들이 포함된 폴더 (주로 예제 데이터).

---

## 📌 주요 코드

### 1. `Azure OpenAI` 클라이언트 초기화 및 챗봇 구현
*환경 변수에서 API 설정 값을 로드하고, `AzureOpenAI` 클라이언트를 초기화하여 챗 모델과 상호작용하는 코드입니다.*
```python
import os
from dotenv import load_dotenv
from openai import AzureOpenAI

def main():
    try:
        load_dotenv()
        azure_openai_key = os.getenv("AZURE_OPENAI_API_KEY")
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT_URL")
        azure_openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

        client = AzureOpenAI(
            azure_endpoint=azure_openai_endpoint,
            api_key=azure_openai_key,
            api_version="2025-01-01-preview",
        )

        while True:
            input_text = input("Enter the prompt (or type 'quit' to exit): ")
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            messages = [
                {"role": "user", "content": input_text},
            ]

            completion = client.chat.completions.create(
                model=azure_openai_deployment,
                messages=messages,
                max_tokens=800,
                temperature=0.8,
                top_p=0.95,
            )
            print(completion.choices[0].message.content)

    except Exception as ex:
        print(ex)

if __name__ == "__main__":
    main()
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
