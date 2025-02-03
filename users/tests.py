from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from courses_lessons.models import Course
from users.models import User


class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="autotest@mail.ru")
        self.course = Course.objects.create(name="autoTestSubscription", owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_post(self):
        url = reverse("courses_lessons:course_subscribe", args=(self.course.pk,))
        data = {"id": self.course.pk}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'message': 'подписка добавлена'})
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'message': 'подписка удалена'})
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'message': 'подписка добавлена'})
