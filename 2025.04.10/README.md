# 2025.04.10 - 학습 노트 (김유빈)

---

## 핵심 학습 내용

Python 프로그래밍의 기본적인 구성 요소와 제어 구조를 학습했습니다. 변수 선언부터 시작하여 다양한 데이터 타입과 연산자를 익혔고, `if` 조건문과 `while` 반복문을 사용하여 프로그램의 흐름을 제어하는 방법을 실습했습니다. 또한, `input()` 함수를 통해 사용자 입력을 처리하고, 문자열 인덱싱과 슬라이싱으로 데이터를 가공하는 방법을 배웠습니다.

---

## 파일 목록

- `practice_01.ipynb`: Python 기초 문법 및 제어문 학습을 위한 Jupyter Notebook 실습 파일

---

## 주요 코드

### 1. 사용자 입력 및 산술 연산
*사용자로부터 두 개의 숫자를 입력받아 다양한 산술 연산 결과를 출력하는 코드입니다.*
```python
# 사용자로부터 두 개의 정수를 입력 받아서 산술 연산자의 결과를 출력
num_1 = int(input('Enter first number: '))
num_2 = int(input('Enter second number: '))

print(f"""\
num_1 + num_2 = {num_1 + num_2}
num_1 * num_2 = {num_1 * num_2}
num_1 // num_2 = {num_1 // num_2}
num_1 ** num_2 = {num_1 ** num_2}
""")
```

### 2. 조건문을 이용한 학점 계산
*점수에 따라 `if-elif-else` 문을 사용하여 학점을 부여하는 코드입니다.*
```python
# 점수가 90점 이상인 경우 'A', 80점 이상인 경우 'B', ... 60점 미만인 경우 'F' 출력
score = int(input('점수를 입력하세요: '))

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
```

### 3. while 반복문을 이용한 팩토리얼 계산
*`while` 문을 사용하여 사용자가 입력한 숫자의 팩토리얼을 계산하는 코드입니다.*
```python
# factorial을 구하는 프로그램
number = int(input('정수를 입력하세요: '))

factorial = 1
while number > 1:
    factorial *= number
    number -= 1
print(f'팩토리얼: {factorial}')
```
