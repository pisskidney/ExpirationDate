from django.contrib import admin

import reversion

from cemeteries.models import Cemetery, RestingPlace


class CemeteryAdmin(reversion.VersionAdmin):
    list_display = ('name', 'address', 'postcode', 'phone',
                    'mobile',)
    search_fields = ['name', 'address', 'postcode']


class RestingPlaceAdmin(reversion.VersionAdmin):
    list_display = ('cemetery', 'resident', 'parcel',
                    'row', 'position')
    search_fields = ['cemetery__name', 'parcel', 'row', 'position']

    list_display_links = ('cemetery', 'resident')


admin.site.register(Cemetery, CemeteryAdmin)
admin.site.register(RestingPlace, RestingPlaceAdmin)
