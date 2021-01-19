from django.contrib import admin
from .models import Payment

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('payment_type', 'payment_from', 'payment_to')
    list_filter = ('payment_type',)

admin.site.register(Payment, PaymentAdmin)