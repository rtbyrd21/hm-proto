import os
import sys
import urlparse
import dj_database_url


# db_from_env = dj_database_url.config()



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!iqfrgh@y#otldhh2#kj9umf56dv!7nio2kkpjdo48)45l3unk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'interviews.apps.InterviewsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
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

ROOT_URLCONF = 'brooklyn.urls'

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

WSGI_APPLICATION = 'brooklyn.wsgi.application'



# Register database schemes in URLs.
urlparse.uses_netloc.append('mysql')




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroku_0639161351e83ae',
        'USER': 'bf2906c2b0cbc2',
        'PASSWORD': '86c85ba9',
        'HOST': 'us-cdbr-iron-east-04.cleardb.net',
        'PORT': '3306',
    }
}

# try:
#
#     # Check to make sure DATABASES is set in settings.py file.
#     # If not default to {}
#
#     if 'DATABASES' not in locals():
#         DATABASES = {}
#
#     if 'DATABASE_URL' in os.environ:
#         url = urlparse.urlparse(os.environ['DATABASE_URL'])
#
#         # Ensure default database exists.
#         DATABASES['default'] = DATABASES.get('default', {})
#
#         # Update with environment configuration.
#         DATABASES['default'].update({
#             'NAME': url.path[1:],
#             'USER': url.username,
#             'PASSWORD': url.password,
#             'HOST': url.hostname,
#             'PORT': url.port,
#         })
#
#
#         if url.scheme == 'mysql':
#             DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
# except Exception:
#     print 'Unexpected error:', sys.exc_info()



#
# DATABASES['default'].update(db_from_env)
#
# try:
#
#     # Check to make sure DATABASES is set in settings.py file.
#     # If not default to {}
#
#     if 'DATABASES' not in locals():
#         DATABASES = {}
#
#     if 'DATABASE_URL' in os.environ:
#         url = urlparse.urlparse(os.environ['DATABASE_URL'])
#
#         # Ensure default database exists.
#         DATABASES['default'] = DATABASES.get('default', {})
#
#         # Update with environment configuration.
#         DATABASES['default'].update({
#             'NAME': url.path[1:],
#             'USER': url.username,
#             'PASSWORD': url.password,
#             'HOST': url.hostname,
#             'PORT': url.port,
#         })
#
#
#         if url.scheme == 'mysql':
#             DATABASES['default']['ENGINE'] = 'django.db.backends.mysql'
# except Exception:
#     print 'Unexpected error:', sys.exc_info()


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
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/


STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, 'static'),
]

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

try:
    from settings_local import *
except ImportError, e:
    pass