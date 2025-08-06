# 💻 2025.08.06 - 학습 노트: Django REST Framework 상세 API 구현

---

## ✏️ 학습 내용

오늘은 어제 구현한 뉴스 기사 목록 API에 이어, 특정 기사를 상세 조회, 수정, 삭제할 수 있는 API를 `PostDetailView`를 통해 구현했습니다. 이를 통해 RESTful API의 개별 리소스에 대한 CRUD(Create, Read, Update, Delete) 기능을 완성했습니다.

-   **상세 조회 (GET)**: `Post.objects.get()`을 사용하여 특정 ID를 가진 기사 데이터를 조회합니다. 해당 ID의 기사가 없거나 이미 삭제된 경우, 404 Not Found 응답을 반환합니다.
-   **수정 (PUT)**: `request.data`를 통해 전달받은 제목(title)과 내용(content)으로 기존 데이터를 업데이트합니다. `post.save()` 메서드를 호출하여 변경 사항을 데이터베이스에 반영합니다.
-   **삭제 (DELETE)**: 실제로 데이터를 삭제하는 대신, `removed_at` 필드에 현재 시간을 기록하여 '논리적 삭제(Soft Delete)'를 구현했습니다. 이를 통해 데이터 복구 및 추적 가능성을 열어두었습니다.
-   **URL 라우팅**: `news/urls/v1/post.py`에 `<uuid:post_id>/` 형태의 URL 패턴을 추가하여 `PostDetailView`와 연결했습니다.

---

## 📁 `news-back-service` 파일 구조 변경점

| 파일 경로 | 설명 |
| :--- | :--- |
| `news/apis/v1/post.py` | `PostDetailView`가 추가되어 개별 기사의 **조회, 수정, 삭제** 기능을 처리합니다. |
| `news/urls/v1/post.py` | `v1/posts/<uuid:post_id>/` 엔드포인트가 `PostDetailView`에 연결되도록 라우팅이 추가되었습니다. |

---

## 📌 주요 코드

### 1. `PostDetailView` 구현 (`news/apis/v1/post.py`)
*개별 기사에 대한 GET, PUT, DELETE 메서드를 처리하는 API 뷰입니다.*
```python
class PostDetailView(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id, removed_at=None)
        except Post.DoesNotExist:
            return JsonResponse(dict(
                status="NOT_FOUND",
                message="해당 글을 찾을 수 없습니다."
            ), status=404)

        # ... (데이터 직렬화)
        return JsonResponse(dict(status="OK", data=post_data))

    def put(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id, removed_at=None)
        except Post.DoesNotExist:
            return JsonResponse(dict(
                status="NOT_FOUND",
                message="해당 글을 찾을 수 없습니다."
            ), status=404)
        
        title = request.data.get('title')
        content = request.data.get('content')

        if title:
            post.title = title
        if content:
            post.content = content
        
        post.save()
        # ... (업데이트된 데이터 반환)
        return JsonResponse(dict(status="OK", message="글을 수정하였습니다.", data=post_data))

    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id, removed_at=None)
        except Post.DoesNotExist:
            return JsonResponse(dict(
                status="NOT_FOUND",
                message="해당 글을 찾을 수 없습니다."
            ), status=404)
        
        post.removed_at = datetime.datetime.now()
        post.save()

        return JsonResponse(dict(status="OK", message="글을 삭제하였습니다."))
```

### 2. URL 라우팅 설정 (`news/urls/v1/post.py`)
*새로운 상세 뷰를 URL과 연결합니다.*
```python
from django.urls import path
from news.apis.v1.post import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<uuid:post_id>/', PostDetailView.as_view(), name='post_detail'),
]
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ubinn0210@gmail.com)

---
