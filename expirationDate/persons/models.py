from django.db import models
from django.utils.translation import ugettext_lazy as _

from persons.constants import PersonGender, PersonReligion


class Person(models.Model):
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    birth_date = models.DateField(_('birth date'), null=True, blank=True)
    date_of_death = models.DateField(_('date of death'), null=True, blank=True)
    birth_place = models.CharField(_('birth place'), max_length=100,
                                   blank=True)
    address = models.CharField(_('address'), max_length=200, blank=True)
    postcode = models.CharField(_('postcode'), max_length=10, blank=True,
                                help_text=_('(e.g.:1234 AB)'))

    phone = models.CharField(_('phone'), max_length=20, blank=True)
    mobile = models.CharField(_('mobile'), max_length=20, blank=True)

    gender = models.PositiveSmallIntegerField(
        _('gender'),
        help_text=_('Indicates the gender of the user.'),
        choices=PersonGender.GENDER_OPTIONS,
        default=PersonGender.NOT_SPECIFIED)
    religion = models.PositiveSmallIntegerField(
        _('religion'),
        help_text=_('Indicates the religion of the user.'),
        choices=PersonReligion.RELIGION_OPTIONS,
        default=PersonReligion.NOT_SPECIFIED)
    is_deceased = models.BooleanField(_('is deceased'), default=False,
                                      blank=True)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    @property
    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        if any([self.is_deceased, self.date_of_death]):
            raise ValueError("If the person died you must"
                             "supply the date of death")
        return super().save(args, kwargs)
