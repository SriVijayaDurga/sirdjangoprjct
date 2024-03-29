"""
Django settings for api_framework project.

Generated by 'django-admin startproject' using Django 2.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

from api_framework.credential_config import *
import os
# from jproperties import Properties
from api_framework.constants import *

# CREDENTIAL_PATH = os.environ.get(CREDENTIAL_PATH)
# print(CREDENTIAL_PATH)
# configs = Properties()
#
# with open(CREDENTIAL_PATH, 'rb') as config_file:
#     configs.load(config_file)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ev&=6=g_h&86#j+)dqoom5lw#=i8!f=0=onh6823kwy6=71r*6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ORIGIN_ALLOW_ALL = True
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'django_jenkins',
    'application_interface',
    'util'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

JENKINS_TASKS = ('django_jenkins.tasks.run_pylint',)

ROOT_URLCONF = 'api_framework.urls'

PROJECT_APPS = (
    'django.contrib.sessions',  # just to ensure that dotted apps test works
    'django_jenkins',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'api_framework.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
# 'OPTIONS': {
#             'options': '-c search_path=django,{schema}'.format(schema='fleet')
#         },

#
        # 'NAME': 'smartweld new_db',
        # 'USER': 'isense4i',
        # 'PASSWORD': 'isense4i',
        # 'HOST': 'smartweld.livnsense.com',
        # 'PORT':  '5432'
#        'NAME': 'smartweld_test',

        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT':  os.environ.get('DB_PORT')

        # 'NAME': 'postgres',
        # 'SCHEMA': 'smartweld',
        # 'USER': 'admin',
        # 'PASSWORD': 'f9GfdZnEN#P5jh',
        # 'HOST': '192.168.1.16',
        # 'PORT': '5858'

    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': 'mydatabase',
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'azure_ad_auth.backends.AzureActiveDirectoryBackend',
)

SESSION_COOKIE_SECURE = True
LOGIN_REDIRECT_URL = '/login_successful/'

AAD_TENANT_ID = '0e7528b6-f7df-4ede-875f-6cd4f954890d'
AAD_CLIENT_ID = '9cf41a0d-6e1c-498f-a4ed-4f6543ed58ef'

# SESSION_ENGINE = "django.contrib.sessions.backends.file"
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
