from django.db import models
from django.db.models.functions import Coalesce

from .querysets import TireQuerySet

__all__ = (
    'TireManager',
)


class TireManager(models.Manager):

    def get_queryset(self) -> models.QuerySet:
        queryset = TireQuerySet(self.model, using=self._db)

        return queryset.annotate(
            count=Coalesce(models.Sum(models.F('balance__count')), 0),
        )

    def available(self) -> models.QuerySet:
        return self.get_queryset().available()
