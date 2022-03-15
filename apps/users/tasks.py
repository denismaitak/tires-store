from django.conf import settings
from django.core.mail import send_mail

from apps.utils.celery import extended_shared_task

from .models import User


@extended_shared_task()
def send_notification_to_created_user(user_id):
    user = User.objects.get(pk=user_id)

    send_mail(
        "Welcome to Tires Store",
        f"Hi, {user.get_full_name()}!",
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
