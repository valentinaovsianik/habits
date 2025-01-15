from rest_framework import serializers

from .models import Habit


class HabitSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source="owner.id")

    class Meta:
        model = Habit
        fields = "__all__"
