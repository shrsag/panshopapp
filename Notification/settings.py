
import os
from pathlib import Path
from decouple import config

import os
import dj_database_url
from dotenv import load_dotenv


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'NotificationApp',
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

ROOT_URLCONF = 'Notification.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
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

WSGI_APPLICATION = 'Notification.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST', default='localhost'),
#         'PORT': config('DB_PORT', default='5433'),
#     }
# }

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))



DATABASES = {
    "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
}


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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = config('EMAIL_HOST_USER')  
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


# SECURITY: Force HTTPS and Secure Cookies
# SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000  # 1 Year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = False
SECURE_SSL_REDIRECT = False



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# WSGI Server
WSGI_APPLICATION = 'Notification.wsgi.application'
# settings.py
SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # This keeps the session after browser close
SESSION_COOKIE_AGE = 3600 * 24 * 7  # Expire after 1 week (optional)
import logging.handlers

log_directory = os.path.join(BASE_DIR, 'logs')
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': '{levelname} {asctime} {module} {message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname} {message}',
#             'style': '{',
#         },
#     },
#     'handlers': {
#         # Logs to a file for general information (INFO and above)
#         'file': {
#             'level': 'INFO',
#             'class': 'logging.handlers.RotatingFileHandler',  # Using RotatingFileHandler for log rotation
#             'filename': os.path.join(BASE_DIR, 'logs/django.log'),
#             'maxBytes': 1024 * 1024 * 10,  # 10 MB max per log file
#             'backupCount': 5,  # Keep the last 5 log files
#             'formatter': 'verbose',
#         },
        
#         # Logs to a file for errors and critical issues (ERROR and above)
#         'error_file': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/error.log'),
#             'maxBytes': 1024 * 1024 * 10,
#             'backupCount': 5,
#             'formatter': 'verbose',
#         },
        
#         # Sends critical errors via email to admins
#         'email': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',  # AdminEmailHandler sends an email
#             'formatter': 'verbose',
#         },
        
#         # Logs to a centralized log management service like Sentry (optional)
#         # 'sentry': {
#         #     'level': 'ERROR',
#         #     'class': 'logging.handlers.SysLogHandler',
#         #     'formatter': 'verbose',
#         # },
#     },
#     'loggers': {
#         # General Django logs
#         'django': {
#             'handlers': ['file'],
#             'level': 'INFO',  # Captures all logs at INFO level and above
#             'propagate': True,
#         },
        
#         # Logs for Django requests (useful for debugging server-side issues)
#         'django.request': {
#             'handlers': ['file', 'error_file'],
#             'level': 'ERROR',  # Captures errors related to requests (500 errors)
#             'propagate': True,
#         },

#         # Logs for database queries (useful for debugging slow queries or errors)
#         'django.db.backends': {
#             'handlers': ['file'],
#             'level': 'DEBUG',  # Logs SQL queries at DEBUG level
#             'propagate': False,
#         },

#         # Security-related logs (warnings about access issues, etc.)
#         'django.security': {
#             'handlers': ['file'],
#             'level': 'WARNING',  # Captures warnings and above
#             'propagate': True,
#         },

#         # Logs for email-related issues (for debugging issues with sending emails)
#         'django.mail': {
#             'handlers': ['email'],  # Sends critical email-related errors to admins
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     },
# }
