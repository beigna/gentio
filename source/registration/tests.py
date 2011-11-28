
from django.utils import unittest

from registration.forms import RegistrationForm

class RegistrationTest(unittest.TestCase):
    def test_empty_password(self):
        form = RegistrationForm({
            'email': 'my@email.com',
            'password1': None,
            'password2': None,
        })

        self.assertFalse(form.is_valid())

    def test_ok(self):
        form = RegistrationForm({
            'email': 'my@email.com',
            'password1': '1234',
            'password2': '1234',
        })

        self.assertTrue(form.is_valid())
