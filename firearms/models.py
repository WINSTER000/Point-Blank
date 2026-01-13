from django.db import models
from datetime import datetime

# Create your models here.
class Firearms(models.Model):
    firearms_name = models.CharField(null=False, blank=False, max_length=100)
    firearms_image = models.CharField(null=False, blank=False, max_length=200, default=None)
    firearms_price = models.DecimalField(max_digits=12, decimal_places=2)
    firearms_description = models.TextField(null=False, blank=False, max_length=500)
    firearms_ammo = models.CharField(null=False, blank=False, max_length=50)
    firearms_ammo_capacity = models.CharField(null=False, blank=False, max_length=50)
    firearms_caliber = models.CharField(null=False, blank=False, max_length=50)
    firearms_barrel_length = models.CharField(null=False, blank=False, max_length=50)
    firearms_overall_length = models.CharField(null=False, blank=False, max_length=50)
    firearms_weight = models.CharField(null=False, blank=False, max_length=50)
    firearms_finish = models.CharField(null=False, blank=False, max_length=50)
    firearms_action = models.CharField(null=False, blank=False, max_length=50)
    added_date = models.DateTimeField(default=datetime.now)