
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    email = forms.EmailField()

    password1 = forms.CharField(widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=False))

    def clean_email(self):
        try:
            user = User.objects.get(email__iexact=self.cleaned_data['email'])

        except User.DoesNotExist:
            return self.cleaned_data['email']

        raise forms.ValidationError('A user with that username already exists.')

    def clean(self):
        passwd1 = self.cleaned_data.get('password1')
        passwd2 = self.cleaned_data.get('password2')

        if passwd1 != passwd2:
            raise forms.ValidationError('The passwords don\'t match.')

        return self.cleaned_data
