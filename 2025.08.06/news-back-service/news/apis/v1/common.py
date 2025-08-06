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

    
class IndexView(APIView):
    def get(self, request):

        return JsonResponse(dict(
            status="OK",
            message="Index Page"
        ))