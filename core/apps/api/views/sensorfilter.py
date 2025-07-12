from rest_framework.viewsets import ModelViewSet
from django.db.models.functions import TruncHour, TruncDay
from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from core.apps.api.models import SensordataModel
from core.apps.api.filters.sensordata import SensorDataFilter
from django_core.mixins import BaseViewSetMixin

from rest_framework.permissions import AllowAny
from core.apps.api.serializers.sensordata import BaseSensordataSerializer



class SensorDataViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = SensordataModel.objects.all()
    serializer_class = BaseSensordataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SensorDataFilter
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if 'daily' in request.GET:
            data = queryset.annotate(hour=TruncHour('time')) \
                .values('hour') \
                .annotate(total_flow=Sum('flow')) \
                .order_by('hour')

            result = [
                {"hour": item['hour'].strftime("%H:00"), "flow": round(item['total_flow'], 2)}
                for item in data
            ]
            return Response(result)

        elif 'weekly' in request.GET or 'monthly' in request.GET:
            data = queryset.annotate(day=TruncDay('time')) \
                .values('day') \
                .annotate(total_flow=Sum('flow')) \
                .order_by('day')

            result = [
                {"date": item['day'].strftime("%Y-%m-%d"), "flow": round(item['total_flow'], 2)}
                for item in data
            ]
            return Response(result)

        return super().list(request, *args, **kwargs)
