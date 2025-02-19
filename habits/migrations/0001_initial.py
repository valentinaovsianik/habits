# Generated by Django 5.1.4 on 2025-01-12 14:58

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Habit",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "action",
                    models.CharField(
                        help_text="Действие, которое вы хотите превратить в привычку",
                        max_length=255,
                        verbose_name="Действие",
                    ),
                ),
                (
                    "time",
                    models.TimeField(
                        help_text="Выберите время суток, когда вы собираетесь выполнять привычку", verbose_name="Время"
                    ),
                ),
                (
                    "place",
                    models.CharField(help_text="Место выполнения привычки", max_length=255, verbose_name="Место"),
                ),
                (
                    "pleasant",
                    models.BooleanField(
                        default=False,
                        help_text="Является ли привычка приятной? Установите True, если да.",
                        verbose_name="Приятная привычка",
                    ),
                ),
                (
                    "reward",
                    models.CharField(
                        blank=True,
                        help_text="Вознаграждение, которое вы получите за выполнение привычки (необязательно)",
                        max_length=255,
                        null=True,
                        verbose_name="Вознаграждение после выполнения привычки",
                    ),
                ),
                (
                    "duration",
                    models.PositiveIntegerField(
                        default=120,
                        help_text="Продолжительность выполнения привычки в секундах (максимум 120 секунд)",
                        verbose_name="Продолжительность",
                    ),
                ),
                (
                    "periodicity",
                    models.PositiveIntegerField(
                        default=1,
                        help_text="Как часто привычка должна выполняться (в днях, максимум раз в 7 дней)",
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(7),
                        ],
                        verbose_name="Периодичность",
                    ),
                ),
                (
                    "public",
                    models.BooleanField(
                        default=False,
                        help_text="Доступна ли привычка для просмотра другими пользователями?",
                        verbose_name="Публичная привычка",
                    ),
                ),
                (
                    "linked_habit",
                    models.ForeignKey(
                        blank=True,
                        help_text="Связанная привычка, которая выполняется вместе с этой (необязательно).",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="habits.habit",
                        verbose_name="Связанная привычка",
                    ),
                ),
                (
                    "owner",
                    models.ForeignKey(
                        help_text="Пользователь, который создал эту привычку",
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_habits",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Создатель привычкм",
                    ),
                ),
            ],
        ),
    ]
