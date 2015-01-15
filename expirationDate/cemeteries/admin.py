from django.contrib import admin

import reversion

from cemeteries.models import Cemetery


class CemeteryAdmin(reversion.VersionAdmin):
    list_display = ('name', 'address', 'postcode', 'phone',
                    'mobile',)
    search_fields = ['name', 'address', 'postcode']


admin.site.register(Cemetery, CemeteryAdmin)
