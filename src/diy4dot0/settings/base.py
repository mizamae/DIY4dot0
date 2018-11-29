"""
Django settings for HomeAutomation project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from os.path import dirname, join, exists

from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
import environ


# Use 12factor inspired environment variables or from a file
env = environ.Env()

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
#os.environ["SECRET_KEY"]="kak(4m!d=)pc0idl1jq4nqrda7lu5b2%rucly)22qj4%9l8l5"

SECRET_KEY = env('SECRET_KEY')
 
# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(dirname(__file__))) # points to the folder src
STATICFILES_DIRS = [join(BASE_DIR, 'static')]
MEDIA_ROOT = join(BASE_DIR, 'media')
RELEASES_ROOT = join(BASE_DIR, 'releases','files')
RELEASES_TEMP = join(BASE_DIR, 'releases')
MEDIA_URL = "/media/"

LOCALE_PATHS = [ 
        join(BASE_DIR, "diy4dot0/locale"), 
        join(BASE_DIR, "templates/locale"), 
    ]


# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ALLOWED_HOSTS = [
    'mizamae2.ddns.net:8000',]

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'authtools',
    'crispy_forms',
    'easy_thumbnails',

    'profiles',
    'accounts',
    'diy4dot0',
    'releases',
    
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'diy4dot0.urls'

WSGI_APPLICATION = 'diy4dot0.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases


DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    #'default': env.db(),
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR,'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

ALLOWED_HOSTS = []

# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Authentication Settings
AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
LOGIN_URL = reverse_lazy("accounts:login")

THUMBNAIL_EXTENSION = 'png'     # Or any extn for your thumbnails
