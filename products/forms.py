from django.forms import ModelForm, Textarea, TextInput, Select
from .models import Product, Model, Category
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
            'accessory': Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['model'].queryset = Model.objects.none()
        self.fields['category'].queryset = Category.objects.none()
