from django.contrib import admin

from persons.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date',
                    'date_of_death', 'birth_place', 'address',
                    'postcode', 'phone', 'mobile', 'gender',
                    'is_deceased', 'religion')
    search_fields = ['first_name', 'last_name', 'postcode', 'religion',
                     'address']

admin.site.register(Person, PersonAdmin)
