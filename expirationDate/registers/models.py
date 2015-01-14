from django.db import models
from django.utils.translation import ugettext_lazy as _


from persons.models import Person
from cemeteries.models import RestingPlace, Cemetery


class WithImageMixin(models.Model):
    image = models.ImageField(null=True)

    class Meta():
        abstract = True

    def render_image(self):
        if self.image:
            return u'<img src="%s" height="64"/>' % self.image.url
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


class Grave(WithImageMixin, models.Model):
    cemetery = models.ForeignKey(Cemetery)
    owner = models.ForeignKey(Person, related_name='graves')
    deceased = models.ForeignKey(Person)
    receipt_number = models.BigIntegerField(_('receipt_number'))
    funeral_date = models.DateTimeField(_('funeral date'))
    surface_area = models.DecimalField(_('surface area'),
                                       max_digits=5, decimal_places=2)
    has_funeral_constructions = models.BooleanField(default=False)

    def __str__(self):
        return "Cemetery: {} Owner: {}".format(self.cemetery.name,
                                               self.owner.full_name)


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
