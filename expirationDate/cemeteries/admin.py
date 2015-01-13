from django.contrib import admin

from cemeteries.models import Cemetery, RestingPlace


class CemeteryAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'postcode', 'phone',
                    'mobile',)


class RestingPlaceAdmin(admin.ModelAdmin):
    list_display = ('cemetery', 'resident', 'parcel',
                    'row', 'position')


admin.site.register(Cemetery, CemeteryAdmin)
admin.site.register(RestingPlace, RestingPlaceAdmin)
