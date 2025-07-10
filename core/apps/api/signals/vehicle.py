from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import VehicleModel


@receiver(post_save, sender=VehicleModel)
def VehicleSignal(sender, instance, created, **kwargs): ...
