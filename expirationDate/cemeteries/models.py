from django.db import models
from django.utils.translation import ugettext_lazy as _

from persons.models import Person
from registers.models import WithImageMixin


class Cemetery(models.Model):
    name = models.CharField(_('cemetery name'), max_length=50)
    address = models.CharField(_('address'), max_length=200, blank=True)
    postcode = models.CharField(_('postcode'), max_length=10, blank=True,
                                help_text=_('(e.g.:1234 AB)'))
    phone = models.CharField(_('phone'), max_length=20, blank=True)
    mobile = models.CharField(_('mobile'), max_length=20, blank=True)

    class Meta:
        verbose_name_plural = "cemeteries"

    def __str__(self):
        return self.name


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
