from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class DeviceModel(AbstractBaseModel):
    deviceId = models.IntegerField(unique=True, verbose_name=_("Device id"))

    def __str__(self):
        return str(self.deviceId)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "device"
        verbose_name = _("DeviceModel")
        verbose_name_plural = _("DeviceModels")
