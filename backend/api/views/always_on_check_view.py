from rest_framework.response import Response
from rest_framework import status
from rest_framework import views

class AlwaysOnCheckView(views.APIView):
    """
    AWS側から/にリクエストが来てしまうのでエンドポイントを用意している（ただ200を返すだけ）
    """
    permission_classes = ()
    authentication_classes = ()

    def get(self, request, *args, **kwargs):
        return Response({}, status=status.HTTP_200_OK)
