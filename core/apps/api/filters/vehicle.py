from django_filters import rest_framework as filters

from core.apps.api.models import VehicleModel


class VehicleFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = VehicleModel
        fields = [
            "name",
        ]
