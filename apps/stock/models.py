from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from apps.tires.models import Tire

__all__ = (
    'Balance',
    'Contractor',
)


class Contractor(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Contractor"),
    )
    phone = models.CharField(
        max_length=32,
        verbose_name=_("Phone number"),
    )
    tires = models.ManyToManyField(
        to=Tire,
        through='Balance',
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Contractor")
        verbose_name_plural = _("Contractors")


class Balance(models.Model):
    tire = models.ForeignKey(
        to=Tire,
        on_delete=models.CASCADE,
        verbose_name=_("Tire"),
    )
    contractor = models.ForeignKey(
        to=Contractor,
        on_delete=models.CASCADE,
        verbose_name=_("Contractor"),
    )
    count = models.PositiveIntegerField(
        default=0,
        verbose_name=_("Count"),
        help_text=_("Count of tires available"),
    )
    updated = models.DateTimeField(
        default=timezone.now,
        editable=False,
        verbose_name=_("Updated"),
    )

    class Meta:
        verbose_name = _("Balance")
        verbose_name_plural = _("Balance")
