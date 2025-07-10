from django import forms

from core.apps.api.models import DeviceModel


class DeviceForm(forms.ModelForm):

    class Meta:
        model = DeviceModel
        fields = "__all__"
