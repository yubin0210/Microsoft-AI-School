# 💻 2025.08.07 - 학습 노트: 프론트엔드-백엔드 연동 및 뉴스 목록 구현

---

## ✏️ 학습 내용

오늘은 프론트엔드(`news-app`)와 백엔드(`news-back-service`) 간의 연동을 설정하고, 백엔드에서 제공하는 뉴스 기사 목록 API를 활용하여 프론트엔드에 뉴스 목록을 구현했습니다.

### 백엔드 (`news-back-service`)
-   **CORS 설정**: 프론트엔드와의 통신을 위해 `django-cors-headers` 라이브러리를 설치하고 `settings.py`에 CORS 설정을 추가했습니다. 이를 통해 다른 도메인에서의 API 요청을 허용했습니다.
-   **사용자 정보 조회 API 추가**: 로그인한 사용자의 정보를 조회할 수 있는 `/v1/users/me/` 엔드포인트를 `UserMySelfView`를 통해 구현했습니다.
-   **뉴스 시리얼라이저 확장**: 뉴스 아이템 API 응답에 `guid`, `description`, `source`, `source_url` 필드를 추가하여 더 풍부한 정보를 제공합니다.

### 프론트엔드 (`news-app`)
-   **뉴스 목록 화면 구현**: `app/index.tsx` 파일을 전면적으로 개편하여 뉴스 목록을 표시하는 화면을 구현했습니다.
    -   `useState`와 `useEffect` 훅을 사용하여 백엔드 API로부터 뉴스 데이터를 비동기적으로 가져오고 관리합니다.
    -   `FlatList` 컴포넌트를 활용하여 가져온 뉴스 데이터를 효율적으로 렌더링합니다.
    -   각 뉴스 항목은 제목, 발행일, 출처를 포함하며, `StyleSheet`를 통해 카드 형태로 시각적으로 구성했습니다.
    -   `package.json`에 `react-native-render-html` 의존성을 추가하여 향후 HTML 콘텐츠 렌더링을 위한 기반을 마련했습니다.
    -   `expo-router`의 `Stack.Screen`을 사용하여 화면 상단 헤더를 "뉴스"로 설정하고 스타일을 적용했습니다.

---

## 📁 파일 구조 변경점

### `news-back-service`
| 파일 경로 | 설명 |
| :--- | :--- |
| `project/settings.py` | CORS 관련 설정 (`CORS_ORIGIN_ALLOW_ALL`, `CORS_ALLOW_CREDENTIALS`, `INSTALLED_APPS`, `MIDDLEWARE`) 추가. |
| `news/apis/v1/user.py` | `UserMySelfView` 클래스 추가 (사용자 정보 조회 API). |
| `news/urls/v1/user.py` | `/v1/users/me/` 엔드포인트 추가 및 `UserMySelfView` 연결. |
| `news/serializers/news.py` | `NewsSerializer`에 `guid`, `description`, `source`, `source_url` 필드 추가. |

### `news-app`
| 파일 경로 | 설명 |
| :--- | :--- |
| `package.json` | `react-native-render-html` 의존성 추가. |
| `app/index.tsx` | 뉴스 목록을 표시하기 위한 UI 및 데이터 연동 로직 전면 개편. |

---

## 📌 주요 코드

### 1. `news-back-service/project/settings.py` 변경 사항
*CORS 설정을 추가하여 프론트엔드와의 통신을 허용합니다.*
```python
# ... (기존 설정)

ALLOWED_HOSTS = []

AUTH_USER_MODEL = 'news.User'
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Application definition

INSTALLED_APPS = [
    'news',
    'corsheaders', # 추가
    'rest_framework',
    # ... (기존 앱)
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware', # 추가
    # ... (기존 미들웨어)
]

# ... (나머지 설정)
```

### 2. `news-back-service/news/apis/v1/user.py` 변경 사항
*사용자 정보 조회 API (`UserMySelfView`) 추가*
```python
# ... (기존 UserSignInView)

class UserMySelfView(APIView):
    def get(self, request):
        
        user = request.user

        if user.is_anonymous:
            return JsonResponse(dict(
                stauts="NOT_AUTHENTICATED",
                message="로그인이 필요합니다."
            ), status=status.HTTP_401_UNAUTHORIZED)
        
        return JsonResponse(dict(
            status="OK",
            message="사용자 정보 조회 성공",
            token=request.META.get('CSRF_COOKIE', ''),
            user=dict(
                username=user.username,
                name=user.name,
                address=user.address,
                phone_number=user.phone_number
            )
        ))
```

### 3. `news-back-service/news/urls/v1/user.py` 변경 사항
*사용자 정보 조회 엔드포인트 추가*
```python
from django.urls import path

from news.apis.v1.user import UserMySelfView, UserSignInView


urlpatterns = [
    path('sign-in/', UserSignInView.as_view(), name='sign-in'),
    path('me/', UserMySelfView.as_view(), name='me'), # 추가
]
```

### 4. `news-back-service/news/serializers/news.py` 변경 사항
*뉴스 시리얼라이저 필드 확장*
```python
from rest_framework import serializers

from news.models.news import NewsItem

class NewsSerializer(serializers.ModelSerializer):
    pub_date = serializers.DateTimeField(format="%Y년 %m월 %d일 %H:%M:%S", read_only=True)

    current_date = serializers.SerializerMethodField()
    channel_name = serializers.SerializerMethodField()

    class Meta:
        model = NewsItem
        fields = [
            'id',
            'title',
            'guid', # 추가
            'pub_date',
            'description', # 추가
            'source', # 추가
            'source_url', # 추가
            'current_date',
            'channel_name'
        ]
        read_only_fields = ['id', 'pub_date', 'current_date', 'channel_name']

    def get_current_date(self, obj):
        return obj.pub_date.strftime("%Y년 %m월 %d일")
    
    def get_channel_name(self, obj):
        return "{}({})".format(obj.channel.title, obj.channel.generator) if obj.channel else "Unknown Channel"
```

### 5. `news-app/app/index.tsx` 주요 변경 사항
*뉴스 목록을 가져와 표시하는 `RootScreen` 컴포넌트*
```typescript
import { Box } from "@/components/ui/box";
import { Text } from "@/components/ui/text";
import { Pressable, StyleSheet } from "react-native";
import { FlatList } from "@/components/ui/flat-list";
import { useEffect, useState } from "react";
import { Stack } from "expo-router";

interface NewsItemProps {
    title: string;
    link?: string;
    guid?: string;
    pubDate?: string;
    description?: string;
    source?: string;
    sourceUrl?: string;
}

export default function RootScreen() {
    const [news, setNews] = useState<NewsItemProps[]>([]);

    useEffect(() => {
        console.log("INITIALIZED ROOT SCREEN")
        requestNews();
    }, []);

    useEffect(() => {
        console.log("NEWS 데이터가 변경되었습니다.", news)
    }, [news]);

    const requestNews = async () => {
        const response = await fetch("http://localhost:8000/v1/news/", {
            method: "GET",
        });
        const response_json = await response.json()
        console.log(response_json)
        setNews(response_json.data);
    }

    const getItemView = (item: NewsItemProps) => {
    return (
        <Pressable
            style={styles.card}
            onPress={() => {
                if (item.link) {
                    console.log("뉴스 링크:", item.link);
                    // Linking.openURL(item.link);
                }
            }}
        >
            <Text size="xl" style={styles.title}>
                {item.title}
            </Text>

            {item.pubDate && (
                <Text size="sm" style={styles.date}>
                    {new Date(item.pubDate).toLocaleString()}
                </Text>
            )}

            {item.source && (
                <Text size="sm" style={styles.source}>
                    {item.source}
                </Text>
            )}
        </Pressable>
        );
    };
    
    const renderList = () => {
        return (
            <Box style={{flex: 1}}>
                <FlatList
                    data={news}
                    renderItem={({ item }) => getItemView(item)}
                    keyExtractor={(item, index) => index.toString()}
                />
            </Box>
        )
    }

    return (
        <Box style={{ flex: 1 }}>
            <Stack.Screen
                options={{
                    headerTitle: "뉴스",
                    headerStyle: { backgroundColor : "#5477d7ff"},
                    headerTitleStyle: { color: "#ffffffff"},
                }}
            />
            {renderList()}
        </Box>
    )
}

const styles = StyleSheet.create({
    card: {
        backgroundColor: 'white',
        borderRadius: 12,
        padding: 16,
        marginVertical: 8,
        marginHorizontal: 16,
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.1,
        shadowRadius: 4,
        elevation: 3,
    },
    title: {
        fontWeight: 'bold',
        marginBottom: 6,
    },
    date: {
        color: '#888',
        marginBottom: 8,
    },
    description: {
        color: '#444',
    },
    source: {
        color: '#0066cc',
        marginTop: 8,
    },
    descriptionContainer: {
    marginBottom: 8,
    maxHeight: 60, // 높이 제한 (선택사항)
    overflow: 'hidden',
    },
});
```

---

## About Me

**Yubin Kim (김유빈)**

[![Blog](https://img.shields.io/badge/Blog-FF5722?style=for-the-badge&logo=blogger&logoColor=white)](https://cases.tistory.com/)
<a href="https://github.com/yubi0210"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub"/></a>

## 📞 Contact
[![Gmail](https://img.shields.io/badge/ubinn0210@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ubinn0210@gmail.com)

---