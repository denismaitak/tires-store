from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    """Configuration for Users app."""
    name = 'apps.users'
    verbose_name = "Users"

    def ready(self):
        from . import signals  # noqa
