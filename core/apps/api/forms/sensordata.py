from django import forms

from core.apps.api.models import SensordataModel


class SensordataForm(forms.ModelForm):

    class Meta:
        model = SensordataModel
        fields = "__all__"
