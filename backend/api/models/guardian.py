from django.db import models
from api.models.client_user import ClientUser

class Guardian(models.Model):
    """利用者の家族"""
    user = models.ForeignKey(ClientUser, on_delete=models.CASCADE, related_name='guardians', verbose_name='利用者')
    name = models.CharField('名前', max_length=100)
    email = models.EmailField('メールアドレス', max_length=255, null=True, blank=True)
    tel = models.CharField('連絡先', max_length=20, unique=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    deleted_at = models.DateTimeField('削除日時', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '利用者の家族'
        verbose_name_plural = '利用者の家族一覧'
        db_table = 'guardians'