from rest_framework import serializers

from core.apps.api.models import SensordataModel


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
            "temperature"
        ]


class ListSensordataSerializer(BaseSensordataSerializer):
    class Meta(BaseSensordataSerializer.Meta): ...


class RetrieveSensordataSerializer(BaseSensordataSerializer):
    class Meta(BaseSensordataSerializer.Meta): ...


class CreateSensordataSerializer(BaseSensordataSerializer):
    class Meta(BaseSensordataSerializer.Meta):
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
