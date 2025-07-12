from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import DeviceModel
from core.apps.api.serializers.device import CreateDeviceSerializer, ListDeviceSerializer, RetrieveDeviceSerializer
from core.apps.api.filters import DeviceFilter 

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action



class DeviceStatusViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = ListDeviceSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["get"], url_path="inactive")
    def inactive_devices(self, request):
        queryset = DeviceModel.objects.filter(is_active=False)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=["post"], url_path="activate")
    def activate_device(self, request):
        device_id = request.data.get("deviceId")
        
        device_id = int(device_id)
        device = DeviceModel.objects.get(deviceId=device_id)
    

        device.is_active = True
        device.save(update_fields=["is_active"])

        return Response({
            "status": True,
            "message": f"Yartildi"
        }, status=status.HTTP_200_OK)



@extend_schema(tags=["device"])
class DeviceView(BaseViewSetMixin, ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = ListDeviceSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = DeviceFilter
    search_fields = ["deviceId", "status"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListDeviceSerializer,
        "retrieve": RetrieveDeviceSerializer,
        "create": CreateDeviceSerializer,
        "partial_update": CreateDeviceSerializer
    }
    
    def get_queryset(self):
        return DeviceModel.objects.filter(is_active=True)
    

    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active = False
        instance.save(update_fields=["is_active"])
        
        return Response({
            "status": True,
            "message": "o'chirildi"
        }, status=status.HTTP_200_OK)
    
    
    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response(
            response.data
        )
    
    
