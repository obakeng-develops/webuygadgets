from django.contrib import admin
from .models import PurchaseOrder

# Register your models here.
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_date', 'order_number')
    list_filter = ('user', 'order_date', 'order_status')

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)