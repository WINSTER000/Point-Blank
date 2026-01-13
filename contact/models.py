from django.db import models
from datetime import datetime

# Create your models here.
class Clients(models.Model):
    client_name = models.CharField(null=False, blank=False, max_length=100)
    client_email = models.EmailField(null=False, blank=False, max_length=100)
    client_phone_number = models.CharField(null=True, max_length=20)
    client_subject = models.CharField(null=False, blank=False, max_length=100)
    client_message = models.CharField(null=False, blank=False, max_length=100)
    added_date = models.DateTimeField(default=datetime.now)

class Users(models.Model):
    user_first_name = models.CharField(null=False, blank=False, max_length=100)
    user_last_name = models.CharField(null=False, blank=False, max_length=100)
    user_email = models.EmailField(null=False, blank=False, max_length=100)
    user_phone_number = models.CharField(null=True, max_length=20)
    user_password = models.CharField(null=False, max_length=25)
    user_date_of_birth = models.DateField()
    added_date = models.DateTimeField(default=datetime.now)

class Orders(models.Model):
    buyer_first_name = models.CharField(null=False, blank=False, max_length=100)
    buyer_last_name = models.CharField(null=False, blank=False, max_length=100)
    buyer_email = models.EmailField(null=False, blank=False, max_length=100)
    buyer_phone_number = models.CharField(null=False,blank=False, max_length=20)
    buyer_dealer_name = models.CharField(null=False,blank=False, max_length=100)
    buyer_street_address = models.CharField(null=False, blank=False, max_length=200, default=None)
    buyer_city = models.CharField(null=False, blank=False, max_length=50, default=None)
    buyer_state = models.CharField(null=False, blank=False, max_length=50, default=None)
    buyer_zip_code = models.CharField(null=False, blank=False, max_length=10, default=None)
    buyer_user_id = models.ForeignKey(Users,on_delete=models.CASCADE, blank=False, null= False)
    added_date = models.DateTimeField(default=datetime.now)