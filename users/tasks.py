from dateutil.relativedelta import *

from celery import shared_task
from django.utils import timezone

from users.models import User


@shared_task
def check_user_activity():
    today = timezone.now().today().date()
    users = User.objects.filter(is_active=True, last_login__isnull=False)
    for user in users:
        if user.last_login.date() + relativedelta(months=+1) < today:
            user.is_active = False
            user.save()
