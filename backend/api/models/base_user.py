from django.contrib.auth.models import AbstractUser
from django.db import models

class BaseUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('staff', '施設スタッフ'),
        ('client', '利用者'),
        ('family', '家族'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    
    # メールを必須にする
    email = models.EmailField(unique=True, verbose_name='メールアドレス')
    
    # メールアドレスをユーザー識別子として使用
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_type']
    
    def __str__(self):
        return f"{self.email} ({self.get_user_type_display()})"