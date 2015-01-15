from django.contrib import admin

import reversion

from persons.models import Person


class PersonAdmin(reversion.VersionAdmin):
    list_display = ('first_name', 'last_name', 'birth_date',
                    'date_of_death', 'birth_place', 'address',
                    'postcode', 'phone', 'mobile', 'gender',
                    'is_deceased', 'religion')

    fieldsets = (
        ('Required Information', {'fields': ('first_name', 'last_name')}),
        ('Personal Information', {
            'classes': ('collapse', 'extrapretty'),
            'fields': ('birth_date', 'address',
                       'postcode', 'phone', 'mobile',
                       'gender', 'religion')}),
        ('Deceased Information', {
            'classes': ('collapse', ),
            'fields': ('is_deceased', 'date_of_death')})
    )
    search_fields = ['first_name', 'last_name', 'postcode', 'religion',
                     'address']

admin.site.register(Person, PersonAdmin)
