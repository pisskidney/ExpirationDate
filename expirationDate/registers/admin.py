from django.contrib import admin

from registers.models import (
    UpcomingFuneral, Grave, FuneralMonument
)


class UpcomingFuneralAdmin(admin.ModelAdmin):
    list_display = ('deceased', 'resting_place', 'funeral_date',
                    'date_added',)


class GraveAdmin(admin.ModelAdmin):
    list_display = ('cemetery', 'owner', 'deceased',
                    'receipt_number', 'funeral_date',
                    'surface_area')


class FuneralMonumentAdmin(admin.ModelAdmin):
    list_display = ('location', 'owner', 'deceased',
                    'receipt_number', 'funeral_date',
                    'surface_area')

admin.site.register(UpcomingFuneral, UpcomingFuneralAdmin)
admin.site.register(Grave, GraveAdmin)
admin.site.register(FuneralMonument, FuneralMonumentAdmin)
