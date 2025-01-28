from rest_framework import serializers

from .models import Habit
from .validators import validate_habit


class HabitSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source="owner.id")

    class Meta:
        model = Habit
        fields = "__all__"

    def validate(self, data):
        try:
            return validate_habit(data)
        except serializers.ValidationError as e:
            raise serializers.ValidationError(e.detail)
