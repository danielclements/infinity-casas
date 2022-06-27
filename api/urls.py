from django.urls import path
from . import views

urlpatterns = [
    path('xml',views.propertyXMLViewSet.as_view(), name="property-xml"),
]

# urlpatterns = [
#     path('xml',views.allPropertiesxml, name='allPropertiesxml'),
# ]

