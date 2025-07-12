from django_filters import rest_framework as filters

from core.apps.api.models import SensordataModel


class SensorDataFilter(filters.FilterSet):
    daily = filters.DateFilter(method="filter_daily")
    weekly = filters.CharFilter(method="filter_range")
    monthly = filters.CharFilter(method="filter_range")

    class Meta:
        model = SensordataModel
        fields = ['daily', 'weekly', 'monthly']

    def filter_daily(self, queryset, name, value):
        return queryset.filter(time__date=value)

    def filter_range(self, queryset, name, value):
        try:
            start_str, end_str = value.split("&")
        except ValueError:
            return queryset.none()
        
        from django.utils.dateparse import parse_date
        start_date = parse_date(start_str)
        end_date = parse_date(end_str)
        return queryset.filter(time__date__range=(start_date, end_date))
