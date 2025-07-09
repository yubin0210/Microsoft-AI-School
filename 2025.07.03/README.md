# 💻 2025.07.03 - 학습 노트

---

## ✏️ 학습 내용

`Azure Computer Vision` 서비스를 활용하여 이미지 분석 및 시각화를 수행하는 방법을 학습했습니다. `requests` 라이브러리를 사용하여 이미지를 불러오고, `Azure Computer Vision` API를 호출하여 이미지 내의 객체, 캡션, 태그, 밀집 캡션(dense captions), 스마트 크롭(smart crops) 등 다양한 시각적 특징을 분석했습니다. 분석된 결과는 `PIL (Pillow)` 라이브러리를 사용하여 원본 이미지 위에 바운딩 박스와 텍스트로 시각화하여 표시했습니다. `Gradio`를 활용하여 사용자가 이미지 URL을 입력하고 분석 결과를 즉시 확인할 수 있는 웹 인터페이스를 구축했습니다.

---

## 📁 파일 목록

- `vision_20250703.ipynb`: `Azure Computer Vision` 서비스를 이용한 이미지 분석 및 시각화의 기본 실습.
- `vision_20250703_2.ipynb`: `Azure Computer Vision` 서비스를 이용한 이미지 분석 및 시각화의 추가 실습.

---

## 📌 주요 코드

### 1. `Azure Computer Vision` API 요청 및 이미지 시각화
*이미지 URL을 통해 `Azure Computer Vision` API를 호출하고, 반환된 분석 결과를 이미지 위에 시각화하는 코드입니다.*
```python
import requests
from PIL import Image, ImageDraw
from io import BytesIO
import gradio as gr
import random

IMAGE_URL = "https://cdn.pixabay.com/photo/2023/12/13/22/29/young-woman-8447841_1280.jpg"
ENDPOINT_URL = "YOUR_AZURE_VISION_ENDPOINT_URL"
API_KEY = "YOUR_AZURE_VISION_API_KEY"

def get_font(): # 폰트 설정 함수 (OS별 한글 폰트 지원)
    # ... (폰트 로드 로직 생략)
    pass

def request_image_analysis(image_url, features=["objects"], **kwargs):
    params = {"api-version": "2024-02-01", "features": ",".join(features)}
    headers = {"Ocp-Apim-Subscription-Key": API_KEY}
    body = {"url": image_url}
    response = requests.post(ENDPOINT_URL, params=params, headers=headers, json=body)
    if response.status_code != 200: return None
    return response.json()

def draw_image(image_url, features, data):
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))
    draw = ImageDraw.Draw(image)
    font = get_font()

    for feature in features:
        if feature == "tags" or feature == "caption": continue
        feature_key = '{}Result'.format(feature)
        result_object = data[feature_key]
        block_list = result_object['values']
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        for block in block_list:
            bounding_box = block['boundingBox']
            x, y, w, h = bounding_box['x'], bounding_box['y'], bounding_box['w'], bounding_box['h']
            formatted_text = None
            if feature == "objects": formatted_text = block['tags'][0]['name']
            elif feature == "denseCaptions": formatted_text = block["text"]

            draw.rectangle([(x, y), (x + w, y + h)], outline=color, width=2)
            draw.text((x, y), feature, fill="black", font=font)
            if formatted_text: draw.text((x + 5, y + 20), formatted_text, fill="white", font=font)
    return image

with gr.Blocks() as demo:
    def click_send(image_url):
        features = ["objects", "caption", "denseCaptions", "tags", "smartCrops"]
        response_data = request_image_analysis(image_url, features)
        image = draw_image(image_url, features, response_data)
        return image

    image_url_textbox = gr.Textbox(label="이미지 URL")
    send_button = gr.Button("전송")
    output_image = gr.Image(label="결과 화면", interactive=False, type="pil")

    send_button.click(click_send, inputs=[image_url_textbox], outputs=[output_image])

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
