from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Setting Model.
class Setting(models.Model):
    site_name = models.CharField(max_length=50)
    support_email = models.CharField(max_length=100)
    stripe_secret_key = models.CharField(max_length=250)
    stripe_publishable_key = models.CharField(max_length=250)
    coinbase_api_Key = models.CharField(max_length=250)
    coinbase_scrate_key = models.CharField(max_length=250)
    def __str__(self):
        site_name = self.site_name
        support_email = self.support_email
        return site_name
