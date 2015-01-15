from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


from persons.models import Person
from cemeteries.models import Cemetery
from helpers.mixins import WithImageMixin
from registers.constants import RequestStatus


class Grave(WithImageMixin, models.Model):
    cemetery = models.ForeignKey(Cemetery)
    owner = models.ForeignKey(Person, related_name='graves',
                              null=True, blank=True)
    deceased = models.ForeignKey(Person)
    receipt_number = models.BigIntegerField(_('receipt_number'))
    funeral_date = models.DateTimeField(_('funeral date'))
    surface_area = models.DecimalField(_('surface area'),
                                       max_digits=5, decimal_places=2)
    has_funeral_constructions = models.BooleanField(default=False)
    parcel = models.SmallIntegerField(_('parcel'), default=0)
    row = models.SmallIntegerField(_('row'), default=0)
    position = models.SmallIntegerField(_('position'), default=0)
    social_services_request = models.BigIntegerField(
        _('IML request'), null=True, blank=True)

    def __str__(self):
        return "Cemetery: {} Position: {}".format(
            self.cemetery.name, self.position)


class UpcomingFuneral(models.Model):
    deceased = models.ForeignKey(Person, related_name="upcomming_funerals")
    grave = models.ForeignKey(
        Grave, related_name="grave")
    funeral_date = models.DateTimeField(_('funeral date'))
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)

    def __str__(self):
        return "Deceased: {} Date: {}".format(self.deceased.full_name,
                                              self.funeral_date)

    def clean_fields(self, *args, **kwargs):
        if self.funeral_date < timezone.now():
            raise ValidationError(
                "Funeral date needs to be greater than today")
        super(UpcomingFuneral, self).clean_fields()


class UpcomingFuneralArchive(UpcomingFuneral):

    class Meta:
        proxy = True

    def clean_fields(self, *args, **kwargs):
        if self.funeral_date > timezone.now():
            raise ValidationError(
                "Funeral date needs to be smaller than today")
        super(UpcomingFuneral, self).clean_fields()


class FuneralMonument(Grave):

    class Meta:
        proxy = True


class AnnualDeathIndexRegister(Person):

    class Meta:
        proxy = True

    def cemetery(self):
        return self.grave_set.first().cemetery.name
    cemetery.short_description = _('Cemetery')

    def parcel(self):
        return self.grave_set.first().parcel
    parcel.short_description = _('Parcel')

    def number(self):
        return self.grave_set.first().position
    number.short_description = _('Number')


class AnnualOwnerlessDeathRegister(Grave):

    class Meta:
        proxy = True

    def social_services_request(self):
        return self.social_services_request
    social_services_request.short_description = _('IML request')

    def receipt_number(self):
        return self.receipt_number
    receipt_number.short_description = _('Recepit Number')

    # se cere map dar nu avem si am pus coordonate si numar
    def parcel(self):
        return self.parcel
    parcel.short_description = _('Parcel')

    def row(self):
        return self.row
    row.short_description = _('Row')

    def number(self):
        return self.position
    number.short_description = _('Number')


class GraveOwnershipRequestsRegister(models.Model):
    current_number = models.BigIntegerField(_('current_number'), unique=True)
    registration_date = models.DateTimeField(_('registration_date'))
    infocet_number = models.BigIntegerField(_('infocet_number'))
    status = models.PositiveSmallIntegerField(
        _('status'),
        choices=RequestStatus.REQUEST_OPTIONS,
        default=RequestStatus.FAVORABLE
    )
