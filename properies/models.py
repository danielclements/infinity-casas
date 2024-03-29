from datetime import datetime, date
from tabnanny import verbose
from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import model_to_dict


# Create your models here.


class property(models.Model):
    class Meta:
        verbose_name_plural = "Properties"

    title               = models.CharField(max_length=254, null=True, blank=True)
    Beds                = models.IntegerField(blank=True, null=True)
    bathrooms           = models.IntegerField(blank=True, null=True)
    pool                = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(1), MinValueValidator(0)])
    ref                 = models.CharField(max_length=254, null=True, blank=True)
    price               = models.IntegerField(blank=True, null=True)
    currency            = models.ForeignKey('currency_type', null=True, blank=True, on_delete=models.SET_NULL)
    price_freq          = models.ForeignKey('price_freq', null=True, blank=True, on_delete=models.SET_NULL) 
    type                = models.ForeignKey('property_type', null=True, blank=True, on_delete=models.SET_NULL)
    town                = models.CharField(max_length=254, null=True, blank=True)
    provence            = models.ForeignKey('provence', null=True, blank=True, on_delete=models.SET_NULL)
    country             = models.ForeignKey('country', null=True, blank=True, on_delete=models.SET_NULL)
    # video_url url// optional
    desc                = models.CharField(max_length=254, null=True, blank=True)
             #  No HTML, UTF-8 encoded text only
			# Sentence case, no excessive capitalisation
			# Use &#13; to force a line break in the text (remember, no HTML)
    # features array  
    features            = models.ManyToManyField('features', blank=True)  
    status              = models.ForeignKey('property_status', null=True, blank=True, on_delete=models.SET_NULL)
    sold                = models.BooleanField(null=True, blank=True)
    secret_key          = models.CharField(max_length=254, null=True, blank=True)
    # Images
    pool_image          = models.ImageField(null=True, blank=True)
    main_image          = models.ImageField(null=True, blank=True)
    living_room_image   = models.ImageField(null=True, blank=True)
    kitchen_image       = models.ImageField(null=True, blank=True)
    bedroom_1_image     = models.ImageField(null=True, blank=True)
    bedroom_2_image     = models.ImageField(null=True, blank=True)
    bathroom_image      = models.ImageField(null=True, blank=True)

    date = models.DateField(auto_now=True, blank=True)
    agent = models.ForeignKey('agent', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title + " - " + self.ref + " - " + str(self.agent)


class property_image(models.Model):
    class Meta:
        verbose_name_plural = "Property Images"
    link_ID = models.ForeignKey('property', null=True, on_delete=models.CASCADE)
    extra_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.link_ID.ref

class currency_type(models.Model):
    class Meta:
        verbose_name_plural = "Currency Type"
    currency_type = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.currency_type

class price_freq(models.Model):
    class Meta:
        verbose_name_plural = "Sale Type"
    price_freq = models.CharField(max_length=254, null=True, blank=False)

    def __str__(self):
        return self.price_freq

# https://help.kyero.com/property-types-used-in-kyero Kyero property type source page
class property_type(models.Model):
    class Meta:
        verbose_name_plural = "Property Types"
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

class agent(models.Model):
    agent = models.CharField(max_length=128, null=True, blank=False)
    def __str__(self):
        return self.agent

class property_status(models.Model):
    class Meta:
        verbose_name_plural = "Status"
    status = models.CharField(max_length=100,  null=True, blank=False)
    def __str__(self):
        return self.status

class features(models.Model):
    class Meta:
        verbose_name_plural = "Features"
    feature = models.CharField(max_length=100,  null=False, blank=False)
    def __str__(self):
        return self.feature