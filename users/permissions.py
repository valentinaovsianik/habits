from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Разрешение на доступ только владельцу привычки"""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
