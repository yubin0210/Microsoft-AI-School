import uuid
from django.db import models

from news.models.common import BaseModel

class NewsChannel(BaseModel):

    generator = models.CharField(max_length=100, verbose_name='제작자')
    title = models.CharField(max_length=500, verbose_name='제목')
    link = models.URLField(max_length=800, verbose_name='링크')
    language = models.CharField(max_length=10, verbose_name='언어')
    web_master = models.EmailField(max_length=100, verbose_name='웹 마스터')
    copyright = models.CharField(max_length=1000, verbose_name='저작권')
    last_build_date = models.DateTimeField(verbose_name='마지막 빌드 날짜')
    description = models.TextField(verbose_name='설명')
    image_title = models.CharField(max_length=500, verbose_name='이미지 제목')
    image_url = models.URLField(max_length=800, verbose_name='이미지 링크')
    image_link = models.URLField(max_length=800, verbose_name='이미지 링크')
    image_height = models.IntegerField(verbose_name='이미지 높이')
    image_width = models.IntegerField(verbose_name='이미지 너비')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = verbose_name_plural = '뉴스 채널'

class NewsItem(BaseModel):

    channel = models.ForeignKey(NewsChannel, on_delete=models.CASCADE, verbose_name='뉴스 채널')
    title = models.CharField(max_length=500, verbose_name='제목')
    link = models.URLField(max_length=1000, verbose_name='링크')
    guid = models.CharField(max_length=700, verbose_name='GUID')
    pub_date = models.DateTimeField(verbose_name='게시 날짜')
    description = models.TextField(verbose_name='설명')
    source = models.CharField(max_length=100, verbose_name='신문사 이름', blank=True, null=True)
    source_url = models.URLField(max_length=100, verbose_name='신문사 사이트', blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = verbose_name_plural = '뉴스'