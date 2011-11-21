
from django import forms


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField()

    password1 = froms.CharField(
        widget=forms.PasswordInput(attrs=attrs_dict, render_value=False))
    password2 = froms.CharField(
        widget=forms.PasswordInput(attrs=attrs_dict, render_value=False))

    def clean(self):
        passwd1 = self.cleaned_data.get('password1')
        passwd2 = self.cleaned_data.get('password2')

        if not passwd1 or passwd1 != passwd2:
                raise forms.ValidationError('The passwords doesn\'t match.')

        return self.cleaned_data
