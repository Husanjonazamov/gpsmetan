from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class SensordataModel(AbstractBaseModel):
    deviceId = models.ForeignKey(
        "api.DeviceModel",
        on_delete=models.CASCADE,
        to_field="deviceId",
        blank=True, null=True
    )
    flow = models.FloatField(blank=True, null=True)
    pressure = models.FloatField(blank=True, null=True)    
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    
    
    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "SensorData"
        verbose_name = _("SensordataModel")
        verbose_name_plural = _("SensordataModels")
