from multiprocessing import context
from django.shortcuts import render
from django.db.models import Q
from .models import property

# Create your views here.
def allProperties(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    properties = property.objects.filter(
        Q(title__icontains=q) or
        Q(town__icontains=q)
        )
    property_count = properties.count()
    
    context = {'properties': properties,
                'property_count': property_count
                }


 
    return render(request, 'properies/properties.html', context) 

 