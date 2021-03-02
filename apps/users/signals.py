from django.db.models.signals import post_save
from django.dispatch import receiver

from . import tasks
from .models import User

__all__ = (
    'send_notifications_to_created_user',
)


@receiver(post_save, sender=User)
def send_notifications_to_created_user(*, instance, created, **_):
    """Send a notification to created user."""

    # if not created:
    #     return

    tasks.send_notification_to_created_user(instance.id)
