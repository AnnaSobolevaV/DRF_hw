# Generated by Django 5.1.5 on 2025-02-05 20:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_subscription"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment_card",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "amount",
                    models.PositiveIntegerField(
                        help_text="Сумма платежа", verbose_name="Сумма платежа"
                    ),
                ),
                (
                    "session_id",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="id сессии"
                    ),
                ),
                (
                    "link",
                    models.URLField(
                        blank=True,
                        max_length=400,
                        null=True,
                        verbose_name="ссылка на оплату",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Пользователь",
                    ),
                ),
            ],
            options={
                "verbose_name": "Оплата картой",
                "verbose_name_plural": "Оплата картой",
            },
        ),
    ]
