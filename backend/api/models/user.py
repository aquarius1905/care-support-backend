from django.db import models

class User(models.Model):
    """利用者モデル"""
    name = models.CharField('名前', max_length=100)
    email = models.EmailField('メールアドレス', max_length=255, null=True, blank=True)
    tel = models.CharField('電話番号', max_length=20, unique=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    deleted_at = models.DateTimeField('削除日時', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '利用者'
        verbose_name_plural = '利用者一覧'
        db_table = 'users'