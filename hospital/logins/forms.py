from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)
    phone_number = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')

        if not email and not phone_number:
            raise forms.ValidationError('You must provide either an email or phone number.')

        return cleaned_data


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Email or Phone Number')

    def clean(self):
        username = self.cleaned_data.get('username')
        if '@' in username:
            self.cleaned_data['email'] = username
        else:
            self.cleaned_data['phone_number'] = username
        return super().clean()
