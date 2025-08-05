# 💻 2025.08.05 - 학습 노트: Django REST Framework와 데이터베이스 연동

---

## ✏️ 학습 내용

오늘은 Django REST Framework를 사용하여 뉴스 기사(Post) CRUD API를 구축하고, 데이터베이스와 연동하는 과정을 심층적으로 학습했습니다. 특히 Django ORM을 활용하여 SQLite 데이터베이스를 조작하는 방법에 중점을 두었습니다.

-   **데이터베이스 설정**: `project/settings.py`에서 `DATABASES` 설정을 통해 `db.sqlite3`를 기본 데이터베이스로 지정했습니다.
-   **Django Models**: `news/models/common.py`에 `Post` 모델을 정의하고, `python manage.py makemigrations` 및 `migrate` 명령을 통해 데이터베이스 스키마를 생성 및 동기화했습니다.
-   **ORM을 이용한 데이터 조작**:
    -   **조회 (Read)**: `Post.objects.filter()`와 `Q` 객체를 사용하여 특정 조건(키워드 검색)에 맞는 데이터를 조회했습니다.
    -   **생성 (Create)**: `Post.objects.create()`를 사용하여 새로운 기사 데이터를 데이터베이스에 저장했습니다.
-   **API 구현**: `APIView`를 상속받은 `PostListView`에서 ORM을 통해 얻은 QuerySet을 JSON 형식으로 변환하여 클라이언트에 응답하는 로직을 구현했습니다.

---

## 📁 `news-back-service` 파일 구조

| 파일 경로 | 설명 |
| :--- | :--- |
| `manage.py` | Django 프로젝트 관리를 위한 커맨드라인 유틸리티입니다. |
| `project/settings.py` | 프로젝트의 전반적인 설정을 담당합니다. (**데이터베이스**, 시간대 등) |
| `db.sqlite3` | 프로젝트의 기본 데이터베이스 파일입니다. |
| `news/models/common.py` | `Post` 모델이 정의된 파일입니다. |
| `news/apis/v1/post.py` | `PostListView`가 구현되어 기사 조회 및 생성을 처리합니다. |
| `news/urls/v1/post.py` | `v1/posts/` 엔드포인트에 대한 URL 라우팅을 설정합니다. |

---

## 📌 주요 코드

### 1. 데이터베이스 설정 (`project/settings.py`)
*SQLite3를 기본 데이터베이스로 설정하는 부분입니다.*
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### 2. `PostListView`의 데이터베이스 연동 로직 (`news/apis/v1/post.py`)
*Django ORM을 사용하여 데이터베이스를 조회하고 새로운 데이터를 생성하는 핵심 로직입니다.*
```python
# ... (imports)
from news.models.common import Post
from django.db.models import Q

class PostListView(APIView):
    def get(self, request):
        q = request.query_params.get('q', '')

        # ORM을 사용하여 제목 또는 내용에 'q'가 포함된 Post 객체를 필터링
        post_queryset = Post.objects.filter(
            (Q(title__icontains=q) | Q(content__icontains=q)),
            removed_at=None
        )

        # ... (데이터 직렬화)
        return JsonResponse(dict(status="OK", data=post_list))
    
    def post(self, request):
        title = request.data.get('title', '')
        content = request.data.get('content', '')

        # ... (유효성 검사)
        
        # ORM을 사용하여 새로운 Post 객체를 생성하고 데이터베이스에 저장
        post = Post.objects.create(title=title, content=content, author_id=1)

        # ... (성공 응답 반환)
        return JsonResponse(dict(status="OK", message="글을 작성하였습니다."))
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ubinn0210@gmail.com)

---