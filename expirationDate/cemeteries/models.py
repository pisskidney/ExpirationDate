from django.db import models
from django.utils.translation import ugettext_lazy as _


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
