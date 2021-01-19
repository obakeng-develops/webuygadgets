from django.contrib import admin
from .models import Bank, BankingDetail

# Register your models here.
class BankAdmin(admin.ModelAdmin):
    list_display = ('bankName', 'bankCode',)
    list_filter = ('bankName', 'bankCode',)

class BankingDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'bankId',)
    list_filter = ('user', 'bankId',)
    search_fields = ('user',)
    ordering = ('user',)

admin.site.register(Bank, BankAdmin)
admin.site.register(BankingDetail, BankingDetailAdmin)
