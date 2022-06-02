from audioop import reverse
from gc import get_objects
from importlib.metadata import files
from weakref import ref
from django.contrib import messages
from multiprocessing import context
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.contrib import messages

from properies.forms import add_property_form, image_form
from .models import property, property_image
from django.core.files.uploadedfile import SimpleUploadedFile

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

def add_property(request):
    if request.method == "POST":
        fullForm = add_property_form(request.POST, request.FILES)
        files = request.FILES.getlist("image")
        if fullForm.is_valid():
            f = fullForm.save(commit=False)
            f.save()
            for i in files:
                property_image.objects.create(ID=f, extra_image=i)
            return render(request, "home/index.html")
            
        else:
            print(fullForm.errors)
            
    else:
        fullForm = add_property_form()
        imageForm = image_form()
    
    return render(request, "properies/create_property.html", {"fullForm": fullForm, "imageForm": imageForm} )


def property_detail(request, property_ref):
        # """ This view returns the individual property  page """

        property_item = get_object_or_404(property, ref=property_ref)
        extra_images = property_image.objects.filter(link_ID=property_item.id)


        context = {
            'property': property_item,
            'extra_images': extra_images
        }
        return render(request, 'properies/propertyPage.html', context)
 