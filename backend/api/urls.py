from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.client_user_view import ClientUserViewSet
from api.views.transport_schedule_view import TransportScheduleViewSet
from api.views.client_user_token_view import ClientUserTokenViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', ClientUserViewSet)
router.register(r'transport-schedules', TransportScheduleViewSet)
router.register(r'push-token', ClientUserTokenViewSet, basename='push-token')

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]