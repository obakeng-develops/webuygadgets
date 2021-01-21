from django.contrib import admin
from .models import Category, Brand, Product

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)

class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name',)
    list_filter = ('brand_name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'category',)
    list_filter = ('id', 'brand', 'model', 'category')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Product, ProductAdmin)
