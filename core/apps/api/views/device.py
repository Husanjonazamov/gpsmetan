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
    

    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "status": True,
            "message": "o'chirildi"
        }, status=status.HTTP_200_OK)
    
    
    def partial_update(self, request, *args, **kwargs):
        response = super().partial_update(request, *args, **kwargs)
        return Response(
            response.data
        )
    
    
