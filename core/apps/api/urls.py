from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import (
    SensordataView,
    DeviceView,
    VehicleView
)

router = DefaultRouter()
router.register(r"sensor-data", SensordataView, basename="sensor")
router.register(r"device", DeviceView, basename="device")
router.register(r"vehicle", VehicleView, basename="vehicle")


urlpatterns = [
    path("", include(router.urls)),
]
