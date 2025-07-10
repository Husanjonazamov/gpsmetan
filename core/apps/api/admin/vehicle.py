from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import VehicleModel


@admin.register(VehicleModel)
class VehicleAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
