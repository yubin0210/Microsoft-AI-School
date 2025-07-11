# 💻 2025.07.11 - 학습 노트

---

## ✏️ 학습 내용

JavaScript의 기본적인 문법과 핵심 개념에 대해 학습했습니다. 변수 선언 방식(`let`, `const`), 다양한 데이터 타입(String, Number, Boolean, Object 등)의 특징과 사용법을 익혔습니다. 또한, 산술, 비교, 논리 연산자를 활용하는 방법과 `if-else`, `for` 반복문과 같은 제어 흐름을 통해 코드의 실행 순서를 제어하는 방법을 학습했습니다. 마지막으로, 코드의 재사용성을 높이는 함수(기본 함수, 화살표 함수)를 정의하고 호출하는 방법을 실습하며 JavaScript 프로그래밍의 기초를 다졌습니다.

---

## 📁 파일 목록

- `javascript_basic.html` / `javascript_basic.js`: JavaScript의 가장 기본적인 "Hello, World!" 예제를 통해 HTML과 스크립트 파일을 연결하는 방법을 보여줍니다.
- `javascript_variables.html` / `javascript_variables.js`: `let`, `const`를 사용한 변수 및 상수 선언, 그리고 다양한 데이터 타입을 콘솔에 출력하는 예제입니다.
- `javascript_core_concepts.html` / `javascript_core_concepts.js`: 변수, 데이터 타입, 연산자, 제어 흐름, 함수 등 JavaScript의 핵심 기초 개념을 종합적으로 다루는 통합 예제 파일입니다.

---

## 📌 주요 코드

### 1. JavaScript 핵심 개념 종합 (`javascript_core_concepts.js`)
*변수, 데이터 타입, 연산자, 제어 흐름, 함수 등 JavaScript의 핵심적인 기초 문법을 하나의 파일에 정리한 코드입니다.*
```javascript
/*
 * JavaScript 핵심 기초 개념 예제
 * 변수, 연산자, 제어 흐름, 함수
 */

// HTML 문서의 특정 요소에 결과를 출력하기 위한 헬퍼 함수
const printToPage = (title, content) => {
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML += `<h2>${title}</h2><pre>${content}</pre>`;
};

// 1. 변수 (Variables)
console.log('--- 1. 변수 (Variables) ---');
let fruit = '사과';
fruit = '바나나';
const PI = 3.14159;
printToPage('변수와 상수', `let fruit = "${fruit}";\nconst PI = ${PI};`);

// 2. 데이터 타입 (Data Types)
console.log('\n--- 2. 데이터 타입 (Data Types) ---');
let name = "Alice";       // String
let age = 30;             // Number
let isStudent = false;    // Boolean
let hobbies = ['코딩', '독서', '영화감상']; // Array
let person = { name: 'Bob', age: 25 }; // Object
printToPage('데이터 타입', `String: ${name}\nNumber: ${age}\nBoolean: ${isStudent}\nArray: ${hobbies.join(', ')}\nObject: ${JSON.stringify(person)}`);

// 3. 연산자 (Operators)
console.log('\n--- 3. 연산자 (Operators) ---');
let x = 10;
let y = 4;
const operatorsOutput = `
  산술: ${x} + ${y} = ${x + y}
  비교: '5' === 5 -> ${'5' === 5}
  논리: (true && false) -> ${true && false}
`;
printToPage('연산자', operatorsOutput);

// 4. 제어 흐름 (Control Flow)
console.log('\n--- 4. 제어 흐름 (Control Flow) ---');
let score = 85;
let grade = (score >= 90) ? 'A' : (score >= 80) ? 'B' : 'C';
let forLoopOutput = '';
for (let i = 0; i < 3; i++) { forLoopOutput += i + ' '; }
printToPage('제어 흐름', `점수 ${score}점은 ${grade} 등급입니다.\nfor 반복문: ${forLoopOutput.trim()}`);

// 5. 함수 (Functions)
console.log('\n--- 5. 함수 (Functions) ---');
function add(a, b) {
    return a + b;
}
const subtract = (a, b) => a - b;
printToPage('함수', `add(5, 3) = ${add(5, 3)}\nsubtract(10, 4) = ${subtract(10, 4)}`);
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ubinn0210@gmail.com)

---

