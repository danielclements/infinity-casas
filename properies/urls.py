from django.urls import path
from . import views

urlpatterns = [
    path('all-properties/', views.allProperties, name="all-properties")

]