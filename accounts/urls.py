from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="dashboard"),
    path('sellers', views.sellers, name="sellers"),
    path("register", views.register, name="register"),
]