# Generated by Django 4.2.7 on 2023-12-04 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_placename_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="status",
            field=models.BooleanField(default=True, verbose_name="Видимость коммента"),
        ),
        migrations.AlterField(
            model_name="comment",
            name="update_at",
            field=models.DateTimeField(
                auto_now=True, verbose_name="Дата и время изменения комментария"
            ),
        ),
    ]