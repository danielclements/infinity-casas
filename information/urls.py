from django.urls import path
from . import views

urlpatterns = [
    path('about-us', views.aboutUsView, name='about-us'),
    
]