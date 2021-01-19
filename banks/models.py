from django.db import models
from accounts.models import Account

# Create your models here.
class Bank(models.Model):
    bankName = models.CharField(max_length=30)
    bankCode = models.CharField(max_length=6)

class BankingDetail(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    accountNumber = models.CharField(max_length=13)
    bankId = models.ForeignKey(Bank, on_delete=models.CASCADE)
    accountHolder = models.CharField(max_length=30)
    accountType = models.CharField(max_length=20)