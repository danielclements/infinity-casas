from multiprocessing import context
from django.shortcuts import render
from .models import property

# Create your views here.
def allProperties(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    properties = property.objects.filter(title__icontains=q)
    context = {'properties': properties}
 
    return render(request, 'properies/properties.html', context) 

 