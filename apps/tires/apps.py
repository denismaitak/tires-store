from django.apps import AppConfig


class TiresAppConfig(AppConfig):
    """Configuration for Tires app."""
    name = 'apps.tires'
    verbose_name = "Tires"

    def ready(self):
        from . import signals  # noqa
