from django.db import models

class MyUser(models.Model):
    first_name = models.CharField(name=('first_name'), max_length=150)
    last_name = models.CharField(name=('last_name'), max_length=150)
    email = models.EmailField(name=('email'), unique=True)
    trBalance = models.FloatField(name=('trBalance'), default=0)
    usdBalance = models.FloatField(name=('usdBalance'), default=0)
    euroBalance = models.FloatField(name=('euroBalance'), default=0)
    btcBalance = models.FloatField(name=('btcBalance'), default=0)
    ethBalance = models.FloatField(name=('ethBalance'), default=0)
    totalBalance = models.FloatField(name=('totalBalance'), default=0)
    investingBalance = models.FloatField(name=('investingBalance'), default=0)