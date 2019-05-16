from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #additional
    portfolio_site = models.URLField(max_length=200, blank = True)
    profile_pic = models.ImageField(upload_to='profile_pics', height_field=None, width_field=None, max_length=None, blank = True)

    def __str__(self):
        return self.user.username

   
