from rest_framework import serializers

from core.apps.api.models import SensordataModel, DeviceModel




class SensorDeviceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensordataModel
        fields = [
            'device'
        ]
    
class BaseSensordataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensordataModel
        fields = [
            "id",
            "flow",
            "pressure",
            "lat",
            "lon",
            "time",
            "temperature",
            "created_at"
            
        ]


class ListSensordataSerializer(BaseSensordataSerializer):
    class Meta(BaseSensordataSerializer.Meta): ...


class RetrieveSensordataSerializer(BaseSensordataSerializer):
    class Meta(BaseSensordataSerializer.Meta): ...


class CreateSensordataSerializer(serializers.ModelSerializer):
    deviceId = serializers.IntegerField(write_only=True)
    
    class Meta:
        model = SensordataModel
        fields = [
            "deviceId",
            "id",
            "flow",
            "pressure",
            "lat",
            "lon",
            "time",
            "temperature"
        ]
        
        
    def create(self, validated_data):
        deviceId = validated_data.pop("deviceId")
        
        device, create = DeviceModel.objects.get_or_create(
            deviceId=deviceId,
            defaults={"is_active": False}
        )
        return SensordataModel.objects.create(deviceId=device, **validated_data)
        
        
