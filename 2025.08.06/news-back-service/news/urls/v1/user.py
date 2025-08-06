from django.urls import path

from news.apis.v1.user import UserSignInView


urlpatterns = [
    path('sign-in/', UserSignInView.as_view(), name='sign-in'),
]
