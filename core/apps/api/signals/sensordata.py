from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.api.models import SensordataModel


@receiver(post_save, sender=SensordataModel)
def SensordataSignal(sender, instance, created, **kwargs): ...
