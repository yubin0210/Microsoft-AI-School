# 💻 2025.05.21 - 학습 노트

---

## ✏️ 학습 내용

Python의 데이터 시각화 라이브러리인 `Matplotlib`의 다양한 기능을 학습하고, `PyTorch`를 활용한 간단한 이미지 분류 모델 구축의 기초를 다졌습니다. `Matplotlib` 튜토리얼을 통해 기본적인 그래프 생성, 스타일 지정, 여러 데이터 시리즈 플롯, 그리고 범주형 데이터를 활용한 시각화 방법을 익혔습니다. 또한, `CIFAR-10` 데이터셋을 사용하여 신경망을 구성하고, 모델을 학습시키며 성능을 평가하는 과정을 실습하여 이미지 분류의 기본적인 워크플로우를 이해했습니다. CSV 파일에서 데이터를 읽어와 시각화하는 실용적인 예제도 포함되어 있습니다.

---

## 📁 파일 목록

- `notebooks/`: 학습 내용을 담은 Jupyter Notebook 파일들이 포함된 폴더입니다.
  - `image-classifier.ipynb`: `PyTorch`와 `CIFAR-10`을 이용한 간단한 이미지 분류기 구축 실습.
  - `matplotlib.ipynb`: `Matplotlib`의 `pyplot` 인터페이스를 소개하는 튜토리얼.
  - `population.ipynb`: CSV 파일에서 인구 데이터를 읽어와 `Matplotlib`으로 시각화하는 예제.
- `data/`: 실습에 사용된 데이터 파일들이 포함된 폴더입니다.
  - `atlantis.csv`: `population.ipynb`에서 사용되는 샘플 인구 데이터.

---

## 📌 주요 코드

### 1. `PyTorch`를 이용한 이미지 분류기 학습
*신경망을 정의하고, `CIFAR-10` 데이터셋을 사용하여 모델을 학습시키는 코드입니다.*
```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from tqdm import tqdm

# 신경망 정의 (Net 클래스 생략)
# 데이터 로드 (trainloader, testloader 생략)

net = Net()
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)

EPOCHS = 2
for epoch in range(EPOCHS):
    running_loss = 0.0
    for i, data in enumerate(tqdm(trainloader, desc=f"Epoch {epoch + 1} of {EPOCHS}")):
        inputs, labels = data
        optimizer.zero_grad()
        outputs = net(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

# 모델 저장
PATH = './cifar_net.pth'
torch.save(net.state_dict(), PATH)
```

### 2. `Matplotlib` 기본 플롯 및 스타일 지정
*간단한 선 그래프를 그리고, 색상, 마커, 선 스타일을 지정하는 코드입니다.*
```python
import matplotlib.pyplot as plt
import numpy as np

# 단일 리스트 플롯
plt.plot([1, 2, 3, 4, 5])
plt.ylabel('Numbers')
plt.show()

# 여러 데이터 시리즈 플롯 및 스타일 지정
t = np.arange(0., 5., 0.2)
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

### 3. CSV 데이터 읽어와 시각화
*`pandas`를 사용하여 CSV 파일을 읽고, `Matplotlib`으로 데이터를 시각화하는 코드입니다.*
```python
import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv('../data/atlantis.csv')
x = df['year']
y = df['population']

plt.plot(x,y)
plt.title("Population of Atlantis")
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
