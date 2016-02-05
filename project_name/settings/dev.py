# -*- coding: utf-8 -*-
# development/debug environment settings
from .project import *


# SECURITY WARNING: move this variable to secret.py, don't commit secret.py!
SECRET_KEY = '{{ secret_key }}'

DEBUG = True

INSTALLED_APPS += [
    'debug_toolbar',
]
