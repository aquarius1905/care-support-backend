from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from api.models.client_user import ClientUser
from api.serializers.client_user_token_serializer import ClientUserTokenSerializer

class ClientUserTokenViewSet(viewsets.ModelViewSet):
    queryset = ClientUser.objects.all()
    serializer_class = ClientUserTokenSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user_id = serializer.validated_data.get('id')
        expo_token = serializer.validated_data.get('expo_push_token')
        
        try:
            user = ClientUser.objects.get(id=user_id)
            user.expo_push_token = expo_token
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ClientUser.DoesNotExist:
            return Response(
                {"error": "指定されたユーザーが存在しません"}, 
                status=status.HTTP_404_NOT_FOUND
            )
    
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)