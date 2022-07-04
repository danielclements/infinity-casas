from django.shortcuts import render
from django.http import JsonResponse


from rest_framework.decorators import api_view
from rest_framework.response import Response
from.serializers import PropertySerializer
from properies.models import property
# Create your views here.


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/api/property-list/',
        'Detail View': '/api/properties/<int:pk>/',
    }

    return Response(api_urls)

@api_view(['GET'])
def property_list(request):
    properties = property.objects.all()
    serializer = PropertySerializer(properties, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def property_detail(request, pk):
    properties = property.objects.get(ref=pk)
    serializer = PropertySerializer(properties, many=False)
    return Response(serializer.data)