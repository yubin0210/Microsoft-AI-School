from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth import authenticate, login, logout

class UserSignInView(APIView):

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        if not username or not password:
            return JsonResponse(dict(
                status = "WRONG_USERNAME_OR_PASSWORD",
                message="이메일 또는 패스워드를 확인하세요."
            ), status=status.HTTP_401_UNAUTHORIZED)
        
        user = authenticate(username=username, password=password)

        if user is None:
            return JsonResponse(dict(
                status = "WRONG_USERNAME_OR_PASSWORD",
                message="이메일 또는 패스워드를 확인하세요."
            ), status=status.HTTP_401_UNAUTHORIZED)
        
        login(request, user)

        return JsonResponse(dict(
            status="OK",
            message="로그인 성공",
            username=user.username
        ))

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