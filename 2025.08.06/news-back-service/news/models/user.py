from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from news.models.common import BaseModel

class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, username, password=None, **extra_fields):
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(username, password, **extra_fields)


class User(BaseModel, AbstractUser):

    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = "사용자"

    username = models.EmailField(max_length=50, unique=True, verbose_name="이메일")
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name="이름")
    address = models.CharField(max_length=20, blank=True, null=True, verbose_name="주소")
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="전화번호")

    first_name = None
    last_name = None

    objects = UserManager()

    def __str__(self):
        return self.username