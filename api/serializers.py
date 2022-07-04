from django.contrib.auth.models import User, Group
from rest_framework import serializers
from properies.models import property, property_image



class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = property
        fields = ['title', 'ref', 'status']
