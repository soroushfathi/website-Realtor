from django.db import models
from datetime import datetime

SITUATION = (('deny','deny'),('accept','accept'),('loading','loading'))
class Order(models.Model):
    listing_name = models.CharField(max_length=30, blank=False, null=True)
    listing_id = models.IntegerField(blank=False,)
    client_email = models.CharField(max_length=30, blank=False, null=True)
    client_name = models.CharField(max_length=25, blank=False, null=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    checking = models.BooleanField(default=False) 

    def __str__(self):
        return self.client_name