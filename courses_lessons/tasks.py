from celery import shared_task
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from courses_lessons.models import Course
from users.models import Subscription


@shared_task
def course_updated_send_email(course_pk):
    course = Course.objects.get(pk=course_pk)
    course_subscription_list = Subscription.objects.filter(course=course)
    if course_subscription_list:
        for subscription in course_subscription_list:
            print(f' В курсе {course}, на который вы подписаны, внесены изменения', subscription)
            send_mail(
                subject='Материалы курса изменились',
                message=f'В курсе {course}, на который вы подписаны, внесены изменения',
                from_email=EMAIL_HOST_USER,
                recipient_list=[subscription.user.email]
            )
