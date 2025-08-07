from django.db import models
import uuid


class ModelManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(removed_at=None)

class BaseModel(models.Model):
    
    objects = ModelManager()

    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, verbose_name='ID')
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='생성일')
    removed_at = models.DateTimeField(blank=True, null=True, verbose_name='삭제일')


# 블로그 글 테이블
class Post(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, verbose_name='ID')
    title = models.CharField(max_length=100, verbose_name='제목')
    content = models.TextField(verbose_name='내용', blank=True, null=True)
    author = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name='작성자')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    removed_at = models.DateTimeField(blank=True, null=True, verbose_name='삭제일')

    def __str__(self):
        return "{}({})".format(self.id, self.title)
    
    class Meta:
        verbose_name = verbose_name_plural = '블로그'

