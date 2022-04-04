from django.shortcuts import render

# Create your views here.
def allProperties(request):
    return render(request, 'properies/properties.html') 