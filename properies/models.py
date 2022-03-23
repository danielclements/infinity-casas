from datetime import datetime, date
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class property(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    Beds = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    pool = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(1), MinValueValidator(0)])
    ref = models.CharField(max_length=254, null=True, blank=True)
    price = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey(
        'currency_type', null=True, blank=True, on_delete=models.SET_NULL)
    price_freq = models.ForeignKey(
        'price_freq', null=True, blank=True, on_delete=models.SET_NULL) 

    type = models.ForeignKey(
        'property_type', null=True, blank=True, on_delete=models.SET_NULL)
    town = models.CharField(max_length=254, null=True, blank=True)

    provence = models.ForeignKey(
        'provence', null=True, blank=True, on_delete=models.SET_NULL)

    country = models.ForeignKey(
        'country', null=True, blank=True, on_delete=models.SET_NULL)

    # video_url url// optional
    # desc text // description Mandatory, No HTML,UTF-8 encoded text only
    # features array
    # images array
    # date datetime //Used if the property should be added or updated Ex. 2013-04-05 13:45:45
    date = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.title


class currency_type(models.Model):
    currency_type = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.currency_type

class price_freq(models.Model):
    price_freq = models.CharField(max_length=254, null=True, blank=False)

    def __str__(self):
        return self.price_freq

# https://help.kyero.com/property-types-used-in-kyero Kyero property type source page
class property_type(models.Model):
    property_type = models.CharField(max_length=254, null=True, blank=False)

    def __str__(self):
        return self.property_type

class provence(models.Model):
    provence = models.CharField(max_length=100,  null=True, blank=False)
    def __str__(self):
        return self.provence


class country(models.Model):
    country = models.CharField(max_length=100,  null=True, blank=False)
    def __str__(self):
        return self.country