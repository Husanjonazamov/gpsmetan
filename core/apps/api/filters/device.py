from django_filters import rest_framework as filters

from core.apps.api.models import DeviceModel
from core.apps.api.models.device import DeviceStatusChoice


class DeviceFilter(filters.FilterSet):
    status = filters.ChoiceFilter(choices=DeviceStatusChoice.choices)

    class Meta:
        model = DeviceModel
        fields = [
            "status",
        ]
