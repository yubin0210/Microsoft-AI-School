from django.urls import path
from news.apis.v1.common import HelloWorldView

urlpatterns = [
    path('helloworld/', HelloWorldView.as_view(), name='hello_world'),
]