# 💻 2025.07.02 - 학습 노트

---

## ✏️ 학습 내용

`Gradio`를 활용하여 `Azure AI Vision` 및 `Azure AI Face` 서비스를 통합한 웹 애플리케이션을 구축했습니다. 이 애플리케이션은 사용자가 이미지를 업로드하거나 URL을 입력하면, `Azure AI Vision` 서비스를 통해 이미지 분석(태그, 캡션, 객체, 스마트 크롭 등)을 수행하고, `Azure AI Face` 서비스를 통해 얼굴 감지 및 속성 분석(얼굴 ID, 랜드마크, 나이, 성별 등)을 수행합니다. 분석된 결과는 `Gradio` 인터페이스를 통해 시각적으로 표시되어, 사용자가 AI 기반의 이미지 및 얼굴 분석 기능을 쉽게 체험할 수 있도록 합니다.

---

## 📁 파일 목록

- `main.py`: `Gradio` 웹 애플리케이션의 메인 파일로, `Azure AI Vision` 및 `Azure AI Face` 서비스를 통합한 사용자 인터페이스를 제공합니다.
- `vision.http`: `Azure AI Vision` 서비스에 대한 HTTP 요청 예제 파일.
- `services/`: `Azure AI Vision` 및 `Azure AI Face` 서비스와의 상호작용을 담당하는 클래스 파일들이 포함된 폴더.
  - `face_service.py`: `Azure AI Face` 서비스와의 통신을 담당하는 클래스.
  - `vision_service.py`: `Azure AI Vision` 서비스와의 통신을 담당하는 클래스.
- `data/`: 이미지 분석에 사용되는 이미지 데이터가 포함된 폴더.
- `results/`: 분석 결과가 저장될 수 있는 폴더.

---

## 📌 주요 코드

### 1. `Gradio`를 이용한 Vision 및 Face 서비스 통합 웹 애플리케이션
*`Gradio`의 `gr.Blocks()`를 사용하여 이미지 분석 및 얼굴 감지 기능을 통합한 사용자 인터페이스를 정의하는 코드입니다.*
```python
import gradio as gr
from pprint import pformat
from PIL import Image

from services.vision_service import VisionService
from services.face_service import FaceService

def vision_api_call(
    vision_image_url: str,
    vision_image_upload: str,
    features: list[str],
    smart_crops_aspect_ratios: str,
    gender_neutral_caption: bool,
) -> tuple:
    # ... (입력 유효성 검사 및 VisionService 호출 로직 생략)
    pass

def face_api_call(
    image_path: str,
    return_face_id: bool,
    return_face_landmarks: bool,
    return_face_attributes: list[str],
) -> str:
    # ... (입력 유효성 검사 및 FaceService 호출 로직 생략)
    pass

with gr.Blocks(theme=gr.themes.Soft(), title="Azure AI Vision & Face Demo") as demo:
    gr.Markdown("# Azure AI Vision and Face Services Demo")
    with gr.Tabs():
        with gr.TabItem("🖼️ Image Analysis (Vision)"):
            with gr.Row():
                with gr.Column(scale=1):
                    vision_image_url = gr.Textbox(label="이미지 Url")
                    vision_image_upload = gr.Image(type="filepath", label="이미지 업로드")
                    vision_features = gr.CheckboxGroup(label="분석할 기능 선택")
                    vision_gender_neutral_caption = gr.Checkbox(label="성 중립성 캡션", visible=False)
                    vision_smart_crops_aspect_ratios = gr.Textbox(label="Aspect Ratios", visible=False)
                    analyze_button = gr.Button("이미지 분석", variant="primary")
                with gr.Column(scale=2):
                    vision_dense_captions_output = gr.AnnotatedImage(label="Dense Captions 분석 결과")
                    vision_objects_output = gr.AnnotatedImage(label="Objects 분석 결과")
                    vision_cropped_images_output = gr.Gallery(label="Cropped Images 결과")
                    vision_tags_output = gr.Markdown(label="이미지 태그")
                    vision_raw_output = gr.Textbox(label="전체 API 응답 (Raw)", interactive=False)

        with gr.TabItem("😊 Face Detection (Face)"):
            with gr.Row():
                with gr.Column(scale=1):
                    face_image_input = gr.Image(type="filepath", label="이미지 업로드")
                    face_id_checkbox = gr.Checkbox(label="얼굴 ID 반환")
                    face_landmarks_checkbox = gr.Checkbox(label="얼굴 특징점 반환")
                    face_attributes_checkbox_group = gr.CheckboxGroup(label="반환할 얼굴 속성")
                    detect_button = gr.Button("얼굴 감지", variant="primary")
                with gr.Column(scale=2):
                    face_output = gr.Textbox(label="API 응답", interactive=False)

    analyze_button.click(fn=vision_api_call, inputs=[vision_image_url, vision_image_upload, vision_features, vision_smart_crops_aspect_ratios, vision_gender_neutral_caption], outputs=[vision_dense_captions_output, vision_objects_output, vision_cropped_images_output, vision_tags_output, vision_raw_output])
    detect_button.click(fn=face_api_call, inputs=[face_image_input, face_id_checkbox, face_landmarks_checkbox, face_attributes_checkbox_group], outputs=face_output)

demo.launch()
```

### 2. `FaceService` 클래스 (`services/face_service.py`)
*`Azure AI Face` 서비스와 통신하여 얼굴 감지 및 분석을 수행하는 클래스입니다.*
```python
import os
import requests
from dotenv import load_dotenv
from typing import Any, Dict, List, Optional

load_dotenv()

class FaceService:
    def __init__(self) -> None:
        self.endpoint = os.getenv("AZURE_FACE_ENDPOINT_URL")
        self.api_key = os.getenv("AZURE_FACE_API_KEY")
        if not self.endpoint or not self.api_key: raise ValueError("환경 변수 설정 필요")

    def detect_faces(
        self,
        image_source: str,
        return_face_id: bool = False,
        return_face_landmarks: bool = True,
        return_face_attributes: Optional[List[str]] = None,
        # ... (기타 파라미터 생략)
    ) -> List[Dict[str, Any]]:
        is_url = image_source.startswith("http://") or image_source.startswith("https://")
        detect_url = f"{self.endpoint}/face/v1.0/detect"
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        params = { # ... (파라미터 설정 생략) }

        if is_url:
            headers["Content-Type"] = "application/json"
            response = requests.post(detect_url, headers=headers, params=params, json={"url": image_source})
        else:
            headers["Content-Type"] = "application/octet-stream"
            with open(image_source, "rb") as f: image_data = f.read()
            response = requests.post(detect_url, headers=headers, params=params, data=image_data)

        response.raise_for_status()
        return response.json()
```

### 3. `VisionService` 클래스 (`services/vision_service.py`)
*`Azure AI Vision` 서비스와 통신하여 이미지 분석을 수행하는 클래스입니다.*
```python
import os
import requests
from dotenv import load_dotenv
from typing import Any, Dict, List, Optional

load_dotenv()

class VisionService:
    def __init__(self) -> None:
        self.endpoint = os.getenv("AZURE_VISION_ENDPOINT_URL")
        self.api_key = os.getenv("AZURE_VISION_API_KEY")
        if not self.endpoint or not self.api_key: raise ValueError("환경 변수 설정 필요")

    def analyze_image(
        self,
        image_source: str,
        features: List[str],
        language: str = "en",
        gender_neutral_caption: bool = False,
        smart_crops_aspect_ratios: Optional[str] = None,
    ) -> Dict[str, Any]:
        is_url = image_source.startswith("http://") or image_source.startswith("https://")
        analyze_url = f"{self.endpoint}/computervision/imageanalysis:analyze"
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        params = { # ... (파라미터 설정 생략) }

        if is_url:
            headers["Content-Type"] = "application/json"
            response = requests.post(analyze_url, headers=headers, params=params, json={"url": image_source})
        else:
            headers["Content-Type"] = "application/octet-stream"
            with open(image_source, "rb") as f: image_data = f.read()
            response = requests.post(analyze_url, headers=headers, params=params, data=image_data)

        response.raise_for_status()
        return response.json()
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
