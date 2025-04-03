from rest_framework import serializers
from api.models.client_user import ClientUser

class ClientUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUser
        fields = ['id', 'name', 'created_at', 'updated_at']