from django.db import models
from accounts.models import Account
from banks.models import BankingDetail

# Create your models here.
class Payment(models.Model):
    payment_type = models.CharField(max_length=10)
    bankingDetails = models.ForeignKey(BankingDetail, on_delete=models.CASCADE)
    payment_from = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_payment_from')
    payment_date = models.DateTimeField()
    payment_to = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_payment_to')
