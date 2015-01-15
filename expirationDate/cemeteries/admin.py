from django.contrib import admin

import reversion

from cemeteries.models import Cemetery, Grave


class CemeteryAdmin(reversion.VersionAdmin):
    list_display = ('name', 'address', 'postcode', 'phone',
                    'mobile',)
    search_fields = ['name', 'address', 'postcode']


class GraveAdmin(reversion.VersionAdmin):
    list_display = ('cemetery', 'deceased', 'parcel',
                    'row', 'position')
    search_fields = ['cemetery__name', 'parcel', 'row', 'position']


admin.site.register(Cemetery, CemeteryAdmin)
admin.site.register(Grave, GraveAdmin)
