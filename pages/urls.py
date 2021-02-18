from django.urls import path, include
from .views import index, aboutSeller, collection, load_models

urlpatterns = [
    path('', index, name="sell"),
    path('seller', aboutSeller, name="aboutSeller"),
    path('collection', collection, name="collection"),

    path('ajax/load-models/', load_models, name="ajax_load_models"),
]