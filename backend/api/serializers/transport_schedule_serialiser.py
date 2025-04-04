from rest_framework import serializers
from api.models.transport_schedule import TransportSchedule

class TransportScheduleSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.name', read_only=True)
    
    class Meta:
        model = TransportSchedule
        fields = ['id', 'user', 'user_name', 'scheduled_transport_datetime', 'actual_transport_datetime', 'created_at', 'updated_at']
        
    def validate(self, data):
        """送迎時間が営業時間内かチェック（例: 8:00-18:00）"""
        scheduled_transport_time = data.get('scheduled_transport_datetime')
        if scheduled_transport_time:
            hour = scheduled_transport_time.hour
            if hour < 8 or hour >= 18:
                raise serializers.ValidationError("送迎時間は8:00から18:00の間で設定してください。")
        actual_transport_datetime = data.get('actual_transport_datetime')
        if actual_transport_datetime:
            hour = actual_transport_datetime.hour
            if hour < 8 or hour >= 18:
                raise serializers.ValidationError("送迎時間は8:00から18:00の間で設定してください。")
        return data