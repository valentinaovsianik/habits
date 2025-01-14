from rest_framework.routers import DefaultRouter
from django.urls import path
from habits.views import HabitViewSet, PublicHabitList

app_name = "habits"

router = DefaultRouter()
router.register(r"habits", HabitViewSet, basename="habit")

urlpatterns = [
    path("public/", PublicHabitList.as_view(), name="habit-list"),  # Путь для публичных привычек
]

urlpatterns += router.urls
