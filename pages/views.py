from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.forms import ProductForm, ManufacturerForm, CategoryForm
from transaction.forms import SellerForm

from products.models import Product
from transaction.models import Seller

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            # Process form data
            form.save()
            data = form.save()
            n = data.id
            request.session['id'] = n
            return redirect(aboutSeller)
    else:
        form = ProductForm()
        
    return render(request, "pages/index.html", { 'form': form })

def aboutSeller(request):

    form = SellerForm()

    if request.method == 'POST':
        form = SellerForm(request.POST)
        if form.is_valid():
            seller = Seller()
            seller.firstname = form.cleaned_data['firstname']
            seller.lastname = form.cleaned_data['lastname']
            seller.email = form.cleaned_data['email']
            seller.cellphone_number = form.cleaned_data['cellphone_number']
            seller.alternative_number = form.cleaned_data['alternative_number']
            seller.surburb = form.cleaned_data['surburb']
            seller.city = form.cleaned_data['city']
            seller.province = form.cleaned_data['province']
            seller.product = Product.objects.get(id=request.session['id'])
            seller.save()
            return HttpResponse("Done")
    else:
        form = SellerForm()

    return render(request,"pages/about-seller.html", { 'form': form })

def collection(request):
    return render(request, "pages/collection.html")