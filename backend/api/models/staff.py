from django.db import models
from api.models.facility import Facility
from django.conf import settings  # BaseUserへの参照

class Staff(models.Model):
    """デイサービス等の職員"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='staff_profile',
        verbose_name='ユーザー',
        null=True,  # ← 一時的に追加
        blank=True,  # ← これも追加（adminフォーム対策）
    )
    name = models.CharField('名前', max_length=100)
    email = models.EmailField('メールアドレス', max_length=255, null=True, blank=True)
    tel = models.CharField('連絡先', max_length=20, unique=True)
    facility = models.ForeignKey("api.Facility", verbose_name='施設', on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    deleted_at = models.DateTimeField('削除日時', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'デイサービス等の職員'
        verbose_name_plural = 'デイサービス等の職員一覧'
        db_table = 'staffs'