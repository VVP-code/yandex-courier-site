import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "YandexCurrier.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()


SUPERUSER_USERNAME = os.environ.get("DJANGO_SUPERUSER_USERNAME",)
SUPERUSER_EMAIL = os.environ.get("DJANGO_SUPERUSER_EMAIL",)
SUPERUSER_PASSWORD = os.environ.get("DJANGO_SUPERUSER_PASSWORD",)

if not User.objects.filter(username=SUPERUSER_USERNAME).exists():
    print(f"Создаем суперпользователя {SUPERUSER_USERNAME}...")
    User.objects.create_superuser(
        username=('SUPERUSER_USERNAME',),
        email=os.environ.get('SUPERUSER_EMAIL',),
        password=os.environ.get('SUPERUSER_PASSWORD',)
    )
    print("Суперпользователь создан!")
else:
    print("Суперпользователь уже существует.")
