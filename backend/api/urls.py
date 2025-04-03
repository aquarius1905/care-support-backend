from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import ClientUserViewSet, TransportScheduleViewSet

router = DefaultRouter()
router.register(r'users', ClientUserViewSet)
router.register(r'schedules', TransportScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]