import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #note appended os.path.dirname for myproj's base.py

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["fav-restaurant.herokuapp.com"]

EMAIL_BACKEND ='django.core.mail.backends.console.EmailBackend'
EMAIL_HOSTS='smtp.gmail.com'
EMAIL_HOST_USER='naw@gmail.com'
# EMAIL_HOST_PASSWORD=''
EMAIL_HOST_PASSWORD=os.environ.get('EMAIL_PASSWORD')
EMAIL_PORT=587
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL='<naw@gmail.com>'
BASE_URL ='127.0.0.1:8000'

MANAGERS=(
    ('James Aung', 'naw@gmail.com'),
)
ADMINS=MANAGERS

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = '%!%agky94xvwuyne=mxugegg2ac!x^qi&5!u1a4mbn&so8u0@q'
SECRET_KEY =os.environ.get('SECRET_KEY','%!%agky94xvwuyne=mxugegg2ac!x^qi&5!u1a4mbn&so8u0@q')
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'crispy_forms',
    'menus',
    'profiles',
    'restaurants',
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

ROOT_URLCONF = 'myproj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # "django.core.context_processors.static",
            ],
        },
    },
]

WSGI_APPLICATION = 'myproj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# add this
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
# DATABASES['default']['CONN_MAX_AGE'] = 500

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,"static_my_proj"),
]

STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static_cdn","static_root")

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static_cdn","media_root")

PROTECTED_ROOT=os.path.join(os.path.dirname(BASE_DIR), "static_cdn","protected_media")

CORS_REPLACE_HTTPS_REFERER      = False
HOST_SCHEME                     = "http://"
SECURE_PROXY_SSL_HEADER         = None
SECURE_SSL_REDIRECT             = False
SESSION_COOKIE_SECURE           = False
CSRF_COOKIE_SECURE              = False
SECURE_HSTS_SECONDS             = None
SECURE_HSTS_INCLUDE_SUBDOMAINS  = False
SECURE_FRAME_DENY               = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS=[
    os.path.join(BASE_DIR,"static_my_proj"),
]


STATIC_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static_cdn","static_root")

MEDIA_URL='/media/'
MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR),"static_cdn","media_root")

#Crispy FORM TAGs SETTINGS
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#DJANGO REGISTRATION REDUX SETTINGS
# ACCOUNT_ACTIVATION_DAYS = 7
# REGISTRATION_AUTO_LOGIN = True
# SITE_ID = 1
# LOGIN_REDIRECT_URL = '/'

