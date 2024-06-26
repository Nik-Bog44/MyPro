# Generated by Django 5.0.4 on 2024-05-29 12:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("goals", "0001_add_doals_catagory_model"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Goal",
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
                    "created",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания"
                    ),
                ),
                (
                    "updated",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата последнего обновления"
                    ),
                ),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True, null=True)),
                ("due_date", models.DateField(blank=True, null=True)),
                (
                    "status",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "К выполнению"),
                            (2, "В процессе"),
                            (3, "Выполнено"),
                            (4, "Архив"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "priority",
                    models.PositiveSmallIntegerField(
                        choices=[
                            (1, "Низкий"),
                            (2, "Средний"),
                            (3, "Высокий"),
                            (4, "Критичный"),
                        ],
                        default=2,
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="goals",
                        to="goals.goalcategory",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="goals",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Цель",
                "verbose_name_plural": "Цели",
            },
        ),
    ]
