"""
Django settings for sonicecommerce project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = 'django-insecure-8g%hr97^3$rakzpi%$2g%k%d%$vn%&48w6#8g0edc=c#at&m(c'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'home',
    'category',
    'store',
    'cadmin',
    'coupon',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    #'social_django',  # Google SSO,
    'carts',
    'orders',
    'image_cropping',
    'easy_thumbnails',
    'wishlist',
    'wallet',
    'offers',
    'variation',
    
]
# settings.py



SOCIALACCOUNT_ADAPTER = 'accounts.adapters.MySocialAccountAdapter'


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'social_django.middleware.SocialAuthExceptionMiddleware',
    'allauth.account.middleware.AccountMiddleware', 
]

# settings.py

SOCIALACCOUNT_PIPELINE = (
    'allauth.socialaccount.pipeline.social_auth.social_login',
    'allauth.socialaccount.pipeline.social_auth.social_user',
    'allauth.socialaccount.pipeline.social_auth.associate_by_email',
    'allauth.socialaccount.pipeline.social_auth.load_extra_data',
    'allauth.socialaccount.pipeline.user.get_username',
    'allauth.socialaccount.pipeline.user.create_user',
    'allauth.socialaccount.pipeline.socialaccount.setup_user_email',
    'allauth.socialaccount.pipeline.socialaccount.save_social_account',
    'allauth.socialaccount.pipeline.socialaccount.sync_user_avatar',
    'accounts.auth_pipeline.activate_user',  # Add your custom function here
)


ROOT_URLCONF = 'sonicecommerce.urls'

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
                'category.context_processors.menu_links',
                'carts.context_processors.counter',
                #'social_django.context_processors.backends',
                #'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'sonicecommerce.wsgi.application'

AUTH_USER_MODEL = 'accounts.Accounts'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sonic',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',  # Or the IP address of your PostgreSQL server
        'PORT': '5432',  # Default port for PostgreSQL
    }
}
# Password validation
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [
    BASE_DIR / 'sonicecommerce/static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}




# Twilio Configuration
TWILIO_ACCOUNT_SID = 'AC04a3991696e792c6c83832cd160de294'
TWILIO_AUTH_TOKEN = 'c3341c03ff63e4271c28fdd2ec05e7a3'
TWILIO_PHONE_NUMBER = '+14064761924'
#sso
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
    
)
SITE_ID = 1




LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': '855458142857-j4n46bfqprcjj63ldk13tba08otijtbs.apps.googleusercontent.com',
            'secret': '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',
            'key': ''

        },
        'AUTH_PARAMS': {
            'access_type': 'offline',
        },
        'SCOPE': [
            'profile',
            'email',
            
        ],
        #'OVERRIDE_URLS': {
           # 'login': 'accounts/google/login/',
        #}
    }
}


# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # For Gmail
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'sonicshopkart2@gmail.com'
EMAIL_HOST_PASSWORD = 'zpvt omjg tnje ftjp'

from easy_thumbnails.conf import Settings as thumbnail_settings

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'easy_thumbnails.processors.scale_and_crop',
    'easy_thumbnails.processors.filters',
)

# Add the crop_corners processor from django-image-cropping
THUMBNAIL_PROCESSORS += (
    'image_cropping.thumbnail_processors.crop_corners',
)

