import logging
from api.models.client_user import ClientUser
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.dateparse import parse_date, parse_datetime
from django.utils.timezone import make_aware
from datetime import datetime, time
from api.models.transport_schedule import TransportSchedule
from api.serializers.transport_schedule_serializer import TransportScheduleSerializer
from zoneinfo import ZoneInfo
from django.conf import settings

logger = logging.getLogger(__name__)
JST = ZoneInfo(settings.TIME_ZONE)

class TransportScheduleViewSet(viewsets.ModelViewSet):
    queryset = TransportSchedule.objects.select_related('user').all()
    serializer_class = TransportScheduleSerializer

    def get_queryset(self):
        queryset = self.queryset
        date_str = self.request.query_params.get('date')
        if date_str:
            date = parse_date(date_str)
            if date:
                start = make_aware(datetime.combine(date, time.min), timezone=JST)
                end = make_aware(datetime.combine(date, time.max), timezone=JST)
                return queryset.filter(scheduled_transport_datetime__range=(start, end))
        return queryset

    
    def update(self, request, *args, **kwargs):
        """送迎時間の更新API"""
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        # リクエストデータから time が送られてきた場合の処理
        time_str = request.data.get('time')
        if time_str:
            # 現在の scheduled_transport_datetime の日付部分を取得
            current_date = instance.scheduled_transport_datetime.date()
            
            # 時間文字列を解析 (HH:MM 形式を想定)
            try:
                hours, minutes = map(int, time_str.split(':'))
                # 日付と時間を組み合わせる
                new_datetime = make_aware(
                    datetime.combine(current_date, time(hours, minutes)), 
                    timezone=JST
                )
                
                # actual_transport_datetime を更新
                request.data['actual_transport_datetime'] = new_datetime
            except (ValueError, TypeError):
                return Response(
                    {"error": "無効な時間形式です。HH:MM 形式で指定してください。"}, 
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
    
    @action(detail=False, methods=['post'])
    def update_transport_time(self, request):
        """送迎時間の更新API (レガシー対応)"""
        user_id = request.data.get('user_id')
        datetime_str = request.data.get('datetime')
        
        if not user_id or not datetime_str:
            return Response(
                {"error": "送迎者ID, 送迎時間は必須です"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            date_time_obj = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            date_time_obj = make_aware(date_time_obj, timezone=JST)
            
            # 既存のスケジュールを検索
            schedule = TransportSchedule.objects.filter(user_id=user_id).first()
            
            if not schedule:
                return Response(
                    {"error": "指定されたユーザーのスケジュールが見つかりません"}, 
                    status=status.HTTP_404_NOT_FOUND
                )
            
            # 実際の送迎時間を更新
            schedule.actual_transport_datetime = date_time_obj
            schedule.save()
            
            serializer = self.get_serializer(schedule)
            return Response(serializer.data)
            
        except (ValueError, ClientUser.DoesNotExist):
            return Response(
                {"error": "無効なデータ形式または存在しないユーザーです"}, 
                status=status.HTTP_400_BAD_REQUEST
            )