from rest_framework import serializers

from core.apps.api.models import DeviceModel







class BaseDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceModel
        fields = [
            "id",
            "deviceId",
            "status",
        ]


class ListDeviceSerializer(BaseDeviceSerializer):
    class Meta(BaseDeviceSerializer.Meta): ...


class RetrieveDeviceSerializer(BaseDeviceSerializer):
    class Meta(BaseDeviceSerializer.Meta): ...


class CreateDeviceSerializer(BaseDeviceSerializer):
    class Meta(BaseDeviceSerializer.Meta):
        fields = [
            "id",
            "deviceId",
        ]
