from .celery import app as celery_app

__all__ = ("celery_app",)

TEST_DOMAIN = '127.0.0.1:8000'