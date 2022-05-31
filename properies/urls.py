from django.urls import path
from . import views

urlpatterns = [
    path('', views.allProperties, name="all-properties"),
    path('add_property', views.add_property),
    path('<property_ref>', views.property_detail, name='property_detail'),

]