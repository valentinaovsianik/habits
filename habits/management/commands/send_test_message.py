import requests
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Отправка тестового сообщения в Telegram"

    def handle(self, *args, **kwargs):
        chat_id = "667981652"
        message = "Тестовое сообщение"
        url = f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage"
        response = requests.get(url, params={"chat_id": chat_id, "text": message})

        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS("Сообшение доставлено!"))
        else:
            self.stdout.write(self.style.ERROR(f"Сообщение не доставлено: {response.json()}"))
