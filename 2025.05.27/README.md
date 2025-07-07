# 💻 2025.05.27 - 학습 노트

---

## ✏️ 학습 내용

이미지 분류 및 객체 탐지 기술에 대한 심층적인 학습을 진행했습니다. `PyTorch`와 `ResNet50` 사전 학습 모델을 활용하여 이미지 분류기를 구축하는 과정을 실습했습니다. 데이터 로딩, 데이터셋 분할, 이미지 변환, 모델의 Fully Connected Layer(FCL) 수정, 모델 학습 및 검증, 그리고 학습된 모델을 이용한 이미지 예측을 포함합니다. 또한, Azure Cognitive Services를 활용하여 이미지 내 객체를 탐지하는 기본적인 과정을 다루었으며, 탐지된 객체에 바운딩 박스를 표시하는 시각화까지 수행했습니다.

---

## 📁 파일 목록

- `ClassifySpaceRockCode.ipynb`: `PyTorch`와 `ResNet50`을 이용한 이미지 분류기 구축 및 학습, 예측 실습.
- `requirements.txt`: 프로젝트에 필요한 Python 라이브러리 목록.
- `data/`: 이미지 분류에 사용되는 이미지 데이터가 포함된 폴더.
- `notebooks/`:
  - `imageclassification.ipynb`: 이미지 분류 모델 구축의 상세 과정 및 코드.
  - `objectdetection.ipynb`: Azure Cognitive Services를 이용한 객체 탐지 실습.

---

## 📌 주요 코드

### 1. `PyTorch` 이미지 데이터 로딩 및 분할
*이미지 데이터를 불러와 학습 및 테스트 세트로 분할하고, 데이터 로더를 생성하는 코드입니다.*
```python
import torch
from torchvision import datasets, transforms
from torch.utils.data.sampler import SubsetRandomSampler
import numpy as np

data_dir = "./data"
valid_size = 0.2

t_transforms = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.Resize(224),
    transforms.ToTensor()
])

train_data = datasets.ImageFolder(data_dir, transform=t_transforms)

num_train = len(train_data)
indices = list(range(num_train))
np.random.shuffle(indices)
split = int(np.floor(valid_size * num_train))
train_idx, test_idx = indices[split:], indices[:split]

train_sampler = SubsetRandomSampler(train_idx)
test_sampler = SubsetRandomSampler(test_idx)

train_loader = torch.utils.data.DataLoader(train_data, batch_size=16, sampler=train_sampler)
test_loader = torch.utils.data.DataLoader(train_data, batch_size=16, sampler=test_sampler)
```

### 2. `ResNet50` 모델의 FCL(Fully Connected Layer) 수정
*사전 학습된 `ResNet50` 모델의 마지막 Fully Connected Layer를 새로운 분류 작업에 맞게 수정하는 코드입니다.*
```python
from torchvision import models
from torch import nn, optim

model = models.resnet50(pretrained=True)

# 기존 FCL의 가중치 고정
for param in model.parameters():
    param.requires_grad = False

# 새로운 FCL 정의
model.fc = nn.Sequential(
    nn.Linear(2048, 512),
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(512, 2),
    nn.LogSoftmax(dim=1)
)

criterion = nn.NLLLoss()
optimizer = optim.Adagrad(model.fc.parameters(), lr=0.003)
model.to(device) # 모델을 GPU 또는 CPU로 이동
```

### 3. 이미지 예측 함수
*학습된 모델을 사용하여 새로운 이미지의 클래스를 예측하는 함수입니다.*
```python
from PIL import Image

def predict_image(image):
    image_tensor = t_transforms(image).float()
    input = image_tensor.unsqueeze_(0)
    input = input.to(device)

    output = model(input)
    index = output.data.cpu().numpy().argmax()
    return index
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
