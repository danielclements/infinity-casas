from django.urls import path
from . import views

# Returns all listings
urlpatterns = [
    path('', views.listings, name='listings'),
]