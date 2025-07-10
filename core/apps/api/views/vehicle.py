from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from core.apps.api.models import VehicleModel
from core.apps.api.serializers.vehicle import CreateVehicleSerializer, ListVehicleSerializer, RetrieveVehicleSerializer

from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.db.models import Q

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
    
    @action(detail=False, methods=['post'], url_path="search", permission_classes=[AllowAny])
    def search(self, request):
        search_term = request.query_params.get("search")
        
        if not search_term:
            return Response({"detail": "Qidiruv so'zi yuborilmadi"}, status=400)
        
        queryset = self.get_queryset().filter(
            Q(name__icontains=search_term) |
            Q(device__deviceId__icontains=search_term) |
            Q(year__icontains=search_term) |
            Q(category__icontains=search_term) |
            Q(number__icontains=search_term) 
        )
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    
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
    
