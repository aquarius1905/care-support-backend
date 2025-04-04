from django.db import models
from api.models.client_user import ClientUser

class Facility(models.Model):
    """デイサービス等の施設情報"""
    name = models.CharField('施設名', max_length=100)
    email = models.EmailField('メールアドレス', max_length=255)
    tel = models.CharField('連絡先', max_length=20, unique=True)
    zip = models.CharField('郵便番号', max_length=8)
    address = models.CharField('住所', max_length=255)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    deleted_at = models.DateTimeField('削除日時', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'デイサービス等の施設情報'
        verbose_name_plural = 'デイサービス等の施設情報一覧'
        db_table = 'facilities'