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

// `let`을 사용한 변수 선언 (재할당 가능)
let fruit = '사과';
let fruitOutput = `처음 선언된 과일: ${fruit}\n`;
fruit = '바나나'; // 재할당
fruitOutput += `재할당된 과일: ${fruit}`;
console.log(fruitOutput);
printToPage('변수 (let)', fruitOutput);

// `const`를 사용한 상수 선언 (재할당 불가)
const PI = 3.14159;
const piOutput = `원주율 (PI): ${PI}`;
// PI = 3.14; // 이 코드는 오류를 발생시킵니다.
console.log(piOutput);
printToPage('상수 (const)', piOutput);

// 2. 데이터 타입 (Data Types)
console.log('\n--- 2. 데이터 타입 (Data Types) ---');
let name = "Alice";       // String
let age = 30;             // Number
let isStudent = false;    // Boolean
let hobbies = ['코딩', '독서', '영화감상']; // Array (Object)
let person = {            // Object
    name: 'Bob',
    age: 25
};
let nothing = null;       // Null
let notDefined;           // Undefined

const typesOutput = `
이름: ${name} (${typeof name})
나이: ${age} (${typeof age})
학생인가?: ${isStudent} (${typeof isStudent})
취미: ${hobbies.join(', ')} (${typeof hobbies})
개인정보: ${JSON.stringify(person)} (${typeof person})
Null 값: ${nothing} (${typeof nothing})
정의되지 않은 값: ${notDefined} (${typeof notDefined})
`;
console.log(typesOutput);
printToPage('데이터 타입', typesOutput);

// 3. 연산자 (Operators)
console.log('\n--- 3. 연산자 (Operators) ---');
let x = 10;
let y = 4;

const operatorsOutput = `
산술 연산자:
  ${x} + ${y} = ${x + y}
  ${x} - ${y} = ${x - y}
  ${x} * ${y} = ${x * y}
  ${x} / ${y} = ${x / y}
  ${x} % ${y} = ${x % y} (나머지)

비교 연산자:
  ${x} > ${y} -> ${x > y}
  '5' == 5 -> ${'5' == 5} (값만 비교)
  '5' === 5 -> ${'5' === 5} (값과 타입 모두 비교)

논리 연산자:
  (true && false) -> ${true && false}
  (true || false) -> ${true || false}
  !true -> ${!true}
`;
console.log(operatorsOutput);
printToPage('연산자', operatorsOutput);

// 4. 제어 흐름 (Control Flow)
console.log('\n--- 4. 제어 흐름 (Control Flow) ---');

// if-else
let score = 85;
let grade;
if (score >= 90) {
    grade = 'A';
} else if (score >= 80) {
    grade = 'B';
} else {
    grade = 'C';
}
const ifElseOutput = `점수 ${score}점은 ${grade} 등급입니다.`;
console.log(ifElseOutput);
printToPage('if-else', ifElseOutput);

// for 반복문
let forLoopOutput = 'for 반복문 (0부터 4까지):\n';
for (let i = 0; i < 5; i++) {
    forLoopOutput += i + ' ';
}
console.log(forLoopOutput.trim());
printToPage('for 반복문', forLoopOutput.trim());

// 5. 함수 (Functions)
console.log('\n--- 5. 함수 (Functions) ---');

// 함수 선언식
function add(a, b) {
    return a + b;
}

// 화살표 함수 (Arrow Function)
const subtract = (a, b) => a - b;

const functionsOutput = `
함수 선언식: add(5, 3) = ${add(5, 3)}
화살표 함수: subtract(10, 4) = ${subtract(10, 4)}
`;
console.log(functionsOutput);
printToPage('함수', functionsOutput);
