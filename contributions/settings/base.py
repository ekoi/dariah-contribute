"""
Django settings for contributions project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

SITE_ROOT = os.path.dirname(os.path.realpath(__file__)).rsplit('/', 2)[0]
PROJECT_NAME = os.path.dirname(os.path.realpath(__file__)).rsplit('/', 2)[1]
BASE_DIR = os.path.join(SITE_ROOT, PROJECT_NAME)


ROOT_URLCONF = PROJECT_NAME + '.urls.prod'

MAINTENANCE_MODE = True

DOMAIN_NAME = ''
SITE_NAME = 'Dariah Contributions'

ALLOWED_HOSTS = '*'

# By default use the console e-mail backend so no e-mails are ever send in
# development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=^awu!pd8i=d+!_%t-fh=#ctbr87i!0h$fi$!^mlbkb9@v&n!!'

DEBUG = False
TEMPLATE_DEBUG = False

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
ugettext = lambda s: s
LANGUAGES = (
    ('en', ugettext("English")),
    ('nl', ugettext("Dutch")),
)
FORMAT_MODULE_PATH = PROJECT_NAME + '.formats'
# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True
USE_THOUSAND_SEPARATOR = True
# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True
DATE_FORMAT = 'F j, Y'
DATETIME_FORMAT = 'F j, Y, G:i'
TIME_FORMAT = 'G:i'
#SHORT_DATE_FORMAT =

# DATABASES
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Application definition
INSTALLED_APPS = (
    'dariah_contributions',
    'dariah_static_data',
    'south',
    'axes',  # Limit login attempts
    'bootstrap3',
    'bootstrap3_datetime',
    'grappelli',
    'autocomplete_light',
    'taggit',

    'django.contrib.flatpages',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'django_cleanup',  # SHOULD GO AFTER ALL OTHER APPS
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    'maintenancemode.middleware.MaintenanceModeMiddleware',
    'axes.middleware.FailedLoginMiddleware',  # Limit login attempts
)

ROOT_URLCONF = 'contributions.urls'

WSGI_APPLICATION = 'contributions.wsgi.application'
# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'wsgi.application'

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static_collected')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    "django.core.context_processors.request",  # Necessary for Grappelli
)

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'templates'),
)

LOGIN_REDIRECT_URL = '/contribution/'

MAINTENANCE_IGNORE_URLS = (
    r'^' + STATIC_URL + '.*',
    r'^' + MEDIA_URL + '.*',
    r'^/accounts/logout',
    r'^/$',
)

# django-axes (limit login attempts) settings
AXES_LOGIN_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 1
AXES_LOCKOUT_URL = '/lockout'
AXES_LOCKOUT_TEMPLATE = 'axes/lockout.html'
AXES_USE_USER_AGENT = True

GRAPPELLI_ADMIN_TITLE = ugettext("Dariah Contributions Admin")

BOOTSTRAP3 = {
    'javascript_in_head': True,
    'set_placeholder': False,
}

SOUTH_MIGRATION_MODULES = {
    'taggit': 'taggit.south_migrations',
}
