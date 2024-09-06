from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Appointment

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['doctor', 'appointment_date', 'appointment_time', 'reason']

 
    patient_name = forms.CharField(max_length=100, required=False)
    patient_email = forms.EmailField(required=False)
    patient_phone = forms.CharField(max_length=15, required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        
        if user and user.is_authenticated:
            self.fields['patient_name'].widget = forms.HiddenInput()
            self.fields['patient_email'].widget = forms.HiddenInput()
            self.fields['patient_phone'].widget = forms.HiddenInput()

