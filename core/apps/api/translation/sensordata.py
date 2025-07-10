from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import SensordataModel


@register(SensordataModel)
class SensordataTranslation(TranslationOptions):
    fields = []
