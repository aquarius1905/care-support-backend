from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

class StaffTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        if self.user.user_type != 'staff':
            raise serializers.ValidationError("このユーザーは施設スタッフではありません。")
        return data