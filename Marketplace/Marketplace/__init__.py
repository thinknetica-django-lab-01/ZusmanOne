# Это будет гарантировать, что приложение всегда импортируется при запуске Django,
# так что shared_task будет использовать это приложение.
from __future__ import absolute_import
from .celery import app as celery_app

__all__ = ('celery_app',)