from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.client_user_view import ClientUserViewSet
from api.views.transport_schedule_view import TransportScheduleViewSet
from api.views.client_user_token_view import ClientUserTokenViewSet

router = DefaultRouter()
router.register(r'users', ClientUserViewSet)
router.register(r'transport-schedules', TransportScheduleViewSet)
router.register(r'push-token', ClientUserTokenViewSet, basename='push-token')

urlpatterns = [
    path('', include(router.urls)),
]