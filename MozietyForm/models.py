from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=30)
    dept= models.CharField(max_length=30)
    usn = models.CharField(max_length=30)
    semester = models.CharField(max_length=2)
    email = models.EmailField()
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered with country code. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)