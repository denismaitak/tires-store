from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

from .models import User

__all__ = (
    'send_notifications_to_created_user',
)


@receiver(post_save, sender=User)
def send_notifications_to_created_user(*, instance, created, **_):
    """Send a notification to created user."""

    if not created:
        return

    send_mail(
        "Welcome to Tires Store",
        f"Hi, {instance.get_full_name()}!",
        settings.DEFAULT_FROM_EMAIL,
        [instance.email],
        fail_silently=False,
    )
