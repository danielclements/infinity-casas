from rest_framework_xml.renderers import XMLRenderer
from django.shortcuts import render, HttpResponse
from django.urls import path
from requests import Response
from properies.models import property, property_image, currency_type, price_freq, property_type, provence, country, agent, property_status
from rest_framework import routers, serializers, viewsets
from rest_framework_xml.parsers import XMLParser
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView



class propertySerializer(serializers.ModelSerializer):
    provence = serializers.CharField(source='provence.provence', read_only=True)
    

    class Meta:
        model = property
        fields = ('title', 'town', 'provence', 'desc', 'ref')

class propertyXMLRenderer(XMLRenderer):

    root_tag_name = 'feed'
    item_tag_name = 'property'
    creation_tag_name = 'Kyero'

    def _to_xml(self, xml, data):
        xml.startElement(self.creation_tag_name, {})
        xml.characters('3')
        self._to_xml(xml, data)
        xml.endElement(self.creation_tag_name)
        

class propertyXMLViewSet(APIView):
    renderer_classes = [propertyXMLRenderer, ]

    def get(self, request, format=None):
        queryset = property.objects.all()
        serializer_class = propertySerializer(queryset, many=True)
        return Response(serializer_class.data)




