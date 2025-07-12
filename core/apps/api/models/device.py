from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class DeviceStatusChoice(models.TextChoices):
    connected = "connected", _("Ulangan")
    disconnected = "disconnected", _("Ulanmagan")
    waiting = "waiting", _("Kutilmoqda")



class DeviceModel(AbstractBaseModel):
    deviceId = models.IntegerField(unique=True, verbose_name=_("Device id"))
    status = models.CharField(
        verbose_name=_("Holat"),
        max_length=20,
        choices=DeviceStatusChoice.choices,
        default=DeviceStatusChoice.disconnected
    )
    is_active = models.BooleanField(verbose_name=_("Faolmi ?"), default=False)

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
