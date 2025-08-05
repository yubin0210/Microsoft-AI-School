import datetime
from django.http import JsonResponse
from django.db.models import Q
from rest_framework.views import APIView

from news.models.common import Post

class PostListView(APIView):
    def get(self, request):

        q = request.query_params.get('q', '')

        post_list = list()
        now = datetime.datetime(2025, 8, 5, 16, 0, 0, 0)

        post_queryset = Post.objects.filter((Q(title__icontatins=q) |
                                             Q(content__icontains=q)
                                             ), removed_at=None)

        for post in post_queryset:
            post_list.append(dict(
                id=str(post.id),
                title=post.title,
                content=post.content,
                author=post.author.username if post.author else 'Unknown',
                now=now.timestamp(),
                created_at_t=post.created_at.timestamp(),
                created_at=post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                removed_at=post.removed_at.strftime('%Y-%m-%d %H:%M:%S') if post.removed_at else None
            ))

        return JsonResponse(dict(
            status="OK",
            message="조회에 성공했습니다",
            data=post_list
        ))
    
    def post(self, request):
        title = request.data.get('title', '')
        content = request.data.get('content', '')

        if title == '' or content == '':
            return JsonResponse(dict(
                status="BAD_REQUEST",
                message="제목과 내용을 모두 입력하세요."
            ), status=400)
        
        post = Post.objects.create(title=title,
                                   content=content, author_id=1)

        return JsonResponse(dict(
            status="OK",
            message="글을 작성하였습니다.",
            data=dict(
                title=post.title,
                content=post.content,
                author=post.author.username,
                created_at=post.created_at.strftime('%Y-%m-%d%H:%M:%S'),
                id=str(post.id)
            )
        ))