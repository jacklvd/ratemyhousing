from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# from django.dispatch import receiver
from django_google_maps import fields as map_fields
from django.core import validators


# class Rental(models.Model):
#     address = map_fields.AddressField(max_length=200)
#     geolocation = map_fields.GeoLocationField(max_length=100)

class Person(models.Model):
    # models.CASCADE to delete the object when the referenced object is deleted
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50, blank=True, null=True)
    User.email = models.EmailField(initial = 'Enter your email', required=True, validators=[validators.EmailValidator(message="Invalid Email")])
    
    def __str__(self) -> str:
        return self.user.first_name