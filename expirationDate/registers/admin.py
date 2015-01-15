from django import forms
from django.contrib import admin
from django.forms import ValidationError
from django.utils import timezone

import reversion

from registers.models import (
    UpcomingFuneral, Grave, FuneralMonument, AnnualDeathIndexRegister,
    AnnualOwnerlessDeathRegister, UpcomingFuneralArchive,
    GraveOwnershipRequestsRegister
)


class UpcomingFuneralAdmin(reversion.VersionAdmin):
    list_display = ('deceased', 'resting_place', 'funeral_date',
                    'date_added')

    search_fields = ['resting_place', 'funeral_date', 'date_added']

    def get_queryset(self, request):
        queryset = self.model.objects.filter(
            funeral_date__gt=timezone.now())
        return queryset.order_by('funeral_date')


class UpcomingFuneralAdminArchive(reversion.VersionAdmin):
    list_display = ('deceased', 'resting_place', 'funeral_date',
                    'date_added')

    search_fields = ['resting_place', 'funeral_date', 'date_added']

    def get_queryset(self, request):
        queryset = self.model.objects.filter(
            funeral_date__lt=timezone.now())
        return queryset.order_by('funeral_date')


class GraveAdminForm(forms.ModelForm):

    def clean(self):
        if (self.cleaned_data.get('social_services_request')
                and self.cleaned_data.get('owner')):
            raise ValidationError("Can't set both owner and IML request")
        elif not (self.cleaned_data.get("social_services_request")
                  or self.cleaned_data.get('owner')):
            raise ValidationError("Owner or IML request must be set")


class GraveAdmin(reversion.VersionAdmin):
    form = GraveAdminForm
    list_display = ('cemetery', 'owner', 'deceased',
                    'receipt_number', 'funeral_date',
                    'surface_area', 'parcel', 'row',
                    'position', 'social_services_request',
                    'render_image')

    list_display_links = ('cemetery', 'owner', 'deceased')

    search_fields = ['owner__first_name', 'owner__last_name',
                     'receipt_number', 'funeral_date']


class FuneralMonumentAdmin(reversion.VersionAdmin):
    list_display = ('location', 'owner', 'deceased',
                    'receipt_number', 'funeral_date',
                    'surface_area', 'render_image')
    search_fields = ['location', 'owner', 'funeral_date']


class AnnualDeathIndexRegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'cemetery', 'parcel')

    search_fields = ['first_name', 'last_name']

    def get_queryset(self, request):
        q = self.model.objects.filter(grave__isnull=False)
        return q.order_by('last_name', '-date_of_death')

    def has_add_permission(self, request):
        return False


class AnnualOwnerlessDeathRegisterAdmin(admin.ModelAdmin):
    list_display = ('receipt_number', 'social_services_request', 'parcel',
                    'row', 'number')

    def get_queryset(self, request):
        return self.model.objects.filter(owner__isnull=True)

    def has_add_permission(self, request):
        return False


class GraveOwnershipRequestsRegisterAdmin(admin.ModelAdmin):
    list_display = ('current_number', 'registration_date',
                    'infocet_number', 'status')

    def get_queryset(self, request):
        return self.model.objects.all()

    # nobody has the right to delete a request, stated in docs
    def has_delete_permission(self, request, object=False):
        return False

admin.site.register(UpcomingFuneral, UpcomingFuneralAdmin)
admin.site.register(UpcomingFuneralArchive, UpcomingFuneralAdminArchive)
admin.site.register(Grave, GraveAdmin)
admin.site.register(FuneralMonument, FuneralMonumentAdmin)
admin.site.register(AnnualDeathIndexRegister, AnnualDeathIndexRegisterAdmin)
admin.site.register(AnnualOwnerlessDeathRegister,
                    AnnualOwnerlessDeathRegisterAdmin)
admin.site.register(GraveOwnershipRequestsRegister,
                    GraveOwnershipRequestsRegisterAdmin)
