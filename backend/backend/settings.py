
"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os 
from pathlib import Path
# import json
# from six.moves.urllib import request
# from cryptography.x509 import load_pem_x509_certificate
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives import serialization
#from rest_framework.authtoken.models import Token
print('************************///////////////////*************************')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^^mf4ndpr(bjf@yvtny-lgdk3yb7f_y)qtr)4=&+b50&@8kdn5'
#  token = Token.objects.create(user="xoro")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'api',
    'backend',
    'corsheaders',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework_jwt',
    'djoser',
    'phone_field',
    'django_filters',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# If this is used then `CORS_ORIGIN_WHITELIST` will not have any effect
CORS_ORIGIN_ALLOW_ALL = True 
CORS_ALLOW_CREDENTIALS = True
# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:8000',
# ]
# If this is used, then not need to use `CORS_ORIGIN_ALLOW_ALL = True`
# CORS_ORIGIN_REGEX_WHITELIST = [
#     'http://localhost:8000',
# ]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if os.getenv('GAE_APPLICATION', None):
    # Running on production App Engine, so connect to Google Cloud SQL using
    # the unix socket at /cloudsql/blackpearl2:us-central1:blackpearl
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '/cloudsql/blackpearl2:us-central1:blackpearl',
            'USER': 'xoro',
            'PASSWORD': '',
            'NAME': 'blackpearl',
        }
    }
# else:
#     # Running locally so connect to either a local MySQL instance or connect to Cloud SQL via the proxy. 
#     # To host the database locally
#     # run $ ./cloud_sql_proxy -instances=blackpearl2:us-central1:blackpearl=tcp:3306
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.mysql',
#             'HOST': '127.0.0.1',
#             'PORT': '3306',
#             'NAME': 'blackpearl',
#             'USER': 'xoro',
#             'PASSWORD': '',
#         }
#     }
else:
    # run offline database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = 'static'

# REST

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ]

     'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication', 
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'RemoteUserBackend'
     ],
    
     
    
   'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.IsAuthenticated'
      # 'rest_framework.permissions.AllowAny'
   ],

   'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

AUTH_USER_MODEL = 'api.User'

DJOSER = {
    'LOGIN_FIELD': 'username',
    'USER_CREATE_PASSWORD_RETYPE':True,
    'SERIALIZERS': {
        'user_create': 'api.serializers.UserSerializer',
        'user': 'api.serializers.UserSerializer'

    }
}

# AUTH0_DOMAIN = 'xoro.eu.auth0.com'
# API_IDENTIFIER = 'https://xoro.eu.auth0.com/api/v2/'
# PUBLIC_KEY = None
# JWT_ISSUER = None
# if AUTH0_DOMAIN:
#     jsonurl = request.urlopen('https://' + AUTH0_DOMAIN + '/.well-known/jwks.json')
#     jwks = json.loads(jsonurl.read().decode('utf-8'))
#     cert = '-----BEGIN CERTIFICATE-----\n' + jwks['keys'][0]['x5c'][0] + '\n-----END CERTIFICATE-----'
#     certificate = load_pem_x509_certificate(cert.encode('utf-8'), default_backend())
#     PUBLIC_KEY = certificate.public_key()
#     JWT_ISSUER = 'https://' + AUTH0_DOMAIN + '/'

# def jwt_get_username_from_payload_handler(payload):
#     return "dima"

# JWT_AUTH = {
#     'JWT_PAYLOAD_GET_USERNAME_HANDLER': jwt_get_username_from_payload_handler,
#     'JWT_PUBLIC_KEY': PUBLIC_KEY,
#     'JWT_ALGORITHM': 'RS256',
#     'JWT_AUDIENCE': API_IDENTIFIER,
#     'JWT_ISSUER': JWT_ISSUER,
#     'JWT_AUTH_HEADER_PREFIX': 'Bearer',
# }