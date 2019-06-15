from config import db

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-asql$a+8k*x%yp^mez=ze#c5dhkfbjbbs0shkq#b!ft09_dmr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'team',
    'django.contrib.auth',
    'django.contrib.contenttypes',
]

MIDDLEWARE = []

ROOT_URLCONF = 'instawork_interview.urls'

WSGI_APPLICATION = 'instawork_interview.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db['db_name'],
        'HOST': db['host'],
        'PORT': db['port'],
        'USER': db['user'],
        'PASSWORD': db['password'],
    }
}
