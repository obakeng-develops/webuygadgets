from django.db import models
from accounts.models import Account
from payments.models import Payment

# Create your models here.
class PurchaseOrder(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    order_number = models.IntegerField()
    order_total = models.DecimalField(max_digits=8, decimal_places=2)
    order_status = models.CharField(max_length=1)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)