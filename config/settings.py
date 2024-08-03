"""
Django settings for config project.
Generated by 'django-admin startproject' using Django 4.2.4.
"""

import os
from datetime import timedelta
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', 'secret-key-default')

DEBUG = bool(int(os.getenv('DEBUG', 1)))

ALLOWED_HOSTS = ['*']

# Application definition

DJANGO_APPS = [
    'apps.api.apps.ApiConfig',
    'apps.user.apps.UserConfig',
]

THIRD_PARTY_PACKAGES = [
    'rest_framework',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    *DJANGO_APPS,
    *THIRD_PARTY_PACKAGES,
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

ROOT_URLCONF = 'config.urls'

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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'user.User'

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.getenv('CACHES_REDIS_HOST', default='redis://127.0.0.1:6379'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'TIMEOUT': int(os.getenv('REDIS_TIMEOUT', default='3600')),
        'KEY_PREFIX': os.getenv('REDIS_KEY_PREFIX', default=''),
    }
}

OTP_EXPIRE_TIME: int = int(os.environ.get('OTP_EXPIRE_TIME', 3600))
CACHE_KEY_PREFIX: str = os.environ.get('CACHE_KEY_PREFIX', 'user_attempts')

LOGIN_ATTEMPT_LIMIT: int = 3
OTP_ATTEMPT_LIMIT: int = 3
BLOCK_DURATION: int = 3600


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=int(os.environ.get('ACCESS_TOKEN_LIFETIME', 10))),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(os.environ.get('REFRESH_TOKEN_LIFETIME', 1))),
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=int(os.environ.get('SLIDING_TOKEN_LIFETIME', 5))),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=int(os.environ.get('SLIDING_TOKEN_REFRESH_LIFETIME', 1))),
}
