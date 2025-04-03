from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import UserViewSet, TransportScheduleViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'schedules', TransportScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]