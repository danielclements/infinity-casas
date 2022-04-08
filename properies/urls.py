from django.urls import path
from . import views

urlpatterns = [
    path('', views.allProperties, name="all-properties"),

]