from django.db import models
from django.utils.translation import ugettext_lazy as _

from .constants import Season

__all__ = (
    'SeasonField',
)

SEASON_CHOICES = (
    (Season.WINTER, _("Winter")),
    (Season.SUMMER, _("Summer")),
    (Season.ALL, _("All seasons")),
)

class SeasonField(models.CharField):

    def __init__(self, *args, **kwargs):

        kwargs.update({
            'max_length': 32,
            'choices': SEASON_CHOICES,
            'default': Season.ALL,
        })

        super().__init__(*args, **kwargs)
