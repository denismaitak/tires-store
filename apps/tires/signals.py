from django.dispatch import receiver, Signal

signal_triggered = Signal()


@receiver(signal_triggered, sender=object)
def log_message(sender, msg, **kwargs):
    raise Exception(msg)
