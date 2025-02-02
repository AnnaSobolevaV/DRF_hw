from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from courses_lessons.models import Course, Lesson
from users.models import User


class CourseTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="autotest@mail.ru")
        self.course = Course.objects.create(name="autoTestCourse", owner=self.user)
        self.lesson = Lesson.objects.create(name="autoTestLesson", owner=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_course_list(self):
        url = reverse("courses_lessons:course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'],
                         [{'id': self.course.pk, 'subscription': False, 'count_lessons': 1, 'lessons': [
                             {'id': self.lesson.pk, 'name': 'autoTestLesson', 'description': None, 'preview': None,
                              'video': None, 'course': self.course.pk,
                              'owner': self.user.pk}], 'name': 'autoTestCourse', 'description': None, 'preview': None,
                           'owner': self.user.pk}])
        self.assertEqual(Course.objects.count(), 1)

    def test_course_retrieve(self):
        url = reverse("courses_lessons:course-detail", args=(self.course.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id': self.course.pk, 'subscription': False, 'count_lessons': 1, 'lessons': [
            {'id': self.lesson.pk, 'name': 'autoTestLesson', 'description': None, 'preview': None, 'video': None,
             'course': self.course.pk,
             'owner': self.user.pk}], 'name': 'autoTestCourse', 'description': None, 'preview': None,
                                           'owner': self.user.pk})

    def test_course_create(self):
        url = reverse("courses_lessons:course-list")
        data = {"name": "autoTestNew"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], 'autoTestNew')
        self.assertEqual(Course.objects.count(), 2)

    def test_course_update(self):
        url = reverse("courses_lessons:course-detail", args=(self.course.pk,))
        data = {"name": "autoTestUpdate"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'id': self.course.pk, 'subscription': False, 'count_lessons': 1, 'lessons': [
            {'id': self.lesson.pk, 'name': 'autoTestLesson', 'description': None, 'preview': None, 'video': None,
             'course': self.course.pk,
             'owner': self.user.pk}], 'name': 'autoTestUpdate', 'description': None, 'preview': None,
                                           'owner': self.user.pk})

    def test_course_delete(self):
        url = reverse("courses_lessons:course-detail", args=(self.course.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="autotest@mail.ru")
        self.course = Course.objects.create(name="autoTestCourse", owner=self.user)
        self.lesson = Lesson.objects.create(name="autoTestLesson", owner=self.user, course=self.course)
        self.client.force_authenticate(user=self.user)

    def test_lesson_list(self):
        url = reverse("courses_lessons:lesson_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['results'], [
            {'id': self.lesson.pk, 'name': 'autoTestLesson', 'description': None, 'preview': None, 'video': None,
             'course': self.course.pk, 'owner': self.user.pk}])
        self.assertEqual(Lesson.objects.count(), 1)

    def test_lesson_retrieve(self):
        url = reverse("courses_lessons:lesson_retrieve", args=(self.lesson.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': self.lesson.pk, 'name': 'autoTestLesson', 'description': None, 'preview': None,
                          'video': None, 'course': self.course.pk, 'owner': self.user.pk})

    def test_lesson_create(self):
        url = reverse("courses_lessons:lesson_create")
        data = {"name": "autoTestNew"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], 'autoTestNew')
        self.assertEqual(Lesson.objects.count(), 2)

    def test_lesson_update(self):
        url = reverse("courses_lessons:lesson_update", args=(self.lesson.pk,))
        data = {"name": "autoTestUpdate"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {'id': self.lesson.pk, 'name': 'autoTestUpdate', 'description': None, 'preview': None,
                          'video': None, 'course': self.course.pk, 'owner': self.user.pk})

    def test_lesson_delete(self):
        url = reverse("courses_lessons:lesson_delete", args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Lesson.objects.count(), 0)
