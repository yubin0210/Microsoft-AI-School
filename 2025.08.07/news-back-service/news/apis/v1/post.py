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

        post_queryset = Post.objects.filter((Q(title__icontains=q) |
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

class PostDetailView(APIView):
    def get(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id, removed_at=None)
        except:
            return JsonResponse(dict(
                status="NOT_FOUND",
                message="해당 글을 찾을 수 없습니다."
            ), status=404)

        post_data = dict(
            id=str(post.id),
            title=post.title,
            content=post.content,
            author=post.author.username if post.author else 'Unknown',
            created_at=post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        )

        if post.removed_at:
            post_data['removed_at'] = post.removed_at.strftime('%Y-%m-%d %H:%M:%S')

        return JsonResponse(dict(
            status="OK",
            message="글 상세 조회 성공ㅋ",
            data=post_data
        ))
    
    def put(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id, removed_at=None)
        except:
            return JsonResponse(dict(
                status="NOT_FOUND",
                message="해당 글을 찾을 수 없습니다."
            ), status=404)
        title = request.data.get('title', None)
        content = request.data.get('content', None)

        if title is not None and title != post.title:
            post.title = title

        if content is not None and content != post.content:
            post.content = content

        post.save()

        post_data = dict(
            id=str(post.id),
            title=post.title,
            content=post.content,
            author=post.author.username if post.author else 'Unknown',
            created_at=post.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        )

        return JsonResponse(dict(
            status="OK",
            message="글을 수정하였습니다.",
            data=post_data
        ))
    
    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id, removed_at=None)
        except:
            return JsonResponse(dict(
                status="NOT_FOUND",
                message="해당 글을 찾을 수 없습니다.",
            ), status=404)
        
        post.removed_at = datetime.datetime.now()
        post.save()

        return JsonResponse(dict(
            status="OK",
            message="글을 삭제하였습니다."
        ))