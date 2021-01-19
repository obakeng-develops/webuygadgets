from django.forms import ModelForm, Textarea, TextInput
from .models import Seller
from django.utils.translation import gettext_lazy as _


class SellerForm(ModelForm):
    class Meta:
        model = Seller
        exclude = ['product']
        widgets = {
            "firstname": TextInput(attrs={'class': 'form-control', 'type': 'text'}),
            "lastname": TextInput(attrs={'class': 'form-control'}),
            "cellphone_number": TextInput(attrs={'class': 'form-control'}),
            "email": TextInput(attrs={'class': 'form-control', 'type': 'email', 'placeholder': 'you@example.com'}),
        }
        labels = {
            "firstname": _('First Name'),
            "lastname": _('Last Name'),
        }