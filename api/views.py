# from rest_framework_xml.renderers import XMLRenderer
from django.shortcuts import render, HttpResponse
from django.urls import path
from requests import Response
from properies.models import property, property_image, currency_type, price_freq, property_type, provence, country, agent, property_status
# from rest_framework import routers, serializers, viewsets
# from rest_framework_xml.parsers import XMLParser
# from rest_framework.response import Response
# from rest_framework.views import APIView



# class propertySerializer(serializers.ModelSerializer):
#     provence = serializers.CharField(source='provence.provence', read_only=True)
    

#     class Meta:
#         model = property
#         fields = ('title', 'town', 'provence', 'desc', 'ref')

# class propertyXMLRenderer(XMLRenderer):

#     item_tag_name = 'property'
#     creation_tag_name = 'kyero'
#     kyeroFeedVersion = 'feed_version'

#     def _to_xml(self, xml, data):

#         xml.startElement(self.creation_tag_name, {})
#         xml.endElement(self.creation_tag_name)
        
#         super()._to_xml(xml, data)

# class propertyXMLViewSet(APIView):
#     renderer_classes = [propertyXMLRenderer, ]

#     def get(self, request, format=None):
#         queryset = property.objects.all()
#         serializer_class = propertySerializer(queryset, many=True)
#         return Response(serializer_class.data)
        


def allPropertiesxml(request):
    
    properties = property.objects.all()
    context = {'properties': properties,
                }

    return HttpResponse(open('api/templates/api/property.xml').read(), context, content_type='text/xml')