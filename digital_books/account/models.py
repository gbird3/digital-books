from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Define models here

class User(AbstractUser):
	# street_address = models.TextField(null=True, blank=True)
	# city = models.TextField(null=True, blank=True)
	# state = models.TextField(null=True, blank=True)
	# country = models.TextField(null=True, blank=True)
	# zip_code = models.TextField(null=True, blank=True)
	# phoneNumber = models.TextField(null=True, blank=True)
	birthday = models.DateTimeField(null=True, blank=True)
	# image = models.ImageField(null=True, blank=True)
