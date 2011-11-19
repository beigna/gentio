from datetime import date

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save


SEX_CHOICES = (('m', 'Male'),('f', 'Female'))

def validate_birthday(value):
    if value > date.today():
        raise ValidationError(u'The birthday mustn\'t be greater than today')


class UserProfile(models.Model):
    user = models.OneToOneField(User)

    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birthday = models.DateField(validators=[validate_birthday])

    is_approved = models.BooleanField()

    def __unicode__(self):
        return u'%s\'s profile' % self.user

    def save(self, *args, **kwargs):
        validate_birthday(self.birthday)
        super(UserProfile, self).save(*args, **kwargs)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile()
        user_profile.user = instance
        user_profile.birthday = date(1900, 1, 1)
        user_profile.save()

post_save.connect(create_user_profile, sender=User)
