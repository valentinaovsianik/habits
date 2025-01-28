from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User


class Habit(models.Model):
    """Модель привычки"""

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_habits",
        verbose_name="Создатель привычкм",
        help_text="Пользователь, который создал эту привычку",
    )
    action = models.CharField(
        max_length=255,
        verbose_name="Действие",
        help_text="Действие, которое вы хотите превратить в привычку",
    )
    time = models.TimeField(
        verbose_name="Время", help_text="Выберите время суток, когда вы собираетесь выполнять привычку"
    )
    place = models.CharField(max_length=255, verbose_name="Место", help_text="Место выполнения привычки")
    pleasant = models.BooleanField(
        default=False,
        verbose_name="Приятная привычка",
        help_text="Является ли привычка приятной? Установите True, если да.",
    )
    linked_habit = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        help_text="Связанная привычка, которая выполняется вместе с этой (необязательно).",
    )
    reward = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="Вознаграждение после выполнения привычки",
        help_text="Вознаграждение, которое вы получите за выполнение привычки (необязательно)",
    )
    duration = models.PositiveIntegerField(
        default=120,
        verbose_name="Продолжительность",
        help_text="Продолжительность выполнения привычки в секундах (максимум 120 секунд)",
    )
    periodicity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(7)],
        verbose_name="Периодичность",
        help_text="Как часто привычка должна выполняться (в днях, максимум раз в 7 дней)",
    )
    public = models.BooleanField(
        default=False,
        verbose_name="Публичная привычка",
        help_text="Доступна ли привычка для просмотра другими пользователями?",
    )

    def __str__(self):
        tg_nik = self.owner.tg_nik or self.owner.email
        return f"{self.action} ({tg_nik})"
