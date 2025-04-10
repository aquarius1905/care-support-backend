from rest_framework_simplejwt.views import TokenObtainPairView
from api.auth.serializers import StaffTokenObtainPairSerializer

class StaffTokenObtainPairView(TokenObtainPairView):
    serializer_class = StaffTokenObtainPairSerializer