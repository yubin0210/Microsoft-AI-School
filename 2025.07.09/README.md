# 💻 2025.07.09 - 학습 노트

---

## ✏️ 학습 내용

HTML의 기본 구조와 시맨틱 태그의 중요성에 대해 학습했습니다. 웹 페이지의 콘텐츠를 의미에 맞게 구성하는 방법을 이해하고, `<table>`, `<form>` 등 다양한 태그를 사용하여 정적인 웹 페이지를 만드는 실습을 진행했습니다. 이를 통해 논리적이고 구조적인 웹 페이지를 설계하는 능력을 길렀습니다.

---

## 📁 파일 목록

- `1-1_index.html`: 기본적인 HTML 태그를 사용하여 자기소개 페이지를 작성한 파일입니다.
- `1-2_semantic-layout.html`: 시맨틱 태그를 활용하여 포트폴리오 페이지의 레이아웃을 구성한 파일입니다.
- `1-3_table.html`: `<table>` 태그를 사용하여 프로젝트 이력 테이블을 만든 파일입니다.
- `1-4_register.html`: `<form>` 관련 태그를 사용하여 회원가입 폼을 구현한 파일입니다.

---

## 📌 주요 코드

### 1. 시맨틱 레이아웃 (`1-2_semantic-layout.html`)
*`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<aside>`, `<footer>` 등 시맨틱 태그를 사용하여 웹 페이지의 구조를 의미적으로 명확하게 표현하는 코드입니다.*
```html
<body>
  <header>
    <nav>
      <h1>김유빈 포트폴리오</h1>
      <ul>
        <li><a href="#home">홈</a></li>
        <li><a href="#about">소개</a></li>
        <li><a href="#skills">기술 스택</a></li>
        <li><a href="#projects">프로젝트</a></li>
        <li><a href="#contact">연락처</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <article>
      <section id="about">
        <h2>소개</h2>
        <p>...</p>
      </section>
      <section id="skills">
        <h2>기술 스택</h2>
        <p>...</p>
      </section>
    </article>
    <aside>
      <h2>최근 활동</h2>
      <ul>...</ul>
    </aside>
  </main>

  <footer id="contact">
    <h3>연락처</h3>
    <address>...</address>
  </footer>
</body>
```

### 2. 테이블 (`1-3_table.html`)
*`<table>` 관련 태그들을 사용하여 데이터를 구조적으로 표현하는 코드입니다.*
```html
<table>
  <caption>프로젝트 수행 이력</caption>
  <thead>
    <tr>
      <th>프로젝트명</th>
      <th>기간</th>
      <th>역할</th>
      <th>주요 내용</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>포트폴리오 웹사이트</td>
      <td>2025.03 ~ 2025.04</td>
      <td>프론트엔드 개발</td>
      <td>HTML, CSS, JavaScript...</td>
    </tr>
  </tbody>
</table>
```

### 3. 폼 (`1-4_register.html`)
*`<form>` 관련 태그들을 사용하여 사용자로부터 데이터를 입력받는 회원가입 폼을 구현한 코드입니다.*
```html
<form action="/submit" method="post">
  <section>
    <h2>기본 정보</h2>
    <p>
      <label for="name">이름:</label>
      <input type="text" id="name" name="name" required />
    </p>
    ...
  </section>
  <section>
    <h2>추가 정보</h2>
    <fieldset>
      <legend>관심 분야:</legend>
      <label><input type="checkbox" name="interest" value="web" /> 웹 개발</label>
      ...
    </fieldset>
  </section>
  <p><input type="submit" value="가입하기" /></p>
</form>
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ubinn0210@gmail.com)

---
