from django.db import models

# Create your models here.

class propertyListing(models.Model):

    # property_header = models.CharField(max_length=254)
    # bedrooms = models.IntegerField(max_digits=2, default=0)
    # bathrooms = models.IntegerField(max_digits=2, default=0)

    

    def __str__(self):
        return self.property_header

class property_type(models.Model):

    type = models.CharField(max_length=254)

    def __str__(self):
        return self.type
