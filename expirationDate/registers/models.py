import datetime

from django.db import models
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


from persons.models import Person
from registers.constants import RequestStatus
from cemeteries.models import RestingPlace, Cemetery


class WithImageMixin(models.Model):
    image = models.ImageField(null=True)

    class Meta():
        abstract = True

    def render_image(self):
        # Do not do this in production
        if self.image:
            return u'<img src="{}" style="width:128px !important"/>'.format(
                self.image.url)
        else:
            return '(No image)'
    render_image.short_description = 'Image preview'
    render_image.allow_tags = True


class UpcomingFuneral(WithImageMixin, models.Model):
    deceased = models.ForeignKey(Person, related_name="upcomming_funerals")
    resting_place = models.ForeignKey(
        RestingPlace, related_name="resting_places")
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


class Grave(WithImageMixin, models.Model):
    cemetery = models.ForeignKey(Cemetery)
    owner = models.ForeignKey(Person, related_name='graves',
                              null=True, blank=True)
    deceased = models.ForeignKey(Person, null=True, blank=True)
    receipt_number = models.BigIntegerField(_('receipt_number'), null=True,
                                            blank=True)
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

    def save(self, *args, **kwargs):
        super(Grave, self).save()
        if not self.owner:
            return super(Grave, self).save()

        try:
            GraveOwnership.objects.get(person=self.owner,
                                       owned_grave=self)
        except ObjectDoesNotExist:
            new_record = GraveOwnership()
            new_record.person = self.owner
            new_record.owned_grave = self

            date = timezone.now()
            new_record.expiration_date = datetime.date(year=date.year + 20,
                                                       month=date.month,
                                                       day=date.day)

            new_record.save()


# TODO: nu cred ca mai avem nevoie de asta ca e cod duplicat
# putem sa facem doar un model cu proxy = True
class FuneralMonument(WithImageMixin, models.Model):
    location = models.ForeignKey(RestingPlace)
    deceased = models.ForeignKey(Person, related_name="funeral_monuments")
    owner = models.ForeignKey(Person)
    receipt_number = models.BigIntegerField(_('receipt_number'))
    funeral_date = models.DateTimeField(_('funeral date'))
    surface_area = models.DecimalField(_('surface area'),
                                       max_digits=5, decimal_places=2)
    has_funeral_constructions = models.BooleanField(default=False)

    def __str__(self):
        return "Owner: {}".format(self.owner.full_name)


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


class ExpiredGrave(Grave):

    class Meta:
        proxy = True


class GravesToExpireThisYear(Grave):

    class Meta:
        proxy = True


class GravesPayedThisYear(Grave):

    class Meta:
        proxy = True


class GraveOwnership(models.Model):
    person = models.ForeignKey(Person, related_name='person')
    owned_grave = models.ForeignKey(Grave, related_name='owned_grave')
    expiration_date = models.DateField(_("expiration_date"))
