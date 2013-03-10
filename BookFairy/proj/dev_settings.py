# Django settings for BookFairy project.

from proj.common_settings import *

TEMPLATE_DEBUG = DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.abspath('%s/db/bookfairy.sql' % PROJECT_ROOT)                     # Or path to database file if using sqlite3.
    }
}
