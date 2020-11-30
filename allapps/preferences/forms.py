from django import forms
from django.core.exceptions import ValidationError
from .models import Preference


class PreferenceModelForm(forms.ModelForm):
    class Meta:
        model = Preference
        fields = '__all__'

    def clean_bio(self):
        bio = self.cleaned_data.get('bio')
        if len(bio) < 10:
            raise ValidationError('Bio is too short!!')
        return bio

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 2:
            raise ValidationError('First Name is too short!!')
        return first_name
