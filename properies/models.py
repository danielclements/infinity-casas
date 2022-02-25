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
    # currency = models.ForeignKey(
    #     'currency_type', null=True, blank=True, on_delete=models.SET_NULL)
    price_freq = models.ForeignKey(
        'price_freq', null=True, blank=True, on_delete=models.SET_NULL)
    # type = models.ForeignKey(
    #     'type', null=True, blank=True, on_delete=models.SET_NULL)
    town = models.CharField(max_length=254, null=True, blank=True)
    # province varchar // Mandatory
    # country varchar // Mandatory
    # video_url url// optional
    # desc text // description Mandatory, No HTML,UTF-8 encoded text only
    # features array
    # images array
    # date datetime //Used if the property should be added or updated



    meal_type = models.ForeignKey(
        'currency_type', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254, null=True, blank=True)
    calories = models.IntegerField(blank=True, null=True)
    ingredients = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    meal_img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class currency_type(models.Model):
    currency_type = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.currency_type

class price_freq(models.Model):
    price_freq = models.CharField(max_length=254, null=True, blank=False)

    def __str__(self):
        return self.price_freq

class property_type(models.Model):
    property_type = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.property_type

class provence(models.Model):
    provence = models.CharField(max_length=100, null=True)
