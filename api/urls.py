from django.urls import path
from . import views

# urlpatterns = [
#     path('xml',views.propertyXMLViewSet.as_view()),
# ]

urlpatterns = [
    path('xml',views.allPropertiesxml, name='allPropertiesxml'),
]
