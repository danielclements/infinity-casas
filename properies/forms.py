from dataclasses import fields
from django import forms
from .models import property, property_image
from django.utils.translation import gettext_lazy as _


class add_property_form(forms.ModelForm):
    class Meta:
        model = property
        fields = '__all__'
        labels = {
            'title': _('Property Title'),
        }

class image_form(forms.ModelForm):
    image = forms.ImageField(
        label="Image",
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )
    class Meta:
        model = property_image
        fields = ("extra_image",)
 
form = add_property_form()