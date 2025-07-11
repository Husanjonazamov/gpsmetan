from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import DeviceModel





@receiver(post_save, sender=DeviceModel)
def DeviceSignal(sender, instance, created, **kwargs): ...
