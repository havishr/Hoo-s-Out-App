"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

#New imports from https://github.com/heroku/python-getting-started/blob/main/gettingstarted/settings.py
#REQUIRED: pip install gunicorn, pip install dj-database-url, pip install whitenoise
import os
import secrets
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#From https://github.com/heroku/python-getting-started/blob/main/gettingstarted/settings.py
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    default=secrets.token_urlsafe(nbytes=64),
)

# SECURITY WARNING: don't run with debug turned on in production!


ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split()

# Application definition
#From https://www.youtube.com/watch?v=yO6PP0vEOMc
SITE_ID = 4

INSTALLED_APPS = [
    #From https://github.com/heroku/python-getting-started/blob/main/gettingstarted/settings.py
    'whitenoise.runserver_nostatic',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #From https://www.youtube.com/watch?v=yO6PP0vEOMc
    'django.contrib.sites',
    'oauth_app',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    #From https://github.com/heroku/python-getting-started/blob/main/gettingstarted/settings.py
    "whitenoise.middleware.WhiteNoiseMiddleware",

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

#From https://www.youtube.com/watch?v=yO6PP0vEOMc
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#From https://github.com/heroku/python-getting-started/blob/main/gettingstarted/settings.py
# if IS_HEROKU_APP:
#         DATABASES = {
#         "default": dj_database_url.config(
#             conn_max_age=600,
#             conn_health_checks=True,
#             ssl_require=True,
#         ),
#     }
#
# else:
#     DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#         }
#     }

ON_HEROKU = os.environ.get('ON_HEROKU')

ON_HEROKU = True

if ON_HEROKU:
    DATABASES = {
        'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
    }
else:
    DATABASE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')
    DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}





# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

#From https://github.com/heroku/python-getting-started/blob/main/gettingstarted/settings.py
STATIC_ROOT = BASE_DIR / "staticfiles"

STATIC_URL = 'static/'

#From https://github.com/heroku/python-getting-started/blob/main/gettingstarted/settings.py
STORAGES={
     "staticfiles":{
          "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
     },
}
WHITENOISE_KEEP_ONLY_HASHED_FILES=True


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#From https://www.youtube.com/watch?v=yO6PP0vEOMc
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend"
)

#From https://www.youtube.com/watch?v=yO6PP0vEOMc
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"


#From https://www.youtube.com/watch?v=yO6PP0vEOMc
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email"
        ],
        "AUTH_PARAMS": {"access_type": "online"}
    }
}

