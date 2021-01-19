from django.shortcuts import render
from rolepermissions.decorators import has_role_decorator

def index(request):
    return render(request, "index.html")

def howItWorks(request):
    return render(request, "how-it-works.html")

def ourTips(request):
    return render(request, "our-tips.html")

def faqs(request):
    return render(request, "faq.html")

def applyNow(request):
    return render(request, "apply-now.html")
