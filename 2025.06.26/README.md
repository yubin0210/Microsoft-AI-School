# 💻 2025.06.26 - 학습 노트

---

## ✏️ 학습 내용

`Gradio`를 활용하여 `Azure Document Intelligence` 서비스를 위한 웹 인터페이스를 구축하는 방법을 학습했습니다. 사용자가 이미지를 업로드하고 `prebuilt-document` 또는 `prebuilt-read`와 같은 사전 빌드된 모델을 선택하면, 해당 이미지를 `Azure Document Intelligence` 서비스로 전송하여 분석을 요청합니다. 분석 결과로 반환된 텍스트 라인과 그 위치 정보를 원본 이미지 위에 시각적으로 표시하여, 문서에서 추출된 정보를 직관적으로 확인할 수 있도록 구현했습니다.

---

## 📁 파일 목록

- `main.py`: `Gradio` 웹 애플리케이션의 메인 파일로, `Azure Document Intelligence` 서비스를 활용한 문서 분석 인터페이스를 제공합니다.
- `app_screenshot.png`: 애플리케이션의 스크린샷 이미지 파일.
- `language.http`: 관련 HTTP 요청 예제 파일.

---

## 📌 주요 코드

### 1. `Gradio`를 이용한 문서 분석 웹 인터페이스
*`Gradio`의 `gr.Blocks()`를 사용하여 이미지 업로드, 모델 선택, 분석 결과 표시 기능을 포함하는 웹 인터페이스를 정의하는 코드입니다.*
```python
import gradio as gr
import sys
import os
from PIL import Image, ImageDraw, ImageFont

# 2025.06.25 디렉토리의 document_intelligence.py 임포트
sibling_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "2025.06.25"))
if sibling_dir not in sys.path:
    sys.path.append(sibling_dir)

from document_intelligence import analyze_document, get_analyze_result

def change_image_callback(model, image_path):
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()

    api_version_by_model = {
        "prebuilt-document": "2023-07-31",
        "prebuilt-read": "2024-11-30",
    }

    request_analyze_result_url = analyze_document(
        data=image_bytes,
        service="formrecognizer",
        model=model,
        api_version=api_version_by_model[model],
        content_type="image/png",
    )

    result = get_analyze_result(request_analyze_result_url)
    result_image = draw_result_image(image_path, result)

    return result, result_image

# ... (draw_result_image 함수는 생략)

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            model_select = gr.Dropdown(
                label="모델 선택", choices=["prebuilt-document", "prebuilt-read"]
            )
            input_image = gr.Image(type="filepath", label="이미지 선택")
            response_text = gr.Text(label="분석 요청 결과", interactive=False)
        output_image = gr.Image(type="pil", label="결과 이미지", interactive=False)

    input_image.change(
        fn=change_image_callback,
        inputs=[model_select, input_image],
        outputs=[response_text, output_image],
    )

demo.launch()
```

### 2. 분석 결과 이미지에 시각화 (`draw_result_image` 함수)
*`Azure Document Intelligence`에서 반환된 분석 결과를 바탕으로 원본 이미지 위에 텍스트 라인의 폴리곤과 내용을 그리는 함수입니다.*
```python
# ... (main.py 파일 내)

def draw_result_image(image_path: str, result: dict) -> Image.Image:
    image = Image.open(image_path)
    # font = ImageFont.truetype("폰트_경로", size=16) # 폰트 경로 설정 필요
    draw = ImageDraw.Draw(image)

    if result.get("analyzeResult"):
        for page in result["analyzeResult"]["pages"]:
            for line in page["lines"]:
                color = (
                    random.randint(0, 255),
                    random.randint(0, 255),
                    random.randint(0, 255),
                )
                draw.polygon(line["polygon"], outline=color, width=2)

                text_x = line["polygon"][0]
                text_y = line["polygon"][1]

                # draw.text((text_x, text_y - 20), line["content"], fill=color, font=font)

    return image
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
