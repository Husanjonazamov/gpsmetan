from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import SensordataModel



@admin.register(SensordataModel)
class SensordataAdmin(ModelAdmin):
    list_display = (
        "id",
        "deviceId",
        "flow",
        "pressure",
        "lat",
        "lon",
        "temperature",
    )
