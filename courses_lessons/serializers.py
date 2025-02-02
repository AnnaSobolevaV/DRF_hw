from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from courses_lessons.models import Course, Lesson
from courses_lessons.validators import lesson_video_link_validator
from users.models import Subscription


class LessonSerializer(ModelSerializer):
    video = serializers.URLField(validators=[lesson_video_link_validator], required=False)

    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(ModelSerializer):
    subscription = SerializerMethodField(read_only=True)
    count_lessons = SerializerMethodField(read_only=True)
    lessons = LessonSerializer(source='lesson_set', many=True, read_only=True)

    def get_lessons(self, course):
        return [lesson.name for lesson in Lesson.objects.filter(course=course)]

    def get_count_lessons(self, course):
        return Lesson.objects.filter(course=course).count()

    def get_subscription(self, course):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user, course=course).exists()

    class Meta:
        model = Course
        fields = "__all__"
