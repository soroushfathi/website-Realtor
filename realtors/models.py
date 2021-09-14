from os import name
from django.db import models

class Realtor(models.Model):
    name    = models.CharField(max_length=100, blank=False)
    phone   = models.CharField(max_length=13, blank=False)
    email   = models.CharField(max_length=25, blank=False)
    address = models.TextField(blank=True)
    main_photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name
