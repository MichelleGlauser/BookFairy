# Django settings for BookFairy project.

from proj.common_settings import *

TEMPLATE_DEBUG = DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bookfairy_db', # Or path to database file if using sqlite3.
        'USER': 'michelleglauser',
        'HOST': 'localhost',
    }
}
