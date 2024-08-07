import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(6f)q9&+mk#%%r&!*ar6w-_f6rkx7$=0lbzgy*noey6w%&)+tr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]
#CSRF_TRUSTED_ORIGINS = ["http://147.78.66.163", "https://147.78.66.163", "http://127.0.0.1:8000", ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
    'loyixa',
    'corsheaders',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#CORS_ALLOWED_ORIGINS = [
#    "http://localhost:3000",
#    "http://127.0.0.1:3000",
#    "http://127.0.0.1:5500",
#    "http://localhost:3001",
#    "http://localhost:3002",
#    "http://localhost:3003",
#    "http://localhost:3004",
#    "http://localhost:3005",
#    "http://127.0.0.1:3001",
#    "http://127.0.0.1:3002",
#    "http://127.0.0.1:3003",
#    "http://127.0.0.1:3004",
#    "http://127.0.0.1:8000",
#]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'http://127.0.0.1',
    'https://makler1.herokuapp.com',
    'https://84.252.75.67',
    'https://api.makleruz.uz',
    'https://back2.protools.uz/'
    'https://147.78.66.163'
    'http://147.78.66.163'
)

ROOT_URLCONF = 'loyiha.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'static'],
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

WSGI_APPLICATION = 'loyiha.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
     'default': {
         "ENGINE": 'django.db.backends.postgresql_psycopg2',
         "NAME": "loyiha_db",
         "USER": "loyiha",
         "PASSWORD": "loyiha",
         "HOST": "localhost",
         "PORT": 5432,
     }
}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "static"
# STATICFILES_DIRS = [
#     BASE_DIR / "static/"
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

#CORS_ALLOW_ALL_ORIGINS = True
#CORS_ORIGIN_ALLOW_ALL = True
#CORS_ALLOW_CREDENTIALS = True

#CORS_ORIGIN_WHITELIST = (
#    'http://localhost:4200',
#    'http://127.0.0.1',
#    'https://makler1.herokuapp.com',
#    'https://84.252.75.67',
#    'https://api.makleruz.uz',
#    'https://back2.protools.uz/'
#    'https://147.78.66.163'
#    'http://147.78.66.163'
#)

CORS_ALLOW_ALL_ORIGINS = True
# CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_WHITELIST = (
    'http://localhost:4200',
    'http://127.0.0.1',
    'https://makler1.herokuapp.com',
    'https://84.252.75.67',
    'https://api.makleruz.uz',
    'https://back2.protools.uz',
    'https://147.78.66.163',
    'http://147.78.66.163'
)

SITE_ID = 1

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'