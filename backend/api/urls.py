from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views.client_user_view import ClientUserViewSet
from api.views.transport_schedule_view import TransportScheduleViewSet

router = DefaultRouter()
router.register(r'users', ClientUserViewSet)
router.register(r'schedules', TransportScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]