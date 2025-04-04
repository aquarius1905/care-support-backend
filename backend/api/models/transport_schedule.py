from django.db import models
from api.models.choices.transport_schedule_status import TransportScheduleType
from api.models.client_user import ClientUser

class TransportSchedule(models.Model):
    """送迎スケジュール"""
    user = models.ForeignKey(ClientUser, on_delete=models.CASCADE, related_name='transport_schedules', verbose_name='利用者')
    scheduled_transport_datetime = models.DateTimeField('送迎予定時間')
    actual_transport_datetime = models.DateTimeField('変更後の送迎予定時間')
    status = models.IntegerField('ステータス', default=TransportScheduleType.SCHEDULED, choices=TransportScheduleType.choices)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    deleted_at = models.DateTimeField('削除日時', null=True, blank=True)

    def __str__(self):
        return f"{self.user.name} - {self.scheduled_transport_datetime}"

    class Meta:
        verbose_name = '送迎スケジュール'
        verbose_name_plural = '送迎スケジュール一覧'
        unique_together = ['user', 'scheduled_transport_datetime']  # 同じユーザーの同じ日付での重複を防ぐ
        db_table = 'transport_schedules'