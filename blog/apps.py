from django.apps import AppConfig
from django.conf import settings


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

    def ready(self):
        if not settings.DEBUG:
            pass
