from django.utils.translation import ugettext_lazy as _


class RequestStatus():
    FAVORABLE = 0
    NOT_FAVORABLE = 1
    PARTIAL = 2
    REJECTED = 3
    INTERNAL = 4

    REQUEST_OPTIONS = (
        (FAVORABLE, _('Favorable')),
        (NOT_FAVORABLE, _('Not favorable')),
        (PARTIAL, _('Partial')),
        (REJECTED, _('Rejected')),
        (INTERNAL, _('Internal'))
    )
