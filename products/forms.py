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

        if 'brand' in self.data:
            try:
                brand_id = int(self.data.get('brand'))
                self.fields['model'].queryset = Model.objects.filter(brand_id=brand_id).order_by('model_name')
            except (ValueError, TypeError):
                pass # Invalid input from the client; ignore and fallback to empty Model queryset
        elif self.instance.pk:
            self.fields['model'].queryset = self.instance.brand.model_set.order_by('model_name')

        if 'model' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['category'].queryset = Category.objects.filter(id=category_id).order_by('category_name')
            except (ValueError, TypeError):
                pass # Invalid input from the client; ignore and fallback to empty Model queryset