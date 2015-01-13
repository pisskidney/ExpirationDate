from django.contrib import admin

from registers.models import (
    UpcomingFuneral, Grave, FuneralMonument
)


class UpcomingFuneralAdmin(admin.ModelAdmin):
    list_display = ('deceased', 'resting_place', 'funeral_date',
                    'date_added',)

    search_fields = ['resting_place', 'funeral_date', 'date_added']


class GraveAdmin(admin.ModelAdmin):
    list_display = ('cemetery', 'owner', 'deceased',
                    'receipt_number', 'funeral_date',
                    'surface_area')
    search_fields = ['owner', 'receipt_number', 'funeral_date']


class FuneralMonumentAdmin(admin.ModelAdmin):
    list_display = ('location', 'owner', 'deceased',
                    'receipt_number', 'funeral_date',
                    'surface_area')
    search_fields = ['location', 'owner', 'funeral_date']

admin.site.register(UpcomingFuneral, UpcomingFuneralAdmin)
admin.site.register(Grave, GraveAdmin)
admin.site.register(FuneralMonument, FuneralMonumentAdmin)
