# 💻 2025.08.04 - 학습 노트: Django와 React Native를 이용한 뉴스 앱 개발

---

## ✏️ 학습 내용

Django REST Framework를 사용하여 백엔드 API를 구축하고, React Native와 Expo를 사용하여 모바일 클라이언트를 개발하는 실습을 진행했습니다. Django 프로젝트 내에 가상 환경을 설정하고, 기본적인 API 엔드포인트를 만드는 방법을 학습했습니다. React Native에서는 Expo를 사용하여 프로젝트를 초기 설정하고, 기본적인 UI 컴포넌트를 구성하여 백엔드와 통신하는 방법을 익혔습니다.

-   **Django REST Framework**: `APIView`를 상속받아 간단한 "Hello World" API를 만들고, `GET` 및 `POST` 요청을 처리하는 방법을 학습했습니다.
-   **React Native (Expo)**: Expo를 사용하여 React Native 프로젝트를 생성하고, `Pressable`과 `Text` 컴포넌트를 사용하여 간단한 로그인 화면 UI를 구성했습니다.
-   **가상 환경**: Django 프로젝트별로 독립적인 개발 환경을 구축하기 위해 가상 환경을 설정하고, 필요한 패키지를 관리하는 방법을 학습했습니다.

---

## 📁 파일 목록

### 📄 news-back-service (Django)

| 파일 경로 | 설명 |
| :--- | :--- |
| `manage.py` | Django 프로젝트 관리를 위한 커맨드라인 유틸리티입니다. |
| `project/urls.py` | 프로젝트의 최상위 URL 라우팅을 설정합니다. |
| `news/apis/v1/common.py` | "Hello World" API 로직이 구현된 `APIView`가 포함되어 있습니다. |
| `news/urls/v1/common.py` | `v1/common/` API 엔드포인트의 URL 라우팅을 설정합니다. |

### 📄 news-app (React Native)

| 파일 경로 | 설명 |
| :--- | :--- |
| `app/index.tsx` | 앱의 메인 화면으로, 로그인 버튼이 포함된 UI를 구성합니다. |
| `package.json` | 프로젝트의 의존성 및 스크립트가 정의된 파일입니다. |
| `babel.config.js` | Babel 컴파일러 설정 파일입니다. |
| `metro.config.js` | Metro 번들러 설정 파일입니다. |

---

## 📌 주요 코드

### 1. Django "Hello World" API (`news/apis/v1/common.py`)
*`GET`과 `POST` 요청에 따라 다른 응답을 반환하는 간단한 API 뷰입니다.*
```python
from rest_framework.views import APIView
from django.http import JsonResponse

class HelloWorldView(APIView):
    def get(self, request):
        name = request.query_params.get('name', '')
        return JsonResponse(dict(
            status="OK",
            message="Hello World",
            method='get',
            name=name,
            query_params=request.query_params
        ))
    
    def post(self, request):
        address = request.data.get('address', '')
        address_detail = request.data.get('address_detail', '')

        return JsonResponse(dict(
            status="OK",
            message="Hello World",
            method="post",
            address=address,
            address_detail=address_detail,
            data=request.data
        ))
```

### 2. React Native 로그인 화면 (`app/index.tsx`)
*로그인 버튼을 누르면 `/sign-in` 경로로 이동하는 간단한 React Native 화면입니다.*
```typescript
import { Box } from "@/components/ui/box";
import { Text } from "@/components/ui/text";
import { router } from "expo-router";
import { Pressable } from "react-native";

export default function RootScreen() {

    const onItemClicked = () => {
        router.push("/sign-in");
    }
    return (
        <Box>
            <Pressable onPress={onItemClicked} style={{alignItems: 'center', padding: 20, backgroundColor: 'orange',
                borderRadius: 10, margin: 20
            }}>
                <Text style={{color: 'white'}}>로그인</Text>
            </Pressable>
        </Box>
    )
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
