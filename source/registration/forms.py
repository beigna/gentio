
from django import forms


class RegistrationForm(forms.Form):
    email = forms.EmailField()

    password1 = forms.CharField(widget=forms.PasswordInput(render_value=False))
    password2 = forms.CharField(widget=forms.PasswordInput(render_value=False))

    def clean(self):
        passwd1 = self.cleaned_data.get('password1')
        passwd2 = self.cleaned_data.get('password2')

        if passwd1 != passwd2:
            raise forms.ValidationError('The passwords don\'t match.')

        return self.cleaned_data
