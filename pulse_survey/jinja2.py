from django.conf import settings
from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment


def environment(**options):
    extra_options = dict()
    env = Environment(
        **{
            **options,
            **extra_options,
        }
    )
    env.globals.update(
        {
            "static": static,
            "url": reverse,
            "DEBUG": settings.DEBUG,
        }
    )
    return env
