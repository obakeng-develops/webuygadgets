from django.contrib import admin
from .models import Profile, UserAddress

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'lastname', 'phone_number')
    list_filter = ('user',)
    search_fields = ('user',)
    ordering = ('user',)

class UserAddresAdmin(admin.ModelAdmin):
    list_display = ('contact', 'addressLineOne', 'addressLineTwo', 'surburb', 'city', 'province',)
    list_filter = ('contact', 'surburb', 'city', 'province',)
    search_fields = ('contact', 'surburb', 'city', 'province')
    ordering = ('contact',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserAddress, UserAddresAdmin)
