# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver

# from core.apps.api.models import VehicleModel


# def update_device_status(device):
#     if not device:
#         return
#     is_connected = hasattr(device, 'vehicle') and device.vehicle is not None
#     device.status = "connected" if is_connected else "disconnected"
#     device.save(update_fields=["status"])



# @receiver(post_save, sender=VehicleModel)
# @receiver(post_delete, sender=VehicleModel)
# def VehicleSignal(sender, instance, **kwargs):
#     update_device_status(instance.device)
