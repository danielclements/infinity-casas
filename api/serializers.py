from django.contrib.auth.models import User, Group
from rest_framework import serializers
from properies import models


class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = property
        fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']