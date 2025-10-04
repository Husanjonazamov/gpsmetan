from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import SensordataModel, DeviceModel
from core.apps.api.serializers.sensordata import (
    CreateSensordataSerializer,
    ListSensordataSerializer,
    RetrieveSensordataSerializer,
    SensorDeviceItemSerializer
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from core.apps.api.views.statistika import get_filtered_device_stats



@extend_schema(tags=["SensorData"])
class SensordataView(BaseViewSetMixin, ModelViewSet):
    queryset = SensordataModel.objects.all()
    serializer_class = ListSensordataSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListSensordataSerializer,
        "retrieve": RetrieveSensordataSerializer,
        "create": CreateSensordataSerializer,
    }
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({"status": "ok"}, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=['get'], url_path=r"by-device/(?P<device_id>\d+)", permission_classes=[AllowAny])
    def by_device(self, request, device_id):
        try:
            device = DeviceModel.objects.get(deviceId=device_id)
        except DeviceModel.DoesNotExist:
            return Response({"error": "Device topilmadi"}, status=404)

        queryset = self.queryset.filter(deviceId=device)

        stats_result = get_filtered_device_stats(queryset, request)

        if stats_result["type"] != "none":
            return Response({
                "status": True,
                "deviceId": device.deviceId,
                "stats": stats_result["data"]
            })
        sensor_data = queryset.order_by("-created_at")
        serializer = ListSensordataSerializer(sensor_data, many=True)
        
        return Response({
            "status": True,
            "deviceId": device.deviceId,
            "sensors": serializer.data
        })


                
