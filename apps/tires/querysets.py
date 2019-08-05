from django.db import models

__all__ = (
    'TireQuerySet',
)


class TireQuerySet(models.QuerySet):

    def available(self) -> models.QuerySet:
        return self.filter(count__gt=0)
