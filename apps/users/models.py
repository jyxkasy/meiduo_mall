from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    class Mate:
        db_table = 'tb_users'  # 指明数据库表名
        verbose_name = '用户'  # 在admin站点中显示名称

    def __str__(self):
        return self.username
