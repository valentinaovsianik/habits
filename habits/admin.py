from django.contrib import admin

from .models import Habit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "action",
        "owner",
        "time",
        "place",
        "pleasant",
        "linked_habit",
        "reward",
        "public",
        "duration",
        "periodicity",
    )
    list_filter = ("pleasant", "public", "periodicity")
    search_fields = ("action", "owner__email", "owner__tg_nik")
