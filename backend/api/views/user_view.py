
from rest_framework import viewsets
from api.models.user import User
from api.serializers.user_serialiser import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """利用者のCRUD操作を提供するAPI"""
    queryset = User.objects.all().order_by('name')
    serializer_class = UserSerializer