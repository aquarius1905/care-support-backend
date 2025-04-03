from django.db import models
from api.models.choices.transport_schedule_status import TransPortScheduleType
from backend.api.models.user import Users

class TransportSchedule(models.Model):
    """送迎スケジュールモデル"""
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='schedules', verbose_name='利用者')
    transport_time = models.TimeField('送迎時間')
    date = models.DateField('日付')
    status = models.CharField('ステータス', default=TransPortScheduleType.SHEDULED, choices=TransPortScheduleType.choices)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    deleted_at = models.DateTimeField('削除日時', null=True, blank=True)

    def __str__(self):
        return f"{self.user.name} - {self.date} {self.transport_time}"

    class Meta:
        verbose_name = '送迎スケジュール'
        verbose_name_plural = '送迎スケジュール一覧'
        unique_together = ['user', 'date']  # 同じユーザーの同じ日付での重複を防ぐ
        db_table = 'transport_schedules'