
# Django Modules
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Role Permissions
from rolepermissions.checkers import has_role

# User Roles
from .roles import Finance, Operations

# Forms
from products.forms import ProductForm
from .forms import CustomUserCreationFprm

# Models
from products.models import Product
from profiles.models import Profile
from accounts.models import Account
from transaction.models import Seller

# Create your views here.
def home(request):
    if has_role(request.user, Finance):
        products = Product.objects.all()
        account = Account.objects.get(email=request.user)
        profile = Profile.objects.get(user=account)

        context = {
            "products": products,
            "profile": profile
        }

        return render(request, "accounts/staff/dashboard.html", context)

    if has_role(request.user, Operations):
        form  = ProductForm()

        context = {
            "form": form
        }
        
        return render(request, "accounts/members/dashboard.html", context)

def sellers(request):
    if has_role(request.user, Finance):
        sellers = Seller.objects.all()

        context = {
            "sellers": sellers
        }

        return render(request, "accounts/staff/sellers.html", context)

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

    context = {}

    return render(request, 'account/login.html', context)

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))