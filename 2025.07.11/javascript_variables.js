// JavaScript 변수 선언 및 할당

// var: 함수 스코프 변수 (옛날 방식, 사용을 지양하는 것이 좋음)
var oldSchoolVar = "이것은 var입니다.";
console.log(oldSchoolVar);

// let: 블록 스코프 변수, 재할당 가능
let myName = "홍길동";
console.log("내 이름은 " + myName + "입니다.");

myName = "성춘향"; // 재할당
console.log("이제 내 이름은 " + myName + "입니다.");

// const: 블록 스코프 상수, 재할당 불가능
const pi = 3.14159;
console.log("원주율(pi)의 값은 " + pi + "입니다.");

// pi = 3.14; // 이 줄은 오류를 발생시킵니다. (주석 해제 시)

// 데이터 타입
let age = 25; // 숫자 (Number)
let isStudent = true; // 불리언 (Boolean)
let favoriteFruit = null; // Null
let notAssigned; // Undefined

console.log("나이:", age, "(타입:", typeof age, ")");
console.log("학생인가?:", isStudent, "(타입:", typeof isStudent, ")");
console.log("좋아하는 과일:", favoriteFruit, "(타입:", typeof favoriteFruit, ")");
console.log("할당되지 않은 변수:", notAssigned, "(타입:", typeof notAssigned, ")");
