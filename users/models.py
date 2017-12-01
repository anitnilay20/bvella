from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class users(models.Model):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=10)
    pincode = models.CharField(max_length=8)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=16)
    phno = models.CharField(max_length=10)

    def __str__(self):
        return self.name
