from django.utils import timezone

class Datetime:

    @classmethod
    def now(cls):
        return timezone.now()
