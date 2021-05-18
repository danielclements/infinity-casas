from django.shortcuts import render

# Create your views here.

def listings(request):
    """ This view returns the listings page """
    return render(request, 'listings/listings.html')