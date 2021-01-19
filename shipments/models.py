from django.db import models
from orders.models import PurchaseOrder

# Create your models here.
class Courier(models.Model):
    courier_name = models.CharField(max_length=50)

class Shipment(models.Model):
    shipment_type = models.CharField(max_length=30)
    shipment_number = models.CharField(max_length=30)
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    shipment_cost = models.DecimalField(max_digits=8, decimal_places=2)
    shipment_option = models.CharField(max_length=30)
    courier = models.ForeignKey(Courier, on_delete=models.CASCADE)
    shipment_from = models.CharField(max_length=50)
    shipment_to = models.CharField(max_length=50)
    shipment_start_date = models.DateTimeField()
    shipment_end_date = models.DateTimeField()
