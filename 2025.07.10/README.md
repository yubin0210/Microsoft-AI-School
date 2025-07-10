# 💻 2025.07.10 - 학습 노트

---

## ✏️ 학습 내용

CSS를 사용하여 웹 페이지를 시각적으로 디자인하고, 반응형 웹을 구현하는 방법에 대해 학습했습니다. 외부 스타일 시트를 통해 HTML과 CSS를 분리하고, Flexbox와 Grid를 활용하여 유연한 레이아웃을 구성했습니다. 또한, 미디어 쿼리를 적용하여 다양한 디바이스 환경에서 최적화된 화면을 제공하는 방법을 실습했습니다.

---

## 📁 파일 목록

- `style.css`: 웹 페이지의 전반적인 스타일을 정의하는 외부 CSS 파일입니다.
- `1-1_index.html` ~ `1-4_register.html`: `style.css`를 연결하여 시각적인 디자인을 적용한 HTML 파일들입니다.

---

## 📌 주요 코드

### 1. 반응형 테이블 스타일 (`style.css`)
*미디어 쿼리를 사용하여 화면 너비가 768px 이하일 때 테이블의 레이아웃을 수직으로 변경하는 반응형 CSS 코드입니다.*
```css
/* Responsive Table */
@media (max-width: 768px) {
    thead {
        display: none;
    }

    tr {
        display: block;
        margin-bottom: 1rem;
        border: 1px solid #ddd;
        border-radius: 4px;
    }

    td {
        display: block;
        text-align: right;
        border-bottom: 1px dotted #ccc;
        padding-left: 50%;
        position: relative;
    }

    td:before {
        content: attr(data-label);
        position: absolute;
        left: 10px;
        width: 45%;
        padding-right: 10px;
        white-space: nowrap;
        text-align: left;
        font-weight: bold;
        color: #34495e;
    }

    td:last-child {
        border-bottom: 0;
    }
}
```

### 2. 모던 폼 스타일 (`style.css`)
*`<form>` 요소에 현대적인 디자인을 적용하여 사용자 경험을 개선하는 CSS 코드입니다.*
```css
/* Form Styles */
form {
    width: 100%;
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

fieldset {
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}

legend {
    font-size: 1.2rem;
    font-weight: bold;
    color: #3498db;
    padding: 0 0.5em;
}

input[type="submit"] {
    background-color: #3498db;
    color: white;
    padding: 12px 24px;
    border: none;
    border-radius: 4px;
    font-size: 1.1rem;
    cursor: pointer;
    transition: background-color 0.3s;
    display: block;
    width: 100%;
}

input[type="submit"]:hover {
    background-color: #2980b9;
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
