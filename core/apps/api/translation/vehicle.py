from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import VehicleModel


@register(VehicleModel)
class VehicleTranslation(TranslationOptions):
    fields = []
