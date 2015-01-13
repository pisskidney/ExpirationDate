from django.utils.translation import ugettext_lazy as _


class PersonGender():
    NOT_SPECIFIED = 0
    MALE = 1
    FEMALE = 2

    GENDER_OPTIONS = (
        (NOT_SPECIFIED, _('Not specified')),
        (MALE, _('Male')),
        (FEMALE, _('Female')),
    )


class PersonReligion():
    NOT_SPECIFIED = 0
    CHRISTIANITY = 1
    ISLAM = 2
    HINDUISM = 3
    BUDDHISM = 4

    RELIGION_OPTIONS = (
        (NOT_SPECIFIED, _('Not specified')),
        (CHRISTIANITY, _('Christianity')),
        (ISLAM, _('Islam')),
        (HINDUISM, _('Hinduism')),
        (BUDDHISM, _('Buddhism')),
    )
