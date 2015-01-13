from django.contrib import admin

from cemeteries.models import Cemetery, RestingPlace


class CemeteryAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'postcode', 'phone',
                    'mobile',)
    search_fields = ['name', 'address', 'postcode']


class RestingPlaceAdmin(admin.ModelAdmin):
    list_display = ('cemetery', 'resident', 'parcel',
                    'row', 'position')
    search_fields = ['cemetery__name', 'parcel', 'row', 'position']


admin.site.register(Cemetery, CemeteryAdmin)
admin.site.register(RestingPlace, RestingPlaceAdmin)
