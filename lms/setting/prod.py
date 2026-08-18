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


CSRF_COOKIE_SECURE = True

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
COMPRESS_ROOT = STATIC_ROOT

COMPRESS_CSS_FILTERS = [
    "compressor.filters.cssmin.CSSMinFilter"
]

COMPRESS_JS_FILTERS = [
    "compressor.filters.jsmin.JSMinFilter"
]

SECURE_SSL_REDIRECT = True


SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True


SECURE_BROWSER_XSS_FILTER = True


X_FRAME_OPTIONS = 'DENY'


SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True