from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class Tema2Config(AppConfig):
    name = "cybersecurity.tema2"
    verbose_name = _("Tema 2")

    def ready(self):
        try:
            import cybersecurity.tema2.signals  # noqa F401
        except ImportError:
            pass
