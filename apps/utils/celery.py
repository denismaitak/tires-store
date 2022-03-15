from django.conf import settings

from celery import shared_task


def extended_shared_task(*decorator_args, **decorator_kwargs):
    """Decorator to avoid boilerplate with ``shared_task`` decorator.

    Allow avoid following code:

        if settings.USE_CELERY:
            some_task.delay(**kwargs)
        else:
            some_task(**kwargs)

    """
    def extended_shared_task_decorator(func):
        func = shared_task(func, *decorator_args, **decorator_kwargs)

        def _wrapped(*args, **kwargs):
            if settings.USE_CELERY:
                return func.delay(*args, **kwargs)
            return func(*args, **kwargs)

        return _wrapped

    return extended_shared_task_decorator
