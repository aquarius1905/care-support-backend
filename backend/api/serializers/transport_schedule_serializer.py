from rest_framework import serializers
from api.models.transport_schedule import TransportSchedule

class TransportScheduleSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = TransportSchedule
        fields = ['id', 'user', 'user_name', 'scheduled_transport_datetime']

    def get_user_name(self, obj):
        return f"{obj.user.last_name} {obj.user.first_name}"