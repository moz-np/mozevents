# Django settings for mozevents project.

#
# DO NOT edit this file, add you configuration in settings_local.py
#

# l10n
from django.utils.translation import ugettext_lazy as _

# Get project path
from os.path import dirname, join, realpath
PROJECT_PATH = realpath(join(dirname(__file__), '..'))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = PROJECT_PATH+'/public/media/'

STATIC_ROOT = PROJECT_PATH+"/static/"
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    PROJECT_PATH+"/public/static/",
)

LANGUAGES = (
    ('es', _('Spanish')),
    ('en', _('English')),
)

LOCALE_PATHS = (
    PROJECT_PATH+'/locale',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    #"django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    'events.context_processors.site_settings',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'mozevents.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_PATH+"/templates",
    PROJECT_PATH+"/templates/events",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'south',
    'django_countries',
    'recaptcha',
    'events'
)

CACHE_BACKEND = 'file://'+PROJECT_PATH+'/cache'
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = 'mozevents'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True

# Import local settings
try:
    from settings_local import *
except Exception:
    pass

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = SITE_URL+'/media/'
