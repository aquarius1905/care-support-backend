

from django.db import models

class TransportScheduleType(models.IntegerChoices):
    SCHEDULED = 1 # 予定
    COMPLETED = 2 # 完了
    CANCELLED = 3 # キャンセル
