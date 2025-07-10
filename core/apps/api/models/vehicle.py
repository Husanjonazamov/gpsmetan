from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class VehicleModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255, blank=True, null=True)
    device = models.OneToOneField(
        "api.DeviceModel",
        on_delete=models.SET_NULL,
        related_name="vehicle",
        verbose_name=_("Device"),
        blank=True, null=True
    )
    number = models.IntegerField(verbose_name=_("Number"))
    category = models.CharField(verbose_name=_("Category"), max_length=100)
    color = models.CharField(verbose_name=_("Color"), max_length=50)
    year = models.IntegerField(verbose_name=_("Year"))
    image = models.ImageField(verbose_name=_("Image"), upload_to="images/", blank=True, null=True)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "Vehicle"
        verbose_name = _("VehicleModel")
        verbose_name_plural = _("VehicleModels")
