"""
Django settings for pyconcz_2017 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
TMP_DIR = os.path.join(BASE_DIR, '..', 'tmp')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'provide in local.py'

ADMINS = [
    ('admins', 'admin@pycon.cz'),
]

DEFAULT_FROM_EMAIL = 'admin@pycon.cz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

SITE_ID = 1

if DEBUG:
    ALLOWED_HOSTS = []
else:
    ALLOWED_HOSTS = [
        'cz.pycon.org',
        'pycon.cz',
    ]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

    'import_export',

    'pyconcz_2017.announcements',
    'pyconcz_2017.common',
    'pyconcz_2017.team',
    'pyconcz_2017.proposals',
    'pyconcz_2017.sponsors',
    'pyconcz_2017.speakers',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pyconcz_2017.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'pyconcz_2017.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

try:
    DB_USER = os.environ['DB_USER']
    DB_HOST = os.environ['DB_HOST']
    DB_PASS = os.environ['DB_PASS']
except KeyError:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'pyconcz',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': DB_HOST,
            'NAME': os.environ.get('DB_NAME', DB_USER),
            'USER': DB_USER,
            'PASSWORD': DB_PASS,
            'PORT': os.environ.get('DB_PORT', 5432),
        }
    }


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
]

USE_TZ = True
TIME_ZONE = 'Europe/Prague'

FORMAT_MODULE_PATH = [
    'pyconcz_2017.formats'
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/2017/static/'
STATIC_ROOT = os.path.join(TMP_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(TMP_DIR, 'media')

SLACK_WEBHOOK = ''  # This variable is set in local.py

TALKS_DATES = [datetime.date(2017, 6, 8), datetime.date(2017, 6, 9)]
WORKSHOPS_DATES = [datetime.date(2017, 6, 10)]
TALKS_ROOMS = [
    (1, 'Big hall'),
    (2, 'Theatre'),
]
WORKSHOPS_ROOMS = [
    (4, 346),
    (5, 347),
    (6, 301),
    (7, 302),
    (8, 303),
]
SPRINT_ROOMS = [
    (9, 343),
]
OTHER_ROOMS = [
    (3, 'Foyer'),
]
ALL_ROOMS = TALKS_ROOMS + WORKSHOPS_ROOMS + SPRINT_ROOMS + OTHER_ROOMS
