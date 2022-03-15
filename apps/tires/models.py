from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.utils.files import get_random_filename

from .fields import SeasonField
from .managers import TireManager

__all__ = (
    'Manufacturer',
    'Size',
    'Tire',
)


def upload_tire_image_to(_, filename: str) -> str:
    return settings.TIRE_IMAGE_STORING_PATH_TEMPLATE.format(
        filename=get_random_filename(filename),
    )


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("Description"),
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = _("Manufacturer")
        verbose_name_plural = _("Manufacturers")


class Size(models.Model):
    WIDTH_CHOICES = (
        (175, "175"),
        (185, "185"),
        (205, "205"),
        (265, "265"),
    )
    HEIGHT_CHOICES = (
        (60, "60"),
        (65, "65"),
        (70, "70"),
        (80, "80"),
    )
    DIAMETER_CHOICES = (
        (13, "13"),
        (14, "14"),
        (15, "15"),
        (17, "17"),
    )

    width = models.IntegerField(
        verbose_name=_("Width"),
        choices=WIDTH_CHOICES,
    )
    height = models.IntegerField(
        choices=HEIGHT_CHOICES,
        verbose_name=_("Height"),
    )
    diameter = models.IntegerField(
        choices=DIAMETER_CHOICES,
        verbose_name=_("Diameter"),
    )

    def __str__(self):
        return f'{self.width}/{self.height}R{self.diameter}'

    class Meta:
        unique_together = ('width', 'height', 'diameter')
        verbose_name = _("Size")
        verbose_name_plural = _("Sizes")


class Tire(models.Model):
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE,
        verbose_name=_("Manufacturer"),
    )
    size = models.ForeignKey(
        to=Size,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("Size"),
    )
    title = models.CharField(
        max_length=255,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("Description"),
    )
    season = SeasonField(
        verbose_name=_("Season"),
        help_text=_("Optimal season for a tire using."),
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        null=True,
        blank=True,
        upload_to=upload_tire_image_to,
        max_length=200,
    )

    objects = TireManager()

    def __str__(self):
        return f'{self.title} {self.size}'

    class Meta:
        unique_together = ('manufacturer', 'size', 'title')
        verbose_name = _("Tire")
        verbose_name_plural = _("Tires")
