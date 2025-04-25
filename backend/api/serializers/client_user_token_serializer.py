from rest_framework import serializers
from api.models.client_user import ClientUser

class ClientUserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUser
        fields = ['id', 'expo_push_token']
        extra_kwargs = {
            'id': {'read_only': False, 'required': True}
        }