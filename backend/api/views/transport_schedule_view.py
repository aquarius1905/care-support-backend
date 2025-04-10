
import logging
from api.models.client_user import ClientUser
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.dateparse import parse_date
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
        date_str = self.request.query_params.get('date')
        if date_str:
            date = parse_date(date_str)
            if date:
                start = make_aware(datetime.combine(date, time.min), timezone=JST)
                end = make_aware(datetime.combine(date, time.max), timezone=JST)
                return self.queryset.filter(scheduled_transport_datetime__range=(start, end))
        return self.queryset.none()
    
    # @action(detail=False, methods=['post'])
    # def update_transport_time(self, request):
    #     """送迎時間の更新API"""
    #     user_id = request.data.get('user_id')
    #     datetime_str = request.data.get('datetime')
        
    #     if not user_id or not datetime_str:
    #         return Response(
    #             {"error": "送迎者ID, 送迎時間は必須です"}, 
    #             status=status.HTTP_400_BAD_REQUEST
    #         )
            
    #     try:
    #         date_time_obj = datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')
            
    #         # 既存のスケジュールを検索するか、新規作成
    #         schedule, created = TransportSchedule.objects.get_or_create(
    #             user_id=user_id,
    #             actual_transport_datetime=date_time_obj,
    #             defaults={'scheduled_transport_datetime': date_time_obj}
    #         )
            
    #         if not created:
    #             # 既存のスケジュールの場合は時間を更新
    #             schedule.actual_transport_datetime = date_time_obj
    #             schedule.save()
            
    #         serializer = self.get_serializer(schedule)
    #         return Response(serializer.data)
            
    #     except (ValueError, ClientUser.DoesNotExist):
    #         return Response(
    #             {"error": "無効なデータ形式または存在しないユーザーです"}, 
    #             status=status.HTTP_400_BAD_REQUEST
    #         )