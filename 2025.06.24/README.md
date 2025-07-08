# 💻 2025.06.24 - 학습 노트

---

## ✏️ 학습 내용

`Gradio`를 활용하여 `Azure OpenAI` 서비스의 다양한 기능을 통합한 웹 애플리케이션을 구축했습니다. 주요 기능으로는 챗봇, 이미지 생성(`DALL-E`), 웹 검색, 그리고 `Azure AI Search`를 활용한 일본 여행 정보 검색(`RAG` 패턴)이 있습니다. 이를 통해 사용자와의 상호작용을 위한 직관적인 웹 인터페이스를 설계하고, `OpenAI` 모델의 강력한 기능을 활용하여 다양한 질의에 응답하며, 외부 데이터를 연동하여 정보의 정확성과 풍부함을 높이는 방법을 학습했습니다.

---

## 📁 파일 목록

- `main.py`: `Gradio` 웹 애플리케이션의 메인 파일로, 다양한 `OpenAI` 서비스 기능을 통합한 사용자 인터페이스를 제공합니다.
- `services/openai_service.py`: `Azure OpenAI` API와의 상호작용을 담당하는 서비스 로직을 포함합니다. 챗봇, 이미지 생성, 웹 검색, 그리고 `Azure AI Search`를 활용한 `RAG` 패턴 구현이 포함되어 있습니다.
- `utils/duckduckgo.py`: 웹 검색 기능을 위한 유틸리티 파일입니다.

---

## 📌 주요 코드

### 1. `Gradio`를 이용한 웹 애플리케이션 구조
*`Gradio`의 `gr.Blocks()`를 사용하여 여러 탭으로 구성된 사용자 인터페이스를 정의하는 코드입니다.*
```python
import gradio as gr
from services.openai_service import OpenAIService

if __name__ == "__main__":
    openai_service = OpenAIService()

    with gr.Blocks() as demo:
        with gr.Tab("채팅"):
            chatbot = gr.Chatbot(label="채팅")
            input_textbox = gr.Textbox(label="메시지를 입력하세요.")
            submit_button = gr.Button("채팅 전송")

            submit_button.click(
                fn=openai_service.chat,
                inputs=[input_textbox, chatbot],
                outputs=[input_textbox, chatbot],
            )
            input_textbox.submit(
                fn=openai_service.chat,
                inputs=[input_textbox, chatbot],
                outputs=[input_textbox, chatbot],
            )

        with gr.Tab("이미지 생성"):
            image_prompt_textbox = gr.Textbox(label="이미지 생성 프롬프트")
            image_submit_button = gr.Button("이미지 생성")
            image_output_image = gr.Image(label="생성된 이미지")

            image_submit_button.click(
                fn=openai_service.generate_image,
                inputs=[image_prompt_textbox],
                outputs=[image_output_image],
            )
            image_prompt_textbox.submit(
                fn=openai_service.generate_image,
                inputs=[image_prompt_textbox],
                outputs=[image_output_image],
            )

        # ... (텍스트 검색, 일본 여행 정보 탭은 생략)

    demo.launch()
```

### 2. `OpenAIService`의 챗 기능 (`services/openai_service.py`)
*`Azure OpenAI` 챗 모델과 상호작용하며, 필요에 따라 웹 검색 도구를 호출하여 답변을 강화하는 코드입니다.*
```python
import os
import json
from typing import Any, Dict, List, Optional
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

class OpenAIService:
    def __init__(self) -> None:
        self.chat_client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-12-01-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_URL"),
        )
        self.chat_system_prompt: Dict[str, Any] = {
            "role": "system",
            "content": "사용자가 정보를 찾는 데 도움이 되는 AI professional assistant. 검색어는 영문으로 번역 한 뒤 진행, 검색 결과는 한글로 정리",
        }

    def chat(
        self,
        prompt: str,
        history: List[List[str]],
        tools: Optional[List[Dict[str, Any]]] = None,
        args: Optional[Dict[str, Any]] = None,
    ) -> tuple[str, list[list[str]]]:
        messages: List[Dict[str, Any]] = [self.chat_system_prompt]
        for h in history:
            if h[0]: messages.append({"role": "user", "content": h[0]})
            if h[1]: messages.append({"role": "assistant", "content": h[1]})
        messages.append({"role": "user", "content": prompt})

        response_message = self._request_to_openai(messages, tools, args)

        if response_message.tool_calls:
            # ... (도구 호출 처리 로직 생략)
            pass

        if response_message.content:
            history.append([prompt, response_message.content])
            
        return "", history

    def _request_to_openai(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
        args: Optional[Dict[str, Any]] = None,
    ) -> Any:
        response = self.chat_client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=messages,
            tools=tools,
            max_tokens=args.get("max_tokens", 16384),
            temperature=args.get("temperature", 0.7),
            # ... (기타 파라미터 생략)
        )
        return response.choices[0].message

    # ... (generate_image, search, japan_travel 메서드 생략)
```

### 3. `OpenAIService`의 일본 여행 정보 검색 기능 (`services/openai_service.py`)
*`Azure AI Search`를 데이터 소스로 활용하여 일본 여행 관련 질문에 답변하는 `RAG` 패턴 구현 코드입니다.*
```python
# ... (OpenAIService 클래스 내부)

    def japan_travel(
        self,
        prompt: str,
        history: List[List[str]],
    ) -> tuple[str, list[list[str]]]:
        data_sources = [
            {
                "type": "azure_search",
                "parameters": {
                    "endpoint": os.getenv("AZURE_OPENAI_SEARCH_ENDPOINT_URL"),
                    "index_name": os.getenv("AZURE_OPENAI_SEARCH_INDEX"),
                    "semantic_configuration": os.getenv("AZURE_OPENAI_SEARCH_SEMANTIC"),
                    "query_type": "semantic",
                    "strictness": 3,
                    "top_n_documents": 20,
                    "authentication": {
                        "type": "api_key",
                        "key": os.getenv("AZURE_OPENAI_SEARCH_API_KEY"),
                    },
                },
            }
        ]

        return self.chat(
            prompt, history, args={"extra_body": {"data_sources": data_sources}}
        )
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
