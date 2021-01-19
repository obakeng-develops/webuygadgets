from django.contrib import admin
from .models import Shipment

# Register your models here.
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'shipment_number', 'order', 'shipment_from', 'shipment_to', 'shipment_start_date', 'shipment_end_date')
    list_filter = ('id', 'shipment_number', 'order', 'shipment_from', 'shipment_to', 'shipment_start_date', 'shipment_end_date')

admin.site.register(Shipment, ShipmentAdmin)
