from django.db import models
from django.utils.translation import ugettext_lazy as _


from persons.models import Person
from cemeteries.models import RestingPlace, Cemetery


class UpcomingFuneral(models.Model):
    deceased = models.ForeignKey(Person, related_name="upcomming_funerals")
    resting_place = models.ForeignKey(
        RestingPlace, related_name="resting_places")
    funeral_date = models.DateTimeField(_('funeral date'))
    date_added = models.DateTimeField(_('date added'), auto_now_add=True)


class Grave(models.Model):
    cemetery = models.ForeignKey(Cemetery)
    owner = models.ForeignKey(Person, related_name='graves')
    deceased = models.ForeignKey(Person)
    receipt_number = models.BigIntegerField(_('receipt_number'))
    funeral_date = models.DateTimeField(_('funeral date'))
    surface_area = models.DecimalField(_('surface area'),
                                       max_digits=5, decimal_places=2)
    has_funeral_constructions = models.BooleanField(default=False)
    image = models.ImageField()


class FuneralMonument(models.Model):
    location = models.ForeignKey(RestingPlace)
    deceased = models.ForeignKey(Person, related_name="funeral_monuments")
    owner = models.ForeignKey(Person)
    receipt_number = models.BigIntegerField(_('receipt_number'))
    funeral_date = models.DateTimeField(_('funeral date'))
    surface_area = models.DecimalField(_('surface area'),
                                       max_digits=5, decimal_places=2)
    has_funeral_constructions = models.BooleanField(default=False)
    image = models.ImageField()
