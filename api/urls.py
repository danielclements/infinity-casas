from django.urls import path
from . import views

urlpatterns = [
    path('', views.jsonData, name="json-data"),

]