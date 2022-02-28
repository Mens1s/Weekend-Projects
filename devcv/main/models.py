from django.db import models

# Create your models here.
class Userdata(models.Model):
    username = models.TextField(max_length=20)
    bio = models.TextField(max_length=450)
    school = models.TextField(max_length=20)
    projects = models.TextField(null=True)
    