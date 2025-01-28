from django.urls import path
from rest_framework.routers import DefaultRouter

from habits.views import HabitViewSet, PublicHabitList

app_name = "habits"

router = DefaultRouter()
router.register(r"", HabitViewSet, basename="habit")

urlpatterns = [
    path("public/", PublicHabitList.as_view(), name="public-habit-list"),  # Путь для публичных привычек
]

urlpatterns += router.urls
