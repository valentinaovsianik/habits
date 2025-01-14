from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """ViewSet для управления пользователями (CRUD)"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserCreateAPIView(CreateAPIView):
    """Представление для регистрации пользователя"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Создание пользователя"""
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
