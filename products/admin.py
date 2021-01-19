from django.contrib import admin
from .models import Category, Manufacturer, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('manufacturer_name',)
    list_filter = ('manufacturer_name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_year', 'product_model', 'manufacturer', 'product_type')
    list_filter = ('id', 'product_name', 'product_year', 'product_model', 'manufacturer', 'product_type')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Product, ProductAdmin)
