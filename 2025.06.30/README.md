# 💻 2025.06.30 - 학습 노트

---

## ✏️ 학습 내용

`Gradio`를 활용하여 `Azure OpenAI` 서비스의 챗봇 기능을 통합한 웹 애플리케이션을 구축했습니다. 이 애플리케이션은 사용자의 텍스트 입력을 받아 `Azure OpenAI` 챗 모델이 응답을 생성하고, 이 응답을 `Azure Speech Service`를 통해 음성으로 변환하여 사용자에게 제공합니다. 또한, 마이크를 통한 음성 입력(`STT`)과 텍스트를 음성으로 변환(`TTS`)하는 기능도 포함되어 있어, 음성 기반의 대화형 AI 경험을 제공합니다.

---

## 📁 파일 목록

- `main.py`: `Gradio` 웹 애플리케이션의 메인 파일로, 챗봇, 음성-텍스트 변환(STT), 텍스트-음성 변환(TTS) 기능을 통합한 사용자 인터페이스를 제공합니다.
- `services/openai_service.py`: `Azure OpenAI` API와의 상호작용을 담당하는 서비스 로직을 포함합니다. 챗봇 응답을 음성으로 변환하는 기능이 포함되어 있습니다.
- `data/`: 데이터 파일들이 포함된 폴더.
- `results/`: 결과 파일들이 저장되는 폴더.

---

## 📌 주요 코드

### 1. `Gradio`를 이용한 챗봇 및 음성 기능 통합 웹 애플리케이션
*`Gradio`의 `gr.Blocks()`를 사용하여 챗봇, STT, TTS 기능을 통합한 사용자 인터페이스를 정의하는 코드입니다.*
```python
import gradio as gr
import sys
import os

# 필요한 모듈 경로 추가
current_dir = os.path.dirname(os.path.abspath(__file__))
directories_to_add = ["2025.06.24", "2025.06.27"]
for directory in directories_to_add:
    path_to_add = os.path.abspath(os.path.join(current_dir, "..", directory))
    if path_to_add not in sys.path: sys.path.append(path_to_add)

from speech import transcribe_audio, synthesize_speech, get_voice_list
from services.openai_service import OpenAIService

if __name__ == "__main__":
    with gr.Blocks() as demo:
        openai_service = OpenAIService()
        with gr.Row():
            with gr.Column():
                chatbot = gr.Chatbot(type="messages")
                user_input = gr.Textbox(label="Message", placeholder="Enter your message here...")
                send_button = gr.Button("Send")

                send_button.click(
                    fn=openai_service.chat,
                    inputs=[user_input, chatbot],
                    outputs=[user_input, chatbot, gr.Audio(visible=True)], # output_audio를 visible하게 설정
                )
                user_input.submit(
                    fn=openai_service.chat,
                    inputs=[user_input, chatbot],
                    outputs=[user_input, chatbot, gr.Audio(visible=True)],
                )

            with gr.Column():
                gr.Markdown("# Speech to Text")
                input_audio = gr.Audio(label="음성 입력", type="filepath", sources=["microphone"])
                output_text = gr.Textbox(label="음성 인식 결과", interactive=False)
                input_audio.change(
                    lambda audio_path: (
                        transcribe_audio(audio_path, language="ko-KR").get("DisplayText")
                        if audio_path is not None
                        else ""
                    ),
                    inputs=[input_audio],
                    outputs=[output_text],
                )

                gr.Markdown("# Text to Speech")
                input_text = gr.Textbox(label="텍스트 입력", placeholder="텍스트를 입력하고 음성으로 변환합니다.")
                voice_list = gr.Dropdown(label="음성 선택", choices=get_voice_list())
                submit_button = gr.Button("음성 생성")
                output_audio = gr.Audio(label="음성 출력", type="filepath", interactive=False, autoplay=True)
                submit_button.click(
                    lambda text, voice: synthesize_speech(text, voice),
                    inputs=[input_text, voice_list],
                    outputs=[output_audio],
                )

    demo.launch()
```

### 2. `OpenAIService`의 챗 기능 (`services/openai_service.py`)
*`Azure OpenAI` 챗 모델과 상호작용하며, 챗봇 응답을 음성으로 변환하여 반환하는 코드입니다.*
```python
import os
import sys
from typing import Any, Dict, List, Optional
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

# speech 모듈 임포트 (경로 설정 필요)
current_dir = os.path.dirname(os.path.abspath(__file__))
directories_to_add = ["2025.06.27"]
for directory in directories_to_add:
    path_to_add = os.path.abspath(os.path.join(current_dir, "..", directory))
    if path_to_add not in sys.path: sys.path.append(path_to_add)
from speech import synthesize_speech

class OpenAIService:
    def __init__(self) -> None:
        self.chat_client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version="2024-12-01-preview",
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_URL"),
        )
        self.chat_system_prompt: Dict[str, Any] = {
            "role": "system",
            "content": "사용자가 정보를 찾는 데 도움이 되는 AI professional assistant입니다.",
        }

    def chat(
        self,
        prompt: str,
        history: List[List[str]],
        args: Optional[Dict[str, Any]] = None,
    ) -> tuple[str, list[list[str]]]:
        if not prompt: return "", history, None
        messages: List[Dict[str, Any]] = [self.chat_system_prompt]
        messages.extend(history)
        messages.append({"role": "user", "content": prompt})

        response_message = self._request_to_openai(messages, args)
        messages.append({"role": "assistant", "content": response_message.content})

        return "", messages, synthesize_speech(response_message.content, "ko-KR-YuJinNeural")

    def _request_to_openai(
        self,
        messages: List[Dict[str, Any]],
        args: Optional[Dict[str, Any]] = None,
    ) -> Any:
        response = self.chat_client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=messages,
            max_tokens=args.get("max_tokens", 16384),
            temperature=args.get("temperature", 0.7),
            top_p=args.get("top_p", 0.95),
            frequency_penalty=args.get("frequency_penalty", 0),
            presence_penalty=args.get("presence_penalty", 0),
            stop=args.get("stop", None),
            stream=args.get("stream", False),
            extra_body=args.get("extra_body", {}),
        )
        return response.choices[0].message
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
