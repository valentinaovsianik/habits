from rest_framework import serializers
from .models import Habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        # Проверка на уникальность имени привычки
        data = super().validate(data)
        if Habit.objects.filter(action=data["action"], owner=self.context["request"].user).exists():
            raise serializers.ValidationError("Привычка с таким названием уже существует.")
        return data
    