from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import VehicleModel
from core.apps.api.serializers.vehicle import CreateVehicleSerializer, ListVehicleSerializer, RetrieveVehicleSerializer


@extend_schema(tags=["Vehicle"])
class VehicleView(BaseViewSetMixin, ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = ListVehicleSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListVehicleSerializer,
        "retrieve": RetrieveVehicleSerializer,
        "create": CreateVehicleSerializer,
    }
