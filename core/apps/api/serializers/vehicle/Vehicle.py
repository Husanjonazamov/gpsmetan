from rest_framework import serializers

from core.apps.api.models import VehicleModel
from core.apps.api.serializers.device import BaseDeviceSerializer

class BaseVehicleSerializer(serializers.ModelSerializer):
    device = serializers.SerializerMethodField()
    
    class Meta:
        model = VehicleModel
        fields = [
            "id",
            "name",
            "device",
            "number",
            "category",
            "color",
            "year",
            "image",
        ]

    def get_device(self, obj):
        return BaseDeviceSerializer(obj.device).data

class ListVehicleSerializer(BaseVehicleSerializer):
    class Meta(BaseVehicleSerializer.Meta): ...


class RetrieveVehicleSerializer(BaseVehicleSerializer):
    class Meta(BaseVehicleSerializer.Meta): ...


class CreateVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = [
            "id",
            "name",
            "device",
            "number",
            "category",
            "color",
            "year",
            "image",
        ]
