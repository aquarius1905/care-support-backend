
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models.transport_schedule import TransportSchedule
from api.serializers.transport_schedule_serialiser import TransportScheduleSerializer
import datetime

class TransportScheduleViewSet(viewsets.ModelViewSet):
    """送迎予定のCRUD操作を提供するAPI"""
    queryset = TransportSchedule.objects.all().order_by('date', 'transport_time')
    serializer_class = TransportScheduleSerializer
    
    def get_queryset(self):
        """クエリパラメータによるフィルタリング"""
        queryset = TransportSchedule.objects.all().order_by('date', 'transport_time')
        
        # 日付でフィルタリング
        date = self.request.query_params.get('date')
        if date:
            try:
                date_obj = datetime.datetime.strptime(date, '%Y-%m-%d').date()
                queryset = queryset.filter(date=date_obj)
            except ValueError:
                pass  # 無効な日付形式の場合は無視
        
        # ユーザーでフィルタリング
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
            
        return queryset
    
    @action(detail=False, methods=['post'])
    def update_transport_time(self, request):
        """送迎時間の更新API"""
        user_id = request.data.get('user_id')
        date_str = request.data.get('date')
        time_str = request.data.get('time')
        
        if not user_id or not date_str or not time_str:
            return Response(
                {"error": "user_id, date, timeは必須です"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
            
        try:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            time_obj = datetime.datetime.strptime(time_str, '%H:%M').time()
            
            # 既存のスケジュールを検索するか、新規作成
            schedule, created = TransportSchedule.objects.get_or_create(
                user_id=user_id,
                date=date_obj,
                defaults={'transport_time': time_obj}
            )
            
            if not created:
                # 既存のスケジュールの場合は時間を更新
                schedule.transport_time = time_obj
                schedule.save()
            
            serializer = self.get_serializer(schedule)
            return Response(serializer.data)
            
        except (ValueError, User.DoesNotExist):
            return Response(
                {"error": "無効なデータ形式または存在しないユーザーです"}, 
                status=status.HTTP_400_BAD_REQUEST
            )