from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import DeviceModel


@admin.register(DeviceModel)
class DeviceAdmin(ModelAdmin):
    list_display = (
        "id",
        "deviceId",
        "is_active",
        "status"
    )
