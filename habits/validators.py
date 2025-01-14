from rest_framework import serializers

def validate_habit(data):
    pleasant = data.get("pleasant", False)
    reward = data.get("reward")
    linked_habit = data.get("linked_habit")
    duration = data.get("duration", 120)
    periodicity = data.get("periodicity", 1)

    if pleasant and (reward or linked_habit):
        raise serializers.ValidationError(
            "Приятная привычка не может иметь вознаграждение или связанную привычку."
        )
    if not pleasant and not (reward or linked_habit):
        raise serializers.ValidationError(
            "У полезной привычки должно быть либо вознаграждение, либо связанная привычка."
        )
    if duration > 120:
        raise serializers.ValidationError("Время выполнения не может превышать 120 секунд.")
    if periodicity > 7:
        raise serializers.ValidationError("Нельзя выполнять привычку реже, чем раз в 7 дней.")
    return data
