from django.contrib import admin
from .models import property,currency_type, price_freq, property_type, provence, country, agent
# Register your models here.


admin.site.register(currency_type)
admin.site.register(price_freq)
admin.site.register(property_type)
admin.site.register(provence)
admin.site.register(country)
admin.site.register(agent)


class PropertyAdmin(admin.ModelAdmin):


    ordering = ('agent',)


admin.site.register(property, PropertyAdmin)