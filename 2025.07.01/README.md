# 💻 2025.07.01 - 학습 노트

---

## ✏️ 학습 내용

`Gradio`를 활용하여 `Azure Speech Service`의 음성-텍스트 변환(STT) 및 텍스트-음성 변환(TTS) 기능을 통합한 웹 인터페이스를 구축했습니다. 사용자가 마이크를 통해 음성을 입력하면 텍스트로 변환하고, 텍스트를 입력하면 다양한 음성으로 변환하여 재생할 수 있습니다. 또한, `GPT` 모델과의 연동을 통해 음성으로 질문하고 음성으로 답변을 받는 대화형 AI 시스템의 가능성을 탐색했습니다. 이를 통해 음성 기반의 사용자 인터페이스를 개발하는 기술을 습득했습니다.

---

## 📁 파일 목록

- `speech.ipynb`: `Gradio`를 사용하여 `Azure Speech Service`의 STT 및 TTS 기능을 통합하고, `GPT` 모델과의 연동을 시도하는 Jupyter Notebook 파일.

---

## 📌 주요 코드

### 1. `Gradio`를 이용한 STT/TTS 웹 인터페이스
*`Gradio`의 `gr.Blocks()`를 사용하여 음성 입력, 텍스트 변환, 텍스트 입력, 음성 변환 기능을 포함하는 웹 인터페이스를 정의하는 코드입니다.*
```python
import gradio as gr
import requests
import os
import dotenv

dotenv.load_dotenv()

# STT(음성 → 텍스트) 요청 함수
def request_stt(audio_path):
    endpoint = f"{os.getenv('AZURE_SPEECH_ENDPOINT_URL')}/speech/recognition/conversation/cognitiveservices/v1?language=ko-KR"
    headers = {"Ocp-Apim-Subscription-Key": os.getenv('AZURE_SPEECH_API_KEY')}
    with open(audio_path, "rb") as audio_file: audio_data = audio_file.read()
    response = requests.post(endpoint, headers=headers, data=audio_data)
    if response.status_code != 200: return None
    return response.json()["DisplayText"]

# TTS(텍스트 → 음성) 요청 함수
def request_tts(text, voice="ko-KR-SunHiNeural"):
    endpoint = f"{os.getenv('AZURE_SPEECH_ENDPOINT_URL')}/cognitiveservices/v1"
    headers = {
        "Ocp-Apim-Subscription-Key": os.getenv('AZURE_SPEECH_API_KEY'),
        "X-Microsoft-OutputFormat": "riff-8khz-16bit-mono-pcm",
        "Content-Type": "application/ssml+xml",
    }
    body = f"""<speak version='1.0' xml:lang='ko-KR'><voice xml:lang='ko-KR' xml:gender='Female' name='{voice}'>{text}</voice></speak>"""
    response = requests.post(endpoint, headers=headers, data=body)
    if response.status_code != 200: return None
    import datetime; now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"tts_result_{now}.wav"
    with open(filename, "wb") as audio_file: audio_file.write(response.content)
    return filename

# GPT API 요청 함수 (생략)

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column(scale=3):
            chatbot = gr.Chatbot(type="messages")
            prompt_audio = gr.Audio(sources="microphone", label="질문", type="filepath")
            prompt_textbox = gr.Textbox(label="메시지 입력", interactive=False)
            voice_dropdown = gr.Dropdown(choices=["ko-KR-SunHiNeural"], label="음성 선택", value="ko-KR-SunHiNeural")
            gpt_audio = gr.Audio(label="GPT 음성 출력", type="filepath", interactive=False, autoplay=True)

        with gr.Column(scale=1):
            gr.Markdown("### STT")
            input_audio = gr.Audio(sources="microphone", type="filepath", label="마이크 입력")
            output_text = gr.Textbox(label="음성 인식 결과", interactive=False)

            gr.Markdown("### TTS")
            tts_textbox = gr.Textbox(label="텍스트 입력", placeholder="텍스트를 입력하세요.")
            send_tts_button = gr.Button("음성으로 변환")
            output_tts_audio = gr.Audio(label="음성 출력", type="filepath", interactive=False, autoplay=True)

    input_audio.change(request_stt, inputs=[input_audio], outputs=[output_text])
    send_tts_button.click(request_tts, inputs=[tts_textbox], outputs=[output_tts_audio])

    # ... (GPT 연동 및 기타 이벤트 연결 생략)

demo.launch()
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
