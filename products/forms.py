from django.forms import ModelForm, Textarea, TextInput, Select
from .models import Product, Manufacturer, Category
from django.utils.translation import gettext_lazy as _

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'product_condition':Select(attrs={'class': 'form-control', 'title': 'Product Condition'}),
            'product_name': TextInput(attrs={'class': 'form-control'}),
            'product_expected_price': TextInput(attrs={'class': 'form-control', 'placeholder': 'Expected price'}),
            'product_year': TextInput(attrs={'class': 'form-control'}),
            'product_model': TextInput(attrs={'class': 'form-control'}),
            'product_type': TextInput(attrs={'class': 'form-control'}),
            'product_variant': Select(attrs={'class': 'form-control'}),
        }

class ManufacturerForm(ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['manufacturer_name']
        widgets = {
            'manufacturer_name': Select(attrs={'class': 'form-control'}),
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
        widgets = {
            'category_name': Select(attrs={'class': 'form-control'})
        }