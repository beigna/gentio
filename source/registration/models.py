from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class ActivationProfile(models.Model):
    user models.OneToOneField(User)

    activation_key = models.CharField(max_length=40)

