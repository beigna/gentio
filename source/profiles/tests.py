"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from datetime import date

from django.utils import unittest
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from profiles.models import UserProfile


class ProfileTest(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_has_user_profile(self):
        try:
            profile = self.user.get_profile()
        except UserProfile.DoesNotExist:
            profile = None

        self.assertIsNotNone(profile)

    def test_set_sex(self):
        self.user.userprofile.sex = 'f'
        self.user.userprofile.save()

        self.assertEqual(self.user.userprofile.sex, 'f')

    def test_set_birthday(self):
        self.user.userprofile.birthday = date(1984, 9, 28)
        self.user.userprofile.save()

        self.assertEqual(self.user.userprofile.birthday, date(1984, 9, 28))

    def test_set_birthday_greater_than_today(self):
        self.user.userprofile.birthday = date(2984, 9, 28)

        self.assertRaises(ValidationError, self.user.userprofile.save)
