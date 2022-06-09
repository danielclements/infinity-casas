from django.shortcuts import render, redirect

# Create your views here.

def aboutUsView(request):
    return render(request, 'information/about-us.html')
