from lms.settings import *


SECRET_KEY = 'django-insecure-^x5w7@a6_j^c$cbkk95glc*5m%ok4&cd&-!_c)$_d8tv445^a='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

SITE_ID = 1

# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'
STATICFILES_DIRS = [
    BASE_DIR / "statics"
]

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True