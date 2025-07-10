from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import DeviceModel


@register(DeviceModel)
class DeviceTranslation(TranslationOptions):
    fields = []
