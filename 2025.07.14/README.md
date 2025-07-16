# 💻 2025.07.14 - 학습 노트: JavaScript 심화

---

## ✏️ 학습 내용

JavaScript의 고급 주제들을 깊이 있게 탐구하며, 모던 웹 애플리케이션 개발에 필수적인 내부 동작 원리와 핵심 패턴을 학습했습니다. 함수형 프로그래밍 기법부터 비동기 처리 모델, 브라우저의 다양한 API까지 폭넓은 실습을 진행했습니다.

-   **함수형 프로그래밍 패러다임**: 상태를 안전하게 캡슐화하고 관리하는 **클로저(Closure)**의 동작 원리를 이해하고, 함수 재사용성을 극대화하는 **커링(Currying)** 기법을 학습했습니다.

-   **JavaScript 비동기 모델 심층 분석**: JavaScript 런타임의 핵심인 **이벤트 루프(Event Loop)**와 콜 스택, 태스크 큐(마이크로/매크로)의 상호작용을 학습하여 비동기 코드의 실행 흐름을 정확히 예측하는 능력을 길렀습니다.

-   **모던 비동기 처리 패턴**: 전통적인 콜백(Callback) 패턴의 한계(콜백 지옥)를 이해하고, 이를 개선한 **프로미스(Promise)**와 `async/await` 문법을 사용하여 가독성 높고 효율적인 비동기 코드를 작성하는 방법을 숙달했습니다.

-   **브라우저 저장소 API 활용**: `Cookie`, `Web Storage(localStorage/sessionStorage)`, `IndexedDB`의 특징과 차이점을 비교 분석하고, 각 시나리오에 맞는 데이터 저장 기술을 선택하고 활용하는 방법을 익혔습니다.

-   **웹 통신 기술**: `fetch`/`XHR` 기반의 기본적인 비동기 HTTP 요청부터, `Long Polling`, `WebSocket`, `Server-Sent Events(SSE)`와 같은 실시간 통신 기술까지 직접 구현하며 각 방식의 장단점과 적합한 사용 사례를 파악했습니다.

---

## 📁 파일 목록

| 구분 | 파일명 | 설명 |
| :--- | :--- | :--- |
| **DOM** | `javascript_dom_manipulation.html` / `.js` | JavaScript로 웹 페이지의 요소를 선택, 생성, 변경, 삭제하는 DOM 조작법 |
| **함수형** | `javascript_currying.html` / `.js` | 여러 인자를 받는 함수를 단일 인자 함수들의 연속으로 변환하는 커링 기법 |
| | `javascript_closure.html` / `.js` | 함수가 선언될 때의 환경을 기억하는 클로저의 개념과 상태 관리 패턴 |
| **비동기** | `javascript_event_loop.html` / `.js` | 이벤트 루프와 태스크 큐의 동작 원리를 보여주는 비동기 흐름 분석 |
| | `javascript_callback.html` / `.js` | 비동기 처리의 기본인 콜백 함수의 사용법과 콜백 지옥 문제 |
| | `javascript_promise.html` / `.js` | 비동기 작업의 상태를 관리하는 Promise 객체와 `.then()`, `.catch()` 체이닝 |
| | `javascript_async_await.html` / `.js` | Promise를 간결하게 작성하는 `async/await` 문법과 예외 처리 |
| **통신** | `javascript_fetch.html` / `.js` | 최신 비동기 HTTP 요청 표준인 `fetch` API |
| | `javascript_xhr.html` / `.js` | 전통적인 비동기 통신 방법인 `XMLHttpRequest` 객체 |
| | `javascript_long_polling.html` / `.js` | 실시간 통신을 흉내 내는 롱 폴링(Long Polling) 기법 |
| | `javascript_websocket.html` / `.js` | 양방향 실시간 통신을 위한 WebSocket 프로토콜 |
| | `javascript_sse.html` / `.js` | 서버-클라이언트 단방향 실시간 통신 기술인 Server-Sent Events(SSE) |
| **저장소** | `javascript_cookie.html` / `.js` | 상태 유지를 위한 쿠키(Cookie)의 동작 원리와 생성, 조회, 삭제 방법 |
| | `javascript_local_storage.html` / `.js` | 데이터가 영구적으로 유지되는 `localStorage` 사용법 |
| | `javascript_session_storage.html` / `.js` | 세션 동안만 데이터가 유지되는 `sessionStorage` 사용법 |
| | `javascript_indexeddb.html` / `.js` | 대용량 정형 데이터를 위한 클라이언트 DB인 `IndexedDB` 사용법 |

---

## 📌 주요 코드

### 1. 이벤트 루프 동작 순서 예측 (`javascript_event_loop.js`)
*동기 코드, 마이크로태스크(Promise), 매크로태스크(setTimeout)의 실행 우선순위를 통해 이벤트 루프의 동작을 명확히 이해하는 코드입니다.*
```javascript
console.log("  (1) 동기: 코드 시작");

// Macrotask
setTimeout(() => {
  console.log("  (5) Macrotask: setTimeout 콜백");
}, 0);

// Microtask
Promise.resolve().then(() => {
  console.log("  (3) Microtask: Promise.then");
});

console.log("  (2) 동기: 코드 종료");

/*
실행 순서:
  (1) 동기 코드 -> (2) 동기 코드 -> (3) 모든 Microtask -> (5) Macrotask
*/
```

### 2. async/await를 사용한 간결한 비동기 처리 (`javascript_fetch.js`)
*`async/await`와 `fetch` API를 결합하여, 비동기 네트워크 요청을 동기 코드처럼 직관적으로 작성하고 예외를 처리하는 코드입니다.*
```javascript
const getPostById = async (postId) => {
  try {
    const response = await fetch(
      `https://jsonplaceholder.typicode.com/posts/${postId}`
    );

    if (!response.ok) {
      throw new Error(`HTTP 에러! status: ${response.status}`);
    }

    const data = await response.json();
    console.log("  - async/await 데이터 수신:", data);
  } catch (error) {
    console.error("  - async/await 요청 실패:", error);
  }
};

getPostById(2);
```

### 3. IndexedDB 트랜잭션 (`javascript_indexeddb.js`)
*대용량 데이터를 위한 클라이언트 사이드 DB인 `IndexedDB`에서 'readwrite' 트랜잭션을 시작하여 객체 저장소에 데이터를 추가하는 비동기 작업의 예시입니다.*
```javascript
function performDatabaseOperations(db) {
  // 'readwrite' 모드로 트랜잭션을 시작합니다.
  const transaction = db.transaction(["notes"], "readwrite");
  const noteObjectStore = transaction.objectStore("notes");

  const newNote = {
    text: "IndexedDB 배우기",
    timestamp: new Date().getTime(),
  };

  const addRequest = noteObjectStore.add(newNote);
  
  addRequest.onsuccess = () => {
    console.log(`  - 데이터 추가 성공! ID: ${addRequest.result}`);
  };
  addRequest.onerror = (event) => {
    console.error("데이터 추가 실패:", event.target.error);
  };
}
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ubinn0210@gmail.com)

---
