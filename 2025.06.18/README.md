# 💻 2025.06.18 - 학습 노트

---

## ✏️ 학습 내용

### 1. Azure OpenAI Service를 활용한 애플리케이션 개발

Azure OpenAI Service의 REST API와 Python SDK를 사용하여 챗봇 애플리케이션을 개발하는 방법을 학습했습니다. 특히, 프롬프트 엔지니어링 기술을 활용하여 생성형 AI 모델의 응답을 제어하고, 시스템 메시지, 사용자 메시지, few-shot 학습 등을 통해 모델의 응답 형식과 톤을 조정하는 방법을 익혔습니다. 또한, `grounding.txt` 파일을 통해 외부 데이터를 모델에 제공하고, 대화 기록을 유지하여 문맥을 이해하는 챗봇을 구현하는 실습을 진행했습니다.

### 2. (미완료) Azure OpenAI Service와 함께 자체 데이터 사용 (RAG)

검색 증강 생성(Retrieval Augmented Generation, RAG)을 구현하여 자체 데이터를 Azure OpenAI 모델과 함께 사용하는 방법을 학습하기 시작했습니다. Azure AI Search를 사용하여 데이터를 인덱싱하고, 이를 Azure OpenAI 프롬프트에 보강하여 사용하는 과정을 다룹니다. (다음 날짜에 이어서 진행 예정)

---

## 📁 파일 목록

- `Instructions/`: 실습 안내 Markdown 문서
  - `Labs/`
    - `01-app-develop.md`: Azure OpenAI Service를 사용한 애플리케이션 개발 실습 가이드
    - `02-use-own-data.md`: 자체 데이터를 활용한 RAG 구현 실습 가이드
  - `Exercises/`: (내용 없음)
- `Labfiles/`: 실습용 소스 코드 및 데이터
  - `01-app-develop/`
    - `Python/`
      - `application.py`: 시스템 프롬프트, 사용자 입력, 대화 기록을 관리하며 Azure OpenAI 모델과 상호작용하는 메인 애플리케이션 스크립트
      - `system.txt`: 챗봇의 역할과 응답 톤을 정의하는 시스템 메시지 파일
      - `grounding.txt`: 모델에 추가적인 컨텍스트를 제공하기 위한 데이터 파일
    - `openai.ipynb`: `requests` 라이브러리와 `openai` SDK를 사용하여 Azure OpenAI API의 기본적인 호출 방법을 테스트하는 Jupyter Notebook
  - `(02-use-own-data/는 다음 날짜에 이어서 진행될 수 있음)`

---

## 📌 주요 코드

### 1. `openai` SDK를 이용한 비동기 챗봇 애플리케이션 (`application.py`)

*`openai` 라이브러리의 `AsyncAzureOpenAI` 클라이언트를 사용하여 비동기적으로 Azure OpenAI 모델을 호출하고, `system.txt`와 `grounding.txt` 파일을 읽어와 대화의 컨텍스트를 설정하는 코드입니다.*

```python
import os
import asyncio
from dotenv import load_dotenv
from openai import AsyncAzureOpenAI

async def main():
    try:
        load_dotenv()
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT_URL")
        azure_openai_key = os.getenv("AZURE_OPENAI_API_KEY")
        azure_openai_deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

        client = AsyncAzureOpenAI(
            azure_endpoint=azure_openai_endpoint,
            api_key=azure_openai_key,
            api_version="2024-02-15-preview"
        )

        # Initialize messages array with grounding context
        print("\nAdding grounding context from grounding.txt")
        grounding_text = open(file="grounding.txt", encoding="utf8").read().strip()
        messages_array = [{"role": "user", "content": grounding_text}]

        while True:
            print("------------------\nPausing the app to allow you to change the system prompt.\nPress enter to continue...")
            input()

            system_text = open(file="./system.txt", encoding="utf8").read().strip()
            user_text = input("Enter user message, or 'quit' to exit: ")
            if user_text.lower() == "quit":
                break

            # Append system and user messages to the array
            messages_array.append({"role": "system", "content": system_text})
            messages_array.append({"role": "user", "content": user_text})

            await call_openai_model(
                messages=messages_array,
                model=azure_openai_deployment,
                client=client
            )

    except Exception as ex:
        print(ex)

async def call_openai_model(messages, model, client):
    print("\nSending request to Azure OpenAI model...\n")

    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
        max_tokens=800
    )

    print("Response:\n" + response.choices[0].message.content + "\n")
    # Append assistant's response to maintain chat history
    messages.append({"role": "assistant", "content": response.choices[0].message.content})

if __name__ == "__main__":
    asyncio.run(main())
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---

```