from rest_framework.views import APIView
from django.http import JsonResponse

from news.models.news import NewsItem
from news.serializers.news import NewsSerializer

class NewsListView(APIView):
    def get(self, request):

        news_queryset = NewsItem.objects.all()

        news_serializer = NewsSerializer(news_queryset, many=True)

        return JsonResponse(dict(
            status="OK",
            message="데이터를 조회하였습니다.",
            data=news_serializer.data
        ))