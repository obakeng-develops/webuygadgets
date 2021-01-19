from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomAccountCreationForm, CustomAccountChangeForm
from .models import Account

# Register your models here.
class CustomAccountAdmin(UserAdmin):
    add_form = CustomAccountCreationForm
    form = CustomAccountChangeForm
    model = Account

    list_display = ('id', 'email', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active')

    fieldsets = (
        (None, { 'fields' : ('email', 'password') }),
        ('Permissions', {'fields': ('is_staff', 'is_active')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(Account, CustomAccountAdmin)