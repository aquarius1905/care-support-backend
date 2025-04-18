
from rest_framework import viewsets
from api.models.client_user import ClientUser
from api.serializers.client_user_serializer import ClientUserSerializer

class ClientUserViewSet(viewsets.ModelViewSet):
    """利用者のCRUD操作を提供するAPI"""
    queryset = ClientUser.objects.all().order_by('facility')
    serializer_class = ClientUserSerializer