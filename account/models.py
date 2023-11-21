from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_image = models.ImageField(blank=True, null=True)
    phone = models.CharField(verbose_name='전화번호', max_length=11)