import os
from pathlib import Path
import dj_database_url  # ставится через pip install dj-database-url

# -----------------------
# Папка проекта
# -----------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# Секретный ключ
# -----------------------
SECRET_KEY = os.environ.get('SECRET_KEY', 'fallback-secret-key')  # на Render добавь SECRET_KEY

# -----------------------
# Продакшен / отладка
# -----------------------
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'yandex-courier-site.onrender.com').split(',')

# -----------------------
# Приложения
# -----------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # твои приложения
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # для статики
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'YandexCurrier.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # если у тебя есть шаблоны
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

WSGI_APPLICATION = 'YandexCurrier.wsgi.application'

# -----------------------
# База данных
# -----------------------
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')  # в Render добавь DATABASE_URL = External Database URL
    )
}

# -----------------------
# Пароли
# -----------------------
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

# -----------------------
# Локализация
# -----------------------
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

# -----------------------
# Статика
# -----------------------
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise для продакшена
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# -----------------------
# Прочее
# -----------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
