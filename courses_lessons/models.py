from django.db import models

from django.contrib.auth import get_user_model

from config import settings


class Course(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Название", help_text="", blank=True, null=True
    )
    description = models.TextField(
        verbose_name="Описание", help_text="", blank=True, null=True
    )
    preview = models.ImageField(
        upload_to="courses/preview/", verbose_name="превью", blank=True, null=True
    )
    # settings.AUTH_USER_MODEL
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        help_text=""
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Название", help_text="", blank=True, null=True
    )
    description = models.TextField(
        verbose_name="Описание", help_text="", blank=True, null=True
    )
    preview = models.ImageField(
        upload_to="lessons/preview/", verbose_name="превью", blank=True, null=True
    )

    video = models.URLField(verbose_name="видео", blank=True, null=True)

    course = models.ForeignKey(
        Course,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Курс",
        help_text=""
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Владелец",
        help_text=""
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name
