from django import forms
from .models import Preference


class PreferenceModelForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = '__all__'
