from django.db import models

from api.models.facility import Facility

class ClientUser(models.Model):
    """利用者"""
    facility = models.ForeignKey(Facility, verbose_name='施設', on_delete=models.CASCADE)
    last_name = models.CharField('姓', max_length=255, blank=True)
    first_name = models.CharField('名', max_length=255, blank=True)
    last_name_furigana = models.CharField('セイ', max_length=255, blank=True)
    first_name_furigana = models.CharField('メイ', max_length=255, blank=True)
    birthday = models.DateField('生年月日', default='1950-01-01')
    email = models.EmailField('メールアドレス', max_length=255, null=True, blank=True)
    tel = models.CharField('電話番号', max_length=20, unique=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    deleted_at = models.DateTimeField('削除日時', null=True, blank=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

    class Meta:
        verbose_name = '利用者'
        verbose_name_plural = '利用者一覧'
        db_table = 'client_users'