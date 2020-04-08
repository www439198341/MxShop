from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.utils.datetime_safe import datetime


class UserProfile(AbstractUser):
    """
    用户
    """
    gender_choice = (('M', '男'), ('F', '女'))
    name = models.CharField(max_length=30, null=True, blank=True, verbose_name='姓名')
    birthday = models.DateField(null=True, blank=True, verbose_name='出生年月')
    mobile = models.CharField(max_length=11, verbose_name='电话')
    gender = models.CharField(max_length=6, choices=gender_choice, default='F', verbose_name='性别')
    email = models.EmailField(max_length=100, null=True, blank=True, verbose_name='邮箱')

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class VerifyCode(models.Model):
    """
    短信验证码
    """
    code = models.CharField(max_length=10, verbose_name='验证码')
    mobile = models.CharField(max_length=11, verbose_name='电话')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '短信验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code
