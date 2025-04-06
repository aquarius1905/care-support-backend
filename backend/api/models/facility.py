from django.db import models

class Facility(models.Model):
    """デイサービス等の施設情報"""
    name = models.CharField('施設名', max_length=100)
    email = models.EmailField('メールアドレス', max_length=255)
    representative_last_name = models.CharField('担当者姓', max_length=255, blank=True)
    representative_first_name = models.CharField('担当者名', max_length=255, blank=True)
    tel = models.CharField('連絡先', max_length=20, unique=True)
    zip = models.CharField('郵便番号', max_length=8)
    address1 = models.CharField('住所', max_length=255)
    address2 = models.CharField('建物名等', max_length=255, blank=True)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    deleted_at = models.DateTimeField('削除日時', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'サービス事業所'
        verbose_name_plural = 'サービス事業所一覧'
        db_table = 'facilities'