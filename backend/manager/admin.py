import json 
from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import Person

admin.site.register(Person)
class RentalAdmin(admin.ModelAdmin): formfield_overrides = {
    map_fields.AddressField: { 'widget':
    map_widgets.GoogleMapsAddressWidget(attrs={
      'data-autocomplete-options': json.dumps({ 'types': ['geocode',
      'establishment'], 'componentRestrictions': {
                  'country': 'us'
                }
            })
        })
    },
}