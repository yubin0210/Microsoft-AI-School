# 💻 2025.04.14 - 학습 노트 (김유빈)

---

## ✏️ 학습 내용

Python의 고급 문법과 구조에 대해 학습했습니다. 튜플과 세트 자료구조의 특징과 활용법을 익혔고, 함수를 정의하고 사용하는 방법을 실습했습니다. 특히 가변 인자, 여러 값 반환, 기본 인자 값 설정 등 다양한 함수 활용법을 다루었습니다. 또한, 모듈을 직접 만들어 불러오고, 클래스를 정의하여 객체 지향 프로그래밍의 기초를 다졌습니다.

---

## 📁 파일 목록

- `practice_01.ipynb`: Python 튜플, 세트, 함수, 모듈, 클래스 등 고급 문법 학습을 위한 Jupyter Notebook 실습 파일입니다.
- `my_module.py`: `practice_01.ipynb`에서 불러와 사용하는 간단한 모듈 파일입니다.
- `calculator.py`: `practice_01.ipynb`에서 불러와 사용하는 계산기 클래스 파일입니다.

---

## 📌 주요 코드

### 1. 함수를 이용한 윤년 확인
*4년마다 윤년, 100년마다는 평년, 400년마다는 다시 윤년이 되는 규칙을 함수로 구현한 코드입니다.*
```python
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
```

### 2. 모듈 생성 및 사용
*별도의 `.py` 파일에 함수를 정의하고, 다른 파일에서 `import`하여 사용하는 코드입니다.*
```python
# my_module.py
def add(a, b):
    return a + b

# main.py
import my_module

result = my_module.add(1, 2)
print(result) # 3
```

### 3. 클래스(Class)를 이용한 계산기 구현
*덧셈 기능을 가진 간단한 계산기 클래스를 정의하고, 객체를 생성하여 사용하는 코드입니다.*
```python
# calculator.py
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

# main.py
from calculator import Calculator

cal1 = Calculator()
print(cal1.add(2)) # 2
print(cal1.add(3)) # 5
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
