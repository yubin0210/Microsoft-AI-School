from django.urls import path

from news.apis.v1.user import UserMySelfView, UserSignInView


urlpatterns = [
    path('sign-in/', UserSignInView.as_view(), name='sign-in'),
    path('me/', UserMySelfView.as_view(), name='me'),
]
