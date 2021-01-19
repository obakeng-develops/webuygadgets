from django.urls import path, include
from .views import index, aboutSeller, collection

urlpatterns = [
    path('', index, name="sell"),
    path('seller', aboutSeller, name="aboutSeller"),
    path('collection', collection, name="collection")
]