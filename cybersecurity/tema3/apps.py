from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class Tema3Config(AppConfig):
    name = "cybersecurity.tema3"
    verbose_name = _("Tema 3")

    def ready(self):
        try:
            import cybersecurity.tema3.signals  # noqa F401
        except ImportError:
            pass
