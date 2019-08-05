from django.contrib import admin

from .models import Contractor, Balance

__all__ = (
    'BalanceInline',
    'Contractor',
)


class BalanceInline(admin.StackedInline):
    model = Contractor.tires.through
    extra = 0


@admin.register(Contractor)
class Contractor(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'phone',
    )
    list_display_links = (
        'name',
    )
    inlines = [
        BalanceInline,
    ]
