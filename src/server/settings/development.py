from . import *  # NOQA
from . import INSTALLED_APPS, MIDDLEWARE

DEBUG = True

INSTALLED_APPS += ("debug_toolbar",)

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware", *MIDDLEWARE]


DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK": lambda request: True,
}

ALLOWED_HOSTS = ["localhost"]
