from django.contrib.auth.models import User
from django.db import models

class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contactNumber =  models.CharField(max_length=20, blank=True)
    mobileNumber =  models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=6)
    models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_image', blank=True)
    address_one = models.CharField(max_length=100,blank=True)
    city = models.CharField(max_length=50, blank=True)
    post_code = models.CharField(max_length=6 , blank=True)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=10)
    about_you = models.CharField(max_length=100)

