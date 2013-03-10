# Django settings for BookFairy project.

from proj.common_settings import *

import dj_database_url
config =  dj_database_url.config()

TEMPLATE_DEBUG = DEBUG = False

DATABASES = {
    'default': config
}
