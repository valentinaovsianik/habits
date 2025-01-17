from django.db.models import Q
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import permissions, viewsets
from rest_framework.generics import ListAPIView

from users.permissions import IsOwner

from .models import Habit
from .paginations import HabitPagination
from .serializers import HabitSerializer


@method_decorator(name="list", decorator=swagger_auto_schema(operation_description="Habit ViewSet"))
@method_decorator(name="create", decorator=swagger_auto_schema(operation_description="Create a new habit"))
@method_decorator(name="retrieve", decorator=swagger_auto_schema(operation_description="Retrieve a habit"))
@method_decorator(name="update", decorator=swagger_auto_schema(operation_description="Update a habit"))
@method_decorator(name="destroy", decorator=swagger_auto_schema(operation_description="Delete a habit"))
class HabitViewSet(viewsets.ModelViewSet):
    """CRUD модели привычка"""

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    pagination_class = HabitPagination

    def get_queryset(self):
        user = self.request.user
        queryset = Habit.objects.select_related("owner")
        if self.action == "list":
            return queryset.filter(Q(public=True) | Q(owner=user))
        return queryset.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicHabitList(ListAPIView):
    """Список публичных привычек"""

    serializer_class = HabitSerializer
    pagination_class = HabitPagination
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # Возвращаем публичные привычки
        return Habit.objects.filter(public=True)
