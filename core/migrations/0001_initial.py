# Generated by Django 4.2.7 on 2023-12-02 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="PlaceCategory",
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
                    "name",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="Название"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категорию",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="PlaceName",
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
                    "title",
                    models.CharField(
                        max_length=128, unique=True, verbose_name="Заголовок"
                    ),
                ),
                (
                    "short_description",
                    models.TextField(blank=True, verbose_name="Короткое описание"),
                ),
                (
                    "long_description",
                    tinymce.models.HTMLField(
                        blank=True, verbose_name="Полное описание"
                    ),
                ),
                ("longitude", models.FloatField(verbose_name="Долгота точки")),
                ("latitude", models.FloatField(verbose_name="Широта точки")),
                (
                    "published_at",
                    models.DateTimeField(verbose_name="Дата и время публикации"),
                ),
                (
                    "update_at",
                    models.DateTimeField(
                        verbose_name="Дата и время изменения публикации"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.placecategory",
                    ),
                ),
                (
                    "likes",
                    models.ManyToManyField(
                        blank=True,
                        related_name="liked_posts",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Кто лайкнул",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пост",
                "verbose_name_plural": "Посты",
            },
        ),
        migrations.CreateModel(
            name="PlaceImage",
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
                    "sequence_number",
                    models.IntegerField(
                        blank=True,
                        db_index=True,
                        default=0,
                        verbose_name="Порядковый номер:",
                    ),
                ),
                (
                    "picture",
                    models.ImageField(upload_to="img", verbose_name="Картинка"),
                ),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="pictures",
                        to="core.placename",
                        verbose_name="Место",
                    ),
                ),
            ],
            options={
                "verbose_name": "Картинка",
                "verbose_name_plural": "Картинки",
                "ordering": ["sequence_number"],
            },
        ),
        migrations.CreateModel(
            name="Comment",
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
                ("text", models.TextField(verbose_name="Текст комментария")),
                (
                    "published_at",
                    models.DateTimeField(verbose_name="Дата и время публикации"),
                ),
                (
                    "update_at",
                    models.DateTimeField(
                        verbose_name="Дата и время изменения комментария"
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Автор",
                    ),
                ),
                (
                    "place",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="core.placename",
                        verbose_name="Место, к которому написан",
                    ),
                ),
            ],
        ),
    ]
