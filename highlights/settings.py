"""
Django settings for highlights project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
import dj_database_url

from highlights import env


# Get environment variable
def get_env_var(var_name):
    env_var = os.environ.get(var_name)

    if env_var is None:
        raise KeyError('Environnement variable ' + var_name + ' not set !!')

    return env_var

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_var('SECRET_KEY')


def is_prod():
    return env.PROD_STATUS == 'prod'


ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'fb_highlights',
    'webpack_loader',
    'ddtrace.contrib.django',  # ENABLES Datadog tracing
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Tell user which mode
print("Starting server in DEBUG MODE: " + str(env.DEBUG))

# Disable SENTRY in debug mode
if not env.DEBUG:
    INSTALLED_APPS.append('raven.contrib.django.raven_compat')
    MIDDLEWARE.append('fb_bot.middleware.messenger_middleware.MessengerMiddleware')


ROOT_URLCONF = 'highlights.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'highlights.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'highlights',
        'USER': 'highlights',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Set heroku database config
config = dj_database_url.config()

if config:
    DATABASES['default'] = config


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
    }
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
STATIC_HOST = os.environ.get('DJANGO_STATIC_HOST', env.BASE_URL)
STATIC_URL = STATIC_HOST + '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

# Raven config for sentry logging

RAVEN_CONFIG = {
    'dsn': get_env_var('SENTRY_URL'),
}

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# For WEBPACK

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'build/' if env.DEBUG else 'dist/',
        'STATS_FILE': os.path.join(BASE_DIR, 'static/webpack-stats-dev.json' if env.DEBUG else 'static/webpack-stats-prod.json'),
    }
}

# For Datadog tracer

DATADOG_TRACE = {
    'DEFAULT_SERVICE': 'django',
    'TAGS': {'env': env.PROD_STATUS},
    'ANALYTICS_ENABLED': True  # Enable trace analytics
}

if not env.DEBUG:
    LOGGING = {
        'version': 1,
        'formatters': {
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
        },
        'loggers': {
            'ddtrace': {
                'handlers': ['console'],
                'level': 'INFO',
            },
        },
    }
