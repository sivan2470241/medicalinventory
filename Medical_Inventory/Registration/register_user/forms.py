from django import forms
from django.core.exceptions import ValidationError
from .models import User

class RegistrationForm(forms.ModelForm):
    def clean_name(self):
        name = self.cleaned_data['name']
        if not name.isalpha():
            raise ValidationError('Name should contain only letters.')
        if len(name) > 50:
            raise ValidationError('Name should not exceed 50 characters.')
        return name

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        if not mobile.isdigit() or len(mobile) != 10:
            raise ValidationError('Mobile number should be a 10-digit number.')
        return mobile

    def clean_photo(self):
        photo = self.cleaned_data['photo']
        if photo:
            if not photo.name.lower().endswith(('.jpg', '.jpeg')):
                raise ValidationError('Photo must be in JPG/JPEG format.')
            if photo.size > 200 * 1024:
                raise ValidationError('Photo size should not exceed 200KB.')
        return photo

    def clean_resume(self):
        resume = self.cleaned_data['resume']
        if resume:
            if not resume.name.lower().endswith(('.pdf', '.doc')):
                raise ValidationError('Resume must be in PDF/DOC format.')
            if resume.size > 500 * 1024:
                raise ValidationError('Resume size should not exceed 500KB.')
        return resume

    class Meta:
        model = User
        fields = ['name', 'email', 'mobile', 'highest_qualification', 'specialized_subject','photo','resume']
        widgets = {
            'registration_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'highest_qualification': forms.Select(attrs={'class': 'form-control'}),
            'specialized_subject': forms.Select(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'resume': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
