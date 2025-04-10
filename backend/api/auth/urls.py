# auth/urls.py
from django.urls import path
from api.auth.views import StaffTokenObtainPairView

urlpatterns = [
    path('staff/token/', StaffTokenObtainPairView.as_view(), name='staff_token_obtain_pair'),
]
