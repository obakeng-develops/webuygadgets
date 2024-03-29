from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from products.forms import ProductForm
from django.core import serializers
from transaction.forms import SellerForm

from products.models import Product, Model, Category
from transaction.models import Seller

# Create your views here.
def index(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        print(request.POST["brand"])
        print(request.POST["model"])
        print(request.POST["category"])

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
            seller.product = Product.objects.get(id=request.session['id'])
            seller.save()
            return HttpResponse("Done")
    else:
        form = SellerForm()

    return render(request,"pages/about-seller.html", { 'form': form })

def collection(request):
    return render(request, "pages/collection.html")

def load_models(request):
    brand_id = request.GET.get('brand')
    models = Model.objects.filter(brand_id=brand_id).order_by('model_name')

    return render(request, 'pages/model_dropdown_list.html', { 'models': models })

def load_category(request):
    model_id = request.GET.get('model')
    category = Category.objects.get(pk=1)

    return render(request, 'pages/category_dropdown_list.html', { 'category': category })