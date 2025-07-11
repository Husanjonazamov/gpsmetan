from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import DeviceModel
from core.apps.api.serializers.device import CreateDeviceSerializer, ListDeviceSerializer, RetrieveDeviceSerializer
from core.apps.api.filters import DeviceFilter 

from django_filters.rest_framework import DjangoFilterBackend




@extend_schema(tags=["device"])
class DeviceView(BaseViewSetMixin, ModelViewSet):
    queryset = DeviceModel.objects.all()
    serializer_class = ListDeviceSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = DeviceFilter

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListDeviceSerializer,
        "retrieve": RetrieveDeviceSerializer,
        "create": CreateDeviceSerializer,
    }
