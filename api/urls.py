from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path ('property-list/', views.property_list, name="property-list"),
    path ('property-detail/<str:pk>/', views.property_detail, name="property-list"),


]