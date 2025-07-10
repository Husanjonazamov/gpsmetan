from django import forms

from core.apps.api.models import VehicleModel


class VehicleForm(forms.ModelForm):

    class Meta:
        model = VehicleModel
        fields = "__all__"
