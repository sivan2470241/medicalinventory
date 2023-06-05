from django import forms
from registration.models import Registration
from .models import Qualification, specializations
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ['name', 'email', 'mobile', 'highest_qualification', 'specialized_subject', 'photo', 'resume']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['highest_qualification'].queryset = Qualification.objects.all()
        self.fields['specialized_subject'].queryset =  specializations.objects.all()
 