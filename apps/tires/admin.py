from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Manufacturer, Size, Tire

__all__ = (
    'Manufacturer',
    'Size',
    'Tire',
)


@admin.register(Manufacturer)
class Manufacturer(admin.ModelAdmin):
    pass


@admin.register(Size)
class Size(admin.ModelAdmin):
    pass


@admin.register(Tire)
class Tire(admin.ModelAdmin):
    list_display = (
        'id',
        'manufacturer',
        'title',
        'size',
        'count',
    )

    def count(self, obj: Tire) -> int:
        return obj.count

    count.short_description = _("Count")
