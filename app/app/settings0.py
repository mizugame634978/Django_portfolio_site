from pathlib import Path
import os

from django.utils.translation import ugettext_lazy as _ #これが原因でエラーとなった。多言語に対応するためのもの
#現在は推奨されておらず、import gettext_lazyに変えないと動かない


BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_NAME = os.path.basename(BASE_DIR)
LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-itmnl0nmi9p^^kp^y3mog*5!xt52!ag-7e*7d&-9fa^s25a*yt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



ALLOWED_HOSTS = ['*']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',#アプリケーション名
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls' #プロジェクト名をxxxに入れる

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'app.wsgi.application' #プロジェクト名をxxxに入れる



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'ja'

# 英語対応の場合は 下記コメントアウトを外す
LANGUAGES = [
    ('ja', _('日本語')),#これで'_'としてimportした関数の引数に'日本語'を渡している
    # ('en', _('English')),
]

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True#日付フォーマットなどのローカライゼーション機能を有効にするか否かを指定します。L10N は localization の略です。

USE_TZ = True


# Static files (CSS, JavaScript, Images) and Media files
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = 'media/'


# Upload Settings

DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000
FILE_UPLOAD_MAX_MEMORY_SIZE = 15728640
DATA_UPLOAD_MAX_MEMORY_SIZE = 15728640



