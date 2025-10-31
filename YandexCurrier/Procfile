release: python create_superuser.py
web: gunicorn YandexCurrier.wsgi:application
web: gunicorn YandexCurrier.wsgi:application --bind 0.0.0.0:$PORT
