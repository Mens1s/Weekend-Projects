from django.db import models

# Create your models here.
class Userdata(models.Model):
    first_name = models.CharField(name=('first_name'), max_length=150)
    last_name = models.CharField(name=('last_name'), max_length=150)
    email = models.EmailField(name=('email'), unique=True)
    description = models.TextField(max_length=450)
    projects = models.TextField(null=True)
    