# 💻 2025.04.11 - 학습 노트

---

## ✏️ 학습 내용

Python의 제어 구조에 대해 더 깊이 학습했습니다. 조건부 표현식을 사용하여 코드를 간결하게 만들고, `while`과 `for` 반복문에서 `break`와 `continue`를 활용하여 흐름을 제어하는 방법을 익혔습니다. 또한, 리스트와 딕셔너리 자료구조의 다양한 메서드를 실습하고, 이를 응용하여 숫자 맞추기 게임, 끝말잇기, 전화번호부 같은 간단한 콘솔 프로그램을 제작했습니다.

---

## 📁 파일 목록

- `practice_01.ipynb`: Python 심화 제어문, 리스트, 딕셔너리 학습을 위한 Jupyter Notebook 실습 파일

---

## 📌 주요 코드

### 1. `while` 반복문과 `random` 모듈을 이용한 숫자 맞추기 게임
*1부터 100 사이의 난수를 맞출 때까지 사용자 입력을 받아 UP/DOWN 힌트를 주는 코드입니다.*
```python
# 숫자 맞추기
import random

answer = random.randint(1, 100)

while True:
    user_number = int(input("1~100 사이의 숫자를 입력하세요: "))

    if user_number == answer:
        break
    elif user_number > answer:
        print("DOWN")
    else:
        print("UP")

print(f"{answer} 정답입니다!")
```

### 2. 리스트(List) 데이터 조작
*리스트에 요소를 추가, 삽입, 삭제하고 정렬하는 코드입니다.*
```python
datas = [1, 2, 3, 4, 5]

# 요소 추가
datas.append(6) # [1, 2, 3, 4, 5, 6]

# 요소 삭제
datas.remove(3) # [1, 2, 4, 5, 6]

# 정렬
datas.sort(reverse=True) # [6, 5, 4, 2, 1]

print(datas)
```

### 3. 딕셔너리(Dictionary)를 이용한 전화번호부 프로그램
*딕셔너리를 리스트에 담아 간단한 전화번호부 기능을 구현한 코드입니다.*
```python
# 전화번호 검색 프로그램
contacts = []

while True:
    user_input = input(f"메뉴 선택 (1: 추가, 2: 검색, 0: 종료): ")

    if user_input == "1":
        name_input = input("이름 입력: ")
        phone_number_input = input("전화번호 입력:")
        contacts.append({"name": name_input, "phone_number": phone_number_input})
    elif user_input == "2":
        search_name_input = input("검색 이름 입력: ")
        for contact in contacts:
            if contact["name"] == search_name_input:
                print(f"전화번호: {contact['phone_number']}")
                break
    elif user_input == "0":
        print("프로그램을 종료합니다.")
        break
    else: 
        print("메뉴 선택 오류입니다. 다시 선택하세요.")
```
---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](ubinn0210@gmail.com)


---
