"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 1.8.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from pathlib import Path
import os
BASE_DIR = Path(__file__).resolve().parent.parent
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rn0f6a(ky&o&hvuv@y&afieu_70k+^80unhz!1o&gf_*t=&2rq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'question',
    'contest',
    'gunicorn',
    'tinymce',
    'crispy_forms',
    # 'bootstrap4'
)
CRISPY_TEMPLATE_PACK = 'bootstrap4'
MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'website.urls'

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
                'contest.context_processors.contest_time',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = False

USE_L10N = False

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'staticfiles')]
# STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.FileSystemFinder',
#                        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#                        )


STATICFILES_DIRS = [
    BASE_DIR / "static",
    
]
# STATIC_ROOT = BASE_DIR / 'static'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

SLAVE_ADDRESSES = (('127.0.0.1', 9000),
                   ('127.0.0.1', 9001),
                   ('127.0.0.1', 9002),
                   ('127.0.0.1', 9003),
                   ('127.0.0.1', 9004),
                   ('127.0.0.1', 9005),
                   ('127.0.0.1', 9006),
                   ('127.0.0.1', 9007),
                   ('127.0.0.1', 9008),
                   ('127.0.0.1', 9009),
                   ('127.0.0.1', 9010),
                   ('127.0.0.1', 9011),
                   ('127.0.0.1', 9012),
                   ('127.0.0.1', 9013),
                   ('127.0.0.1', 9014),
                   )
