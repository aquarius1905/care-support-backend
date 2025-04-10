from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from api.models.client_user import ClientUser
from api.serializers.client_user_token_serializer import ClientUserTokenSerializer

class ClientUserTokenViewSet(viewsets.ModelViewSet):
    queryset = ClientUser.objects.all()
    serializer_class = ClientUserTokenSerializer
    permission_classes = [AllowAny]  # ← これ追加！
