from django.forms import ModelForm, Textarea, TextInput, Select
from .models import Product
from django.utils.translation import gettext_lazy as _

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'brand': Select(attrs={'class': 'form-control', 'title': 'Product Condition'}),
            'model': Select(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'variant': Select(attrs={'class': 'form-control'}),
            'condition': Select(attrs={'class': 'form-control'}),
            'accessory': TextInput(attrs={'class': 'form-control'}),
        }
