from rest_framework import serializers

from core.apps.api.models import VehicleModel, DeviceStatusChoice
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
        if obj.device:
            return BaseDeviceSerializer(obj.device).data
        return None

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
        
        extra_kwargs = {
            "device": {"required": False, "allow_null": True}  
        }
    
    def create(self, validated_data):
        device = validated_data.get("device")
        instance = super().create(validated_data)
        
        if device:
            device.status = DeviceStatusChoice.connected
            device.save(update_fields=['status'])
        return instance
    
    
    def update(self, instance, validated_data):
        old_device = instance.device
        new_device = validated_data.get("device", old_device)
        
        instance = super().update(instance, validated_data)
        
        if old_device and old_device != new_device:
            old_device.status = DeviceStatusChoice.disconnected
            old_device.save(update_fields=['status'])
        
        if new_device:
            new_device.status = DeviceStatusChoice.connected
            new_device.save(update_fields=['status'])
        else:
            if old_device:
                old_device.status = DeviceStatusChoice.disconnected
                old_device.save(update_fields=['status'])
                
        return instance