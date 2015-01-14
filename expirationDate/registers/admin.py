from django.contrib import admin

import reversion

from registers.models import (
    UpcomingFuneral, Grave, FuneralMonument
)


class UpcomingFuneralAdmin(reversion.VersionAdmin):
    list_display = ('deceased', 'resting_place', 'funeral_date',
                    'date_added', 'render_image')

    search_fields = ['resting_place', 'funeral_date', 'date_added']


class GraveAdmin(reversion.VersionAdmin):
    list_display = ('cemetery', 'owner', 'deceased',
                    'receipt_number', 'funeral_date',
                    'surface_area', 'render_image')

    list_display_links = ('cemetery', 'owner', 'deceased')

    search_fields = ['owner__first_name', 'owner__last_name',
                     'receipt_number', 'funeral_date']


class FuneralMonumentAdmin(reversion.VersionAdmin):
    list_display = ('location', 'owner', 'deceased',
                    'receipt_number', 'funeral_date',
                    'surface_area', 'render_image')
    search_fields = ['location', 'owner', 'funeral_date']

admin.site.register(UpcomingFuneral, UpcomingFuneralAdmin)
admin.site.register(Grave, GraveAdmin)
admin.site.register(FuneralMonument, FuneralMonumentAdmin)
