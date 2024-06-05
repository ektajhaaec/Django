# models.py
from django.db import models

class Profile(models.Model):
    DoesNotExist = None
    objects = None
    name = models.CharField(max_length=255, unique=True)
    address = models.CharField(max_length=255,  null=True,default='Unknown')
    mobile_number = models.CharField(max_length=255,null =True,default = 'Unknown')
    email = models.EmailField(blank=True, null=True,default='Unknown')

    def __str__(self):
        return self.name