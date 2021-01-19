from django.contrib import admin
from .models import Seller

# Register your models here.
class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstname', 'lastname', 'cellphone_number', 'email',)
    list_filter = ('firstname',)
    search_fields = ('firstname',)
    ordering = ('firstname',)

admin.site.register(Seller, SellerAdmin)