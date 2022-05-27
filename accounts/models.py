from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.core.exceptions import BadRequest
from django.db import models


def validate_input(email, password, nickname):
    if not email:
        raise BadRequest('이메일은 필수 값입니다.')
    if not password:
        raise BadRequest('비밀번호는 필수 값입니다.')
    if not nickname:
        raise BadRequest('닉네임은 필수 값입니다.')


class UserManager(BaseUserManager):
    def create_user(self, email, password, nickname):
        validate_input(email, password, nickname)
        user = self.model(email=self.normalize_email(email), nickname=nickname)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, nickname):
        validate_input(email, password, nickname)
        user = self.model(email=self.normalize_email(email), nickname=nickname)
        user.set_password(password)
        user.is_admin = True
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=100)
    nickname = models.CharField(max_length=10)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'nickname']

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    object = UserManager()

    def __str__(self):
        return self.nickname
