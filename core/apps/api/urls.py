from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import (
    SensordataView,
    DeviceView
)

router = DefaultRouter()
router.register(r"sensor-data", SensordataView, basename="sensor")
router.register(r"device", DeviceView, basename="device")


urlpatterns = [
    path("", include(router.urls)),
]
