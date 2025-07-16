# 💻 2025.07.15 - 학습 노트: JavaScript ES6+ 및 미니 프로젝트

---

## ✏️ 학습 내용

최신 JavaScript(ES6+)의 핵심 문법을 학습하고, 이를 바탕으로 유지보수성과 확장성이 뛰어난 웹 애플리케이션을 설계하는 실전 프로젝트를 진행했습니다. 코드의 가독성과 효율성을 높이는 문법적 설탕(Syntactic Sugar)을 익히고, 관심사 분리 원칙에 기반한 아키텍처 패턴을 직접 구현했습니다.

-   **ES6+ 고급 문법 마스터**:
    -   **구조 분해 할당 (Destructuring)**: 배열과 객체의 데이터를 간결하게 추출하여 변수에 할당하는 방법을 익혔습니다. 중첩 구조, 기본값 설정, 별칭 지정 등 고급 활용법을 통해 코드의 가독성을 크게 향상시켰습니다.
    -   **펼치기 문법 (Spread Syntax) & 나머지 매개변수 (Rest Parameters)**: 배열과 객체를 복사/병합하거나, 함수의 가변 인자를 효과적으로 처리하는 방법을 학습하며 데이터의 불변성을 유지하는 코딩 스타일을 익혔습니다.

-   **계층형 아키텍처 설계 및 구현 (Todo App)**:
    -   UI 상호작용(Controller), 비즈니스 로직(Service), 데이터 영속성(Repository)을 명확히 분리하는 **계층형 아키텍처**를 적용하여 Todo 앱을 리팩토링했습니다.
    -   **리포지토리 패턴(Repository Pattern)** 과 **팩토리 패턴(Factory Pattern)** 을 도입하여, `LocalStorage`와 `IndexedDB` 중 원하는 데이터 저장소를 동적으로 선택하고 교체할 수 있는 유연한 구조를 설계했습니다. 이를 통해 서비스 계층이 데이터 접근 기술의 구체적인 구현으로부터 독립되도록 만들었습니다.

-   **외부 AI 모델 연동 및 서비스 모듈화 (가위바위보 App)**:
    -   **Teachable Machine**으로 직접 학습시킨 이미지 분류 모델을 웹 애플리케이션에 통합하는 방법을 학습했습니다.
    -   웹캠 제어 및 손 모양 판별 로직(`HandDetectionService`)과 게임의 규칙 및 상태 관리 로직(`GameService`)을 별도의 **서비스 모듈로 분리**하여 각 기능의 독립성과 재사용성을 높였습니다. 컨트롤러는 이 서비스들을 조율하는 역할만 담당하도록 하여 코드의 복잡도를 낮췄습니다.

---

## 📁 파일 목록

| 구분 | 파일명 | 설명 |
| :--- | :--- | :--- |
| **ES6+** | `javascript_destructuring.html` / `.js` | 배열과 객체의 값을 간결하게 추출하는 구조 분해 할당 문법 |
| | `javascript_spread_and_rest.html` / `.js` | 펼치기 문법(Spread)과 나머지 매개변수(Rest)의 차이점과 활용법 |
| **Project** | `todo-app/` | **계층형 아키텍처(Controller-Service-Repository)로 구현된 Todo 앱** |
| | `rock-paper-scissor-vs-app/` | **Teachable Machine 모델을 연동한 AI 가위바위보 대전 앱** |

---

## 📌 주요 코드

### 1. 리포지토리 패턴과 팩토리 패턴 (`todo-app/`)
*서비스가 특정 데이터 저장 기술에 종속되지 않도록, 인터페이스를 정의하고 팩토리를 통해 구현체를 동적으로 주입하는 코드입니다.*
```javascript
// repositories/todo.repository.interface.js
// 모든 저장소가 구현해야 할 메서드를 정의
export class TodoRepository {
  async getAll() { throw new Error("Not implemented"); }
  // ... create, update, delete ...
}

// repositories/repository.factory.js
// 사용자의 선택에 따라 적절한 리포지토리 인스턴스를 생성
export function createRepository(type) {
  if (type === 'local') {
    return new LocalStorageTodoRepository();
  } else if (type === 'indexeddb') {
    return new IndexedDbTodoRepository();
  }
}

// services/todo.service.js
// 팩토리로부터 리포지토리를 주입받아 사용하므로, 실제 구현을 알 필요가 없음
const repository = createRepository(userSelection);
const todoService = new TodoService(repository);
```

### 2. 서비스 모듈화 (`rock-paper-scissor-vs-app/`)
*AI 모델 연동 로직과 게임 로직을 별도의 서비스로 분리하여 각 모듈의 독립성과 재사용성을 높인 구조입니다.*
```javascript
// services/hand-detection.service.js
// 웹캠 제어 및 Teachable Machine 모델을 이용한 손 모양 판별 로직만 담당
class HandDetectionService {
  async detectHand(duration) { /* ... */ }
}

// services/game.service.js
// 순수한 가위바위보 게임 규칙(승패 판정, 점수 기록 등)만 담당
class GameService {
  judge(playerHand, computerHand) { /* ... */ }
}

// controllers/game.controller.js
// 두 서비스를 조율하여 게임을 진행
class GameController {
  constructor(gameService, handDetectionService) { /* ... */ }

  async play() {
    const userHand = await this.handDetectionService.detectHand(3000);
    const result = this.gameService.judge(userHand, computerHand);
    this.view.render(result);
  }
}
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https.img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ubinn0210@gmail.com)

---
