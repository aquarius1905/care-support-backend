

from django.db import models

class TransPortScheduleType(models.IntegerChoices):
    SHEDULED = 1 # 予定
    COMPLETED = 2 # 完了
    CANCELLED = 3 # キャンセル
