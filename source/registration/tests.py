
from django.utils import unittest

from registration.forms import RegistrationForm

class RegistrationTest(unittest.TestCase):
    def test_invalid_email(self):
        form = RegistrationForm({
            'email': 'myemail.com',
            'password1': '1',
            'password2': '1',
        })

        form.is_valid()

        self.assertEqual(form.errors['email'][0],
            u'Enter a valid e-mail address.')

    def test_empty_password(self):
        form = RegistrationForm({
            'email': 'my@email.com',
            'password1': '',
            'password2': None,
        })

        form.is_valid()

        self.assertEqual(form.errors['password1'][0],
            u'This field is required.')
        self.assertEqual(form.errors['password2'][0],
            u'This field is required.')

    def test_diff_password(self):
        form = RegistrationForm({
            'email': 'my@email.com',
            'password1': '123',
            'password2': 'abc',
        })

        form.is_valid()

        self.assertEqual(form.errors['__all__'][0],
            u'The passwords don\'t match.')

    def test_valid_form(self):
        form = RegistrationForm({
            'email': 'my@email.com',
            'password1': '123',
            'password2': '123',
        })

        form.is_valid()

        self.assertEqual(len(form.errors), 0)
