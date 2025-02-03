from django.urls import path
from rest_framework.routers import SimpleRouter

from courses_lessons.apps import CoursesLessonsConfig
from courses_lessons.views import CourseViewSet, LessonListAPIView, LessonRetrieveAPIView, LessonCreateAPIView, \
    LessonDestroyAPIView, LessonUpdateAPIView
from users.views import SubscriptionAPIView

app_name = CoursesLessonsConfig.name

router = SimpleRouter()
router.register('', CourseViewSet)

urlpatterns = [
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_retrieve"),
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lesson/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lesson_delete"),
    path("lesson/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lesson_update"),
    path("subscribe/<int:pk>", SubscriptionAPIView.as_view(), name="course_subscribe")
]

urlpatterns += router.urls
