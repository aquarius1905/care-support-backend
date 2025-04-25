import logging
from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from api.models import TransportSchedule
from api.services.notification_service import NotificationService

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = '送迎スケジュールの10分前の通知を送信する'

    def handle(self, *args, **options):
        now = timezone.now()
        
        # 10分後の時間を計算
        notification_time = now + timedelta(minutes=10)
        
        # 現在から10分後に予定されている送迎スケジュールを検索
        # actual_transport_datetimeがある場合はそれを使用し、なければscheduled_transport_datetimeを使用
        schedules = TransportSchedule.objects.filter(
            deleted_at__isnull=True,
            status=1  # Scheduled状態のみ
        ).select_related('user')
        
        for schedule in schedules:
            # 実際の送迎時間かスケジュール時間を使用
            transport_time = schedule.actual_transport_datetime or schedule.scheduled_transport_datetime
            
            # 通知すべき時間かどうかチェック (現在時刻から10分後の時間と一致するか)
            time_diff = (transport_time - now).total_seconds() / 60
            
            # 9分後～11分後の範囲内なら通知を送信（余裕を持たせる）
            if 9 <= time_diff <= 11:
                user = schedule.user
                if user.expo_push_token:
                    # 利用者名
                    user_name = f"{user.last_name} {user.first_name}"
                    
                    # 通知タイトル
                    title = "送迎のお知らせ"
                    
                    # 通知メッセージ
                    message = f"{user_name}様、送迎の10分前です。準備をお願いします。"
                    
                    # 追加データ
                    extra_data = {
                        "schedule_id": schedule.id,
                        "type": "transport_reminder"
                    }
                    
                    # 通知送信
                    success = NotificationService.send_push_notification(
                        user.expo_push_token, 
                        title, 
                        message, 
                        extra_data
                    )
                    
                    if success:
                        self.stdout.write(
                            self.style.SUCCESS(f"送迎通知送信成功: {user_name}")
                        )
                    else:
                        self.stdout.write(
                            self.style.WARNING(f"送迎通知送信失敗: {user_name}")
                        )
                else:
                    self.stdout.write(
                        self.style.WARNING(f"プッシュトークンなし: {user.last_name} {user.first_name}")
                    )
        
        self.stdout.write(self.style.SUCCESS('処理完了'))