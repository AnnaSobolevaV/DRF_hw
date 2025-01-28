from django.contrib.auth.models import AbstractUser
from django.db import models

from courses_lessons.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email")
    phone = models.CharField(
        max_length=35, verbose_name="Телефон", blank=True, null=True
    )
    avatar = models.ImageField(
        upload_to="users/avatars/", verbose_name="Аватар", blank=True, null=True
    )
    city = models.CharField(max_length=200, verbose_name="Город", blank=True, null=True)
    token = models.CharField(
        max_length=100, verbose_name="токен", blank=True, null=True
    )
    is_active = models.BooleanField(
        blank=True, null=True, verbose_name="", help_text=""
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payments(models.Model):
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Пользователь",
        help_text=""
    )
    payment_date = models.DateField(
        blank=True,
        null=True,
        verbose_name="дата оплаты курса или урока",
        help_text=""
    )
    course = models.ForeignKey(
        Course,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="оплаченный курс",
        help_text=""
    )
    lesson = models.ForeignKey(
        Lesson,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="оплаченный урок",
        help_text=""
    )
    payment_amount = models.FloatField(
        blank=True,
        null=True,
        verbose_name="сумма платежа",
        help_text=""
    )
    payment_method = models.CharField(
        max_length=50,
        verbose_name="метод платежа",
        help_text="",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return self.email
