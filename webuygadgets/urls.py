from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('selling/', include('pages.urls')),
    path('how-it-works/', views.howItWorks, name='howItWorks'),
    path('our-tips/', views.ourTips, name='ourTips'),
    path('faqs/', views.faqs, name='faqs'),
    path('apply-now', views.applyNow, name='applyNow'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', include('accounts.urls')),
]
