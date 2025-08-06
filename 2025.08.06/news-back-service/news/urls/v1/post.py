from django.urls import path

from news.apis.v1.post import PostDetailView, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<uuid:post_id>/', PostDetailView.as_view(), name='post_detail'),
]
 