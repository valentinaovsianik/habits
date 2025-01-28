import requests

from config import settings


def send_tg_message(chat_id, message):
    """Отправляет сообщения в Телеграм"""
    params = {"text": message, "chat_id": chat_id}
    requests.get(f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage", params=params)
