from django import forms
from django.contrib.auth.models import User

from .models import Profile


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input header-name', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input header-last', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['department', 'major', 'student_id', 'phone_number', 'date_of_birth', 'enrollment_date', 
                  'address', 'expected_graduation', 'advisor', 'emergency_contact_name', 
                  'emergency_contact_phone', 'emergency_contact_relationship', 'emergency_contact_email']
        widgets = {
            'department': forms.TextInput(attrs={'class': 'form-input'}),
            'major': forms.TextInput(attrs={'class': 'form-input'}),
            'student_id': forms.TextInput(attrs={'class': 'form-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-input'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'enrollment_date': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'address': forms.Textarea(attrs={'class': 'form-input', 'rows': 3}),
            'expected_graduation': forms.DateInput(attrs={'class': 'form-input', 'type': 'date'}),
            'advisor': forms.TextInput(attrs={'class': 'form-input'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-input'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-input'}),
            'emergency_contact_relationship': forms.TextInput(attrs={'class': 'form-input'}),
            'emergency_contact_email': forms.EmailInput(attrs={'class': 'form-input'}),
        }
