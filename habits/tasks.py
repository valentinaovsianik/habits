from datetime import timedelta

from celery import shared_task
from django.utils.timezone import now

from habits.services import send_tg_message

from .models import Habit


@shared_task
def send_habit_reminders():
    """Задача отправки уведомлений за 15 минут до выполнения привычки"""
    current_time = now().time()
    reminder_time = (now() + timedelta(minutes=15)).time()

    # Фильтруем привычки, которые должны быть выполнены через 15 минут
    habits = Habit.objects.filter(time__gte=current_time, time__lte=reminder_time)

    for habit in habits:
        chat_id = habit.owner.tg_nik
        if chat_id:
            message = f"Напоминание! Через 15 минут пора выполнить: {habit.action} в {habit.place}!"
            send_tg_message(chat_id, message)


@shared_task
def send_habit_execution_message():
    """Задача по отправке напоминания о выполнении привычки"""
    current_time = now().time()

    # Привычки, которые нужно выполнить сейчас
    habits = Habit.objects.filter(time=current_time)

    for habit in habits:
        chat_id = habit.owner.tg_nik
        if chat_id:
            message = f"Время выполнять привычку: {habit.action} в {habit.place}! "
            send_tg_message(chat_id, message)


# @shared_task
# def send_test_message():
#     chat_id = "667981652"
#     message = "Это тестовое сообщение от Celery Task!"
#     url = f"{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage"
#     response = requests.get(url, params={"chat_id": chat_id, "text": message})
#
#     return response.status_code == 200
