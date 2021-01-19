from django.db import models
from accounts.models import Account

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='my_profile')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=10)
    bankingDetails = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_banking_details')

class UserAddress(models.Model):
    contact = models.ForeignKey(Profile, on_delete=models.CASCADE)
    addressLineOne = models.CharField(max_length=30)
    addressLineTwo = models.CharField(max_length=30)
    surburb = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=4)