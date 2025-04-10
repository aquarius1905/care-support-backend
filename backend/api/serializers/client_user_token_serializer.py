from rest_framework import serializers
from api.models.client_user import ClientUser

class ClientUserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientUser
        fields = ['expo_push_token']