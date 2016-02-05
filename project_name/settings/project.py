# -*- coding: utf-8 -*-
# general project settings, on top of django base settings 
from .base import *
from ..version import __version__

try:
    # for secret keys, api keys, etc
    from .secret import *
except ImportError:
    pass

try:
    # for machine dependent settings, eg database, redis, etc
    from .local import *
except ImportError:
    pass


INSTALLED_APPS += [
    'django_extensions',
]
