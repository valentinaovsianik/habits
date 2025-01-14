from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView

from .models import Habit
from .serializers import HabitSerializer
from .paginations import HabitPagination
from users.permissions import IsOwner


class HabitViewSet(viewsets.ModelViewSet):
    """CRUD модели привычка"""
    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    pagination_class = HabitPagination

    def get_queryset(self):
        user = self.request.user
        if self.action == "list":
            return Habit.objects.filter(public=True)
        return Habit.objects.filter(owner=user)

    def perform_create(self, serializer):
        # Устанавливаем владельца привычки
        serializer.save(owner=self.request.user)


class PublicHabitList(ListAPIView):
    """Список публичных привычек"""
    serializer_class = HabitSerializer
    pagination_class = HabitPagination

    def get_queryset(self):
        # Возвращаем публичные привычки
        return Habit.objects.filter(public=True)
