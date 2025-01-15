from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from habits.models import Habit
from users.models import User


class HabitAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="testuser@example.com")

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit_1 = Habit.objects.create(
            owner=self.user,
            action="Утренняя пробежка",
            time="07:00:00",
            place="Парк",
            pleasant=True,
            reward="Чашка кофе",
            duration=80,
            periodicity=1,
            public=True,
        )

        self.habit_2 = Habit.objects.create(
            owner=self.user,
            action="Завтрак",
            time="08:00:00",
            place="Кухня",
            pleasant=True,
            reward="Теплый чай",
            duration=60,
            periodicity=1,
            public=True,
        )

    def test_habit_list(self):
        """Тест на получение списка привычек"""
        url = reverse("habits:habit-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)
        # Проверяем, что в ответе присутствуют все привычки пользователя
        actions = [habit["action"] for habit in response.data["results"]]
        self.assertIn(self.habit_1.action, actions)
        self.assertIn(self.habit_2.action, actions)

    def test_habit_retrieve(self):
        """Тест на получение одной привычки"""
        url = reverse("habits:habit-detail", args=(self.habit_1.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], self.habit_1.id)
        self.assertEqual(response.data["action"], "Утренняя пробежка")

    def test_habit_create(self):
        """Тест на создание привычки"""
        url = reverse("habits:habit-list")
        data = {
            "action": "Вечерняя йога",
            "time": "20:00:00",
            "place": "Дом",
            "pleasant": False,
            "reward": "Отдых",
            "duration": 600,
            "periodicity": 2,
            "public": False,
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["action"], data["action"])
        self.assertEqual(response.data["owner"], self.user.id)

    def test_habit_update(self):
        """Тест на обновление привычки"""
        url = reverse("habits:habit-detail", args=(self.habit_1.id,))
        data = {"action": "Обновленная привычка"}
        response = self.client.patch(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.habit_1.refresh_from_db()
        self.assertEqual(self.habit_1.action, "Обновленная привычка")

    def test_habit_delete(self):
        """Тест на удаление привычки"""
        url = reverse("habits:habit-detail", args=(self.habit_1.id,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Habit.objects.filter(id=self.habit_1.id).exists())

    def test_public_habit_list(self):
        """Тест на получение списка публичных привычек"""
        url = reverse("habits:habit-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Ожидаем только публичные привычки
        actions = [habit["action"] for habit in response.data["results"]]
        self.assertIn(self.habit_1.action, actions)
        self.assertIn(self.habit_2.action, actions)
