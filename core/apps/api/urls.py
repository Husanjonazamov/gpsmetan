from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.apps.api.views import (
    SensordataView,
    DeviceView,
    VehicleView,
    DeviceStatusViewSet
)
from core.apps.api.views.sensorfilter import SensorDataViewSet

router = DefaultRouter()
router.register(r"sensor-data", SensordataView, basename="sensor")
router.register(r"device", DeviceView, basename="device")
router.register(r"vehicle", VehicleView, basename="vehicle")
router.register(r"device-activate", DeviceStatusViewSet, basename="device-active")
router.register(r"sensor-data-filter", SensorDataViewSet, basename="sensor-data-filter")


urlpatterns = [
    path("", include(router.urls)),
]
